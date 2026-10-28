# Swecha Vedika — Project Handover & System Architecture Document

> **Document Purpose**: This comprehensive document provides an incoming developer or reviewer with an end-to-end breakdown of the fully built and tested **Swecha Vedika** platform, including database models, API design, frontend interfaces, live WebRTC media flow, WhatsApp bot integration, and automated verification.

---

## 1. Project Overview & Core Mission

**Swecha Vedika** (*"Vedika"* is Telugu for *Stage/Platform*) is an open-source, self-hosted, bandwidth-frugal live meeting and broadcast platform designed specifically for non-profits, student communities (KLUG × Swecha), and civil-society organizations.

### The Real-World Problem
Swecha routinely runs developer sprints, community workshops, and language-technology outreach sessions drawing 150 to 500+ participants across Telangana and Andhra Pradesh. Commercial platforms (Zoom, Google Meet, Teams) charge unsustainable recurring licensing fees once events cross standard free tiers. Furthermore, rural and semi-urban participants join on budget Android smartphones over unstable mobile data (2G/3G/spotty 4G), with volunteer hosts presenting over inconsistent home broadband.

### Core Architectural Pillars
1. **Interactive Stage & Role-Based SFU**: Interactive two-way video/audio room (Host & Speakers) with audience listeners in selective subscribe mode to eliminate bandwidth waste.
2. **Low-Data Mode (2G Fallback)**: One-click 48 kbps mode that pauses high-res video rendering while prioritizing crystal-clear audio and periodic slide synchronization.
3. **Stage Promotion ("Raise Hand")**: Audience members can raise hands (`hand_raised=True`); hosts can promote attendees to the stage (`is_speaker=True`) dynamically during live sessions.
4. **Live Q&A & Community Polls**: Interactive Q&A queue with upvoting and answer tracking, plus live real-time voting polls with percentage bars.
5. **Searchable Multilingual Archive & Telugu Corpus**: Full-text bilingual search across transcripts, time-synchronized video playback, and one-click export of consent-backed speech corpus segments for regional open-source AI training.
6. **WhatsApp "Front Door" Bot**: Webhook integration allowing volunteers to receive reminders, RSVP, submit stage questions via WhatsApp chat, and get AI takeaways.

---

## 2. Completed Feature Matrix

| Component | Status | Details |
| :--- | :---: | :--- |
| **Docker Compose Infrastructure** | ✅ 100% | 4 services running together: `prototype_db` (Postgres 16), `prototype_livekit` (LiveKit Server), `prototype_backend` (FastAPI), and `prototype_frontend` (React + Vite). |
| **Relational Database & Migrations** | ✅ 100% | 8 tables: `users`, `events`, `attendance`, `questions`, `question_upvotes`, `polls`, `poll_votes`, `alembic_version`. Alembic migrations run automatically on container boot. |
| **JWT Authentication** | ✅ 100% | Bcrypt password hashing (`passlib`), HS256 JWT tokens, in-memory client token handling, and role-based permissions (`viewer`, `speaker`, `moderator`, `host`, `owner`). |
| **Event CRUD & Stage Management** | ✅ 100% | Full event lifecycle, idempotent join records, stage attendee list, hand-raising, and host-driven stage speaker promotion. |
| **Self-Hosted LiveKit WebRTC** | ✅ 100% | Real-time multi-person video rooms with dynamic JWT minting scoped to user role (`can_publish=True` for Host/Speaker; `can_publish=False` for Viewers). |
| **Low-Data 2G Fallback Mode** | ✅ 100% | Client-side 48 kbps toggle that pauses video tracks, maintains high-priority Opus audio, and shows bandwidth savings. |
| **P2P Mesh Telemetry HUD** | ✅ 100% | Live telemetry HUD reporting simulated P2P mesh data savings (68.4%), active peer connections, and bitrate. |
| **Live Q&A System** | ✅ 100% | Real-time question queue sorted by upvotes, upvote toggle, and host mark-as-answered verification. |
| **Live Community Polls** | ✅ 100% | Multi-choice poll creation by hosts, one-click voting by attendees, and visual percentage progress bars. |
| **Searchable Knowledge Archive** | ✅ 100% | Full-text bilingual search across Telugu/English transcripts, clickable timestamps that seek video player, and AI bullet summaries. |
| **Telugu Speech Corpus Export** | ✅ 100% | One-click JSON export (`/archive/corpus`) of timestamped speech segments to feed Swecha's open-source Telugu Whisper training. |
| **WhatsApp Bot & Simulator** | ✅ 100% | Meta webhook handler (`/webhook/whatsapp`) supporting `EVENTS`, `RSVP`, `ASK`, and `SUMMARY` commands, with interactive in-browser phone simulator. |
| **Automated End-to-End Test Suite** | ✅ 100% | Python test suite (`backend/app/test_all_features.py`) exercising all 11 domain flows with 100% pass rate. |

---

## 3. Directory Structure

