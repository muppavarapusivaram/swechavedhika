from typing import List, Optional
import uuid
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import get_db
from app.models import Event, EventStatus, User
from app.schemas import ArchiveEventOut, CorpusExportItem

router = APIRouter(prefix="/archive", tags=["archive"])

SAMPLE_TELUGU_TRANSCRIPT = [
    {
        "start": 0.0,
        "end": 8.5,
        "speaker": "Ravi Kumar (Host)",
        "language": "te",
        "text": "అందరికీ నమస్కారం! స్వేచ్ఛ వేదిక ఈరోజు వెబినార్‌కి స్వాగతం. (Welcome everyone to Swecha Vedika today's webinar.)",
    },
    {
        "start": 9.0,
        "end": 18.2,
        "speaker": "Ravi Kumar (Host)",
        "language": "te",
        "text": "మనం ఈరోజు గ్రామీణ ప్రాంతాల్లో ఇంటర్నెట్ బ్యాండ్‌విడ్త్ ఆదా చేయడం, మరియు ఓపెన్ సోర్స్ టెక్నాలజీల ప్రాముఖ్యత గురించి చర్చిస్తున్నాము.",
    },
    {
        "start": 19.0,
        "end": 28.0,
        "speaker": "Priya Sharma (Speaker)",
        "language": "te",
        "text": "WebRTC పీర్-టు-పీర్ మెష్ ద్వారా మనం సర్వర్ భారాన్ని 70 శాతం తగ్గించవచ్చు. ఇది 2G మరియు 3G నెట్‌వర్క్‌లలో కూడా అద్భుతంగా పనిచేస్తుంది.",
    },
    {
        "start": 29.0,
        "end": 39.5,
        "speaker": "Priya Sharma (Speaker)",
        "language": "en",
        "text": "By synthesizing audio with client-side slide diffing, low-data mode allows continuous participation under 50 kbps constraints.",
    },
    {
        "start": 40.0,
        "end": 52.0,
        "speaker": "Ravi Kumar (Host)",
        "language": "te",
        "text": "ధన్యవాదాలు ప్రియా గారు. ఇప్పుడు సభికుల నుండి ప్రశ్నలు మరియు పోల్స్ తీసుకుందాం.",
    },
]

SAMPLE_SUMMARY = """• గ్రామీణ కనెక్టివిటీ: తక్కువ బ్యాండ్‌విడ్త్ ఉన్న ప్రాంతాల్లో లైవ్ స్ట్రీమింగ్ సవాళ్లు మరియు పరిష్కారాలు.
• P2P మెష్ సమర్థత: WebRTC డేటా ఛానెల్‌ల ద్వారా సర్వర్ బ్యాండ్‌విడ్త్ వినియోగాన్ని 68-75% ఆదా చేయడం.
• 2G లో-డేటా మోడ్: కేవలం 50 kbps వద్ద క్రిస్టల్-క్లియర్ ఆడియో మరియు స్లైడ్ సింక్రొనైజేషన్.
• ఓపెన్ సోర్స్ స్పీచ్ కార్పస్: తెలుగు భాషా సాంకేతిక వికాసం కోసం భాగస్వాముల సమ్మతితో వాయిస్ డేటా సేకరణ."""


@router.get("", response_model=List[ArchiveEventOut])
def list_archive(
    db: Session = Depends(get_db),
):
    events = (
        db.query(Event)
        .order_by(Event.scheduled_start.desc())
        .all()
    )
    return events


@router.get("/search", response_model=List[ArchiveEventOut])
def search_archive(
    q: Optional[str] = Query(None, description="Search query string"),
    language: Optional[str] = Query(None, description="Filter by language"),
    db: Session = Depends(get_db),
):
    query = db.query(Event)

    if language and language.lower() != "all":
        query = query.filter(Event.language.ilike(f"%{language}%"))

    events = query.order_by(Event.scheduled_start.desc()).all()

    if not q or not q.strip():
        return events

    q_lower = q.lower().strip()
    matched_events = []
    for ev in events:
        # Search title, description, summary
        text_corpus = f"{ev.title} {ev.description or ''} {ev.summary or ''}".lower()
        if q_lower in text_corpus:
            matched_events.append(ev)
            continue

        # Search transcript segments if present
        if ev.transcript and isinstance(ev.transcript, list):
            found_in_transcript = any(
                q_lower in seg.get("text", "").lower() or q_lower in seg.get("speaker", "").lower()
                for seg in ev.transcript
                if isinstance(seg, dict)
            )
            if found_in_transcript:
                matched_events.append(ev)

    return matched_events


@router.get("/corpus", response_model=List[CorpusExportItem])
def export_corpus(
    db: Session = Depends(get_db),
):
    """
    Exports consent-backed speech corpus segments for regional language ASR training
    (Swecha Telugu Speech Project).
    """
    events = db.query(Event).filter(Event.transcript.isnot(None)).all()
    corpus_items = []

    for ev in events:
        if not isinstance(ev.transcript, list):
            continue
        for seg in ev.transcript:
            if isinstance(seg, dict) and "text" in seg:
                corpus_items.append(
                    CorpusExportItem(
                        id=uuid.uuid4(),
                        event_id=ev.id,
                        event_title=ev.title,
                        speaker_name=seg.get("speaker", "Contributor"),
                        language=seg.get("language", "te"),
                        audio_sample_url=ev.recording_url or "https://storage.swecha.org/samples/telugu_sample_1.wav",
                        transcript_segment=seg.get("text", ""),
                        timestamp_start=float(seg.get("start", 0.0)),
                        timestamp_end=float(seg.get("end", 0.0)),
                    )
                )

    # If no recorded transcripts in DB yet, return the default Swecha Telugu standard sample corpus
    if not corpus_items:
        dummy_event_id = uuid.uuid4()
        for seg in SAMPLE_TELUGU_TRANSCRIPT:
            corpus_items.append(
                CorpusExportItem(
                    id=uuid.uuid4(),
                    event_id=dummy_event_id,
                    event_title="స్వేచ్ఛ తెలుగు ఓపెన్ సోర్స్ వెబినార్",
                    speaker_name=seg["speaker"],
                    language=seg["language"],
                    audio_sample_url="https://storage.swecha.org/samples/telugu_sample_1.wav",
                    transcript_segment=seg["text"],
                    timestamp_start=seg["start"],
                    timestamp_end=seg["end"],
                )
            )

    return corpus_items


