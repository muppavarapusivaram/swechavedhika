import os
from typing import List
import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from livekit.api import AccessToken, VideoGrants
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import get_db
from app.models import Attendance, Event, EventStatus, User, UserRole
from app.schemas import (
    AttendeeOut,
    AttendanceOut,
    EventCreate,
    EventOut,
    HandRaiseUpdate,
    LiveKitTokenResponse,
    StagePromotion,
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
        is_replay=payload.is_replay,
        recording_url=payload.recording_url,
        language=payload.language or "Telugu/English",
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
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found",
        )

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

    is_host = (event.host_id == current_user.id)
    attendance = Attendance(
        event_id=event.id,
        user_id=current_user.id,
        is_speaker=is_host,
    )
    db.add(attendance)
    db.commit()
    db.refresh(attendance)
    return attendance


@router.get("/{event_id}/attendees", response_model=List[AttendeeOut])
def get_attendees(
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

    attendances = (
        db.query(Attendance)
        .filter(Attendance.event_id == event_id, Attendance.left_at.is_(None))
        .all()
    )

    attendees = []
    for att in attendances:
        user = att.user
        role_str = user.role.value if hasattr(user.role, "value") else str(user.role)
        is_speaker = att.is_speaker or (att.user_id == event.host_id)
        attendees.append(
            AttendeeOut(
                user_id=user.id,
                name=user.name,
                email=user.email,
                role=role_str,
                hand_raised=att.hand_raised,
                is_speaker=is_speaker,
                joined_at=att.joined_at,
            )
        )
    return attendees


@router.post("/{event_id}/raise-hand", response_model=AttendanceOut)
def toggle_hand_raise(
    event_id: uuid.UUID,
    payload: HandRaiseUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    attendance = (
        db.query(Attendance)
        .filter(
            Attendance.event_id == event_id,
            Attendance.user_id == current_user.id,
            Attendance.left_at.is_(None),
        )
        .first()
    )
    if not attendance:
        # Auto-join if not yet joined
        attendance = Attendance(
            event_id=event_id,
            user_id=current_user.id,
            hand_raised=payload.hand_raised,
        )
        db.add(attendance)
    else:
        attendance.hand_raised = payload.hand_raised

    db.commit()
    db.refresh(attendance)
    return attendance


@router.post("/{event_id}/promote-speaker", response_model=AttendanceOut)
def promote_speaker(
    event_id: uuid.UUID,
    payload: StagePromotion,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found",
        )

    # Only host can promote speakers
    if event.host_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only event host can promote attendees to speaker",
        )

    attendance = (
        db.query(Attendance)
        .filter(
            Attendance.event_id == event_id,
            Attendance.user_id == payload.user_id,
            Attendance.left_at.is_(None),
        )
        .first()
    )
    if not attendance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Attendee not found in event",
        )

    attendance.is_speaker = payload.is_speaker
    if payload.is_speaker:
        attendance.hand_raised = False  # Reset hand raise upon promotion

    db.commit()
    db.refresh(attendance)
    return attendance


@router.post("/{event_id}/token", response_model=LiveKitTokenResponse)
def get_event_token(
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

    # Determine if user has speaker privileges
    is_host = (event.host_id == current_user.id)
    attendance = (
        db.query(Attendance)
        .filter(
            Attendance.event_id == event_id,
            Attendance.user_id == current_user.id,
            Attendance.left_at.is_(None),
        )
        .first()
    )
    is_speaker = is_host or (attendance and attendance.is_speaker)

    room_name = str(event.id)
    grants = VideoGrants(
        room_join=True,
        room=room_name,
        can_publish=bool(is_speaker),
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
        is_speaker=bool(is_speaker),
    )
