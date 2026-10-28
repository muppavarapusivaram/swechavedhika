from datetime import datetime
from typing import Any, Dict, List, Optional
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
    is_replay: bool = False
    recording_url: Optional[str] = None
    language: str = "Telugu/English"


class EventOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    title: str
    description: Optional[str] = None
    host_id: UUID
    scheduled_start: datetime
    status: EventStatus
    created_at: datetime
    is_replay: bool = False
    recording_url: Optional[str] = None
    summary: Optional[str] = None
    transcript: Optional[Any] = None
    language: str = "Telugu/English"


class AttendanceOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    event_id: UUID
    user_id: UUID
    joined_at: datetime
    left_at: Optional[datetime] = None
    hand_raised: bool = False
    is_speaker: bool = False


class AttendeeOut(BaseModel):
    user_id: UUID
    name: str
    email: str
    role: str
    hand_raised: bool
    is_speaker: bool
    joined_at: datetime


class HandRaiseUpdate(BaseModel):
    hand_raised: bool


class StagePromotion(BaseModel):
    user_id: UUID
    is_speaker: bool


class LiveKitTokenResponse(BaseModel):
    token: str
    livekit_url: str
    room_name: str
    is_speaker: bool = False


# Q&A Schemas
class QuestionCreate(BaseModel):
    content: str


class QuestionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    event_id: UUID
    user_id: UUID
    user_name: str
    content: str
    upvotes: int
    is_answered: bool
    created_at: datetime
    has_upvoted: bool = False


# Poll Schemas
class PollCreate(BaseModel):
    question: str
    options: List[str]


class PollVoteRequest(BaseModel):
    option_index: int


class PollOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    event_id: UUID
    question: str
    options: List[str]
    is_active: bool
    created_at: datetime
    vote_counts: Dict[str, int]
    total_votes: int
    user_vote: Optional[int] = None


# Archive & Language Schemas
class ArchiveEventOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    title: str
    description: Optional[str]
    scheduled_start: datetime
    status: EventStatus
    recording_url: Optional[str]
    summary: Optional[str]
    transcript: Optional[Any]
    language: str


class CorpusExportItem(BaseModel):
    id: UUID
    event_id: UUID
    event_title: str
    speaker_name: str
    language: str
    audio_sample_url: Optional[str]
    transcript_segment: str
    timestamp_start: float
    timestamp_end: float