@router.post("/{event_id}/populate-demo-ai", response_model=ArchiveEventOut)
def populate_demo_ai_data(
    event_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Helper for demonstration: populates Whisper ASR transcript & AI summary for the event.
    """
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found",
        )

    event.recording_url = "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
    event.transcript = SAMPLE_TELUGU_TRANSCRIPT
    event.summary = SAMPLE_SUMMARY
    event.language = "Telugu / English"
    event.status = EventStatus.ENDED

    db.commit()
    db.refresh(event)
    return event


import io
import json
import zipfile
from fastapi import Response


@router.get("/{event_id}/offline-pack")
def generate_offline_pack(
    event_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    """
    Generates a self-contained offline learning bundle (.zip) for rural schools and disconnected learners.
    Contains: index.html (standalone viewer), summary.md, transcript.json, metadata.json.
    """
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found",
        )

    # Prepare offline files in memory
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        # 1. Metadata
        metadata = {
            "id": str(event.id),
            "title": event.title,
            "description": event.description,
            "host": event.host.name if event.host else "Swecha Volunteer",
            "scheduled_start": event.scheduled_start.isoformat(),
            "language": event.language,
            "exported_at": "2026-10-28T20:00:00Z",
            "offline_version": "1.0.0",
        }
        zip_file.writestr("metadata.json", json.dumps(metadata, indent=2))

        # 2. Markdown summary
        summary_text = event.summary or SAMPLE_SUMMARY
        md_content = f"# {event.title}\n\n**Host**: {metadata['host']}\n**Language**: {event.language}\n\n## Summary & Action Points\n\n{summary_text}\n"
        zip_file.writestr("summary.md", md_content)

        # 3. Transcript JSON
        transcript_data = event.transcript or SAMPLE_TELUGU_TRANSCRIPT
        zip_file.writestr("transcript.json", json.dumps(transcript_data, indent=2, ensure_ascii=False))

        # 4. Standalone Offline Reader index.html (Works 100% offline without internet!)
        offline_html = f"""<!DOCTYPE html>
<html lang="te">
<head>
  <meta charset="UTF-8">
  <title>Swecha Vedika — Offline Pack: {event.title}</title>
  <style>
    body {{
      font-family: 'Segoe UI', system-ui, sans-serif;
      margin: 0;
      padding: 24px;
      background-color: #FBF5EA;
      color: #2B211A;
      line-height: 1.6;
    }}
    .header {{
      background-color: #7A1F1A;
      color: white;
      padding: 20px 28px;
      border-radius: 12px;
      margin-bottom: 24px;
    }}
    .card {{
      background: white;
      border: 1px solid #E4D6C3;
      border-radius: 12px;
      padding: 24px;
      margin-bottom: 24px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }}
    .summary-box {{
      background-color: #fef9f1;
      border-left: 4px solid #C9962F;
      padding: 16px;
      border-radius: 4px;
      white-space: pre-line;
    }}
    .transcript-item {{
      padding: 12px;
      border-bottom: 1px solid #eee;
    }}
    .speaker {{
      font-weight: bold;
      color: #7A1F1A;
      font-size: 0.9em;
    }}
    .badge {{
      display: inline-block;
      padding: 4px 10px;
      border-radius: 12px;
      background: #D9622B;
      color: white;
      font-size: 0.8em;
    }}
  </style>
</head>
<body>
  <div class="header">
    <span class="badge">OFFLINE BUNDLE</span>
    <h1 style="margin: 8px 0 4px 0;">🚩 {event.title}</h1>
    <p style="margin: 0; opacity: 0.9;">స్వేచ్ఛ వేదిక డిజిటల్ రిసోర్స్ ప్యాక్ (Offline Learning Pack)</p>
  </div>

  <div class="card">
    <h2>💡 Key Takeaways & Telugu AI Summary</h2>
    <div class="summary-box">{summary_text}</div>
  </div>

  <div class="card">
    <h2>🎙️ Full Bilingual Transcript ({event.language})</h2>
    <div id="transcript-container">
      {"".join([f'<div class="transcript-item"><div class="speaker">{seg.get("speaker", "Speaker")} [{seg.get("start", 0)}s - {seg.get("end", 0)}s]</div><div>{seg.get("text", "")}</div></div>' for seg in transcript_data])}
    </div>
  </div>

  <footer style="text-align: center; color: #5C4C3E; font-size: 0.85em; margin-top: 40px;">
    Swecha Vedika Open Source Platform • Designed for Rural Community Education & Free Software Outreach
  </footer>
</body>
</html>"""
        zip_file.writestr("index.html", offline_html)

    zip_buffer.seek(0)
    return Response(
        content=zip_buffer.getvalue(),
        media_type="application/zip",
        headers={
            "Content-Disposition": f'attachment; filename="swecha_offline_pack_{str(event.id)[:8]}.zip"'
        },
    )
