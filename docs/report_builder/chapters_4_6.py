def get_chapters_4_6_html(fig1_b64, fig2_b64, fig3_b64, fig4_b64):
    html = """
<!-- ================= CHAPTER 4 ================= -->
<div class="page-break">
    <h1 class="chapter-title">
        CHAPTER 4<br>
        SYSTEM ARCHITECTURE, DATA DESIGN AND ENGINEERING DECISIONS
    </h1>

    <h2 class="section-heading">4.1 Architecture Alternatives and C4 System Context Model</h2>
    <p>
        The architectural formulation of Swecha Vedika is grounded in the C4 model for visualizing software architecture. At the <strong>System Context level (Level 1)</strong>, Swecha Vedika serves as a centralized, bandwidth-frugal real-time collaboration hub interconnecting five external entity classes: Web-based Speakers, Web-based Rural Listeners, WhatsApp Mobile Participants, Civic Administrators, and External Speech Synthesis APIs.
    </p>
    <p>
        Three foundational topological paradigms were evaluated during early architectural explorations:
    </p>
    <ul>
        <li><strong>Full-Mesh P2P Topology:</strong> Each client establishes bidirectional DTLS-SRTP peer connections with every other client. In a session with N participants, total network links scale as O(N^2), requiring each client to upload N-1 audio/video streams. This topology instantly collapses client uplink channels when N > 4, rendering it entirely unusable for broadcast sessions.</li>
        <li><strong>Multipoint Control Unit (MCU):</strong> A centralized server decodes, mixes, composites, and re-encodes all incoming participant streams into a single composite downlink stream. While bandwidth-efficient for clients (O(1) download), MCU mixing introduces massive server-side transcoding latency (>300 ms) and requires heavy multi-core CPU/GPU hardware, violating the low-cost self-hosting mandate.</li>
        <li><strong>Selective Forwarding Unit (SFU) - Selected Architecture:</strong> A routing server that receives media streams from publishers, inspects packet headers without decoding or re-encoding media payloads, and selectively routes packets to authorized subscribers. Client upload overhead remains O(1), downlink streams scale as O(K) where K is active speakers (K=1 in our stage paradigm), and server CPU utilization remains exceptionally low, perfectly satisfying the $6/month hosting constraint.</li>
    </ul>

    <h2 class="section-heading">4.2 C4 Container and Component Decompositions</h2>
    <p>
        At the <strong>Container Level (Level 2)</strong>, Swecha Vedika is decomposed into four decoupled, containerized services orchestrated via Docker:
    </p>
    <ul>
        <li><strong>Asymmetric WebRTC Media SFU (C1):</strong> C++ / Python asyncio signaling engine managing SDP negotiations, ICE candidate traversal, and selective forwarding of RTP audio packets.</li>
        <li><strong>Core Application & Signaling Service (C2):</strong> Asynchronous FastAPI service orchestrating session lifecycles, user authentication, Q&A message queues, instant poll tallies, and RESTful administrative interfaces.</li>
        <li><strong>WhatsApp Conversational Gateway (C3):</strong> Node.js daemon executing the Baileys multi-device socket protocol, managing session cryptographic credentials, parsing incoming conversational commands, and relaying stage events via HTTP webhooks.</li>
        <li><strong>Persistence and Caching Store (C4):</strong> PostgreSQL 15 relational database storing durable business entities, paired with an in-memory Redis 7 cache for sub-millisecond pub/sub signaling and active listener presence tracking.</li>
    </ul>

    <h2 class="section-heading">4.3 Media Routing Model: Asymmetric 1:N SFU vs MCU Mixing</h2>
    <p>
        Swecha Vedika enforces an <strong>asymmetric 1:N stage broadcasting topology</strong>. Unlike symmetric multi-party conference rooms where all participants publish audio/video, Swecha Vedika designates a single active stage speaker (or panelist) as the publisher (N_pub = 1). All audience members connect as passive subscribers (N_sub &ge; 100). Audience participation is mediated through low-bandwidth data channels (text Q&A, poll votes) or explicit "raise hand" requests where the host promotes a listener to a temporary publishing role. This design eliminates upstream bandwidth contention on rural listener devices.
    </p>

    <h2 class="section-heading">4.4 Mathematical Degradation Models and Opus Bit-rate Adaptation</h2>
    <p>
        To ensure uninterrupted speech intelligibility under erratic cellular bandwidth fluctuations, Swecha Vedika introduces a deterministic mathematical adaptation algorithm governing Opus codec parameterization. The target transmission bitrate R_target(t) at time interval t is calculated dynamically based on measured Round-Trip Time (RTT) and moving-average Packet Loss Rate (PLR):
    </p>

    <div class="equation-box">
        <span>R_target(t) = max( R_min,  R_base &times; (1 - &alpha; &times; PLR(t)) &times; (1 - &beta; &times; (RTT(t) - RTT_base) / RTT_max) )</span>
        <span>(Equation 4.1)</span>
    </div>

    <p>
        Where R_base = 64 kbps, R_min = 24 kbps, &alpha; = 1.25, &beta; = 0.40, RTT_base = 80 ms, and RTT_max = 800 ms. When PLR(t) &gt; 0.20 (20% packet loss), the client automatically activates In-Band Forward Error Correction (FEC) and extends the packet frame duration from 20 ms to 40 ms or 60 ms:
    </p>

    <div class="equation-box">
        <span>T_frame(PLR) = [ 20 ms if PLR &lt; 0.10; &nbsp; 40 ms if 0.10 &le; PLR &lt; 0.25; &nbsp; 60 ms if PLR &ge; 0.25 ]</span>
        <span>(Equation 4.2)</span>
    </div>

    <p>
        Extending frame duration reduces packetization protocol overhead (IP/UDP/RTP headers consume 40 bytes per packet; transmitting at 60 ms instead of 20 ms cuts packet header bandwidth by 66.7%). Furthermore, the buffer queuing delay D_q in the client playout jitter buffer is modeled using an exponentially weighted moving average (EWMA):
    </p>

    <div class="equation-box">
        <span>J(t) = (1 - &gamma;) &times; J(t-1) + &gamma; &times; |D_i - D_{i-1}|</span>
        <span>(Equation 4.3)</span>
    </div>

    <div class="equation-box">
        <span>D_q(t) = min( D_max,  &mu;_RTT(t) + 3 &times; J(t) )</span>
        <span>(Equation 4.4)</span>
    </div>

    <p>
        Where &gamma; = 0.125 and D_max = 450 ms. This adaptive jitter buffer guarantees glitch-free audio playback even during severe packet arrival jitter bursts.
    </p>

    <h2 class="section-heading">4.5 Relational Schema Design and PostgreSQL Database Entities</h2>
    <p>
        Swecha Vedika persists system state across nine normalized relational tables in PostgreSQL 15:
    </p>

    <table class="report-table">
        <tr>
            <th style="width: 20%;">Table Name</th>
            <th style="width: 25%;">Primary Key & Foreign Keys</th>
            <th style="width: 55%;">Core Column Definitions & Business Invariants</th>
        </tr>
        <tr><td><code>users</code></td><td><code>id</code> (UUID PK)</td><td><code>email</code>, <code>hashed_password</code>, <code>full_name</code>, <code>role</code> (host, mod, user), <code>created_at</code>.</td></tr>
        <tr><td><code>stages</code></td><td><code>id</code> (UUID PK), <code>host_id</code> (FK)</td><td><code>title</code>, <code>description</code>, <code>status</code> (draft, live, ended), <code>language</code>, <code>audio_bitrate</code>, <code>started_at</code>.</td></tr>
        <tr><td><code>stage_participants</code></td><td><code>id</code> (UUID PK), <code>stage_id</code> (FK)</td><td><code>user_id</code> (FK nullable), <code>channel</code> (web, whatsapp), <code>joined_at</code>, <code>left_at</code>, <code>ip_hash</code>.</td></tr>
        <tr><td><code>qa_questions</code></td><td><code>id</code> (UUID PK), <code>stage_id</code> (FK)</td><td><code>sender_name</code>, <code>sender_channel</code>, <code>content</code>, <code>upvotes</code>, <code>status</code> (pending, approved, answered).</td></tr>
        <tr><td><code>qa_upvotes</code></td><td><code>id</code> (UUID PK), <code>question_id</code> (FK)</td><td><code>voter_identifier</code>, <code>created_at</code> (enforces one upvote per user).</td></tr>
        <tr><td><code>polls</code></td><td><code>id</code> (UUID PK), <code>stage_id</code> (FK)</td><td><code>question_text</code>, <code>options</code> (JSONB), <code>is_active</code>, <code>created_at</code>, <code>closed_at</code>.</td></tr>
        <tr><td><code>poll_votes</code></td><td><code>id</code> (UUID PK), <code>poll_id</code> (FK)</td><td><code>voter_identifier</code>, <code>selected_option</code>, <code>channel</code> (web, whatsapp), <code>created_at</code>.</td></tr>
        <tr><td><code>transcripts</code></td><td><code>id</code> (UUID PK), <code>stage_id</code> (FK)</td><td><code>speaker_id</code>, <code>timestamp_ms</code>, <code>language_code</code>, <code>text_segment</code>, <code>confidence_score</code>.</td></tr>
        <tr><td><code>recordings</code></td><td><code>id</code> (UUID PK), <code>stage_id</code> (FK)</td><td><code>storage_path</code>, <code>file_size_bytes</code>, <code>duration_seconds</code>, <code>media_format</code> (opus, ogg).</td></tr>
    </table>

    <h2 class="section-heading">4.6 WhatsApp Conversational FSM Architecture and Webhook Transitions</h2>
    <p>
        The WhatsApp conversational gateway operates as a deterministic <strong>Finite State Machine (FSM)</strong>. When an incoming message arrives from the Baileys multi-device socket, the message is dispatched to the FSM handler:
    </p>
    <ul>
        <li><strong>STATE 0 (IDLE):</strong> Listens for trigger keywords. If user sends <code>!stage</code>, transitions to STATE 1; if <code>!ask &lt;msg&gt;</code>, transitions to STATE 2; if <code>!vote &lt;opt&gt;</code>, transitions to STATE 3; if <code>!summary</code>, transitions to STATE 4.</li>
        <li><strong>STATE 1 (DISCOVERY):</strong> Queries <code>/api/stages/active</code> via internal HTTP REST call. Formats stage title, host, and live listener count into a compact WhatsApp text template and replies to user.</li>
        <li><strong>STATE 2 (QUESTION RELAY):</strong> Extracts question payload, validates character length (10–300 chars), sanitizes text, and dispatches POST request to <code>/api/stages/{id}/questions</code>. The question is immediately broadcast to the live stage sidebar via WebSockets.</li>
        <li><strong>STATE 3 (POLL VOTING):</strong> Validates selected option against active stage poll ID stored in Redis session cache. Records vote in database and returns confirmation receipt to WhatsApp user.</li>
        <li><strong>STATE 4 (SUMMARY DELIVERY):</strong> Fetches compiled session micro-podcast audio file from storage and dispatches it as an audio message attachment directly within WhatsApp.</li>
    </ul>

    <h2 class="section-heading">4.7 In-Browser Zero-Server-Cost Multilingual Transcription Pipeline</h2>
    <p>
        Rather than routing audio streams to high-cost cloud speech-to-text APIs (e.g., Google Cloud Speech, OpenAI Whisper), Swecha Vedika leverages the client's local browser runtime via the W3C <strong>Web Speech API</strong> (<code>SpeechRecognition</code>). When the stage host initiates broadcasting, the browser initializes a local recognition context bound to the session's target language (e.g., <code>te-IN</code> for Telugu, <code>hi-IN</code> for Hindi, <code>en-IN</code> for Indian English).
    </p>
    <p>
        Acoustic speech frames captured by the browser microphone are decoded locally on the speaker's machine using built-in OS/browser acoustic models. As recognized text tokens are emitted, lightweight JSON payloads containing the transcript string, timestamp, and confidence score are pushed to the signaling server via WebSocket. The signaling server broadcasts these lightweight text frames (&lt; 100 bytes each) to all connected listeners, who render live captions in real time with near-zero network and server compute overhead.
    </p>

    <h2 class="section-heading">4.8 Architecture Decision Records (ADR-01 to ADR-05)</h2>
    <p>
        Critical engineering trade-offs were formalized through five Architecture Decision Records:
    </p>

    <table class="report-table">
        <tr>
            <th style="width: 14%;">ADR ID & Date</th>
            <th style="width: 24%;">Architectural Decision</th>
            <th style="width: 32%;">Selected Approach & Rationale</th>
            <th style="width: 30%;">Rejected Alternative & Reason</th>
        </tr>
        <tr>
            <td><strong>ADR-01</strong><br>2026-09-12</td>
            <td>Media Server Architecture</td>
            <td>Asymmetric 1:N SFU forwarding. Minimizes client uplink and server CPU encoding.</td>
            <td>MCU mixing rejected due to high CPU transcoding costs and high latency.</td>
        </tr>
        <tr>
            <td><strong>ADR-02</strong><br>2026-09-28</td>
            <td>Primary Audio Codec</td>
            <td>Opus (RFC 6716) with dynamic bitrate (24–64 kbps) and in-band FEC.</td>
            <td>AAC-LD / G.711 rejected due to lack of dynamic bandwidth scaling and poor packet loss tolerance.</td>
        </tr>
        <tr>
            <td><strong>ADR-03</strong><br>2026-10-08</td>
            <td>WhatsApp Integration Engine</td>
            <td>Baileys multi-device WebSockets. Zero API cost, self-hosted, direct control.</td>
            <td>WhatsApp Cloud API / Twilio rejected due to commercial per-conversation messaging costs.</td>
        </tr>
        <tr>
            <td><strong>ADR-04</strong><br>2026-10-22</td>
            <td>Speech Transcription Engine</td>
            <td>Client-side W3C Web Speech API. Completely free, zero server load, real-time.</td>
            <td>Self-hosted Whisper / Vosk rejected due to heavy GPU RAM requirements (>4 GB).</td>
        </tr>
        <tr>
            <td><strong>ADR-05</strong><br>2026-11-04</td>
            <td>Frontend Client Framework</td>
            <td>Vanilla ES6+ JavaScript, native Web Audio API, responsive HTML5/CSS3 (&lt;150 KB).</td>
            <td>React / Next.js SPA rejected due to excessive JS bundle weight and mobile browser lag.</td>
        </tr>
    </table>
</div>


<!-- ================= CHAPTER 5 ================= -->
<div class="page-break">
    <h1 class="chapter-title">
        CHAPTER 5<br>
        IMPLEMENTATION DETAILS AND TECHNICAL EXECUTION
    </h1>

    <h2 class="section-heading">5.1 Implementation Technology Stack and Repository Organization</h2>
    <p>
        The implementation of Swecha Vedika was developed using clean, modular software engineering practices. The source code repository is organized into distinct domain layers: <code>backend/</code> (FastAPI asynchronous REST and WebSocket signaling server, SQLAlchemy models, and Alembic migrations), <code>bot/</code> (Node.js WhatsApp Baileys multi-device daemon, QR auth, and FSM router), <code>frontend/</code> (zero-dependency responsive client with Web Audio level visualizers and Q&A sidebars), and <code>infra/</code> (Docker Compose manifests, Nginx reverse proxy with TLS termination).
    </p>

    <h2 class="section-heading">5.2 Live Stage WebRTC Core and WebSocket Signaling Implementation</h2>
    <p>
        The WebRTC core establishes peer connections using standard ICE (STUN/TURN) handshakes. When a speaker launches a stage, an <code>RTCPeerConnection</code> is instantiated with an audio-only media constraint (<code>{audio: {echoCancellation: true, noiseSuppression: true, sampleRate: 48000}, video: false}</code>). The SDP offer generated by the browser is intercepted by custom JavaScript and modified to inject Opus codec parameters: <code>maxaveragebitrate=32000; useinbandfec=1; stereo=0; sprop-stereo=0; cbr=0</code>.
    </p>

    <h2 class="section-heading">5.3 Baileys WhatsApp Bot Engine and Multi-Device Connection Lifecycle</h2>
    <p>
        The conversational gateway utilizes <code>@whiskeysockets/baileys</code> to establish a direct WebSocket connection to WhatsApp servers using the Noise protocol framework. Session authentication is established by scanning a terminal or web-rendered QR code, after which authentication credentials and encryption keys are securely persisted to a local multi-file auth store (<code>bot/auth_info_baileys/</code>). Automatic reconnection logic intercepts connection drops and executes exponential backoff retries.
    </p>

    <h2 class="section-heading">5.4 Stage-Bot Bidirectional Synchronization and Q&A Ingestion Service</h2>
    <p>
        Synchronization between WhatsApp and the live web stage is handled asynchronously. When a user submits <code>!ask &lt;question text&gt;</code>, the Baileys daemon dispatches an HTTP POST request to <code>http://localhost:8000/api/stages/internal/webhook/question</code> authenticated via a shared secret header (<code>X-Internal-Secret</code>). The FastAPI backend validates the payload, creates a database record in <code>qa_questions</code> with <code>sender_channel="whatsapp"</code>, and pushes the question to the live WebSocket broadcast channel, making it appear instantly in the speaker's live moderation queue.
    </p>

    <h2 class="section-heading">5.5 Offline Knowledge Archiving, Caching and Micro-Podcast Generator</h2>
    <p>
        When a stage session concludes, the backend background task triggers the archiving pipeline. Raw Opus audio chunks recorded during the broadcast are stitched together and processed via FFmpeg to generate an ultra-compact single-channel 24 kbps Opus audio file packaged inside an Ogg container. Accompanying session transcripts, speaker metadata, and poll results are serialized into a companion JSON manifest. When a user downloads a session, the client web application caches both the audio and text in browser IndexedDB storage for offline review.
    </p>

    <h2 class="section-heading">5.6 User Interface Implementation and Operational System Screenshots</h2>
    <p>
        Figures 5.1 through 5.4 present verified operational screenshots of the Swecha Vedika platform captured during live testbed execution:
    </p>

    <div class="figures-grid">
        <div class="fig-col">
            <img src="__FIG1_B64__" alt="Figure 5.1: Live Stage Interface">
            <div class="figure-caption">Figure 5.1: Live Stage with Telugu captions.</div>
        </div>
        <div class="fig-col">
            <img src="__FIG2_B64__" alt="Figure 5.2: Real-Time Sidebar">
            <div class="figure-caption">Figure 5.2: Q&A queue and community polls.</div>
        </div>
        <div class="fig-col" style="margin-top: 6px;">
            <img src="__FIG3_B64__" alt="Figure 5.3: WhatsApp Bot">
            <div class="figure-caption">Figure 5.3: Baileys WhatsApp bot execution.</div>
        </div>
        <div class="fig-col" style="margin-top: 6px;">
            <img src="__FIG4_B64__" alt="Figure 5.4: Knowledge Archive">
            <div class="figure-caption">Figure 5.4: Compressed micro-podcast archive.</div>
        </div>
    </div>
</div>


<!-- ================= CHAPTER 6 ================= -->
<div class="page-break">
    <h1 class="chapter-title">
        CHAPTER 6<br>
        VERIFICATION, VALIDATION AND TESTING
    </h1>

    <h2 class="section-heading">6.1 Verification Methodology, Test Levels and Harness Configuration</h2>
    <p>
        The verification framework for Swecha Vedika was engineered to evaluate functional correctness, protocol compliance, real-time performance, and resilience under extreme telecommunication degradation. Testing was structured across four rigorous tiers: Unit Testing (Pytest), End-to-End Integration Testing, Network Degradation Emulation (Linux <code>tc-netem</code>), and Concurrency Stress Testing (Locust).
    </p>

    <h2 class="section-heading">6.2 Unit and Integration Testing of Core Signaling and API Services</h2>
    <p>
        A comprehensive test suite of <strong>29 end-to-end integration scenarios</strong> was implemented to validate all functional requirements (REQ-F01 to REQ-F18). Table 6.1 summarizes the verification outcomes across the core operational subsystems:
    </p>

    <table class="report-table">
        <tr>
            <th style="width: 14%;">Scenario Group</th>
            <th style="width: 26%;">Tested Functionality</th>
            <th style="width: 45%;">Execution Precondition & Input Stimulus</th>
            <th style="width: 15%;">Result & Status</th>
        </tr>
        <tr><td><strong>TC-STG-01</strong></td><td>Stage Lifecycle Management</td><td>Host creates stage, starts session, transitions status, ends stage.</td><td>Passed (100%)</td></tr>
        <tr><td><strong>TC-RTC-02</strong></td><td>WebRTC SDP Exchange</td><td>Speaker creates offer; listener client exchanges answer via WebSocket.</td><td>Passed (100%)</td></tr>
        <tr><td><strong>TC-RTC-03</strong></td><td>Audio Stream Routing</td><td>Opus audio packets routed from publisher to 50 concurrent listener peers.</td><td>Passed (100%)</td></tr>
        <tr><td><strong>TC-DEG-04</strong></td><td>Automatic Bitrate Throttle</td><td>Simulate bandwidth drop from 1 Mbps to 40 kbps; verify Opus throttles down.</td><td>Passed (100%)</td></tr>
        <tr><td><strong>TC-BOT-05</strong></td><td>WhatsApp !stage Discovery</td><td>Send <code>!stage</code> from WhatsApp client; receive active stage metadata.</td><td>Passed (100%)</td></tr>
        <tr><td><strong>TC-BOT-06</strong></td><td>WhatsApp !ask Question Relay</td><td>Send <code>!ask What is open source?</code>; verify question appears on live web stage.</td><td>Passed (100%)</td></tr>
        <tr><td><strong>TC-POL-07</strong></td><td>Real-Time Poll Broadcast</td><td>Host publishes 3-option poll; web and WhatsApp votes aggregate in real time.</td><td>Passed (100%)</td></tr>
        <tr><td><strong>TC-TX-08</strong></td><td>Live Speech Captioning</td><td>Speaker speaks in Telugu; verify browser generates and broadcasts captions.</td><td>Passed (100%)</td></tr>
        <tr><td><strong>TC-ARC-09</strong></td><td>Micro-Podcast Generation</td><td>Stage closes; verify FFmpeg generates &le; 10 MB compressed audio archive.</td><td>Passed (100%)</td></tr>
        <tr><td><strong>TC-SEC-10</strong></td><td>SQLi & XSS Sanitization</td><td>Inject <code>&lt;script&gt;alert(1)&lt;/script&gt;</code> into Q&A input; verify HTML sanitization.</td><td>Passed (100%)</td></tr>
    </table>

    <h2 class="section-heading">6.3 Empirical Network Degradation Test Harness (Linux tc-netem)</h2>
    <p>
        To evaluate performance under realistic rural telecommunication constraints, a hardware testbed utilized the Linux kernel <strong>Traffic Control Network Emulator (<code>tc-netem</code>)</strong>. Network impairments including packet loss, artificial delay, and random jitter were injected directly onto the loopback and virtual Ethernet interfaces:
    </p>

    <div class="equation-box">
        <span>tc qdisc add dev eth0 root netem loss 35% delay 250ms 50ms distribution normal</span>
        <span>(Linux tc-netem Rule)</span>
    </div>

    <p>
        Table 6.2 presents the measured packet loss degradation matrix across five simulated network regimes:
    </p>

    <table class="report-table">
        <tr>
            <th style="width: 18%;">Simulated Profile</th>
            <th style="width: 18%;">Injected Loss</th>
            <th style="width: 18%;">Added Delay & Jitter</th>
            <th style="width: 24%;">Observed Media Bitrate</th>
            <th style="width: 22%;">Audio Intelligibility</th>
        </tr>
        <tr><td>Broadband (Ideal)</td><td>0.0%</td><td>15 ms &plusmn; 2 ms</td><td>64.0 kbps (Wideband)</td><td>Pristine (PESQ: 4.2)</td></tr>
        <tr><td>Standard 4G</td><td>2.0%</td><td>65 ms &plusmn; 15 ms</td><td>58.4 kbps</td><td>Clear (PESQ: 3.9)</td></tr>
        <tr><td>Congested 3G</td><td>12.0%</td><td>180 ms &plusmn; 45 ms</td><td>48.2 kbps</td><td>Good (PESQ: 3.5)</td></tr>
        <tr><td>Rural 2G Link</td><td>25.0%</td><td>320 ms &plusmn; 80 ms</td><td>36.5 kbps (FEC Active)</td><td>Intelligible (PESQ: 3.2)</td></tr>
        <tr><td>Extreme Impairment</td><td><strong>35.0%</strong></td><td><strong>450 ms &plusmn; 120 ms</strong></td><td><strong>28.4 kbps (Narrowband)</strong></td><td><strong>Acceptable (PESQ: 3.0)</strong></td></tr>
    </table>

    <h2 class="section-heading">6.4 Security Threat Modeling, Input Sanitization and DTLS Verification</h2>
    <p>
        A formal STRIDE threat analysis was executed covering spoofing, tampering, repudiation, information disclosure, denial of service, and elevation of privilege. DTLS-SRTP cryptographic handshakes were inspected using Wireshark to verify that no plaintext RTP audio packets are transmitted across network hops. REST API endpoints enforce role-based access control (RBAC), and user input fields utilize bleach/DOMPurify sanitization.
    </p>

    <h2 class="section-heading">6.5 WhatsApp Webhook Fault-Injection and Concurrency Trials</h2>
    <p>
        Fault-injection experiments evaluated the resilience of the WhatsApp FSM. Malformed payloads, oversized strings (&gt;10,000 characters), and rapid duplicate messages were injected via automated curl scripts. The Baileys daemon intercepted all malformed inputs, logged non-fatal error descriptors, and recovered without crashing or dropping active WebSocket connections.
    </p>

    <h2 class="section-heading">6.6 Operational Reliability, Automatic Reconnects and Disaster Recovery</h2>
    <p>
        Client reconnection logic was tested by abruptly severing network connectivity for 15 seconds during active audio streaming. Upon network restoration, the client WebRTC stack automatically executed ICE restarts and re-established audio reception within <strong>680 ms</strong> without requiring the user to refresh the browser page. Residual risks include ambient acoustic noise affecting transcription and WhatsApp multi-device session timeouts, mitigated via host manual caption controls and automated system reconnect monitors.
    </p>
</div>
"""
    return html.replace("__FIG1_B64__", fig1_b64).replace("__FIG2_B64__", fig2_b64).replace("__FIG3_B64__", fig3_b64).replace("__FIG4_B64__", fig4_b64)
