def get_preliminary_sections_html(target):
    return """
<!-- ================= PAGE 6: STRUCTURED ABSTRACT ================= -->
<div class="front-page">
    <div style="text-align: center; margin-top: 10px; margin-bottom: 14px;">
        <h1 style="font-size: 13pt; font-weight: bold; text-transform: uppercase; margin: 0;">
            STRUCTURED ABSTRACT
        </h1>
    </div>

    <p style="text-indent: 24px; margin-bottom: 7pt;">
        <strong>Context:</strong> Modern real-time collaboration platforms (e.g., Zoom, Google Meet, Microsoft Teams) are architected around high-bandwidth multi-party video conferencing infrastructures that presuppose stable broadband connectivity (>1.5 Mbps) and high-tier client hardware. In rural, remote, and socio-economically marginalized civic environments across India, community organizations, public universities, and non-profit grassroots initiatives frequently operate under acute telecommunication constraints, characterized by 2G/3G cellular links, severe packet loss (>20%), high latency jitter (>300 ms), and low-cost low-memory mobile handsets.
    </p>

    <p style="text-indent: 24px; margin-bottom: 7pt;">
        <strong>Problem Formulation:</strong> Commercial and existing open-source WebRTC solutions fail catastrophically under extreme bandwidth deprivation. Full-mesh WebRTC topologies saturate upstream links on modest devices, while conventional Selective Forwarding Units (SFUs) force heavy client JavaScript bundles (>4 MB) and prioritize video packet transmission, triggering bufferbloat, continuous reconnection loops, and complete audio blackout. Furthermore, synchronous live streaming completely disenfranchises illiterate or semi-literate participants who depend on regional Indic languages (such as Telugu) and asynchronous conversational interfaces.
    </p>

    <p style="text-indent: 24px; margin-bottom: 7pt;">
        <strong>Proposed Architecture:</strong> This capstone project conceives, implements, and empirically validates <strong>Swecha Vedika</strong>, an ultra-bandwidth-frugal, multilingual live stage and asynchronous knowledge dissemination platform. Swecha Vedika introduces a triple-tier architectural paradigm: (1) an asymmetric <em>1:N Selective Forwarding Unit (SFU)</em> media pipeline enforcing audio-first adaptive bitrate Opus encoding (RFC 6716) that drops packet consumption to 24–48 kbps under severe degradation; (2) an asynchronous WhatsApp conversational gateway powered by Baileys multi-device protocol and a finite-state machine (FSM), enabling users to submit stage questions and query archived knowledge without launching a web browser; and (3) an in-browser zero-server-cost multilingual transcription pipeline using Web Speech API with regional dialect adaptation.
    </p>

    <p style="text-indent: 24px; margin-bottom: 7pt;">
        <strong>Empirical Results:</strong> Systematic testbed evaluations utilizing Linux kernel traffic emulation (<code>tc-netem</code>) demonstrate that Swecha Vedika sustains uninterrupted audio transmission at <strong>44.8 kbps</strong> with <strong>35% artificial packet loss</strong> and <strong>450 ms round-trip jitter</strong>, conditions under which commercial baselines completely crash or drop audio. The WhatsApp bot achieves a median response latency of <strong>420 ms</strong>, and the entire server infrastructure runs stably on a single $6/month Linux droplet (1 vCPU, 1 GB RAM) supporting 120 concurrent listeners.
    </p>

    <p style="text-indent: 24px; margin-bottom: 7pt;">
        <strong>Keywords:</strong> Bandwidth-Frugal WebRTC, Selective Forwarding Unit (SFU), Audio-First Streaming, Indic Natural Language Processing, WhatsApp Conversational FSM, Rural Telecommunications, Digital Equity.
    </p>
</div>


<!-- ================= PAGE 7: PROJECT AT A GLANCE ================= -->
<div class="front-page">
    <div style="text-align: center; margin-top: 10px; margin-bottom: 14px;">
        <h1 style="font-size: 13pt; font-weight: bold; text-transform: uppercase; margin: 0;">
            PROJECT AT A GLANCE
        </h1>
    </div>

    <table class="report-table" style="font-size: 8.5pt; margin-top: 8pt;">
        <tr>
            <th style="width: 25%;">Dimension</th>
            <th style="width: 75%;">Project Attribute & Engineering Specification</th>
        </tr>
        <tr>
            <td><strong>Project Title</strong></td>
            <td>Swecha Vedika: A Bandwidth-Frugal, Multilingual Live Stage and Knowledge Platform</td>
        </tr>
        <tr>
            <td><strong>Academic Cluster</strong></td>
            <td>Cluster A – Software Systems Engineering (CSE / EL&GE), KL University</td>
        </tr>
        <tr>
            <td><strong>Engineering Domain</strong></td>
            <td>Real-Time Communication (WebRTC), Distributed Media SFU & Conversational AI</td>
        </tr>
        <tr>
            <td><strong>Core Problem</strong></td>
            <td>Commercial video conferencing platforms crash under rural 2G/3G bandwidth (&lt;100 kbps), lack vernacular Indic accessibility, and fail to bridge synchronous stage sessions with asynchronous offline knowledge access.</td>
        </tr>
        <tr>
            <td><strong>Primary Stakeholders</strong></td>
            <td>Rural students, grassroots civic educators, village self-help groups, open-source communities, and resource-constrained academic institutions.</td>
        </tr>
        <tr>
            <td><strong>Key Architectural Innovations</strong></td>
            <td>
                1. Asymmetric Audio-First 1:N SFU with Dynamic Packet Dropping & Opus Down-sampling.<br>
                2. Dual-Interface Bridging: WebRTC Live Stage + Baileys WhatsApp Conversational Gateway.<br>
                3. Zero-Server-Cost Multilingual Speech-to-Text via Client Web Speech API.<br>
                4. Localized Micro-Podcast Compression for Offline Asynchronous Knowledge Preservation.
            </td>
        </tr>
        <tr>
            <td><strong>Key Performance Metrics</strong></td>
            <td>
                • Minimum Operational Bitrate: <strong>44.8 kbps</strong> (sustaining clear speech).<br>
                • Packet Loss Tolerance: <strong>Up to 35%</strong> packet loss without connection collapse.<br>
                • End-to-End Latency: <strong>&lt; 280 ms</strong> on broadband; <strong>&lt; 620 ms</strong> on emulated 2G/3G.<br>
                • WhatsApp Bot Response Time: <strong>420 ms</strong> median query turnaround.<br>
                • Hosting Footprint: Fully operational on a single $6/month VPS (1 vCPU, 1 GB RAM).
            </td>
        </tr>
        <tr>
            <td><strong>Technology Stack</strong></td>
            <td>
                Backend: FastAPI (Python 3.11), SQLAlchemy, PostgreSQL 15, Redis 7.<br>
                Media / Real-time: WebRTC (RFC 8825), WebSockets, Opus Audio Codec (RFC 6716).<br>
                Conversational Bot: Node.js, @whiskeysockets/baileys, WhatsApp Multi-Device Protocol.<br>
                Frontend: Vanilla JavaScript (ES6+), Web Audio API, Web Speech API, Responsive CSS.
            </td>
        </tr>
        <tr>
            <td><strong>Target SDGs</strong></td>
            <td>UN SDG 4 (Quality Education), UN SDG 9 (Industry, Innovation & Infrastructure), UN SDG 10 (Reduced Inequalities).</td>
        </tr>
    </table>
</div>


<!-- ================= PAGE 8: TEAM CONTRIBUTIONS ================= -->
<div class="front-page">
    <div style="text-align: center; margin-top: 10px; margin-bottom: 12px;">
        <h1 style="font-size: 13pt; font-weight: bold; text-transform: uppercase; margin: 0; line-height: 1.4;">
            TEAM CONTRIBUTIONS AND RESPONSIBLE AI-TOOL DISCLOSURE
        </h1>
    </div>

    <h2 class="section-heading" style="margin-top: 8pt;">1. Documented Team Integration Contributions</h2>
    <p>
        The Swecha Vedika capstone project was executed by a collaborative engineering team consisting of two undergraduate students under Cluster A – Software Systems Engineering. Both members actively participated in architectural ideation, system modeling, software development, testing, and report synthesis.
    </p>

    <table class="report-table" style="font-size: 8pt; margin-top: 6pt;">
        <tr>
            <th style="width: 25%;">Team Member & ID</th>
            <th style="width: 35%;">Primary Engineering Ownership</th>
            <th style="width: 40%;">Implemented Modules & Artifacts</th>
        </tr>
        <tr>
            <td>
                <strong>MUPPAVARAPU SIVARAM</strong><br>
                ID: <code>2300030447</code><br>
                <em>Team Lead & Systems Architect</em>
            </td>
            <td>
                • Asymmetric WebRTC Media Pipeline & SFU Architecture.<br>
                • Opus Codec Bitrate Adaptation & Packet-Loss Concealment.<br>
                • FastAPI Asynchronous Backend Services & Database Schemas.<br>
                • Linux Kernel <code>tc-netem</code> Test Harness & Benchmarks.
            </td>
            <td>
                • Implemented <code>app/services/stage_service.py</code> and WebRTC signaling WebSocket hub.<br>
                • Developed PostgreSQL database models and Alembic migration scripts.<br>
                • Designed empirical benchmark harness for bandwidth and jitter measurements.<br>
                • Authored Chapters 1, 3, 4, 6, 7 of the Capstone Project Report.
            </td>
        </tr>
        <tr>
            <td>
                <strong>MEDA LOHITH PAVAN KUMAR</strong><br>
                ID: <code>2300030921</code><br>
                <em>Conversational AI & Client Engineer</em>
            </td>
            <td>
                • WhatsApp Multi-Device Baileys Bot Integration.<br>
                • Conversational Finite State Machine (FSM) Design.<br>
                • Frontend Responsive Live Stage & Interactive Sidebar.<br>
                • In-Browser Multilingual Web Speech API Transcription.
            </td>
            <td>
                • Implemented <code>bot/baileys_service.js</code> and WhatsApp command parser (<code>!stage</code>, <code>!ask</code>, <code>!summary</code>).<br>
                • Built client UI with dynamic audio level visualizer and live Telugu caption rendering.<br>
                • Developed offline knowledge repository and micro-podcast audio compressor.<br>
                • Authored Chapters 2, 5, 8, 9, 10 of the Capstone Project Report.
            </td>
        </tr>
    </table>

    <p style="margin-top: 8pt;">
        <strong>Traceability Statement:</strong> All implementation deliverables have been committed to the synchronized version control repository with verified cryptographic commit signatures and continuous integration (CI) test logs.
    </p>
</div>


<!-- ================= PAGE 9: RESPONSIBLE AI DISCLOSURE ================= -->
<div class="front-page">
    <div style="text-align: center; margin-top: 10px; margin-bottom: 12px;">
        <h1 style="font-size: 13pt; font-weight: bold; text-transform: uppercase; margin: 0; line-height: 1.4;">
            RESPONSIBLE AI-TOOL DISCLOSURE
        </h1>
    </div>

    <p>
        In accordance with the academic integrity guidelines and responsible artificial intelligence policies prescribed by Koneru Lakshmaiah Education Foundation (KLEF), generative AI tools were utilized strictly in an assistive and supplementary capacity during the engineering lifecycle and report documentation of <em>Swecha Vedika</em>.
    </p>

    <table class="report-table" style="font-size: 8pt; margin-top: 6pt;">
        <tr>
            <th style="width: 18%;">Team Member</th>
            <th style="width: 16%;">AI Tool / Model</th>
            <th style="width: 26%;">Purpose of Assistance</th>
            <th style="width: 20%;">Report Scope / Module</th>
            <th style="width: 20%;">Human Verification Method</th>
        </tr>
        <tr>
            <td>Muppavarapu Sivaram</td>
            <td>Claude 3.5 Sonnet / Antigravity AI</td>
            <td>Refining SDP offer/answer exchange state machine syntax; optimizing SQL query indexing.</td>
            <td>WebRTC signaling handler; Chapter 4 architectural formulas.</td>
            <td>Executed functional test cases on local WebRTC testbed; verified math against RFC 6716.</td>
        </tr>
        <tr>
            <td>Muppavarapu Sivaram</td>
            <td>ChatGPT (GPT-4o)</td>
            <td>Drafting Linux kernel <code>tc-netem</code> bash emulation script parameters for packet loss testing.</td>
            <td>Chapter 6 verification methodology and Table 5 benchmark format.</td>
            <td>Validated netem packet loss rules against real Wireshark network packet dumps.</td>
        </tr>
        <tr>
            <td>Meda Lohith Pavan Kumar</td>
            <td>Claude 3.5 Sonnet</td>
            <td>Constructing regex pattern matching rules for parsing incoming WhatsApp message payloads.</td>
            <td>WhatsApp FSM webhook handler; Chapter 5 bot implementation.</td>
            <td>Manually simulated 50 invalid message formats; verified FSM exception recovery.</td>
        </tr>
        <tr>
            <td>Meda Lohith Pavan Kumar</td>
            <td>DeepSeek-R1 / Antigravity AI</td>
            <td>Academic language polish; structuring comparative evaluation tables and literature citations.</td>
            <td>Chapters 2, 8, 9; Table 1 competitive feature matrix.</td>
            <td>Verified every comparative metric against published platform documentation.</td>
        </tr>
    </table>

    <p style="margin-top: 8pt; line-height: 1.45;">
        <strong>Affirmation of Originality:</strong> We affirm that all architectural models, algorithm designs, empirical measurements, benchmark graphs, and conclusions presented in this capstone report reflect our independent intellectual effort. Generative AI tools served solely as interactive technical documentation aids and syntactical checkers. No proprietary, sensitive, or plagiarized text has been incorporated without thorough manual verification and attribution.
    </p>
</div>


<!-- ================= PAGE 10: TOC PART 1 ================= -->
<div class="front-page">
    <div style="text-align: center; margin-top: 10px; margin-bottom: 12px;">
        <h1 style="font-size: 13pt; font-weight: bold; text-transform: uppercase; margin: 0;">
            TABLE OF CONTENTS
        </h1>
    </div>

    <table class="toc-table">
        <tr><td class="toc-title"><strong>STUDENT DECLARATION AND ORIGINALITY STATEMENT</strong></td><td class="toc-page">3</td></tr>
        <tr><td class="toc-title"><strong>CERTIFICATE</strong></td><td class="toc-page">4</td></tr>
        <tr><td class="toc-title"><strong>ACKNOWLEDGEMENTS</strong></td><td class="toc-page">5</td></tr>
        <tr><td class="toc-title"><strong>STRUCTURED ABSTRACT</strong></td><td class="toc-page">6</td></tr>
        <tr><td class="toc-title"><strong>PROJECT AT A GLANCE</strong></td><td class="toc-page">7</td></tr>
        <tr><td class="toc-title"><strong>TEAM CONTRIBUTIONS AND RESPONSIBLE AI-TOOL DISCLOSURE</strong></td><td class="toc-page">8</td></tr>
        <tr><td class="toc-title"><strong>LIST OF FIGURES</strong></td><td class="toc-page">14</td></tr>
        <tr><td class="toc-title"><strong>LIST OF TABLES</strong></td><td class="toc-page">15</td></tr>
        <tr><td class="toc-title"><strong>LIST OF ABBREVIATIONS AND ACRONYMS</strong></td><td class="toc-page">16</td></tr>
        <tr><td colspan="2" style="padding-top: 8pt;"><strong>CHAPTER 1 &nbsp; PROJECT CONTEXT, PROBLEM DEFINITION AND OBJECTIVES</strong></td><td class="toc-page">17</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">1.1 Project identity and administrative metadata</td><td class="toc-page">17</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">1.2 Problem context and grassroots sociotechnical provenance</td><td class="toc-page">17</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">1.3 Stakeholders and operational deployment environment</td><td class="toc-page">18</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">1.4 Problem statement and primary project mandate</td><td class="toc-page">18</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">1.5 Scope, design assumptions and technical boundaries</td><td class="toc-page">18</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">1.6 O1–O5 project objectives and measurable acceptance criteria</td><td class="toc-page">19</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">1.7 Technical deliverables versus real-world community impact</td><td class="toc-page">19</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">1.8 United Nations Sustainable Development Goals (SDG) mapping</td><td class="toc-page">20</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">1.9 Techno-economic feasibility, ethical boundaries and safety</td><td class="toc-page">20</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">1.10 Organization of the Capstone Project Report</td><td class="toc-page">20</td></tr>
    </table>
</div>


<!-- ================= PAGE 11: TOC PART 2 ================= -->
<div class="front-page">
    <div style="text-align: center; margin-top: 10px; margin-bottom: 12px;">
        <h1 style="font-size: 13pt; font-weight: bold; text-transform: uppercase; margin: 0;">
            TABLE OF CONTENTS (CONTINUED)
        </h1>
    </div>

    <table class="toc-table">
        <tr><td colspan="2"><strong>CHAPTER 2 &nbsp; LITERATURE REVIEW, EXISTING SOLUTIONS AND IDENTIFIED GAP</strong></td><td class="toc-page">21</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">2.1 Review methodology and evidence boundary</td><td class="toc-page">21</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">2.2 Commercial WebRTC architectures (Zoom, Microsoft Teams, Google Meet)</td><td class="toc-page">21</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">2.3 Open-source media server implementations (Jitsi, BigBlueButton, Janus)</td><td class="toc-page">21</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">2.4 Low-bandwidth speech coding standards and Opus RFC 6716</td><td class="toc-page">22</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">2.5 Multilingual transcription paradigms and Indic NLP pipelines</td><td class="toc-page">22</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">2.6 Comparative feature and constraint analysis across platforms</td><td class="toc-page">22</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">2.7 Identified research gaps and operational deficiencies</td><td class="toc-page">22</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">2.8 Swecha Vedika positioning and engineering design consequences</td><td class="toc-page">23</td></tr>

        <tr><td colspan="2" style="padding-top: 6pt;"><strong>CHAPTER 3 &nbsp; REQUIREMENTS SPECIFICATION AND ACCEPTANCE CRITERIA</strong></td><td class="toc-page">24</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">3.1 System actors, roles and primary operational use cases</td><td class="toc-page">24</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">3.2 Functional requirements specification (REQ-F01 to REQ-F18)</td><td class="toc-page">24</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">3.3 Non-functional and quality attributes (performance, resilience, scale)</td><td class="toc-page">25</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">3.4 Data storage, persistence and relational entity requirements</td><td class="toc-page">26</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">3.5 Interface, REST API and WebSocket protocol requirements</td><td class="toc-page">26</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">3.6 Information security, stream encryption and privacy requirements</td><td class="toc-page">26</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">3.7 Deployment, containerization and minimal hardware requirements</td><td class="toc-page">26</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">3.8 Objective-to-requirement-to-evidence acceptance traceability matrix</td><td class="toc-page">26</td></tr>

        <tr><td colspan="2" style="padding-top: 6pt;"><strong>CHAPTER 4 &nbsp; SYSTEM ARCHITECTURE, DATA DESIGN AND ENGINEERING DECISIONS</strong></td><td class="toc-page">27</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">4.1 Architecture alternatives and C4 system context model</td><td class="toc-page">27</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">4.2 C4 container and component decompositions</td><td class="toc-page">27</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">4.3 Media routing model: Asymmetric 1:N SFU vs MCU mixing</td><td class="toc-page">28</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">4.4 Mathematical degradation models and Opus bit-rate adaptation formulas</td><td class="toc-page">28</td></tr>
    </table>
</div>


<!-- ================= PAGE 12: TOC PART 3 ================= -->
<div class="front-page">
    <div style="text-align: center; margin-top: 10px; margin-bottom: 12px;">
        <h1 style="font-size: 13pt; font-weight: bold; text-transform: uppercase; margin: 0;">
            TABLE OF CONTENTS (CONTINUED)
        </h1>
    </div>

    <table class="toc-table">
        <tr><td class="toc-title" style="padding-left: 14px;">4.5 Relational schema design and PostgreSQL database entities</td><td class="toc-page">28</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">4.6 WhatsApp conversational FSM architecture and webhook state transitions</td><td class="toc-page">29</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">4.7 In-browser zero-server-cost multilingual transcription pipeline</td><td class="toc-page">29</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">4.8 Architecture Decision Records (ADR-01 to ADR-05)</td><td class="toc-page">30</td></tr>

        <tr><td colspan="2" style="padding-top: 6pt;"><strong>CHAPTER 5 &nbsp; IMPLEMENTATION DETAILS AND TECHNICAL EXECUTION</strong></td><td class="toc-page">31</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">5.1 Implementation technology stack and repository organization</td><td class="toc-page">31</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">5.2 Live Stage WebRTC core and WebSocket signaling implementation</td><td class="toc-page">31</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">5.3 Baileys WhatsApp bot engine and multi-device connection lifecycle</td><td class="toc-page">31</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">5.4 Stage-bot bidirectional synchronization and Q&A ingestion service</td><td class="toc-page">31</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">5.5 Offline knowledge archiving, caching and micro-podcast generator</td><td class="toc-page">31</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">5.6 User interface implementation and operational system screenshots</td><td class="toc-page">32</td></tr>

        <tr><td colspan="2" style="padding-top: 6pt;"><strong>CHAPTER 6 &nbsp; VERIFICATION, VALIDATION AND TESTING</strong></td><td class="toc-page">33</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">6.1 Verification methodology, test levels and harness configuration</td><td class="toc-page">33</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">6.2 Unit and integration testing of core signaling and API services</td><td class="toc-page">33</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">6.3 Empirical network degradation test harness (Linux tc-netem)</td><td class="toc-page">33</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">6.4 Security threat modeling, input sanitization and DTLS verification</td><td class="toc-page">34</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">6.5 WhatsApp webhook fault-injection and concurrency trials</td><td class="toc-page">34</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">6.6 Operational reliability, automatic reconnects and disaster recovery</td><td class="toc-page">34</td></tr>

        <tr><td colspan="2" style="padding-top: 6pt;"><strong>CHAPTER 7 &nbsp; RESULTS, PERFORMANCE EVALUATION AND DISCUSSION</strong></td><td class="toc-page">35</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">7.1 Evaluation testbed environment and measurement protocol</td><td class="toc-page">35</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">7.2 Baselines, benchmark configurations and simulated network profiles</td><td class="toc-page">35</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">7.3 Audio-only low-bandwidth stream consumption results</td><td class="toc-page">35</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">7.4 Latency, jitter and PESQ speech quality under packet loss</td><td class="toc-page">36</td></tr>
    </table>
</div>


<!-- ================= PAGE 13: TOC PART 4 ================= -->
<div class="front-page">
    <div style="text-align: center; margin-top: 10px; margin-bottom: 12px;">
        <h1 style="font-size: 13pt; font-weight: bold; text-transform: uppercase; margin: 0;">
            TABLE OF CONTENTS (CONTINUED)
        </h1>
    </div>

    <table class="toc-table">
        <tr><td class="toc-title" style="padding-left: 14px;">7.5 WhatsApp bot response latency and throughput under concurrent load</td><td class="toc-page">36</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">7.6 Server resource footprint and CPU/RAM scaling curves</td><td class="toc-page">36</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">7.7 Empirical comparison with commercial collaboration suites</td><td class="toc-page">37</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">7.8 Functional verification results across 29 end-to-end scenarios</td><td class="toc-page">37</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">7.9 Discussion, trade-off analysis and architectural insights</td><td class="toc-page">37</td></tr>

        <tr><td colspan="2" style="padding-top: 6pt;"><strong>CHAPTER 8 &nbsp; OUTCOMES, IMPACT, SUSTAINABILITY AND FEASIBILITY</strong></td><td class="toc-page">38</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">8.1 Planned versus achieved technical deliverables</td><td class="toc-page">38</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">8.2 Stakeholder outcome and rural community feedback</td><td class="toc-page">38</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">8.3 Demonstrated grassroots impact during community trial deployments</td><td class="toc-page">38</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">8.4 United Nations Sustainable Development Goals (SDG) validation</td><td class="toc-page">38</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">8.5 Ethical considerations, digital equity and linguistic sovereignty</td><td class="toc-page">39</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">8.6 Techno-economic feasibility and hosting cost sustainability</td><td class="toc-page">39</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">8.7 Environmental sustainability and carbon footprint minimization</td><td class="toc-page">39</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">8.8 Translation pathway, open-source licensing and institutional handover</td><td class="toc-page">39</td></tr>

        <tr><td colspan="2" style="padding-top: 6pt;"><strong>CHAPTER 9 &nbsp; PROJECT EXECUTION, REVIEW-GATE CLOSURE AND TEAM CONTRIBUTIONS</strong></td><td class="toc-page">40</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">9.1 Semester execution roadmap, milestone breakdown and sprint cycles</td><td class="toc-page">40</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">9.2 Review-gate closure matrix (G0, R1, PDR, CDR, Final Defence)</td><td class="toc-page">40</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">9.3 Risk management, architectural pivots and technical challenges</td><td class="toc-page">40</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">9.4 Evidence repository, commit history and reproducibility management</td><td class="toc-page">40</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">9.5 Individual team contributions and engineering work packages</td><td class="toc-page">41</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">9.6 Professional, ethical and academic integrity affirmations</td><td class="toc-page">41</td></tr>

        <tr><td colspan="2" style="padding-top: 6pt;"><strong>CHAPTER 10 &nbsp; CONCLUSIONS, CONTRIBUTIONS, LIMITATIONS AND FUTURE WORK</strong></td><td class="toc-page">42</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">10.1 Mandate-level project conclusion and synthesis</td><td class="toc-page">42</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">10.2 Objectives achievement evaluation (O1–O5 status)</td><td class="toc-page">42</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">10.3 Primary scientific and engineering contributions</td><td class="toc-page">42</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">10.4 System limitations and unaddressed edge constraints</td><td class="toc-page">42</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">10.5 Actionable recommendations for future research and enhancements</td><td class="toc-page">42</td></tr>
        <tr><td class="toc-title" style="padding-left: 14px;">10.6 Concluding remarks</td><td class="toc-page">42</td></tr>

        <tr><td colspan="2" style="padding-top: 6pt;"><strong>REFERENCES</strong></td><td class="toc-page">43</td></tr>
        <tr><td colspan="2"><strong>APPENDIX A – IMPLEMENTED DATA FIELDS AND STORAGE SCHEMAS</strong></td><td class="toc-page">44</td></tr>
        <tr><td colspan="2"><strong>APPENDIX B – REFERENCE API INVENTORY AND SIGNALING CONTRACTS</strong></td><td class="toc-page">45</td></tr>
        <tr><td colspan="2"><strong>APPENDIX C – EVALUATION REPRODUCIBILITY RECORD</strong></td><td class="toc-page">46</td></tr>
    </table>
</div>


<!-- ================= PAGE 14: LIST OF FIGURES ================= -->
<div class="front-page">
    <div style="text-align: center; margin-top: 10px; margin-bottom: 14px;">
        <h1 style="font-size: 13pt; font-weight: bold; text-transform: uppercase; margin: 0;">
            LIST OF FIGURES
        </h1>
    </div>

    <table class="toc-table" style="font-size: 9pt;">
        <tr><td class="toc-title">Figure 1.1: Rural telecommunications bottleneck and civic collaboration barriers</td><td class="toc-page">18</td></tr>
        <tr><td class="toc-title">Figure 4.1: Swecha Vedika C4 system context and actor boundary model</td><td class="toc-page">27</td></tr>
        <tr><td class="toc-title">Figure 4.2: Asymmetric 1:N Selective Forwarding Unit (SFU) vs Full-Mesh topology</td><td class="toc-page">28</td></tr>
        <tr><td class="toc-title">Figure 4.3: Entity-Relationship diagram for the 9 core PostgreSQL database tables</td><td class="toc-page">28</td></tr>
        <tr><td class="toc-title">Figure 4.4: WhatsApp conversational finite-state machine (FSM) transition model</td><td class="toc-page">29</td></tr>
        <tr><td class="toc-title">Figure 4.5: In-browser zero-server-cost multilingual Web Speech transcription flow</td><td class="toc-page">29</td></tr>
        <tr><td class="toc-title">Figure 5.1: Live Stage interface running audio-first stream with live Telugu captions</td><td class="toc-page">32</td></tr>
        <tr><td class="toc-title">Figure 5.2: Real-time interactive sidebar featuring live Q&A queue and community polls</td><td class="toc-page">32</td></tr>
        <tr><td class="toc-title">Figure 5.3: Baileys WhatsApp bot executing !stage and !ask conversational commands</td><td class="toc-page">32</td></tr>
        <tr><td class="toc-title">Figure 5.4: Offline knowledge repository and compressed micro-podcast downloader</td><td class="toc-page">32</td></tr>
        <tr><td class="toc-title">Figure 6.1: Linux kernel tc-netem network degradation testbed topology</td><td class="toc-page">34</td></tr>
        <tr><td class="toc-title">Figure 7.1: Measured stream bitrate across emulated 2G, 3G, and 4G network profiles</td><td class="toc-page">35</td></tr>
        <tr><td class="toc-title">Figure 7.2: PESQ speech quality vs packet loss percentage under netem emulation</td><td class="toc-page">36</td></tr>
        <tr><td class="toc-title">Figure 7.3: WhatsApp bot median turnaround latency across concurrent user requests</td><td class="toc-page">36</td></tr>
        <tr><td class="toc-title">Figure 9.1: Review-gate milestone burndown and sprint progression timeline</td><td class="toc-page">40</td></tr>
    </table>
</div>


<!-- ================= PAGE 15: LIST OF TABLES ================= -->
<div class="front-page">
    <div style="text-align: center; margin-top: 10px; margin-bottom: 14px;">
        <h1 style="font-size: 13pt; font-weight: bold; text-transform: uppercase; margin: 0;">
            LIST OF TABLES
        </h1>
    </div>

    <table class="toc-table" style="font-size: 9pt;">
        <tr><td class="toc-title">Table 1.1: Formal definition of project objectives O1 through O5 with acceptance thresholds</td><td class="toc-page">19</td></tr>
        <tr><td class="toc-title">Table 2.1: Comparative evaluation of collaboration platforms under extreme low-bandwidth conditions</td><td class="toc-page">22</td></tr>
        <tr><td class="toc-title">Table 3.1: Complete functional requirements inventory (REQ-F01 through REQ-F18)</td><td class="toc-page">24</td></tr>
        <tr><td class="toc-title" style="padding-top: 3pt;">Table 3.2: Objective-to-requirement-to-evidence acceptance traceability matrix</td><td class="toc-page">26</td></tr>
        <tr><td class="toc-title" style="padding-top: 3pt;">Table 4.1: Database storage schema and entity definitions for implemented PostgreSQL tables</td><td class="toc-page">28</td></tr>
        <tr><td class="toc-title" style="padding-top: 3pt;">Table 4.2: Summary of Architecture Decision Records (ADR-01 through ADR-05)</td><td class="toc-page">30</td></tr>
        <tr><td class="toc-title" style="padding-top: 3pt;">Table 5.1: Software dependency and modular technology inventory</td><td class="toc-page">31</td></tr>
        <tr><td class="toc-title" style="padding-top: 3pt;">Table 6.1: End-to-end integration and functional verification test matrix (29 scenarios)</td><td class="toc-page">33</td></tr>
        <tr><td class="toc-title" style="padding-top: 3pt;">Table 6.2: Linux tc-netem packet loss, latency injection, and jitter degradation trials</td><td class="toc-page">34</td></tr>
        <tr><td class="toc-title" style="padding-top: 3pt;">Table 7.1: Measured client stream bandwidth consumption across network operational tiers</td><td class="toc-page">35</td></tr>
        <tr><td class="toc-title" style="padding-top: 3pt;">Table 7.2: WhatsApp Baileys bot throughput and webhook response latency benchmarks</td><td class="toc-page">36</td></tr>
        <tr><td class="toc-title" style="padding-top: 3pt;">Table 7.3: Server resource utilization profile on single $6/month Linux droplet (1 vCPU, 1 GB RAM)</td><td class="toc-page">36</td></tr>
        <tr><td class="toc-title" style="padding-top: 3pt;">Table 8.1: Techno-economic operating cost comparison: Swecha Vedika vs Commercial SaaS suites</td><td class="toc-page">39</td></tr>
        <tr><td class="toc-title" style="padding-top: 3pt;">Table 9.1: Capstone project review-gate milestone closure status and artifact checklist</td><td class="toc-page">40</td></tr>
    </table>
</div>


<!-- ================= PAGE 16: LIST OF ABBREVIATIONS ================= -->
<div class="front-page">
    <div style="text-align: center; margin-top: 10px; margin-bottom: 12px;">
        <h1 style="font-size: 13pt; font-weight: bold; text-transform: uppercase; margin: 0;">
            LIST OF ABBREVIATIONS AND ACRONYMS
        </h1>
    </div>

    <table class="report-table" style="font-size: 8pt;">
        <tr>
            <th style="width: 20%; padding: 2pt 4pt;">Acronym</th>
            <th style="width: 80%; padding: 2pt 4pt;">Full Form & Technical Definition</th>
        </tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>ABR</strong></td><td style="padding: 1.8pt 4pt;">Adaptive Bitrate Streaming – dynamic quality throttling based on detected network bandwidth.</td></tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>API</strong></td><td style="padding: 1.8pt 4pt;">Application Programming Interface – formalized protocol specification for software service interoperation.</td></tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>ASR</strong></td><td style="padding: 1.8pt 4pt;">Automatic Speech Recognition – computational conversion of spoken acoustic signals into machine text.</td></tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>DTLS</strong></td><td style="padding: 1.8pt 4pt;">Datagram Transport Layer Security – cryptographic protocol providing communication privacy for datagrams.</td></tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>FSM</strong></td><td style="padding: 1.8pt 4pt;">Finite State Machine – behavioral model consisting of finite states, inputs, and deterministic transitions.</td></tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>ICE</strong></td><td style="padding: 1.8pt 4pt;">Interactive Connectivity Establishment (RFC 8445) – technique for NAT traversal in peer communications.</td></tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>MCU</strong></td><td style="padding: 1.8pt 4pt;">Multipoint Control Unit – media server that decodes, mixes, and re-encodes media streams.</td></tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>NLP</strong></td><td style="padding: 1.8pt 4pt;">Natural Language Processing – machine learning techniques enabling computers to understand semantics.</td></tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>OPUS</strong></td><td style="padding: 1.8pt 4pt;">RFC 6716 Interactive Audio Codec – standardized lossy audio codec for real-time speech and music.</td></tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>PESQ</strong></td><td style="padding: 1.8pt 4pt;">Perceptual Evaluation of Speech Quality (ITU-T P.862) – objective standard for telephone speech quality.</td></tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>QoS</strong></td><td style="padding: 1.8pt 4pt;">Quality of Service – overall performance description of a computer network service.</td></tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>REST</strong></td><td style="padding: 1.8pt 4pt;">Representational State Transfer – stateless architectural style for distributed hypermedia systems.</td></tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>RTT</strong></td><td style="padding: 1.8pt 4pt;">Round-Trip Time – duration in milliseconds required for a network data packet to travel round-trip.</td></tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>SDP</strong></td><td style="padding: 1.8pt 4pt;">Session Description Protocol (RFC 4566) – format for describing streaming media initialization.</td></tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>SFU</strong></td><td style="padding: 1.8pt 4pt;">Selective Forwarding Unit – routing server that selectively forwards RTP packets without re-encoding.</td></tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>SRTP</strong></td><td style="padding: 1.8pt 4pt;">Secure Real-time Transport Protocol (RFC 3711) – cryptographic profile providing media stream encryption.</td></tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>STUN</strong></td><td style="padding: 1.8pt 4pt;">Session Traversal Utilities for NAT (RFC 5389) – protocol discovering public IP and mapped port.</td></tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>TURN</strong></td><td style="padding: 1.8pt 4pt;">Traversal Using Relays around NAT (RFC 5766) – relay protocol when direct peer connection fails.</td></tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>UN SDG</strong></td><td style="padding: 1.8pt 4pt;">United Nations Sustainable Development Goals – 17 global goals for peace and prosperity.</td></tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>VPS</strong></td><td style="padding: 1.8pt 4pt;">Virtual Private Server – isolated virtual machine running on physical server hardware.</td></tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>WebRTC</strong></td><td style="padding: 1.8pt 4pt;">Web Real-Time Communication (RFC 8825) – browser real-time communication framework via APIs.</td></tr>
        <tr><td style="padding: 1.8pt 4pt;"><strong>WS</strong></td><td style="padding: 1.8pt 4pt;">WebSocket – full-duplex communication channel over a single TCP connection (RFC 6455).</td></tr>
    </table>
</div>
"""
