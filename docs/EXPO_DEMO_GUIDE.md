# SAMYAK-2026 Project Expo & Prototype Demonstration Manual
## Swecha Vedika (స్వేచ్ఛ వేదిక) — Live Defense & Evaluation Guide

**Event**: SAMYAK-2026 Annual Capstone Project Expo & Technical Evaluation  
**Department**: Department of Computer Science and Engineering, K L Deemed to be University  
**Project Title**: Swecha Vedika: A Bandwidth-Frugal, Multilingual Live Stage and Knowledge Dissemination Platform for Resource-Constrained Civic Ecosystems  
**Collaborating Community**: Swecha / Free Software Movement India (FSMI) & KLUG  

---

## 1. Expo Checklist & Materials to Carry

### Hardware & Power Setup
- [x] Primary Presentation Laptop (with Docker Compose, LiveKit, Postgres, FastAPI, and Vite React frontend pre-booted).
- [x] Secondary Laptop / Mobile Smartphone (connected to local Wi-Fi or hotspot to demonstrate multi-user live call and role-based permissions).
- [x] Laptop power adapters and phone chargers.
- [x] Multi-plug extension cord / spike buster (essential for expo stalls).
- [x] HDMI / Type-C display adapter (if connecting to external stall monitor/projector).
- [x] USB Flash Drive containing:
  - Complete project repository snapshot (`.zip`).
  - Pre-downloaded sample offline learning bundle (`swecha_offline_pack_*.zip`).
  - Project Research Paper PDF and printable A3 Poster PDF (`docs/poster_a3.html`).

### Documentation & Printed Materials
- [x] Printed Project Poster (A3 Landscape in high-resolution color, generated from `docs/poster_a3.html`).
- [x] Printed Capstone Research Paper (IEEE Conference Format from `docs/RESEARCH_PAPER.md`).
- [x] Project Report / Handover Document (`HANDOVER.md`).
- [x] GitHub Repository QR Code printout (`https://github.com/muppavarapusivaram/swechavedhika`).

---

## 2. Team Member Responsibilities & Role Distribution

To fulfill the SAMYAK-2026 requirement that *"Every team member must have a clear understanding of the complete project and distribute presentation responsibilities"*:

| Team Role | Lead Assignee | Expo Responsibilities |
| :--- | :--- | :--- |
| **Architect & Lead Presenter** | Muppavarapu Sivaram | Introduces the problem statement, high-level distributed architecture, LiveKit SFU design, and answers evaluators' core technical questions. |
| **Media & Network Specialist** | Team Member 2 | Demonstrates the **LiveKit Two-Way Video Stage**, **2G Low-Data Fallback Mode**, and **P2P Mesh Telemetry HUD**; explains WebRTC bitrates and packet loss benchmarks. |
| **Stage & Interactivity Lead** | Team Member 3 | Operates the **Live Q&A Upvote Queue**, **Community Polls**, **Hand-Raising & Stage Speaker Promotion**, and **In-Room Live Chat with Telugu Reactions**. |
| **Conversational & Archive Lead** | Team Member 4 | Demonstrates the **WhatsApp "Front Door" Bot Simulator**, **Whisper Bilingual Search**, **Telugu Speech Corpus JSON Export**, and **Offline .ZIP Learning Pack**. |

---

## 3. High-Impact Live Demonstration Script (5–7 Minute Walkthrough)

When faculty evaluators or judges arrive at your stall, follow this structured, confident walkthrough:

### Step 1: The Hook & Problem Statement (1 Minute)
> *"Good morning, esteemed evaluators. We are presenting **Swecha Vedika**, a self-hosted, bandwidth-frugal live meeting and knowledge dissemination platform built for rural and civic outreach in collaboration with Swecha and the Free Software Movement India.*  
> *Existing platforms like Zoom or Google Meet charge heavy recurring licensing fees, demand high-speed broadband, and collapse over rural 2G/3G connections. Swecha Vedika solves this with an open-source, containerized platform that runs in sub-50 kbps networks, allows rural volunteers to join via WhatsApp, and preserves regional language knowledge."*

### Step 2: The Core Live Stage & 2G Low-Data Mode Demo (2 Minutes)
1. **Show Dashboard**: Navigate to `http://localhost:5173/dashboard`. Point out the civic-tech design system (Swecha maroon, orange, and gold).
2. **Enter Room**: Click **Enter Room →** to enter the live LiveKit video conference.
3. **Point Out Role Permissions**: Show that the host has stage publishing permissions (`can_publish=True`), while audience members join in subscription mode to save server egress.
4. **Trigger 2G Low-Data Mode**: Click the **📡 Low-Data Mode (2G)** toggle in the top navbar.
   - *Explain to Judges*: *"Watch how the video stream is gracefully suppressed while the audio codec (Opus) maintains crystal-clear voice clarity at just **44.8 kbps**, cutting bandwidth consumption by **68.4%** and surviving up to **35% packet loss**."*
