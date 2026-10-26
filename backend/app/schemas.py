from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, EmailStr

from app.models import EventStatus, UserRole


class UserRegister(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    email: EmailStr
    phone_number: str
    role: UserRole
    created_at: datetime


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class EventCreate(BaseModel):
    title: str
    description: Optional[str] = None
    scheduled_start: datetime


class EventOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    title: str
    description: Optional[str] = None
    host_id: UUID
    scheduled_start: datetime
    status: EventStatus
    created_at: datetime


class AttendanceOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    event_id: UUID
    user_id: UUID
    joined_at: datetime
    left_at: Optional[datetime] = None


class LiveKitTokenResponse(BaseModel):
    token: str
    livekit_url: str
    room_name: str

