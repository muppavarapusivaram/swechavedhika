import enum
import uuid
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    JSON,
    String,
    Text,
    UniqueConstraint,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base


class UserRole(str, enum.Enum):
    OWNER = "owner"
    HOST = "host"
    MODERATOR = "moderator"
    SPEAKER = "speaker"
    VIEWER = "viewer"


class EventStatus(str, enum.Enum):
    SCHEDULED = "scheduled"
    LIVE = "live"
    ENDED = "ended"


class User(Base):
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)
    phone_number = Column(String(50), nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(
        Enum(
            UserRole,
            name="user_role",
            native_enum=True,
            values_callable=lambda x: [e.value for e in x],
        ),
        nullable=False,
        default=UserRole.VIEWER,
    )
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # Relationships
    hosted_events = relationship(
        "Event",
        back_populates="host",
        cascade="all, delete-orphan",
    )
    attendances = relationship(
        "Attendance",
        back_populates="user",
        cascade="all, delete-orphan",
    )
    questions = relationship(
        "Question",
        back_populates="user",
        cascade="all, delete-orphan",
    )
    poll_votes = relationship(
        "PollVote",
        back_populates="user",
        cascade="all, delete-orphan",
    )


class Event(Base):
    __tablename__ = "events"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    host_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    scheduled_start = Column(DateTime(timezone=True), nullable=False)
    status = Column(
        Enum(
            EventStatus,
            name="event_status",
            native_enum=True,
            values_callable=lambda x: [e.value for e in x],
        ),
        nullable=False,
        default=EventStatus.SCHEDULED,
    )
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # Features for Replay-as-live & Multilingual Archive
    is_replay = Column(Boolean, default=False, nullable=False)
    recording_url = Column(String(500), nullable=True)
    transcript = Column(JSON, nullable=True)
    summary = Column(Text, nullable=True)
    language = Column(String(50), default="Telugu/English", nullable=False)

    # Relationships
    host = relationship("User", back_populates="hosted_events")
    attendances = relationship(
        "Attendance",
        back_populates="event",
        cascade="all, delete-orphan",
    )
    questions = relationship(
        "Question",
        back_populates="event",
        cascade="all, delete-orphan",
    )
    polls = relationship(
        "Poll",
        back_populates="event",
        cascade="all, delete-orphan",
    )


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    event_id = Column(
        UUID(as_uuid=True),
        ForeignKey("events.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    joined_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    left_at = Column(DateTime(timezone=True), nullable=True)

    # Stage access & Hand Raising
    hand_raised = Column(Boolean, default=False, nullable=False)
    is_speaker = Column(Boolean, default=False, nullable=False)

    # Relationships
    event = relationship("Event", back_populates="attendances")
    user = relationship("User", back_populates="attendances")


class Question(Base):
    __tablename__ = "questions"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    event_id = Column(
        UUID(as_uuid=True),
        ForeignKey("events.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    content = Column(Text, nullable=False)
    upvotes = Column(Integer, default=0, nullable=False)
    is_answered = Column(Boolean, default=False, nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # Relationships
    event = relationship("Event", back_populates="questions")
    user = relationship("User", back_populates="questions")
    upvote_records = relationship(
        "QuestionUpvote",
        back_populates="question",
        cascade="all, delete-orphan",
    )


class QuestionUpvote(Base):
    __tablename__ = "question_upvotes"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    question_id = Column(
        UUID(as_uuid=True),
        ForeignKey("questions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    __table_args__ = (
        UniqueConstraint("question_id", "user_id", name="uq_question_user_upvote"),
    )

    question = relationship("Question", back_populates="upvote_records")
    user = relationship("User")


class Poll(Base):
    __tablename__ = "polls"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    event_id = Column(
        UUID(as_uuid=True),
        ForeignKey("events.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    question = Column(String(500), nullable=False)
    options = Column(JSON, nullable=False)  # List of strings e.g. ["Yes", "No"]
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # Relationships
    event = relationship("Event", back_populates="polls")
    votes = relationship(
        "PollVote",
        back_populates="poll",
        cascade="all, delete-orphan",
    )


class PollVote(Base):
    __tablename__ = "poll_votes"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    poll_id = Column(
        UUID(as_uuid=True),
        ForeignKey("polls.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    option_index = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint("poll_id", "user_id", name="uq_poll_user_vote"),
    )

    poll = relationship("Poll", back_populates="votes")
    user = relationship("User", back_populates="poll_votes")
