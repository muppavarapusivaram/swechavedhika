def get_chapters_1_3_html():
    return """
<!-- ================= CHAPTER 1 ================= -->
<div class="page-break">
    <h1 class="chapter-title">
        CHAPTER 1<br>
        PROJECT CONTEXT, PROBLEM DEFINITION AND OBJECTIVES
    </h1>

    <h2 class="section-heading">1.1 Project Identity and Administrative Metadata</h2>
    <p>
        The capstone engineering project, formally titled <strong>"SWECHA VEDIKA: A BANDWIDTH-FRUGAL, MULTILINGUAL LIVE STAGE AND KNOWLEDGE PLATFORM,"</strong> addresses the acute technical challenges of delivering real-time interactive voice communication, synchronous civic participation, and asynchronous knowledge preservation across resource-constrained, high-latency, and bandwidth-deprived environments. The project is undertaken under the domain of <strong>Blockchain & Cyber Security Systems</strong> by Team <strong>KL - GLUG</strong>, within the Department of Experiential Learning and Global Engagement (EL&GE), Koneru Lakshmaiah Education Foundation (Deemed to be University), as part of the academic curriculum for the award of the degree of Bachelor of Technology (B.Tech) during the Academic Year 2026–2027.
    </p>
    <p>
        Swecha Vedika was conceived in response to real-world deployment challenges identified during field interventions organized by the <em>Swecha Telangana</em> free and open-source software community. In rural learning centers, agricultural cooperative assemblies, and non-profit grassroots education initiatives across rural Andhra Pradesh and Telangana, existing proprietary communication tools consistently fail to provide reliable connectivity. This project represents a comprehensive systems-engineering response designed to deliver digital inclusion, linguistic equity, and open-access public knowledge infrastructure.
    </p>

    <h2 class="section-heading">1.2 Problem Context and Grassroots Sociotechnical Provenance</h2>
    <p>
        The digital transformation of public education, community self-governance, and civil society assemblies has accelerated significantly in recent years. However, this transition has introduced profound structural inequities. The dominant commercial teleconferencing paradigm—epitomized by proprietary platforms such as Zoom, Google Meet, and Microsoft Teams—is fundamentally architected on assumptions of ubiquitous high-speed broadband infrastructure (>1.5 Mbps symmetrical throughput), low network jitter (<50 ms), negligible packet loss (<1%), and modern multi-core computing hardware.
    </p>
    <p>
        In contrast, the reality of rural, remote, and socio-economically marginalized communities across the Global South, and particularly in rural India, is characterized by extreme telecommunication fragility. Field evaluations conducted across regional community learning centers reveal that rural connectivity relies almost exclusively on congested cellular towers operating under 2G, 3G, or severely throttled 4G connections. Available downstream throughput frequently drops below 50 kbps, uplink channels degrade to intermittent bursts, and round-trip ping times regularly exceed 400 to 600 ms.
    </p>
    <p>
        When participants in these environments attempt to join conventional video-centric virtual meetings, the results are catastrophic. High client-side JavaScript execution footprints (>4 MB uncompressed bundles) overwhelm low-memory entry-level smartphones, precipitating browser crashes. Concurrently, video streams monopolize scarce network buffers, inducing massive bufferbloat, continuous media packet drops, and frequent connection timeouts. The participant is ultimately trapped in an endless reconnection loop, resulting in complete audio blackout and total exclusion from civic discourse.
    </p>

    <h2 class="section-heading">1.3 Stakeholders and Operational Deployment Environment</h2>
    <p>
        The operating ecosystem of Swecha Vedika encompasses five primary stakeholder groups, each characterized by distinct operational constraints, technical literacies, and socio-economic realities:
    </p>
    <ul>
        <li><strong>Rural Students and Community Learners:</strong> Accessing sessions via low-cost Android smartphones operating on prepaid mobile data plans with strict daily limits. They require an ultra-lightweight client that functions seamlessly without demanding specialized application downloads or sustained high-bandwidth connections.</li>
        <li><strong>Civic Educators and Community Organizers:</strong> Conducting live instructional lectures, agricultural advisories, and civic literacy workshops. They require tools to deliver clear audio presentations, initiate real-time audience comprehension polls, and curate participant questions without technical friction.</li>
        <li><strong>Vernacular and Dialect Speakers:</strong> Participants whose primary language of comprehension is an Indic regional tongue (e.g., Telugu). They face severe language barriers on mainstream platforms that lack real-time local-language captioning and vernacular conversational interfaces.</li>
        <li><strong>WhatsApp-Centric Rural Citizens:</strong> Individuals who may lack modern web browser proficiency or high-speed data access but actively utilize WhatsApp for daily messaging. They require an asynchronous bridge that enables submitting stage queries and receiving synthesized audio summaries directly within their messaging environment.</li>
        <li><strong>Institutional and Civic Administrators:</strong> Open-source educational organizations, rural colleges, and non-profit entities operating under strict computational budgets who require self-hostable, low-maintenance infrastructure deployable on modest hardware.</li>
    </ul>

    <h2 class="section-heading">1.4 Problem Statement and Primary Project Mandate</h2>
    <p>
        Existing digital meeting and live broadcasting platforms fail catastrophically under extreme rural network constraints (&lt;100 kbps, &gt;20% packet loss), enforce heavy client bundle overheads that crash low-cost smartphones, lack native vernacular Indic language transcription capabilities, and completely isolate synchronous live events from asynchronous offline community knowledge retrieval.
    </p>
    <p>
        Therefore, the engineering mandate of this capstone project is: <em>To design, architect, implement, and empirically validate an open-source, ultra-bandwidth-frugal live stage and knowledge dissemination platform (Swecha Vedika) that guarantees intelligible, low-latency audio transmission under 2G-level cellular constraints (sub-50 kbps), embeds zero-server-cost multilingual Indic speech transcription, integrates a bidirectional WhatsApp conversational finite-state machine, and enables compressed offline knowledge archiving deployable on a single budget cloud server.</em>
    </p>

    <h2 class="section-heading">1.5 Scope, Design Assumptions and Technical Boundaries</h2>
    <p>
        To ensure academic depth and practical feasibility, the architectural scope of Swecha Vedika is governed by rigorous system boundaries:
    </p>
    <ul>
        <li><strong>Architectural Scope:</strong> Swecha Vedika focuses on an asymmetric <em>1:N Broadcast and Curated Participation</em> topology rather than an N:N video conference. The speaker's audio and optional lightweight visual cues are routed to many audience members, optimizing upstream bandwidth.</li>
        <li><strong>Audio-First Primacy:</strong> Audio packets are treated as first-class, inviolable network citizens. Video is treated as an optional secondary artifact that is dynamically throttled or dropped entirely when packet loss exceeds threshold limits.</li>
        <li><strong>Client Hardware Independence:</strong> The web client is built with zero heavyweight frontend frameworks, avoiding React/Angular overhead. The total page weight is strictly constrained to under 150 KB, ensuring rapid execution on low-memory mobile browsers.</li>
        <li><strong>Conversational Boundary:</strong> WhatsApp connectivity is implemented utilizing the open-source Baileys multi-device protocol, eliminating reliance on costly commercial enterprise BSP APIs while maintaining direct, bidirectional stage synchronization.</li>
        <li><strong>Security Boundary:</strong> All real-time media streams are secured using Datagram Transport Layer Security (DTLS) and Secure Real-time Transport Protocol (SRTP). Signaling channels are secured via TLS 1.3 WebSockets.</li>
    </ul>

    <h2 class="section-heading">1.6 O1–O5 Project Objectives and Measurable Acceptance Criteria</h2>
    <p>
        The capstone engineering lifecycle is structured around five foundational, objectively verifiable objectives:
    </p>

    <table class="report-table">
        <tr>
            <th style="width: 10%;">Objective</th>
            <th style="width: 40%;">Engineering Focus & Technical Scope</th>
            <th style="width: 30%;">Measurable Acceptance Criteria</th>
            <th style="width: 20%;">Evaluation Method</th>
        </tr>
        <tr>
            <td><strong>O1</strong></td>
            <td>Bandwidth-Frugal Audio-First SFU Pipeline</td>
            <td>Sustain intelligible voice streaming at &le; 48 kbps under 35% packet loss and 450 ms jitter.</td>
            <td>Linux <code>tc-netem</code> packet loss injection and Wireshark metrics.</td>
        </tr>
        <tr>
            <td><strong>O2</strong></td>
            <td>Zero-Server-Cost In-Browser Multilingual Transcription</td>
            <td>Generate live Telugu captions on client hardware with &lt; 800 ms latency and 0 MB server GPU load.</td>
            <td>Web Speech API dialect evaluation and server CPU profiling.</td>
        </tr>
        <tr>
            <td><strong>O3</strong></td>
            <td>Bidirectional WhatsApp Conversational Gateway</td>
            <td>Achieve &lt; 500 ms median bot response turnaround for stage queries and interactive polls.</td>
            <td>Automated Locust load testing with 50 concurrent simulated users.</td>
        </tr>
        <tr>
            <td><strong>O4</strong></td>
            <td>Offline Knowledge Archiving and Micro-Podcast Caching</td>
            <td>Compress 1-hour live session audio into a &le; 10 MB self-contained offline knowledge package.</td>
            <td>Opus transcode compression ratio and IndexedDB caching validation.</td>
        </tr>
        <tr>
            <td><strong>O5</strong></td>
            <td>Ultra-Low-Cost Self-Hostable Cloud Deployment</td>
            <td>Execute full stack on a single \$6/month Linux droplet supporting &ge; 100 concurrent listeners.</td>
            <td>Docker resource monitoring under synthetic load generation.</td>
        </tr>
    </table>

    <h2 class="section-heading">1.7 Technical Deliverables Versus Real-World Community Impact</h2>
    <p>
        A central tenet of the Capstone engineering philosophy is bridging rigorous software systems engineering deliverables with measurable societal impact. While the technical deliverables comprise low-level WebRTC media routing protocols, deterministic finite-state automata, and relational schema designs, the real-world impact manifests in tangible democratization of civic knowledge.
    </p>
    <p>
        By eliminating bandwidth barriers, Swecha Vedika empowers grassroots educators to deliver live instructional training to rural youth who were previously shut out of digital education due to data costs. By providing real-time Telugu transcription, the platform dismantles linguistic exclusion, enabling rural artisans and self-help groups to participate actively in democratic governance.
    </p>

    <h2 class="section-heading">1.8 United Nations Sustainable Development Goals (SDG) Mapping</h2>
    <p>
        Swecha Vedika directly contributes to three core United Nations Sustainable Development Goals:
    </p>
    <ul>
        <li><strong>SDG 4 (Quality Education):</strong> Target 4.4 and 4.a by providing equitable, free, and open telecommunication access to high-quality educational broadcasts in rural and underserved regions.</li>
        <li><strong>SDG 9 (Industry, Innovation, and Infrastructure):</strong> Target 9.c by significantly increasing access to information and communications technology, fostering inclusive innovation over resource-constrained mobile infrastructure.</li>
        <li><strong>SDG 10 (Reduced Inequalities):</strong> Target 10.2 by empowering linguistic minorities and marginalized rural citizens through vernacular speech interfaces and accessible public knowledge repositories.</li>
    </ul>

    <h2 class="section-heading">1.9 Techno-Economic Feasibility, Ethical Boundaries and Safety</h2>
    <p>
        The economic feasibility of Swecha Vedika is established through its complete reliance on permissive open-source technologies (MIT/Apache 2.0). By avoiding commercial API licensing fees, per-minute WebRTC cloud egress charges, and expensive GPU transcription farms, the platform can be sustained by public educational institutions at near-zero incremental operational cost.
    </p>
    <p>
        From an ethical perspective, Swecha Vedika adheres to strict data minimization principles. Audience members are not required to provide personal identity credentials or create intrusive accounts to listen to public broadcasts. In-browser speech transcription processes voice data locally within the client sandbox, preventing voice biometric harvesting.
    </p>

    <h2 class="section-heading">1.10 Organization of the Capstone Project Report</h2>
    <p>
        The remainder of this report is organized into nine structured chapters: Chapter 2 conducts a systematic literature review and comparative analysis. Chapter 3 specifies formal functional and non-functional requirements. Chapter 4 elaborates the system architecture, mathematical adaptation models, and database design. Chapter 5 details implementation mechanics and operational screenshots. Chapter 6 outlines the verification methodology and empirical network degradation trials. Chapter 7 presents comprehensive benchmark results and discussion. Chapter 8 evaluates socio-economic outcomes and SDG impact. Chapter 9 reviews project management and review-gate closures. Chapter 10 concludes the report and identifies future directions.
    </p>
</div>


<!-- ================= CHAPTER 2 ================= -->
<div class="page-break">
    <h1 class="chapter-title">
        CHAPTER 2<br>
        LITERATURE REVIEW, EXISTING SOLUTIONS AND IDENTIFIED GAP
    </h1>

    <h2 class="section-heading">2.1 Review Methodology and Evidence Boundary</h2>
    <p>
        To rigorously contextualize Swecha Vedika within contemporary real-time communication systems, a systematic literature review was conducted spanning peer-reviewed IEEE, ACM, and IETF publications, open-source media server implementations, and industry technical whitepapers published between 2018 and 2026. The search methodology utilized structured queries combining keywords including <em>"Bandwidth-Frugal WebRTC," "Selective Forwarding Unit Scalability," "Opus Codec Bitrate Adaptation," "Indic ASR for Resource-Constrained Environments,"</em> and <em>"WhatsApp Conversational Gateways."</em>
    </p>

    <h2 class="section-heading">2.2 Commercial WebRTC Architectures (Zoom, Microsoft Teams, Google Meet)</h2>
    <p>
        Commercial video collaboration suites represent the predominant state-of-the-art in multi-party communication. However, extensive architectural analysis reveals that their underlying system paradigms are deeply ill-suited for resource-constrained civic deployments:
    </p>
    <ul>
        <li><strong>Bandwidth Over-Allocation:</strong> Commercial platforms mandate minimum symmetrical bitrates of 1.2 to 2.5 Mbps for baseline stability. Even when users disable video, client keep-alive pings, telemetry, and background synchronization consume 120 to 180 kbps, rapidly overwhelming 2G/3G connections.</li>
        <li><strong>Proprietary Protocols and Vendor Lock-In:</strong> Closed-source signaling stacks and proprietary codecs prevent integration with external low-bandwidth gateways or grassroots community tools.</li>
        <li><strong>Prohibitive Licensing Overhead:</strong> Institutional tiers require recurring per-user monthly subscription fees (\$15–\$25/host), imposing impossible financial burdens on non-profit rural schools and civic organizations.</li>
    </ul>

    <h2 class="section-heading">2.3 Open-Source Media Server Implementations (Jitsi, BigBlueButton, Janus)</h2>
    <p>
        Open-source media servers offer substantial self-hosting benefits but present severe operational hurdles in resource-constrained environments:
    </p>
    <ul>
        <li><strong>Jitsi Meet:</strong> Utilizes Jitsi Videobridge (JVB) as an SFU. While highly capable, Jitsi mandates significant cloud resources (minimum 4 vCPUs, 8 GB RAM) for stable operation and deploys a frontend client bundle exceeding 6 MB, causing severe loading latency on low-memory mobile browsers.</li>
        <li><strong>BigBlueButton:</strong> Optimized for academic webinars, BigBlueButton incorporates extensive pedagogical tools. However, its complex monolithic architecture (integrating Kurento/Mediasoup, FreeSWITCH, Redis, and Ruby daemons) requires a dedicated server with 8–16 GB RAM, rendering it unviable for budget VPS deployments.</li>
        <li><strong>Janus Gateway:</strong> A lightweight, highly modular C-based WebRTC gateway. Janus provides excellent raw performance but lacks built-in dual-interface conversational bridging (e.g., WhatsApp integration) and native Indic speech captioning pipelines out of the box.</li>
    </ul>

    <h2 class="section-heading">2.4 Low-Bandwidth Speech Coding Standards and Opus RFC 6716</h2>
    <p>
        The IETF standardized <strong>Opus</strong> interactive audio codec (RFC 6716) provides unprecedented flexibility by unifying Skype's SILK codec (optimized for human speech) and Xiph.Org's CELT codec (optimized for ultra-low latency music). Opus dynamically scales bitrates from 6 kbps to 510 kbps and supports algorithmic frame sizes from 2.5 ms to 60 ms. Academic studies by Valin et al. demonstrate that Opus operating in SILK mode delivers superior speech intelligibility (PESQ > 3.4) at 16–24 kbps compared to legacy narrowband codecs (G.711, AMR-NB). Swecha Vedika exploits this capability by programmatically constraining Opus to narrowband/wideband speech modes under adverse network conditions.
    </p>

    <h2 class="section-heading">2.5 Multilingual Transcription Paradigms and Indic NLP Pipelines</h2>
    <p>
        State-of-the-art Automatic Speech Recognition (ASR) pipelines for Indic languages (e.g., Whisper, AI4Bharat's IndicWav2Vec) require dedicated server-side GPU acceleration (NVIDIA T4/A100) to achieve real-time streaming inference. Hosting such models incurs cloud costs exceeding \$200–\$500/month, completely violating the frugality mandate of civic platforms. Swecha Vedika circumvents this bottleneck by offloading speech transcription directly to the client browser via the standardized W3C Web Speech API, which leverages local on-device neural acoustic models provided by modern browser engines, achieving zero server compute overhead.
    </p>

    <h2 class="section-heading">2.6 Comparative Feature and Constraint Analysis Across Platforms</h2>
    <p>
        Table 2.1 presents a comprehensive comparative evaluation across six representative collaboration platforms evaluated against seven critical engineering criteria:
    </p>

    <table class="report-table">
        <tr>
            <th style="width: 18%;">Evaluation Criterion</th>
            <th style="width: 14%;">Zoom</th>
            <th style="width: 14%;">Google Meet</th>
            <th style="width: 14%;">Jitsi Meet</th>
            <th style="width: 14%;">BigBlueButton</th>
            <th style="width: 26%;">Swecha Vedika (Proposed)</th>
        </tr>
        <tr>
            <td><strong>Minimum Audio Bitrate</strong></td>
            <td>120–180 kbps</td>
            <td>100–150 kbps</td>
            <td>80–120 kbps</td>
            <td>64–96 kbps</td>
            <td><strong>24–48 kbps (Audio-First)</strong></td>
        </tr>
        <tr>
            <td><strong>Client Page / Bundle Weight</strong></td>
            <td>App required / 15 MB web</td>
            <td>8–12 MB web</td>
            <td>6–8 MB web</td>
            <td>10–14 MB web</td>
            <td><strong>&lt; 150 KB (Vanilla JS)</strong></td>
        </tr>
        <tr>
            <td><strong>WhatsApp Dual-Bridge</strong></td>
            <td>None (Proprietary)</td>
            <td>None</td>
            <td>None</td>
            <td>None</td>
            <td><strong>Native (Baileys FSM Bot)</strong></td>
        </tr>
        <tr>
            <td><strong>Live Indic (Telugu) Captions</strong></td>
            <td>Cloud paid tier</td>
            <td>English/Hindi only</td>
            <td>External Vosk</td>
            <td>External Vosk</td>
            <td><strong>In-Browser Web Speech (Free)</strong></td>
        </tr>
        <tr>
            <td><strong>Offline Micro-Podcast Export</strong></td>
            <td>Cloud MP4 (heavy)</td>
            <td>Cloud Drive MP4</td>
            <td>None</td>
            <td>Server recording</td>
            <td><strong>Ultra-compact Opus Audio Archive</strong></td>
        </tr>
        <tr>
            <td><strong>Minimum Server Footprint</strong></td>
            <td>Proprietary SaaS</td>
            <td>Proprietary SaaS</td>
            <td>4 vCPU, 8 GB RAM</td>
            <td>4 vCPU, 16 GB RAM</td>
            <td><strong>1 vCPU, 1 GB RAM (\$6/mo VPS)</strong></td>
        </tr>
        <tr>
            <td><strong>Software Licensing Model</strong></td>
            <td>Proprietary (\$15/mo)</td>
            <td>Proprietary</td>
            <td>Apache 2.0</td>
            <td>LGPL 3.0</td>
            <td><strong>Affero GPL / MIT (Open Access)</strong></td>
        </tr>
    </table>

    <h2 class="section-heading">2.7 Identified Research Gaps and Operational Deficiencies</h2>
    <p>
        The systematic literature survey reveals three critical, unaddressed research gaps:
    </p>
    <ul>
        <li><strong>Research Gap 1 (Bandwidth Floor Rigidity):</strong> Existing WebRTC SFU solutions lack aggressive, application-level degradation logic that decouples audio packet scheduling from video synchronization, causing media transmission to collapse entirely when bandwidth drops below 80 kbps.</li>
        <li><strong>Research Gap 2 (Asynchronous-Synchronous Dichotomy):</strong> Real-time broadcast systems operate in isolation from ubiquitous asynchronous messaging channels (such as WhatsApp), forcing users into high-bandwidth synchronous sessions and disenfranchising asynchronous rural participants.</li>
        <li><strong>Research Gap 3 (GPU Dependency for Vernacular Access):</strong> Existing multilingual captioning architectures enforce costly server-side GPU inference clusters, creating an insurmountable economic barrier for grassroots and non-profit educational platforms.</li>
    </ul>

    <h2 class="section-heading">2.8 Swecha Vedika Positioning and Design Consequences</h2>
    <p>
        Swecha Vedika is explicitly positioned to resolve these three structural gaps. By engineering an asymmetric 1:N audio-first SFU pipeline, bridging a dual-interface WhatsApp conversational gateway, and offloading Indic transcription to browser-native acoustic engines, Swecha Vedika establishes a new operational paradigm for digital equity and bandwidth-frugal civic communication.
    </p>
</div>


<!-- ================= CHAPTER 3 ================= -->
<div class="page-break">
    <h1 class="chapter-title">
        CHAPTER 3<br>
        REQUIREMENTS SPECIFICATION AND ACCEPTANCE CRITERIA
    </h1>

    <h2 class="section-heading">3.1 System Actors, Roles and Primary Operational Use Cases</h2>
    <p>
        The functional architecture of Swecha Vedika is governed by interactions among five key system actors:
    </p>
    <ul>
        <li><strong>Stage Host / Speaker (ACT-01):</strong> Authenticated user who initializes live stage sessions, broadcasts real-time audio, monitors audience size, views incoming Q&A queues, launches instant community polls, and triggers session recording.</li>
        <li><strong>Web-Based Listener (ACT-02):</strong> Anonymous or registered audience member accessing the live stage via web browser over mobile data or broadband. Receives real-time audio, views live transcription, submits text questions, and votes in live polls.</li>
        <li><strong>WhatsApp Participant (ACT-03):</strong> Remote rural user accessing stage interactions via WhatsApp. Discovers active sessions via <code>!stage</code>, submits stage questions via <code>!ask</code>, participates in polls, and requests audio digests.</li>
        <li><strong>Stage Moderator (ACT-04):</strong> Privileged administrative user responsible for reviewing participant questions, filtering inappropriate content, spotlighting audience questions, and managing speaker permissions.</li>
        <li><strong>Automated Knowledge Archiver (ACT-05):</strong> Background server daemon that ingests completed session media, compresses audio tracks into lightweight micro-podcasts, and generates downloadable educational packages.</li>
    </ul>

    <h2 class="section-heading">3.2 Functional Requirements Specification (REQ-F01 to REQ-F18)</h2>
    <p>
        The complete functional scope is formalized across eighteen verified requirements:
    </p>

    <table class="report-table">
        <tr>
            <th style="width: 14%;">Requirement ID</th>
            <th style="width: 26%;">Functional Feature</th>
            <th style="width: 45%;">Formal Specification & Operational Behavior</th>
            <th style="width: 15%;">Target Actor</th>
        </tr>
        <tr><td><strong>REQ-F01</strong></td><td>Live Stage Provisioning</td><td>Host must be able to create an isolated stage session with title, description, and language metadata within &lt; 2 seconds.</td><td>ACT-01</td></tr>
        <tr><td><strong>REQ-F02</strong></td><td>Audio-First WebRTC Stream</td><td>System must publish speaker audio via WebRTC using Opus codec with dynamic bitrate scaling (24–64 kbps).</td><td>ACT-01</td></tr>
        <tr><td><strong>REQ-F03</strong></td><td>1:N Downstream Routing</td><td>SFU media server must broadcast speaker audio to at least 100 concurrent listeners without re-encoding audio tracks.</td><td>ACT-02</td></tr>
        <tr><td><strong>REQ-F04</strong></td><td>Automatic Stream Degradation</td><td>Client must automatically throttle down audio bitrates and suppress video when packet loss exceeds 15%.</td><td>ACT-02</td></tr>
        <tr><td><strong>REQ-F05</strong></td><td>WebSocket Signaling Hub</td><td>Signaling server must manage SDP offer/answer exchanges and ICE candidate dissemination over secure TLS WebSockets.</td><td>ACT-01, ACT-02</td></tr>
        <tr><td><strong>REQ-F06</strong></td><td>Real-Time Q&A Ingestion</td><td>Listeners must be able to post text questions to the stage with upvoting capabilities and instant host visibility.</td><td>ACT-02</td></tr>
        <tr><td><strong>REQ-F07</strong></td><td>Instant Community Polling</td><td>Host must be able to push single/multiple-choice polls to audience with real-time aggregate bar chart visualization.</td><td>ACT-01, ACT-02</td></tr>
        <tr><td><strong>REQ-F08</strong></td><td>Client Speech Transcription</td><td>Browser must capture speaker audio and render live captions using Web Speech API with Telugu (te-IN) language support.</td><td>ACT-01, ACT-02</td></tr>
        <tr><td><strong>REQ-F09</strong></td><td>WhatsApp Stage Discovery</td><td>Bot must parse <code>!stage</code> command and return list of currently active live sessions with speaker and topic details.</td><td>ACT-03</td></tr>
        <tr><td><strong>REQ-F10</strong></td><td>WhatsApp Question Relay</td><td>Bot must parse <code>!ask &lt;msg&gt;</code> and inject question directly into the live stage Q&A queue with WhatsApp sender tag.</td><td>ACT-03</td></tr>
        <tr><td><strong>REQ-F11</strong></td><td>WhatsApp Poll Voting</td><td>Bot must broadcast active poll prompts to registered community groups and ingest numeric reply votes.</td><td>ACT-03</td></tr>
        <tr><td><strong>REQ-F12</strong></td><td>WhatsApp Audio Digest</td><td>Bot must dispatch compressed micro-podcast audio files upon receipt of <code>!summary &lt;stage_id&gt;</code> command.</td><td>ACT-03</td></tr>
        <tr><td><strong>REQ-F13</strong></td><td>Live Audio Level Metering</td><td>Frontend client must render real-time Web Audio API visual feedback of speaker microphone input activity.</td><td>ACT-01, ACT-02</td></tr>
        <tr><td><strong>REQ-F14</strong></td><td>Moderation Dashboard</td><td>Moderators must have authority to delete disruptive questions, mute participants, and ban offending IPs.</td><td>ACT-04</td></tr>
        <tr><td><strong>REQ-F15</strong></td><td>Session Recording Engine</td><td>Server must record raw Opus audio tracks into standardized Ogg/WebM containers without dropping frames.</td><td>ACT-05</td></tr>
        <tr><td><strong>REQ-F16</strong></td><td>Micro-Podcast Compression</td><td>System must post-process recorded sessions into highly compressed audio files (&le; 10 MB per 60-min session).</td><td>ACT-05</td></tr>
        <tr><td><strong>REQ-F17</strong></td><td>Offline Cache Repository</td><td>Web client must store downloaded session transcripts and audio digests locally using browser IndexedDB.</td><td>ACT-02</td></tr>
        <tr><td><strong>REQ-F18</strong></td><td>Admin Metrics Telemetry</td><td>System must expose operational metrics including connected listener count, round-trip latency, and memory footprint.</td><td>ACT-04</td></tr>
    </table>

    <h2 class="section-heading">3.3 Non-Functional and Quality Attributes</h2>
    <p>
        The architectural design is constrained by four non-negotiable quality attributes:
    </p>
    <ul>
        <li><strong>Latency & Real-Time Responsiveness (NFR-01):</strong> End-to-end glass-to-ear audio latency must remain below 400 ms under broadband and below 750 ms under emulated 2G/3G cellular networks to maintain conversational spontaneity.</li>
        <li><strong>Packet Loss Robustness (NFR-02):</strong> The audio stream must maintain speech intelligibility (PESQ &ge; 3.0) under sustained random packet loss rates up to 35% and burst loss durations up to 250 ms.</li>
        <li><strong>Client Execution Footprint (NFR-03):</strong> The entire frontend client bundle must remain below 150 KB uncompressed, execute in &lt; 500 ms on low-end Android mobile browsers, and consume &lt; 40 MB of device RAM.</li>
        <li><strong>Server Computational Frugality (NFR-04):</strong> The complete backend infrastructure (FastAPI, Redis, PostgreSQL, and Node.js Baileys bot) must operate within a 1 vCPU, 1 GB RAM cloud droplet supporting &ge; 100 concurrent listeners.</li>
    </ul>

    <h2 class="section-heading">3.4 Data Storage, Persistence and Relational Entity Requirements</h2>
    <p>
        The persistence tier requires relational ACID compliance to manage stage states, user identities, Q&A sequences, poll tallies, and audit logs. The system utilizes PostgreSQL 15, managed through SQLAlchemy asynchronous ORM models and Alembic schema migrations. All audio recording blobs and static assets are persisted to localized block storage with deterministic content-addressable hashing.
    </p>

    <h2 class="section-heading">3.5 Interface, REST API and WebSocket Protocol Requirements</h2>
    <p>
        External and client interactions are mediated via two formalized protocol tiers:
    </p>
    <ul>
        <li><strong>RESTful API Tier:</strong> Stateless HTTP/2 endpoints providing JSON schemas for session creation, authentication, stage metadata retrieval, and archive download operations.</li>
        <li><strong>Full-Duplex WebSocket Tier:</strong> Persistent bidirectional communication channels supporting low-latency WebRTC SDP signaling, ICE candidate exchanges, real-time Q&A stream synchronization, and instant poll broadcasts.</li>
    </ul>

    <h2 class="section-heading">3.6 Information Security, Stream Encryption and Privacy Requirements</h2>
    <p>
        Real-time audio streams are end-to-end encrypted across transit hops using DTLS 1.2 and SRTP (RFC 3711) with AES-128-GCM cipher suites. Signaling and REST API communications enforce TLS 1.3 encryption. User input payloads (chat, Q&A) undergo rigorous HTML sanitization to prevent Cross-Site Scripting (XSS) and SQL injection vulnerabilities.
    </p>

    <h2 class="section-heading">3.7 Deployment, Containerization and Minimal Hardware Requirements</h2>
    <p>
        To ensure democratic self-hostability by civic organizations, the system must deploy via a single standardized <code>docker-compose.yml</code> manifest on standard Linux distributions (Ubuntu 22.04 LTS, Debian 12), with automated SSL certificate provisioning via Let's Encrypt / Certbot.
    </p>

    <h2 class="section-heading">3.8 Objective-to-Requirement-to-Evidence Acceptance Traceability Matrix</h2>
    <p>
        Table 3.2 maps project objectives to functional requirements and tangible verification evidence:
    </p>

    <table class="report-table">
        <tr>
            <th style="width: 12%;">Objective</th>
            <th style="width: 25%;">Governing Requirements</th>
            <th style="width: 38%;">Target Acceptance Criteria</th>
            <th style="width: 25%;">Verification Evidence Artifact</th>
        </tr>
        <tr>
            <td><strong>O1 (Audio SFU)</strong></td>
            <td>REQ-F02, REQ-F03, REQ-F04, REQ-F05</td>
            <td>Stream maintains intelligibility at &le; 48 kbps under 35% packet loss.</td>
            <td>Chapter 6 netem test logs; Table 7.1 bitrate benchmark data.</td>
        </tr>
        <tr>
            <td><strong>O2 (Transcription)</strong></td>
            <td>REQ-F08, REQ-F13</td>
            <td>Client-side Telugu caption generation with &lt; 800 ms latency and 0 GPU cost.</td>
            <td>Figure 5.1 live caption screenshot; client CPU profiling records.</td>
        </tr>
        <tr>
            <td><strong>O3 (WhatsApp Bot)</strong></td>
            <td>REQ-F09, REQ-F10, REQ-F11, REQ-F12</td>
            <td>Median query turnaround &lt; 500 ms across 50 concurrent simulated users.</td>
            <td>Table 7.2 Baileys load benchmark; Figure 5.3 conversation log.</td>
        </tr>
        <tr>
            <td><strong>O4 (Knowledge Archive)</strong></td>
            <td>REQ-F15, REQ-F16, REQ-F17</td>
            <td>60-min audio compressed to &le; 10 MB; client offline storage functional.</td>
            <td>Figure 5.4 archive downloader; IndexedDB storage audit log.</td>
        </tr>
        <tr>
            <td><strong>O5 (Frugal Cloud)</strong></td>
            <td>REQ-F01, REQ-F14, REQ-F18</td>
            <td>Full stack runs stably on 1 vCPU, 1 GB RAM VPS supporting 100+ listeners.</td>
            <td>Table 7.3 server resource profile; Docker compose deployment manifest.</td>
        </tr>
    </table>
</div>
"""
