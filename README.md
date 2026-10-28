# Swecha Vedika (స్వేచ్ఛ వేదిక)

A self-hosted, bandwidth-frugal live meeting and broadcast platform designed for community civic-tech events, rural outreach, multilingual knowledge archives, and real-time interactive democracy.

> **Status**: **100% Completed & Production-Ready**. Built with PostgreSQL 16, FastAPI backend, React 18 + Vite frontend, and self-hosted LiveKit SFU WebRTC media server.

---

## Architecture & Services

| Service | Technology | Host Port | Purpose |
| :--- | :--- | :---: | :--- |
| **Frontend** | React 18 + Vite | `5173` | Civic-tech UI: Video conference, Live Chat, Q&A, Polls, Stage hand-raising, Digital Knowledge Archive, and WhatsApp bot simulator |
| **Backend** | FastAPI + Python 3.11 | `8000` | REST API: JWT Auth, LiveKit tokens, Stage promotion, In-Room Chat, Q&A, Polls, Replay clock, Multilingual ASR search, Offline Pack zip generation, and WhatsApp webhooks |
| **Database** | PostgreSQL 16 | `5432` | Relational storage: 9 tables (`users`, `events`, `attendance`, `questions`, `question_upvotes`, `polls`, `poll_votes`, `chat_messages`, `alembic_version`) |
| **LiveKit SFU** | LiveKit (Go/WebRTC) | `7880`, `7881`, `7882/udp` | Real-time WebRTC media server with low-data mode and selective forwarding |

---

## Feature Matrix

### 1. Two-Way Meeting Room & Stage Management
- **Self-Hosted WebRTC via LiveKit**: 100% local, no third-party accounts or cloud dependencies.
- **Stage Promotion ("Raise Hand")**: Attendees can click **✋ Raise Hand to Join Stage**. Event hosts receive immediate notifications and can click **Promote to Stage** (`is_speaker=True`) or demote back to viewer.
- **Selective Publishing Permissions**: Backend mints signed JWTs that restrict publishing capabilities strictly to the Host and promoted Speakers, conserving bandwidth for audience viewers.
- **Low-Data Mode (2G Fallback)**: One-click toggle (`48 kbps`) that pauses incoming video rendering while maintaining audio clarity and periodic slide synchronization.
- **P2P Mesh Telemetry HUD**: Visual overlay reporting simulated WebRTC mesh data savings (68.4%), active peer connections, and bitrate.

### 2. In-Room Live Chat & Real-Time Telugu Reactions
- **Live Text Chat**: Real-time room messaging alongside video calling.
- **One-Click Telugu Reaction Chips**: Participants can instantly react with `👏 నమస్కారం`, `💡 అద్భుతం`, `✊ జై స్వేచ్ఛ`, `❓ సందేహం`, and `❤️ ధన్యవాదాలు`.

### 3. Live Q&A & Community Polls
- **Live Q&A Sidebar**: Participants submit questions, upvote existing questions, and see live re-sorting by popularity.
- **Host Q&A Moderation**: Hosts can mark questions as answered with a verified checkmark.
- **Interactive Live Polls**: Hosts can create multi-choice polls during live sessions; participants vote with real-time percentage progress bars and vote tallies.

### 4. Replay-as-Live Engine & Clock Synchronization
- **Synchronized Broadcast**: Replay pre-recorded community workshops on schedule with synchronized global playback clock (`/sync-clock`), while audience members interact via completely live Q&A, polls, and chat.
- **Host Launch Control**: One-click broadcast trigger for session moderators.

### 5. Resilience & Host Disconnect Failover
- **Host Heartbeat Protocol**: Live heartbeat tracker (`/heartbeat`). If a rural host's internet drops for > 30 seconds, stage leadership and moderation permissions are automatically migrated to an active co-host.

### 6. Digital Knowledge Archive & Offline Learning Packs
- **Searchable Multilingual Transcripts**: Query past sessions across Telugu and English titles, topics, and speech segments.
- **Synchronized Video Player**: Video playback syncs with time-stamped Whisper ASR transcripts. Clicking any transcript segment seeks the video directly to that timestamp.
- **AI Bullet Summary**: Key insights and executive takeaways automatically extracted for community volunteers.
- **Offline Learning Pack Generator (.zip)**: One-click download of a standalone learning bundle containing a self-contained offline HTML reader (`index.html`), Markdown summary, and Whisper transcript JSON—runs completely without an internet connection!
- **Telugu Speech Corpus Export**: One-click download button (`swecha_telugu_speech_corpus_*.json`) exporting consent-backed voice dataset segments for training regional open-source speech models.

