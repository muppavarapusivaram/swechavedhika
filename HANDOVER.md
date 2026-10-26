# Swecha Vedika — Project Handover & Roadmap Document

> **Document Purpose**: This comprehensive document provides the incoming developer with a complete architectural breakdown of what has been implemented so far, how the current codebase works, and a detailed, prioritized technical roadmap of what remains to be built to bring **Swecha Vedika** from its current stage to a production-ready, academic-grade submission.

---

## Table of Contents
1. [Project Overview & Core Mission](#1-project-overview--core-mission)
2. [What Has Been Completed (Current State)](#2-what-has-been-completed-current-state)
3. [Current Architecture & File Structure](#3-current-architecture--file-structure)
4. [Developer Quickstart & Current Verification](#4-developer-quickstart--current-verification)
5. [What Needs to Be Completed (Detailed Roadmap)](#5-what-needs-to-be-completed-detailed-roadmap)
   - [Phase 2: Hybrid Room-to-Broadcast (HLS/LL-HLS) & Stage Promotion](#phase-2-hybrid-room-to-broadcast-hlsll-hls--stage-promotion)
   - [Phase 3: Peer-Assisted (P2P) Streaming Delivery Mesh](#phase-3-peer-assisted-p2p-streaming-delivery-mesh)
   - [Phase 4: WhatsApp Bot as the Front Door](#phase-4-whatsapp-bot-as-the-front-door)
   - [Phase 5: Replay-as-Live Engine & Live Q&A/Polls](#phase-5-replay-as-live-engine--live-qapolls)
   - [Phase 6: Multilingual ASR (Whisper), Searchable Archive & Telugu Corpus](#phase-6-multilingual-asr-whisper-searchable-archive--telugu-corpus)
   - [Phase 7: Resilience Layer, Redis Session Store & Host Migration](#phase-7-resilience-layer-redis-session-store--host-migration)
   - [Phase 8: MinIO Object Storage, Offline Packs & Observability](#phase-8-minio-object-storage-offline-packs--observability)
6. [Prioritized Implementation Sequence](#6-prioritized-implementation-sequence)
7. [Technical Debt, Traps & Architecture Guidelines](#7-technical-debt-traps--architecture-guidelines)

---

## 1. Project Overview & Core Mission

**Swecha Vedika** (*"Vedika"* is Telugu for *Stage/Platform*) is an open-source, self-hosted, bandwidth-frugal live meeting and broadcast platform designed specifically for non-profits, student communities, and civil-society organizations.

### The Real-World Problem
Swecha routinely runs developer sprints, community workshops, and language-technology outreach sessions drawing 150 to 500+ participants across Telangana and Andhra Pradesh. Commercial platforms (Zoom, Google Meet, Teams) charge unsustainable recurring licensing fees once events cross standard free tiers. Furthermore, rural and semi-urban participants join on budget Android smartphones over unstable mobile data (2G/3G/spotty 4G), with volunteer hosts presenting over inconsistent home broadband.

### Core Architectural Vision
Instead of a generic video conferencing tool, Swecha Vedika combines:
1. **Hybrid Core**: An interactive two-way SFU room (~20 speakers/hosts) transcoded into a low-latency one-to-many broadcast for hundreds of audience viewers.
2. **P2P Relay Mesh**: Viewers relay stream segments over browser-native WebRTC data channels, enabling modest two-CPU hardware to serve 500+ viewers.
3. **WhatsApp Front Door**: RSVP, reminder notifications, live Q&A submission, and post-session summaries delivered via WhatsApp (where users actually live).
4. **Replay-as-Live**: Pre-recorded sessions streamed on schedule with live chat/polls.
5. **Telugu-First ASR & Search**: Automatic Whisper transcription (Telugu, English, code-mixed) feeding a searchable archive and contributing to Swecha’s open-source Telugu language corpus.
6. **Resilience & Offline Packs**: Session state in Redis with automatic host failover, plus downloadable offline bundles (audio + slides + transcript) for disconnected learners.

---

## 2. What Has Been Completed (Current State)

The project currently has a working, fully Dockerized core with live two-way WebRTC video capabilities, database persistence, and a custom branded React frontend:

| Component | Status | Implementation Details |
| :--- | :---: | :--- |
| **Docker Compose Orchestration** | ✅ Done | 4 services running together: `db` (Postgres 16), `livekit` (LiveKit WebRTC Server), `backend` (FastAPI), and `frontend` (React + Vite). |
| **Relational Schema & Migrations** | ✅ Done | PostgreSQL schema for `users`, `events`, and `attendance` with UUID keys, native enums (`user_role`, `event_status`), timestamps, foreign keys with cascade deletion, and Alembic migrations. |
| **Automatic Startup Migrations** | ✅ Done | Container entrypoint (`backend/entrypoint.sh`) runs `alembic upgrade head` before Uvicorn starts. Safe and idempotent. |
| **JWT Authentication** | ✅ Done | Password hashing with `bcrypt` via `passlib`, HS256 JWT tokens, `/auth/register`, `/auth/login`, and `/auth/me` with `get_current_user` dependency. Passwords never exposed. |
| **Event CRUD & Attendance API** | ✅ Done | `/events` (list), `/events` (create), `/events/{id}` (retrieve), and `/events/{id}/join` (idempotent attendance recording). |
| **LiveKit Server Token Endpoint** | ✅ Done | `POST /events/{event_id}/token` generates signed LiveKit WebRTC tokens scoped to the event room with publish/subscribe grants. |
| **Swecha Vedika Design System** | ✅ Done | Custom CSS properties in `index.css` (`--maroon`, `--orange`, `--gold`, `--cream`, `--white`, `--ink`, `--slate`, `--border`, `--success`, `--error`), responsive typography, button micro-interactions, and card hover elevations. |
| **React Web Client** | ✅ Done | Client-side routing (`react-router-dom`), in-memory JWT authentication context (`AuthContext`), registration page, login page, responsive event dashboard, and collapsible event creation form. |
| **Live WebRTC Video Room** | ✅ Done | `/room/:eventId` route utilizing `@livekit/components-react` connecting to local LiveKit server with two-way camera/mic video tiles, mute toggles, and participant name tags. |
| **Git & Version Control** | ✅ Done | Pushed to GitHub at `https://github.com/muppavarapusivaram/swechavedhika`. |

---

## 3. Current Architecture & File Structure

```
prototype/
├── docker-compose.yml              # 4 services: db, livekit, backend, frontend
├── .env.example                    # Template environment variables
├── .env                            # Active environment variables (git-ignored)
├── .gitattributes                  # Enforces LF line endings for Linux scripts
├── .gitignore                      # Excludes .env, node_modules, cache
├── README.md                       # Complete operational documentation
├── backend/
│   ├── Dockerfile                  # Python 3.11-slim container
│   ├── entrypoint.sh               # Runs alembic upgrade head -> uvicorn --reload
│   ├── requirements.txt            # Pinned dependencies (FastAPI, Alembic, LiveKit SDK, etc.)
│   ├── alembic.ini                 # Migration config
│   ├── api_tests.http              # 12 ready-to-run REST client test cases
│   ├── alembic/
│   │   ├── env.py                  # Dynamic DB URL resolution
│   │   ├── script.py.mako
│   │   └── versions/
│   │       └── 001_initial_schema.py # Initial migration (users, events, attendance)
│   └── app/
│       ├── main.py                 # FastAPI application root & CORS
│       ├── database.py             # SQLAlchemy engine & session factory
│       ├── models.py               # User, Event, Attendance ORM models
│       ├── schemas.py              # Pydantic v2 validation models
│       ├── auth.py                 # Password hashing & JWT dependency
│       └── routers/
│           ├── auth.py             # /auth/register, /auth/login, /auth/me
│           └── events.py           # /events CRUD, join, and /events/{id}/token
└── frontend/
    ├── Dockerfile                  # Node 20-alpine container
    ├── package.json                # React 18, Vite, React Router, LiveKit components
    ├── vite.config.js              # Host 0.0.0.0, port 5173, polling watch for Docker
    ├── index.html                  # HTML entry point
    └── src/
        ├── main.jsx                # BrowserRouter, AuthProvider, LiveKit styles
        ├── App.jsx                 # Route definitions (/, /login, /register, /dashboard, /room/:eventId)
        ├── index.css               # Swecha Vedika civic-tech design system
        ├── api/
        │   └── client.js           # API fetch wrapper with Bearer token injection
        ├── context/
        │   └── AuthContext.jsx     # In-memory JWT auth state (no localStorage)
        ├── components/
        │   ├── Navbar.jsx          # Maroon brand header with user pill & logout
        │   ├── ProtectedRoute.jsx  # Auth guard
        │   ├── EventCard.jsx       # Card with date formatting, join button, and "Enter Room"
        │   ├── CreateEventForm.jsx # Expandable accordion event creation form
        │   └── LoadingSpinner.jsx  # Branded loading spinner
        └── pages/
            ├── LoginPage.jsx       # Branded sign-in card
            ├── RegisterPage.jsx    # Branded account creation card
            ├── DashboardPage.jsx   # Event list, creation, join actions, empty state
            └── RoomPage.jsx        # LiveKit WebRTC interactive video room
```

---

## 4. Developer Quickstart & Current Verification

### Starting the System
From the project root:
```bash
# 1. Ensure .env exists (copy from .env.example if new setup)
cp .env.example .env

# 2. Build and run all 4 containers in background
docker compose up --build -d

# 3. Check status
docker compose ps
```

### Port Mappings
- **Frontend**: [http://localhost:5173](http://localhost:5173)
- **Backend API & Swagger Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **PostgreSQL Database**: `localhost:5432` (`postgres:postgres`, DB: `prototype_db`)
- **LiveKit WebRTC Server**: `ws://localhost:7880` (HTTP/WS), `7881` (TCP), `7882/udp` (UDP)

### Running Automated Verification Tests
A test script is included in `scratch/test_step5.py`:
```bash
python scratch/test_step5.py
```
This tests user authentication, event fetching, LiveKit token issuance, and error states.

---

## 5. What Needs to Be Completed (Detailed Roadmap)

To fulfill the complete vision in the Swecha Vedika Project Proposal, the following modules must be built. Each module is explained below with technical architecture, recommended open-source tools, and exact requirements.

---

### Phase 2: Hybrid Room-to-Broadcast (HLS/LL-HLS) & Stage Promotion

#### Goal
In the current setup, all participants join the LiveKit WebRTC room. This works for up to ~20 simultaneous speakers, but scaling to 500+ viewers via WebRTC alone will overwhelm CPU and bandwidth on budget servers. The system must decouple the two-way speaker room from the mass audience broadcast.

#### Architecture
```
[20 Speakers in LiveKit WebRTC Room]
                │
                ▼ (LiveKit Egress / FFmpeg Transcoder)
       [HLS / LL-HLS Packager]
         ├── 720p Video (High)
         ├── 360p Video (Medium)
         └── Audio-Only + Slide Snapshot (2G Mode)
                │
                ▼
      [Viewer Video Player (HLS.js)]
```

#### What Needs to Be Built
1. **LiveKit Egress Service**:
   - Add the official `livekit/egress` service to `docker-compose.yml`.
   - Configure Egress to capture the active LiveKit room and pipe an RTMP/HLS stream out via FFmpeg.
2. **HLS Packaging & Storage**:
   - Transcode the room into an adaptive bitrate (ABR) ladder:
     - 720p @ 1200 kbps (Broadband)
     - 360p @ 400 kbps (Mobile data)
     - Audio-only (64 kbps Opus/AAC) + periodic JPEG slide snapshot (for 2G conditions).
   - Output `.m3u8` playlists and `.ts`/`.m4s` segments into a web-accessible directory or MinIO bucket.
3. **Frontend Audience Player**:
   - Create an audience player page using `HLS.js` / Video.js.
   - If user role is `viewer`, default to watching the low-latency HLS stream instead of connecting full WebRTC.
4. **"Raise Hand to Join Stage" Mechanism**:
   - Add a `hand_raised` boolean to the `attendance` table or Redis live session state.
   - Viewer clicks "Raise Hand" in HLS viewer.
   - Host/Moderator sees a queue of raised hands on their dashboard.
   - Host clicks "Promote to Speaker".
   - Backend grants the user speaker permissions and issues a full LiveKit WebRTC room token.
   - The user's browser seamlessly switches from the HLS player to the two-way LiveKit video grid.

---

### Phase 3: Peer-Assisted (P2P) Streaming Delivery Mesh

#### Goal
This is the **primary systems contribution** for the academic project: proving that a small server with 2 CPUs can serve 500+ viewers by letting audience members relay already-downloaded HLS segments to each other over WebRTC DataChannels.

#### Architecture
```
                    [Origin Server (Seeds 1 copy)]
                               │
            ┌──────────────────┴──────────────────┐
            ▼                                     ▼
      [Viewer Node A] ──(WebRTC DataChannel)── [Viewer Node B]
            │                                     │
            └───────────────► [Viewer Node C] ◄───┘
```

#### What Needs to Be Built
1. **P2P Streaming Engine**:
   - Integrate `p2p-media-loader` (open-source library for HLS.js) into the frontend viewer player.
   - `p2p-media-loader` hooks into HLS.js segment fetching:
     - Checks if connected peers in the swarm have the requested segment.
     - Downloads segment from a peer over WebRTC DataChannel if available.
     - Falls back to downloading from the origin server if peers do not respond within a deadline.
2. **Signaling / Swarm Tracker**:
   - Run a lightweight WebRTC signaling / tracker server in Docker (e.g. `bittorrent-tracker` or custom WebSocket tracker).
   - Peers announce which event room they are watching and exchange SDP offers to form the local swarm.
3. **Bandwidth Savings Telemetry & Evaluation**:
   - The frontend player reports metrics back to the backend:
     - Bytes downloaded from HTTP origin vs. bytes downloaded from P2P peers.
   - Store these metrics in PostgreSQL or Prometheus.
   - Build a comparison chart in the host dashboard: **Origin Bandwidth vs. Concurrent Viewers (with vs. without P2P)**. *This chart is the key measurable outcome required by Section 9 of the proposal.*

---

### Phase 4: WhatsApp Bot as the Front Door

#### Goal
Lower the adoption barrier for students and rural volunteers who do not use email or complex dashboards. Users register, receive reminders, submit Q&A questions, and get post-session notes directly inside WhatsApp.

#### Architecture
```
[User on WhatsApp] ◄──► [WhatsApp Business Cloud API] ◄──► [FastAPI Webhook Service]
                                                                  │
                                                        [Swecha Vedika Core DB]
```

#### What Needs to Be Built
1. **Webhook Endpoint in Backend**:
   - Add `POST /webhook/whatsapp` and `GET /webhook/whatsapp` (for Meta webhook challenge verification).
   - Read `WHATSAPP_TOKEN`, `WHATSAPP_PHONE_NUMBER_ID`, and `WHATSAPP_VERIFY_TOKEN` from environment.
2. **Conversational Workflows**:
   - **Registration**: User sends *"Join"* or clicks an event link -> Bot asks for Name -> Registers user in DB and confirms RSVP.
   - **Event Reminders**: Celery / background cron job checks events starting in 15 minutes -> Sends WhatsApp template message with one-click direct access link.
   - **Live Q&A Submission**: During an event, user messages a question -> Bot tags it to the event and pushes it to the moderator Q&A queue.
   - **Post-Event Summary**: Once an event ends and transcription completes, the bot automatically messages attendees a 5-bullet summary and link to slides.
3. **Local Development Mock**:
   - Because Meta WhatsApp Business accounts require verification, create a **Mock WhatsApp Webhook Simulator** (a simple frontend test widget or script) so development and automated tests can run without real WhatsApp credentials.

---

### Phase 5: Replay-as-Live Engine & Live Q&A/Polls

#### Goal
Allows a volunteer in any district to re-broadcast an expert's past recording as if it were a live event, while the local volunteer runs live chat, polls, and Q&A on top of the stream.

#### Architecture
```
[Pre-Recorded MP4 in MinIO]
            │
            ▼ (FFmpeg RTMP/HLS loop on scheduled start)
[Simulated Live HLS Broadcast] ◄────► [Realtime Live Q&A & Polls via WebSockets/Redis]
```

#### What Needs to Be Built
1. **Replay-as-Live Scheduler**:
   - New database fields in `events`: `is_replay` (bool), `source_recording_id` (UUID), `playback_offset` (seconds).
   - A background worker (APScheduler or Celery) monitors scheduled replay events.
   - At the scheduled start time, the engine initiates HLS streaming of the recorded video file synchronized across all viewers.
2. **Real-time Live Q&A & Polls Service**:
   - Add Redis to `docker-compose.yml` (`redis:7-alpine`).
   - Implement WebSocket endpoints in FastAPI:
     - `WS /ws/events/{event_id}/qa`: Upvoted questions, answer tracking.
     - `WS /ws/events/{event_id}/polls`: Multiple-choice live polls created by host, real-time vote tallying.
3. **Frontend Q&A & Polls Widget**:
   - Side panel on the room/player page showing live questions ranked by audience upvotes, and pop-up poll cards.

---

### Phase 6: Multilingual ASR (Whisper), Searchable Archive & Telugu Corpus

#### Goal
Fulfills Swecha's core language-technology mission: automatically transcribing sessions in Telugu, English, and code-mixed speech, creating a searchable archive, and exporting training data for open-source AI models.

#### Architecture
```
[Event Audio Recording] ──► [Whisper ASR Pipeline] ──► [Timestamped Transcripts]
                                                              │
                    ┌─────────────────────────────────────────┴──────────────────────┐
                    ▼                                                                ▼
         [Auto-Summarizer (LLM)]                                        [Search Index (OpenSearch)]
         • 5-bullet key takeaways                                       • Full-text keyword search
         • Action items                                                 • Timestamp jump links
```

#### What Needs to Be Built
1. **ASR Processing Worker**:
   - Asynchronous worker (Celery or background queue) triggered when an event concludes.
   - Extracts audio track (`ffmpeg -i input.mp4 -vn -acodec pcm_s16le -ar 16000 audio.wav`).
   - Runs `faster-whisper` or OpenAI Whisper model (CPU-friendly `small` or `medium` model with Telugu language prompting).
   - Generates timestamped VTT/JSON transcripts: `[ { "start": 12.5, "end": 18.2, "speaker": "Alex", "text": "..." } ]`.
2. **Auto-Summarisation Service**:
   - Feeds the transcript to an open-source LLM (via local Ollama, Mistral, or Gemini API) with a custom prompt tailored for Swecha community workshops.
   - Outputs: Brief summary, 5 key concepts, action items, and speakers list.
3. **Search Indexing & Archive UI**:
   - Index transcripts in OpenSearch / PostgreSQL full-text search (`tsvector` with pg_trgm).
   - Build `/archive` page in frontend:
     - Search bar: *"show every past session that explained Git"*.
     - Returns exact timestamped video links (clicking jumps the video player to that exact second).
4. **Consent & Corpus Export**:
   - In user settings: Checkbox *"I consent to donate my audio for Swecha's open-source Telugu language model training"*.
   - If all speakers in an event consent, provide a button to export audio snippets paired with validated text transcripts in standard HuggingFace dataset format.

---

### Phase 7: Resilience Layer, Redis Session Store & Host Migration

#### Goal
Protect live sessions against sudden power cuts, laptop battery death, or network drops common among volunteer hosts.

#### Architecture
```
[Host Disconnect Detected (Heartbeat Timeout)]
                        │
                        ▼
       [Redis Session State Manager]
                        │
       ├── 1. Elect highest-ranked Co-Host to Host
       ├── 2. Transfer LiveKit room moderator tokens
       └── 3. Instruct Recording Manager to keep stream open without split
```

#### What Needs to Be Built
1. **Redis Session State Manager**:
   - Store ephemeral room state in Redis: active host ID, co-host IDs, heartbeat timestamp, room status.
   - Host client sends heartbeat ping every 5 seconds over WebSocket.
2. **Auto-Promotion Controller**:
   - If host heartbeat expires (e.g. 15 seconds without ping):
     - Controller automatically promotes the first available co-host / moderator.
     - Broadcasts event to all participants: *"Host disconnected. Priya Rao is now presiding."*
     - LiveKit room and HLS stream remain alive without tearing down.
3. **Recording Stitching**:
   - When host disconnects and reconnects, FFmpeg recording should not terminate into two disjoint files. Use an append/concat pipeline to produce a single continuous replay recording.

---

### Phase 8: MinIO Object Storage, Offline Packs & Observability

#### Goal
Ensure recordings and offline materials are stored in a self-hosted S3-compatible store, and provide downloadable lightweight bundles for offline users.

#### What Needs to Be Built
1. **MinIO Object Storage**:
   - Add `minio/minio` to `docker-compose.yml`.
   - Configure buckets: `recordings`, `transcripts`, `offline-packs`.
2. **Offline Event Pack Generator**:
   - After each session, generate a single `.zip` pack under 25MB:
     - Highly compressed audio (Opus 24kbps).
     - Session slide deck (PDF/images).
     - Full Telugu & English text transcript.
     - Text summary and Q&A digest.
   - Provide direct download link and WhatsApp delivery for users with zero live internet.
3. **Observability Stack**:
   - Add Prometheus and Grafana services to `docker-compose.yml`.
   - LiveKit exports Prometheus metrics natively on port `7880/metrics`.
   - Build a simple Grafana dashboard monitoring:
     - Active participant count.
     - Bandwidth consumed.
     - P2P relay ratio.
     - Container CPU and RAM usage.

---

## 6. Prioritized Implementation Sequence

For the next developer taking over, here is the recommended sprint schedule:

```
┌──────────────────────────────────────────────────────────────────────────┐
│ SPRINT 1: Hybrid Broadcast & Stage Promotion                             │
│ • Add LiveKit Egress / FFmpeg HLS packager to docker-compose.            │
│ • Add HLS.js viewer page for audience members.                           │
│ • Implement "Raise Hand" and Host "Promote to Speaker" flow.             │
└──────────────────────────────────────────────────────────────────────────┘
                                     │
                                     ▼
┌──────────────────────────────────────────────────────────────────────────┐
│ SPRINT 2: P2P Delivery Mesh & Bandwidth Metrics (Core Project Novelty)   │
│ • Integrate p2p-media-loader in HLS.js player.                           │
│ • Deploy WebRTC swarm tracker in Docker.                                 │
│ • Instrument origin vs P2P bandwidth metrics and graph in dashboard.     │
└──────────────────────────────────────────────────────────────────────────┘
                                     │
                                     ▼
┌──────────────────────────────────────────────────────────────────────────┐
│ SPRINT 3: Multilingual Transcription & Archive (Swecha Mission Alignment)│
│ • Add Whisper background audio processing task.                          │
│ • Store timestamped VTT transcripts in PostgreSQL / OpenSearch.          │
│ • Build the /archive search page with timestamp seeking.                 │
└──────────────────────────────────────────────────────────────────────────┘
                                     │
                                     ▼
┌──────────────────────────────────────────────────────────────────────────┐
│ SPRINT 4: Replay-as-Live & Realtime Q&A/Polls                            │
│ • Add Redis to Docker Compose.                                           │
│ • Build WebSocket live Q&A upvoting and polling backend + UI.            │
│ • Add replay scheduler engine streaming pre-recorded files on schedule.  │
└──────────────────────────────────────────────────────────────────────────┘
                                     │
                                     ▼
┌──────────────────────────────────────────────────────────────────────────┐
│ SPRINT 5: WhatsApp Bot & Offline Packs                                   │
│ • Implement WhatsApp Cloud API webhook + local test simulator.           │
│ • Build RSVP, reminder, and summary dispatch flows.                      │
│ • Generate downloadable lightweight offline event packs (.zip).          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 7. Technical Debt, Traps & Architecture Guidelines

When continuing this codebase, adhere strictly to these rules:

1. **Keep Secrets Out of Git**:
   - `.env` is ignored by `.gitignore`. Never hardcode secrets in `docker-compose.yml` or Python files. Always use `.env.example` as the source of truth for new configuration keys.
2. **Linux Line Endings in Shell Scripts**:
   - Files like `backend/entrypoint.sh` **must** retain Unix `LF` line endings. Windows `CRLF` will cause Docker startup failure (`/app/entrypoint.sh: line 1: $'\r': command not found`). The included `.gitattributes` file enforces this automatically.
3. **In-Memory JWT vs LocalStorage**:
   - The frontend intentionally maintains JWT tokens in React state (`AuthContext`) rather than `localStorage` to avoid XSS vulnerabilities and mirror clean session lifecycles. If persistent login is added later, implement httpOnly secure cookies, not plain `localStorage`.
4. **PostgreSQL Native Enums**:
   - If you modify enum values in `app/models.py`, generate a formal Alembic migration using `ALTER TYPE ... ADD VALUE`. Do not rely on SQLAlchemy auto-drop/create as Postgres will reject altering enums in use by existing tables.
5. **LiveKit ICE Candidates on Localhost**:
   - In `docker-compose.yml`, LiveKit runs with `--dev --bind 0.0.0.0 --node-ip 127.0.0.1`. When deploying to a cloud VM or physical campus server, `--node-ip` **must** be updated to the server's public or LAN IP address so remote clients can negotiate WebRTC media ports.
6. **Preserve the Civic-Tech Design System**:
   - All new pages must use the CSS custom properties defined in `frontend/src/index.css`. Avoid ad-hoc inline hex colors or unstyled utility classes.

---
*Created by: Muppavarapu Sivaram & Google Antigravity Engineering Assistant*  
*Project: Swecha Vedika — KLU Open Source Community (KLUG) × Swecha / FSMI*