5. **Show P2P Mesh Telemetry HUD**: Point out the live telemetry overlay showing 68.4% bandwidth saved and active WebRTC swarm nodes.

### Step 3: Interactive Stage, Chat & Community Polls (1.5 Minutes)
1. **Hand Raise & Promotion**: Show an attendee clicking **✋ Raise Hand to Join Stage**. Show the host screen receiving the notification and clicking **Promote to Stage** (`is_speaker=True`).
2. **In-Room Live Chat**: Type a message and click the Telugu reaction chips (`👏 నమస్కారం`, `💡 అద్భుతం`, `✊ జై స్వేచ్ఛ`). Point out full regional Unicode script support.
3. **Live Q&A Queue**: Ask a question, click **▲ Upvote**, and show the question dynamically rising to the top of the queue. Mark it answered as the host.
4. **Live Polls**: Create a poll (*"What is your internet speed?"*), cast a vote, and demonstrate real-time percentage progress bars.

### Step 4: WhatsApp "Front Door" Conversational Gateway (1 Minute)
1. Click the **💬 WhatsApp Bot** button in the header to open the interactive mobile phone simulator.
2. Send `EVENTS` -> Show the bot returning scheduled webinars.
3. Send `RSVP <id>` -> Show instant registration confirmation with low-data access link.
4. Send `ASK <id>: Can we deploy this on Raspberry Pi?` -> Switch back to the stage Q&A tab and show that the question sent from WhatsApp was **automatically injected directly into the live meeting queue**!

### Step 5: Digital Archive, Telugu Corpus & Offline Packs (1.5 Minutes)
1. Navigate to `http://localhost:5173/archive`.
2. **Whisper ASR Synchronized Player**: Type *"WebRTC"* in the search bar. Click a matched Telugu transcript line—the video player instantly jumps to that exact second.
3. **Telugu Speech Corpus**: Click **📥 Export Telugu Speech Corpus (JSON)** to download the dataset. Explain that this data directly contributes to training community open-weights Indic AI models.
4. **Offline Learning Pack**: Click **📦 Download Offline Pack (.zip)**. Extract the zip file and open `index.html` in an incognito window with Wi-Fi turned off:
   - *Explain to Judges*: *"This standalone pack allows rural schools without internet to study the complete workshop, reading the summary and synchronized transcript completely offline from a USB stick."*

### Step 6: Automated Test Verification (30 Seconds)
Open a terminal in the stall and run:
```bash
docker compose exec backend python app/test_all_features.py
```
Show evaluators that all **15 domain test suites pass with 100% compliance** in real time!

---

## 4. Comprehensive Evaluator Defense Q&A (25 Technical Questions & Answers)

Be prepared for rigorous questioning from faculty and evaluators:

### Category A: System Architecture & WebRTC
#### Q1: Why did you choose a Selective Forwarding Unit (SFU) instead of a Peer-to-Peer (P2P) mesh or MCU?
> **Answer**: In a pure P2P mesh, every participant uploads their video to every other participant, scaling connections quadratically ($\mathcal{O}(N^2)$). With just 5 participants, uplink saturates on mobile connections. An MCU decodes and re-encodes all video streams into a single composite image on the server, requiring massive multi-core server CPUs. LiveKit SFU forwards media packets without transcoding them, maintaining $\mathcal{O}(N)$ scaling on the server with minimal CPU overhead, making it deployable on low-cost virtual servers.

#### Q2: How does your role-based token minting reduce bandwidth?
> **Answer**: When a user joins, our FastAPI backend checks their database role and stage status. If they are a standard viewer, we mint a LiveKit JWT token with `can_publish: false` and `can_subscribe: true`. This prevents audience members from transmitting unnecessary upstream video or audio tracks, reserving bandwidth strictly for the 2–5 active speakers on stage.

#### Q3: Which ports does LiveKit require, and how does media traverse NAT/firewalls?
> **Answer**: LiveKit uses port `7880 TCP` for HTTP REST and WebSocket signaling, port `7881 TCP` for WebRTC ICE over TCP fallback, and port range `7882 UDP` for direct WebRTC RTP/RTCP media streams. For NAT traversal, WebRTC uses STUN/TURN candidates; in local development, `--node-ip 127.0.0.1` binds public candidates locally.

#### Q4: How does your Low-Data Mode achieve 44.8 kbps on 2G networks?
> **Answer**: On standard video calls, video streams consume 250–600 kbps. In Low-Data Mode, the client transceivers disable incoming video rendering. We prioritize the Opus audio codec, which uses Dynamic Forward Error Correction (FEC) and Discontinuous Transmission (DTX), delivering crystal-clear voice at 32–40 kbps alongside periodic slide diffs, totaling under 45 kbps.

---

### Category B: Security, Authentication & Data Modeling
#### Q5: How do you handle authentication securely without storing JWT tokens in localStorage?
> **Answer**: Storing JWT tokens in `localStorage` or `sessionStorage` exposes tokens to Cross-Site Scripting (XSS) attacks. Swecha Vedika stores JWT access tokens strictly **in-memory** within React state (`AuthContext`). Passwords are never stored in plaintext; they are hashed using `passlib` with `bcrypt` (12 salt rounds).

