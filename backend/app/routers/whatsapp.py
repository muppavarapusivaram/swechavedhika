import os
from typing import Any, Dict, Optional
import uuid
from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Attendance, Event, EventStatus, Question, User, UserRole

router = APIRouter(prefix="/webhook/whatsapp", tags=["whatsapp"])

WHATSAPP_VERIFY_TOKEN = os.getenv("WHATSAPP_VERIFY_TOKEN", "swecha_token_secret")


class WhatsAppSimulateRequest(BaseModel):
    phone: str = "+919876543210"
    name: Optional[str] = "Village Volunteer"
    message: str


class WhatsAppSimulateResponse(BaseModel):
    reply: str
    action_type: str
    event_id: Optional[str] = None


@router.get("")
def verify_webhook(
    hub_mode: Optional[str] = Query(None, alias="hub.mode"),
    hub_challenge: Optional[str] = Query(None, alias="hub.challenge"),
    hub_verify_token: Optional[str] = Query(None, alias="hub.verify_token"),
):
    if hub_mode == "subscribe" and hub_verify_token == WHATSAPP_VERIFY_TOKEN:
        return Response(content=hub_challenge or "", media_type="text/plain")
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Verification token mismatch",
    )


def process_whatsapp_text(message: str, phone: str, name: str, db: Session) -> Dict[str, Any]:
    text = message.strip()
    text_lower = text.lower()

    # 1. Menu / Greeting / EVENTS
    if text_lower in ["hi", "hello", "namaste", "menu", "events", "సహాయం", "హలో"]:
        events = (
            db.query(Event)
            .order_by(Event.scheduled_start.asc())
            .limit(5)
            .all()
        )
        if not events:
            return {
                "reply": "నమస్కారం! Currently no upcoming Swecha Vedika events scheduled.\nCheck back soon!",
                "action_type": "info",
                "event_id": None,
            }
        
        reply_lines = [
            "🚩 *స్వేచ్ఛ వేదిక (Swecha Vedika) WhatsApp సేవా కేంద్రం*",
            "Upcoming live community sessions:\n",
        ]
        for idx, ev in enumerate(events, 1):
            time_str = ev.scheduled_start.strftime("%d %b, %I:%M %p")
            reply_lines.append(f"{idx}. *{ev.title}*")
            reply_lines.append(f"   📅 {time_str}")
            reply_lines.append(f"   💬 Reply: *RSVP {str(ev.id)[:8]}* to join\n")

        reply_lines.append("Commands: *RSVP <id>*, *ASK <id>: <question>*, *SUMMARY <id>*")
        return {
            "reply": "\n".join(reply_lines),
            "action_type": "event_list",
            "event_id": None,
        }

    # Helper: Find or create user for this phone number
    user = db.query(User).filter(User.phone_number == phone).first()
    if not user:
        user = User(
            name=name,
            email=f"{phone.replace('+', '')}@whatsapp.swecha.org",
            phone_number=phone,
            password_hash="whatsapp_auth_token_not_applicable",
            role=UserRole.VIEWER,
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    # 2. RSVP Command: "RSVP <prefix/id>"
    if text_lower.startswith("rsvp"):
        query_term = text[4:].strip()
        event = None
        if query_term:
            # Match UUID prefix or title
            events = db.query(Event).all()
            for ev in events:
                if str(ev.id).startswith(query_term.lower()) or query_term.lower() in ev.title.lower():
                    event = ev
                    break
        else:
            event = db.query(Event).order_by(Event.scheduled_start.asc()).first()

        if not event:
            return {
                "reply": f"❌ Event matching '{query_term}' not found. Send *EVENTS* to see list.",
                "action_type": "error",
                "event_id": None,
            }

        # Check existing attendance
        existing_att = (
            db.query(Attendance)
            .filter(Attendance.event_id == event.id, Attendance.user_id == user.id)
            .first()
        )
        if not existing_att:
            att = Attendance(event_id=event.id, user_id=user.id)
            db.add(att)
            db.commit()

        time_str = event.scheduled_start.strftime("%d %b at %I:%M %p")
        reply = (
            f"✅ *RSVP Confirmed!*\n\n"
            f"Event: *{event.title}*\n"
            f"Time: {time_str}\n"
            f"Low-Bandwidth Web Link: http://localhost:5173/room/{event.id}\n\n"
            f"You will receive live reminders 15 mins before start. Reply *ASK {str(event.id)[:8]}: your question* anytime!"
        )
        return {
            "reply": reply,
            "action_type": "rsvp_success",
            "event_id": str(event.id),
        }

    # 3. ASK Question: "ASK <id>: <question text>"
    if text_lower.startswith("ask"):
        rest = text[3:].strip()
        parts = rest.split(":", 1)
        if len(parts) < 2:
            return {
                "reply": "Format error. Please send: *ASK <event_id>: <your question>*",
                "action_type": "error",
                "event_id": None,
            }
        query_id = parts[0].strip()
        q_content = parts[1].strip()

        events = db.query(Event).all()
        event = next((ev for ev in events if str(ev.id).startswith(query_id.lower())), None)
        if not event:
            return {
                "reply": f"❌ Event matching '{query_id}' not found.",
                "action_type": "error",
                "event_id": None,
            }

        q = Question(
            event_id=event.id,
            user_id=user.id,
            content=f"[WhatsApp from {user.name}]: {q_content}",
            upvotes=1,
            is_answered=False,
        )
        db.add(q)
        db.commit()

        return {
            "reply": f"👍 Question submitted to *{event.title}* live stage queue!\nThe speakers will address it during Q&A.",
            "action_type": "question_submitted",
            "event_id": str(event.id),
        }

    # 4. SUMMARY Command: "SUMMARY <id>"
    if text_lower.startswith("summary"):
        query_id = text[7:].strip()
        events = db.query(Event).all()
        event = next((ev for ev in events if str(ev.id).startswith(query_id.lower())), None)
        if not event:
            event = db.query(Event).filter(Event.summary.isnot(None)).first()

        if not event or not event.summary:
            return {
                "reply": "Summary not available yet for this event. Try again after session concludes.",
                "action_type": "info",
                "event_id": None,
            }

        return {
            "reply": f"📋 *AI Summary ({event.title})*:\n\n{event.summary}",
            "action_type": "summary",
            "event_id": str(event.id),
        }

    # Fallback
    return {
        "reply": (
            "🤖 Swecha Vedika Bot:\n"
            "• Send *EVENTS* for upcoming sessions\n"
            "• Send *RSVP <event_id>* to register\n"
            "• Send *ASK <event_id>: <question>* to ask live speakers\n"
            "• Send *SUMMARY <event_id>* for AI digest"
        ),
        "action_type": "help",
        "event_id": None,
    }


@router.post("")
def handle_meta_webhook(
    payload: Dict[str, Any],
    db: Session = Depends(get_db),
):
    """
    Standard Meta Graph WhatsApp Webhook Handler.
    """
    try:
        entries = payload.get("entry", [])
        for entry in entries:
            for change in entry.get("changes", []):
                value = change.get("value", {})
                messages = value.get("messages", [])
                for msg in messages:
                    if msg.get("type") == "text":
                        sender_phone = msg.get("from")
                        body = msg.get("text", {}).get("body", "")
                        contacts = value.get("contacts", [{}])
                        name = contacts[0].get("profile", {}).get("name", "WhatsApp User")
                        process_whatsapp_text(body, sender_phone, name, db)
        return {"status": "success"}
    except Exception as e:
        return {"status": "ignored", "error": str(e)}


@router.post("/simulate", response_model=WhatsAppSimulateResponse)
def simulate_whatsapp(
    payload: WhatsAppSimulateRequest,
    db: Session = Depends(get_db),
):
    """
    Simulates sending a message from WhatsApp phone app for instant local testing.
    """
    result = process_whatsapp_text(
        message=payload.message,
        phone=payload.phone,
        name=payload.name or "Village Volunteer",
        db=db,
    )
    return WhatsAppSimulateResponse(**result)