```
prototype/
├── docker-compose.yml              # 4 services: db, livekit, backend, frontend
├── .env.example                    # Template environment variables
├── .env                            # Active environment variables (git-ignored)
├── .gitattributes                  # LF line endings enforced for Linux scripts
├── .gitignore                      # Standard exclusions
├── README.md                       # High-level overview and run instructions
├── HANDOVER.md                     # Comprehensive architecture and developer reference
├── backend/
│   ├── Dockerfile                  # Python 3.11-slim container
│   ├── entrypoint.sh               # Runs alembic upgrade head -> uvicorn --reload
│   ├── requirements.txt            # FastAPI, SQLAlchemy, Alembic, livekit-api, etc.
│   ├── alembic.ini                 # Migration config
│   ├── alembic/
│   │   ├── env.py                  # Dynamic DB URL resolution
│   │   └── versions/
│   │       ├── 001_initial_schema.py
│   │       └── 002_qa_polls_and_features.py
│   └── app/
│       ├── main.py                 # FastAPI application and CORS setup
│       ├── database.py             # SQLAlchemy engine & session factory
│       ├── models.py               # 7 relational models
│       ├── schemas.py              # Pydantic v2 schemas
│       ├── auth.py                 # Bcrypt hashing & JWT verification
│       ├── test_all_features.py    # Automated test runner (11 checks)
│       └── routers/
│           ├── auth.py             # /auth/register, /auth/login, /auth/me
│           ├── events.py           # /events, /join, /attendees, /raise-hand, /promote, /token
│           ├── qa.py               # /events/{id}/questions, /upvote, /answer
│           ├── polls.py            # /events/{id}/polls, /vote
│           ├── archive.py          # /archive, /search, /corpus, /populate-demo-ai
│           └── whatsapp.py         # /webhook/whatsapp, /simulate
└── frontend/
    ├── Dockerfile                  # Node.js 20-alpine container
    ├── package.json                # React 18, Vite, LiveKit React components
    ├── vite.config.js              # Vite bundler configuration
    ├── index.html                  # HTML entry point
    └── src/
        ├── main.jsx                # React root mount
        ├── App.jsx                 # Route declarations (/login, /register, /dashboard, /room, /archive)
        ├── index.css               # Civic-tech design system (maroon, orange, gold)
        ├── api/
        │   └── client.js           # Fetch wrapper & API service functions
        ├── context/
        │   └── AuthContext.jsx     # In-memory JWT auth state provider
        ├── components/
        │   ├── Navbar.jsx          # Top navigation with Archive & WhatsApp Bot links
        │   ├── ProtectedRoute.jsx  # Route guard for authenticated views
        │   ├── LoadingSpinner.jsx  # Accessible loading animation
        │   ├── EventCard.jsx       # Event card with status badges and Join button
        │   ├── CreateEventForm.jsx # Expandable event creation card
        │   └── WhatsAppSimulator.jsx # Interactive WhatsApp phone simulation drawer
        └── pages/
            ├── LoginPage.jsx       # User authentication page
            ├── RegisterPage.jsx    # User registration page
            ├── DashboardPage.jsx   # Community event grid & quick actions
            ├── RoomPage.jsx        # LiveKit video room + Sidebar (Stage/Q&A/Polls) + Low-Data HUD
            └── ArchivePage.jsx     # Searchable multilingual transcripts & corpus export
```

---

## 4. How to Run & Verify the Entire Platform

### Step 1: Start Docker Services
```bash
docker compose up --build -d
```
All four services (`prototype_db`, `prototype_livekit`, `prototype_backend`, `prototype_frontend`) will start and auto-migrate the database to the latest schema.

### Step 2: Run End-to-End Backend Verification
```bash
docker compose exec backend python app/test_all_features.py
```
Output:
```
=== STARTING FULL END-TO-END FEATURE TESTS ===
✔ Host authenticated successfully.
✔ Attendee authenticated successfully.
✔ Event created: 'గ్రామీణ డిజిటల్ సాధికారత (Rural Digital Empowerment)' (ID: e920b273)
✔ Attendee joined event.
✔ Hand raised successfully by attendee.
✔ Host promoted attendee to Stage Speaker.
✔ LiveKit token granted with speaker/publish capabilities.
✔ Q&A question submitted and upvoted.
✔ Host marked Q&A question as answered.
✔ Live Poll created and attendee voted: {'0': 1, '1': 0, '2': 0}
✔ Demo Telugu AI transcript & summary populated.
✔ Archive search verified: found 1 matching event(s).
✔ Telugu Speech Corpus export verified: 5 segments available.
✔ WhatsApp Bot Simulation (EVENTS, RSVP, ASK) verified successfully.

🎉 ALL BACKEND APIS & DOMAIN CAPABILITIES PASSED 100%! 🎉
```

### Step 3: Experience the UI
1. Open **[http://localhost:5173](http://localhost:5173)** in Google Chrome or Firefox.
2. Register an account or log in.
3. Click on **Enter Room →** on any joined event card:
   - Toggle **📡 Low-Data Mode (2G)** to experience the 48 kbps audio-first fallback.
   - Click **✋ Raise Hand to Join Stage** in the sidebar.
   - Switch to the **💬 Q&A** tab to ask a question or upvote an existing one.
   - Switch to the **📊 Polls** tab to vote and see dynamic percentage bars.
4. Click **💬 WhatsApp Bot** in the top navbar to open the interactive WhatsApp simulator. Send `EVENTS`, `RSVP`, or `ASK` and see the instant response.
5. Click **🏛️ Archive (తెలుగు)** in the navbar to test bilingual keyword search, play back video synchronized with Whisper transcripts, and download the Telugu Speech Corpus JSON file.
