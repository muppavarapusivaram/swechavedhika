"""add in-room chat, replay-as-live clock, and host failover resilience

Revision ID: 003_chat_and_resilience
Revises: 002_qa_polls_and_features
Create Date: 2026-10-28 20:12:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "003_chat_and_resilience"
down_revision: Union[str, None] = "002_qa_polls_and_features"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Update events table with replay and failover columns
    op.add_column(
        "events",
        sa.Column("replay_started_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.add_column(
        "events",
        sa.Column("last_host_heartbeat", sa.DateTime(timezone=True), nullable=True),
    )
    op.add_column(
        "events",
        sa.Column(
            "failover_host_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="SET NULL"),
            nullable=True,
        ),
    )

    # 2. Create chat_messages table
    op.create_table(
        "chat_messages",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
        ),
        sa.Column(
            "event_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("events.id", ondelete="CASCADE"),
            nullable=False,
            index=True,
        ),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
            index=True,
        ),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_table("chat_messages")
    op.drop_column("events", "failover_host_id")
    op.drop_column("events", "last_host_heartbeat")
    op.drop_column("events", "replay_started_at")
