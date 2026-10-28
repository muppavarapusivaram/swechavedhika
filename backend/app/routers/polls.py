from collections import Counter
from typing import List
import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import get_db
from app.models import Event, Poll, PollVote, User, UserRole
from app.schemas import PollCreate, PollOut, PollVoteRequest

router = APIRouter(prefix="/events/{event_id}/polls", tags=["polls"])


def format_poll_response(poll: Poll, user_id: uuid.UUID, db: Session) -> PollOut:
    votes = db.query(PollVote).filter(PollVote.poll_id == poll.id).all()
    counter = Counter(v.option_index for v in votes)
    
    # Format counts for each option index as string keys
    vote_counts = {str(i): counter.get(i, 0) for i in range(len(poll.options))}
    total_votes = len(votes)

    user_vote_obj = next((v for v in votes if v.user_id == user_id), None)
    user_vote = user_vote_obj.option_index if user_vote_obj else None

    return PollOut(
        id=poll.id,
        event_id=poll.event_id,
        question=poll.question,
        options=poll.options,
        is_active=poll.is_active,
        created_at=poll.created_at,
        vote_counts=vote_counts,
        total_votes=total_votes,
        user_vote=user_vote,
    )


@router.get("", response_model=List[PollOut])
def list_polls(
    event_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found",
        )

    polls = (
        db.query(Poll)
        .filter(Poll.event_id == event_id)
        .order_by(Poll.is_active.desc(), Poll.created_at.desc())
        .all()
    )

    return [format_poll_response(p, current_user.id, db) for p in polls]


@router.post("", response_model=PollOut, status_code=status.HTTP_201_CREATED)
def create_poll(
    event_id: uuid.UUID,
    payload: PollCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found",
        )

    if event.host_id != current_user.id and current_user.role not in [UserRole.MODERATOR, UserRole.OWNER]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only event host or moderator can create polls",
        )

    if not payload.question.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Poll question cannot be empty",
        )

    if len(payload.options) < 2:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Poll must have at least 2 options",
        )

    poll = Poll(
        event_id=event_id,
        question=payload.question.strip(),
        options=payload.options,
        is_active=True,
    )
    db.add(poll)
    db.commit()
    db.refresh(poll)

    return format_poll_response(poll, current_user.id, db)


@router.post("/{poll_id}/vote", response_model=PollOut)
def vote_poll(
    event_id: uuid.UUID,
    poll_id: uuid.UUID,
    payload: PollVoteRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    poll = (
        db.query(Poll)
        .filter(Poll.id == poll_id, Poll.event_id == event_id)
        .first()
    )
    if not poll:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Poll not found",
        )

    if not poll.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Poll is closed for voting",
        )

    if payload.option_index < 0 or payload.option_index >= len(poll.options):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid option index",
        )

    existing_vote = (
        db.query(PollVote)
        .filter(PollVote.poll_id == poll_id, PollVote.user_id == current_user.id)
        .first()
    )

    if existing_vote:
        existing_vote.option_index = payload.option_index
    else:
        new_vote = PollVote(
            poll_id=poll_id,
            user_id=current_user.id,
            option_index=payload.option_index,
        )
        db.add(new_vote)

    db.commit()
    return format_poll_response(poll, current_user.id, db)
