"""add stage promotion, live qa, polls, and replay archive features

Revision ID: 002_qa_polls_and_features
Revises: 001_initial_schema
Create Date: 2026-10-28 19:25:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "002_qa_polls_and_features"
down_revision: Union[str, None] = "001_initial_schema"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Update attendance table
    op.add_column(
        "attendance",
        sa.Column(
            "hand_raised",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
        ),
    )
    op.add_column(
        "attendance",
        sa.Column(
            "is_speaker",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
        ),
    )

    # 2. Update events table
    op.add_column(
        "events",
        sa.Column(
            "is_replay",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
        ),
    )
    op.add_column(
        "events",
        sa.Column("recording_url", sa.String(length=500), nullable=True),
    )
    op.add_column(
        "events",
        sa.Column("transcript", sa.JSON(), nullable=True),
    )
    op.add_column(
        "events",
        sa.Column("summary", sa.Text(), nullable=True),
    )
    op.add_column(
        "events",
        sa.Column(
            "language",
            sa.String(length=50),
            server_default="Telugu/English",
            nullable=False,
        ),
    )

    # 3. Create questions table
    op.create_table(
        "questions",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("event_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column(
            "upvotes",
            sa.Integer(),
            server_default=sa.text("0"),
            nullable=False,
        ),
        sa.Column(
            "is_answered",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["event_id"], ["events.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_questions_id"), "questions", ["id"], unique=False)
    op.create_index(
        op.f("ix_questions_event_id"), "questions", ["event_id"], unique=False
    )
    op.create_index(
        op.f("ix_questions_user_id"), "questions", ["user_id"], unique=False
    )

    # 4. Create question_upvotes table
    op.create_table(
        "question_upvotes",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("question_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["question_id"], ["questions.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "question_id", "user_id", name="uq_question_user_upvote"
        ),
    )
    op.create_index(
        op.f("ix_question_upvotes_id"), "question_upvotes", ["id"], unique=False
    )
    op.create_index(
        op.f("ix_question_upvotes_question_id"),
        "question_upvotes",
        ["question_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_question_upvotes_user_id"),
        "question_upvotes",
        ["user_id"],
        unique=False,
    )

    # 5. Create polls table
    op.create_table(
        "polls",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("event_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("question", sa.String(length=500), nullable=False),
        sa.Column("options", sa.JSON(), nullable=False),
        sa.Column(
            "is_active",
            sa.Boolean(),
            server_default=sa.text("true"),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["event_id"], ["events.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_polls_id"), "polls", ["id"], unique=False)
    op.create_index(
        op.f("ix_polls_event_id"), "polls", ["event_id"], unique=False
    )

    # 6. Create poll_votes table
    op.create_table(
        "poll_votes",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("poll_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("option_index", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["poll_id"], ["polls.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("poll_id", "user_id", name="uq_poll_user_vote"),
    )
    op.create_index(
        op.f("ix_poll_votes_id"), "poll_votes", ["id"], unique=False
    )
    op.create_index(
        op.f("ix_poll_votes_poll_id"), "poll_votes", ["poll_id"], unique=False
    )
    op.create_index(
        op.f("ix_poll_votes_user_id"), "poll_votes", ["user_id"], unique=False
    )


def downgrade() -> None:
    op.drop_table("poll_votes")
    op.drop_table("polls")
    op.drop_table("question_upvotes")
    op.drop_table("questions")

    op.drop_column("events", "language")
    op.drop_column("events", "summary")
    op.drop_column("events", "transcript")
    op.drop_column("events", "recording_url")
    op.drop_column("events", "is_replay")

    op.drop_column("attendance", "is_speaker")
    op.drop_column("attendance", "hand_raised")
