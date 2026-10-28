from typing import List
import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import get_db
from app.models import Event, Question, QuestionUpvote, User, UserRole
from app.schemas import QuestionCreate, QuestionOut

router = APIRouter(prefix="/events/{event_id}/questions", tags=["questions"])


@router.get("", response_model=List[QuestionOut])
def list_questions(
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

    questions = (
        db.query(Question)
        .filter(Question.event_id == event_id)
        .order_by(Question.is_answered.asc(), Question.upvotes.desc(), Question.created_at.asc())
        .all()
    )

    # Get set of question IDs upvoted by current_user
    user_upvotes = set(
        q_id
        for (q_id,) in db.query(QuestionUpvote.question_id)
        .filter(QuestionUpvote.user_id == current_user.id)
        .all()
    )

    result = []
    for q in questions:
        result.append(
            QuestionOut(
                id=q.id,
                event_id=q.event_id,
                user_id=q.user_id,
                user_name=q.user.name if q.user else "Anonymous",
                content=q.content,
                upvotes=q.upvotes,
                is_answered=q.is_answered,
                created_at=q.created_at,
                has_upvoted=(q.id in user_upvotes),
            )
        )
    return result


@router.post("", response_model=QuestionOut, status_code=status.HTTP_201_CREATED)
def submit_question(
    event_id: uuid.UUID,
    payload: QuestionCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found",
        )

    if not payload.content.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Question content cannot be empty",
        )

    question = Question(
        event_id=event_id,
        user_id=current_user.id,
        content=payload.content.strip(),
        upvotes=0,
        is_answered=False,
    )
    db.add(question)
    db.commit()
    db.refresh(question)

    return QuestionOut(
        id=question.id,
        event_id=question.event_id,
        user_id=question.user_id,
        user_name=current_user.name,
        content=question.content,
        upvotes=question.upvotes,
        is_answered=question.is_answered,
        created_at=question.created_at,
        has_upvoted=False,
    )


@router.post("/{question_id}/upvote", response_model=QuestionOut)
def toggle_upvote(
    event_id: uuid.UUID,
    question_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    question = (
        db.query(Question)
        .filter(Question.id == question_id, Question.event_id == event_id)
        .first()
    )
    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Question not found",
        )

    existing_upvote = (
        db.query(QuestionUpvote)
        .filter(
            QuestionUpvote.question_id == question_id,
            QuestionUpvote.user_id == current_user.id,
        )
        .first()
    )

    if existing_upvote:
        # Toggle off
        db.delete(existing_upvote)
        question.upvotes = max(0, question.upvotes - 1)
        has_upvoted = False
    else:
        # Toggle on
        new_upvote = QuestionUpvote(
            question_id=question_id,
            user_id=current_user.id,
        )
        db.add(new_upvote)
        question.upvotes += 1
        has_upvoted = True

    db.commit()
    db.refresh(question)

    return QuestionOut(
        id=question.id,
        event_id=question.event_id,
        user_id=question.user_id,
        user_name=question.user.name if question.user else "Anonymous",
        content=question.content,
        upvotes=question.upvotes,
        is_answered=question.is_answered,
        created_at=question.created_at,
        has_upvoted=has_upvoted,
    )


@router.post("/{question_id}/answer", response_model=QuestionOut)
def mark_answered(
    event_id: uuid.UUID,
    question_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found",
        )

    # Only host or moderator can mark answered
    if event.host_id != current_user.id and current_user.role not in [UserRole.MODERATOR, UserRole.OWNER]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only event host or moderator can mark questions as answered",
        )

    question = (
        db.query(Question)
        .filter(Question.id == question_id, Question.event_id == event_id)
        .first()
    )
    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Question not found",
        )

    question.is_answered = True
    db.commit()
    db.refresh(question)

    existing_upvote = (
        db.query(QuestionUpvote)
        .filter(
            QuestionUpvote.question_id == question_id,
            QuestionUpvote.user_id == current_user.id,
        )
        .first()
    )

    return QuestionOut(
        id=question.id,
        event_id=question.event_id,
        user_id=question.user_id,
        user_name=question.user.name if question.user else "Anonymous",
        content=question.content,
        upvotes=question.upvotes,
        is_answered=question.is_answered,
        created_at=question.created_at,
        has_upvoted=(existing_upvote is not None),
    )