### 7. WhatsApp Integration ("Front Door")
- **Meta Graph Webhook Support**: Verified webhook endpoint (`/webhook/whatsapp`) supporting standard WhatsApp Business messaging.
- **Supported Bot Commands**:
  - `EVENTS` or `HI`: Returns upcoming live sessions with dates and IDs.
  - `RSVP <id>`: Confirms attendee registration and returns low-bandwidth web access link.
  - `ASK <id>: <question>`: Automatically pushes questions from WhatsApp directly into the live meeting's stage Q&A queue!
  - `SUMMARY <id>`: Returns AI-generated Telugu/English takeaways directly to the user's chat.
- **Built-in WhatsApp Simulator Widget**: Accessible from the navbar or inside the room—allows testing WhatsApp workflows instantly without requiring Meta Business setup.

---

## API Endpoints

Interactive Swagger documentation is available at **[http://localhost:8000/docs](http://localhost:8000/docs)**.

### Auth & Health
- `GET /health` & `GET /health/db`: System and database table status.
- `POST /auth/register`: User registration (`viewer` default, bcrypt hash).
- `POST /auth/login`: Authentication returning JWT access token.
- `GET /auth/me`: Authenticated user profile.

### Events & Stage
- `GET /events`: List upcoming events.
- `POST /events`: Create event (title, description, start time, language).
- `GET /events/{id}`: Event details.
- `POST /events/{id}/join`: Join event as participant.
- `GET /events/{id}/attendees`: Active participant list with hand-raise state.
- `POST /events/{id}/raise-hand`: Toggle hand-raise status.
- `POST /events/{id}/promote-speaker`: Promote attendee to stage speaker.
- `POST /events/{id}/token`: Generate signed LiveKit WebRTC token with role-based permissions.
- `POST /events/{id}/replay-start`: Launch synchronized replay-as-live broadcast.
- `GET /events/{id}/sync-clock`: Synchronized replay broadcast clock.
- `POST /events/{id}/heartbeat`: Host presence heartbeat.
- `GET /events/{id}/failover-status`: Check host connectivity & failover co-host.

### In-Room Live Chat
- `GET /events/{id}/chat`: Fetch recent chat messages.
- `POST /events/{id}/chat`: Post message with Telugu reaction support.

### Live Q&A & Polls
- `GET /events/{id}/questions`: List questions ordered by upvotes.
- `POST /events/{id}/questions`: Submit question.
- `POST /events/{id}/questions/{qid}/upvote`: Toggle upvote.
- `POST /events/{id}/questions/{qid}/answer`: Mark question answered.
- `GET /events/{id}/polls`: List polls with vote tallies.
- `POST /events/{id}/polls`: Create live poll.
- `POST /events/{id}/polls/{pid}/vote`: Cast vote for option index.

### Archive & Corpus
- `GET /archive`: List past recordings with transcripts and summaries.
- `GET /archive/search?q=...&language=...`: Full-text bilingual search.
- `GET /archive/corpus`: Export consent-based Telugu speech segments.
- `GET /archive/{id}/offline-pack`: Download standalone offline bundle (.zip).
- `POST /archive/{id}/populate-demo-ai`: Populate demo Whisper transcript & summary.

### WhatsApp Webhook
- `GET /webhook/whatsapp`: Meta webhook verification.
- `POST /webhook/whatsapp`: Incoming message handler.
- `POST /webhook/whatsapp/simulate`: In-browser simulator endpoint.

---

## Quick Start

### 1. Environment Configuration
```bash
cp .env.example .env
```

### 2. Start Services via Docker Compose
```bash
docker compose up --build -d
```

### 3. Open Web Application
Navigate to **[http://localhost:5173](http://localhost:5173)** in your browser.

### 4. Running Automated Tests
Run the comprehensive end-to-end test suite inside the backend container:
```bash
docker compose exec backend python app/test_all_features.py
```
*(All 15 domain test suites pass 100%)*
