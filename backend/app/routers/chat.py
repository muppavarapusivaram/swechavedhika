from typing import List
import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import get_db
from app.models import ChatMessage, Event, User
from app.schemas import ChatMessageCreate, ChatMessageOut

router = APIRouter(prefix="/events/{event_id}/chat", tags=["chat"])


@router.get("", response_model=List[ChatMessageOut])
def list_chat_messages(
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

    messages = (
        db.query(ChatMessage)
        .filter(ChatMessage.event_id == event_id)
        .order_by(ChatMessage.created_at.asc())
        .limit(100)
        .all()
    )

    return [
        ChatMessageOut(
            id=m.id,
            event_id=m.event_id,
            user_id=m.user_id,
            user_name=m.user.name if m.user else "Anonymous",
            content=m.content,
            created_at=m.created_at,
        )
        for m in messages
    ]


@router.post("", response_model=ChatMessageOut, status_code=status.HTTP_201_CREATED)
def send_chat_message(
    event_id: uuid.UUID,
    payload: ChatMessageCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found",
        )

    content = payload.content.strip()
    if not content:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Chat message cannot be empty",
        )

    msg = ChatMessage(
        event_id=event_id,
        user_id=current_user.id,
        content=content,
    )
    db.add(msg)
    db.commit()
    db.refresh(msg)

    return ChatMessageOut(
        id=msg.id,
        event_id=msg.event_id,
        user_id=msg.user_id,
        user_name=current_user.name,
        content=msg.content,
        created_at=msg.created_at,
    )
