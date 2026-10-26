import os
from typing import List
import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from livekit.api import AccessToken, VideoGrants
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import get_db
from app.models import Attendance, Event, EventStatus, User
from app.schemas import (
    AttendanceOut,
    EventCreate,
    EventOut,
    LiveKitTokenResponse,
)

router = APIRouter(prefix="/events", tags=["events"])

LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY", "devkey")
LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET", "secret")
LIVEKIT_URL = os.getenv("LIVEKIT_URL", "ws://localhost:7880")


@router.get("", response_model=List[EventOut])
def list_events(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    events = db.query(Event).order_by(Event.scheduled_start.asc()).all()
    return events


@router.post("", response_model=EventOut, status_code=status.HTTP_201_CREATED)
def create_event(
    payload: EventCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    event = Event(
        title=payload.title,
        description=payload.description,
        host_id=current_user.id,
        scheduled_start=payload.scheduled_start,
        status=EventStatus.SCHEDULED,
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


@router.get("/{event_id}", response_model=EventOut)
def get_event(
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
    return event


@router.post("/{event_id}/join", response_model=AttendanceOut)
def join_event(
    event_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # Verify event exists
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found",
        )

    # Check if user has an active attendance record (left_at is None)
    existing_attendance = (
        db.query(Attendance)
        .filter(
            Attendance.event_id == event_id,
            Attendance.user_id == current_user.id,
            Attendance.left_at.is_(None),
        )
        .first()
    )
    if existing_attendance:
        return existing_attendance

    # Create new attendance record
    attendance = Attendance(
        event_id=event.id,
        user_id=current_user.id,
    )
    db.add(attendance)
    db.commit()
    db.refresh(attendance)
    return attendance


@router.post("/{event_id}/token", response_model=LiveKitTokenResponse)
def get_event_token(
    event_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # Verify event exists
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found",
        )

    room_name = str(event.id)
    grants = VideoGrants(
        room_join=True,
        room=room_name,
        can_publish=True,
        can_subscribe=True,
    )

    token = (
        AccessToken(LIVEKIT_API_KEY, LIVEKIT_API_SECRET)
        .with_identity(str(current_user.id))
        .with_name(current_user.name)
        .with_grants(grants)
        .to_jwt()
    )

    return LiveKitTokenResponse(
        token=token,
        livekit_url=LIVEKIT_URL,
        room_name=room_name,
    )