#### Q6: Why did you use PostgreSQL and Alembic instead of a NoSQL database like MongoDB?
> **Answer**: Swecha Vedika requires strict relational integrity with foreign key cascades (e.g., when an event is deleted, attendance, questions, polls, and chat records must be cleanly cascaded). Furthermore, unique constraints such as `(poll_id, user_id)` and `(question_id, user_id)` ensure that users cannot vote twice at the database level. Alembic provides deterministic, auditable database schema version control.

#### Q7: How do you prevent duplicate voting on polls and questions under high concurrency?
> **Answer**: We enforce composite unique constraints in PostgreSQL (`uq_poll_user_vote` on `(poll_id, user_id)` and `uq_question_user_upvote` on `(question_id, user_id)`). Even if an attendee clicks repeatedly or submits simultaneous requests, the database rejects duplicates at the engine level.

---

### Category C: WhatsApp Bot & Conversational Gateway
#### Q8: How does the WhatsApp Bot communicate with the meeting room in real time?
> **Answer**: The Meta WhatsApp Graph API sends HTTP webhook POST requests to `/webhook/whatsapp`. Our backend parses the message via a finite state machine. When an attendee sends `ASK <id>: <question>`, the backend validates the event and inserts the question directly into the PostgreSQL `questions` table with a special WhatsApp badge. The meeting room's polling hook fetches it within 3 seconds, displaying it on the presenter's stage queue.

#### Q9: How can evaluators test WhatsApp without a verified Meta Business Account?
> **Answer**: We built an in-browser WhatsApp Phone Simulator component (`WhatsAppSimulator.jsx`) backed by `/webhook/whatsapp/simulate`. Evaluators can type real WhatsApp commands (`EVENTS`, `RSVP`, `ASK`, `SUMMARY`) directly inside a simulated phone drawer and observe the real-time stage response.

---

### Category D: Replay-as-Live & Host Failover
#### Q10: How does the Replay-as-Live engine ensure all viewers watch the exact same video timestamp?
> **Answer**: When the host starts a replay broadcast, the server stores $T_0$. Every joining client polls `/sync-clock`, which computes $t_{\text{offset}} = T_{\text{server}} - T_0$. The browser seeks the video element directly to $t_{\text{offset}}$ and disables manual seeking, ensuring synchronized shared viewing while keeping Q&A, chat, and polls live.

#### Q11: What happens if the host's rural internet connection suddenly drops?
> **Answer**: Presenters transmit a heartbeat ping (`/events/{id}/heartbeat`) every 10 seconds. If the server does not receive a heartbeat for $> 30\text{ seconds}$, our automated resilience protocol marks `host_online = False`, queries active attendees, and promotes the highest-priority co-host or speaker (`failover_host_id`) to take over stage moderation, emitting an emergency banner to all participants.

---

### Category E: Whisper ASR, Telugu Corpus & Offline Packs
#### Q12: How does your platform handle multilingual and code-mixed Telugu-English speech?
> **Answer**: We utilize OpenAI Whisper, an acoustic foundation model trained on 680,000 hours of multilingual data. Whisper robustly decodes code-mixed Indic speech (*Telugish*). Each transcript segment is stored with `start`, `end`, `speaker`, and `language` tags.

#### Q13: What is the purpose of the Telugu Speech Corpus export?
> **Answer**: Commercial AI models frequently perform poorly on regional Indian dialects due to a lack of open, consent-backed training datasets. Swecha Vedika outputs structured JSON corpus files containing audio sample URLs, speaker tags, and aligned transcripts, directly contributing to Swecha's initiative to build community-owned open Indic AI speech models.

#### Q14: How does the Offline Pack work without an internet connection?
> **Answer**: The backend dynamically generates a `.zip` archive containing `summary.md`, `transcript.json`, `metadata.json`, and an `index.html` file with embedded inline CSS. A rural student can unzip the archive on any computer and double-click `index.html` in Chrome, Firefox, or Edge—it renders the entire session, notes, and transcripts with zero external dependencies and zero internet connection.

---

## 5. Live Demo Emergency Recovery Procedures

If an unexpected port conflict, network switch, or browser freeze occurs during the expo:

1. **Check Container Status**:
   ```bash
   docker compose ps
   ```
   All 4 containers (`prototype_db`, `prototype_livekit`, `prototype_backend`, `prototype_frontend`) should show `Up`.

2. **Run Quick Health Check**:
   Open browser to `http://localhost:8000/health/db`. Should return:
   ```json
   {"status": "ok", "db": "connected", "tables": {...}}
   ```

3. **Re-run Automated Tests**:
   ```bash
   docker compose exec backend python app/test_all_features.py
   ```
   If all 15 checks pass, the entire stack is 100% operational.

4. **Restart Stack Cleanly (if needed)**:
   ```bash
   docker compose restart
   ```
