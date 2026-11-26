def get_references_and_appendices_html():
    return """
<!-- ================= REFERENCES ================= -->
<div class="page-break">
    <h1 class="chapter-title">
        REFERENCES
    </h1>

    <ol style="margin-left: 20pt; line-height: 1.5; font-size: 9.5pt;">
        <li>J. M. Valin, K. Vos, and T. Terriberry, "Definition of the Opus Audio Codec," <em>IETF RFC 6716</em>, Sep. 2012.</li>
        <li>C. Holmberg, H. Alvestrand, and C. Jennings, "Negotiating Media Multiplexing Using the Session Description Protocol (SDP)," <em>IETF RFC 8843</em>, Jan. 2021.</li>
        <li>H. Alvestrand, "Overview: Real-Time Protocols for Browser-Based Applications," <em>IETF RFC 8825</em>, Jan. 2021.</li>
        <li>H. Schulzrinne, S. Casner, R. Frederick, and V. Jacobson, "RTP: A Transport Protocol for Real-Time Applications," <em>IETF RFC 3550</em>, Jul. 2003.</li>
        <li>E. Rescorla, "Datagram Transport Layer Security Version 1.2," <em>IETF RFC 6347</em>, Jan. 2012.</li>
        <li>M. Baugher, D. McGrew, M. Naslund, E. Carrara, and K. Norrman, "The Secure Real-time Transport Protocol (SRTP)," <em>IETF RFC 3711</em>, Mar. 2004.</li>
        <li>R. Stewart, "Stream Control Transmission Protocol," <em>IETF RFC 4960</em>, Sep. 2007.</li>
        <li>P. Rosenberg, R. Mahy, P. Matthews, and D. Wing, "Session Traversal Utilities for NAT (STUN)," <em>IETF RFC 5389</em>, Oct. 2008.</li>
        <li>R. Mahy, P. Matthews, and J. Rosenberg, "Traversal Using Relays around NAT (TURN): Relay Extensions to STUN," <em>IETF RFC 5766</em>, Apr. 2010.</li>
        <li>J. Rosenberg, "Interactive Connectivity Establishment (ICE): A Protocol for Network Address Translator (NAT) Traversal," <em>IETF RFC 8445</em>, Jul. 2018.</li>
        <li>W3C Audio Working Group, "Web Audio API: W3C Candidate Recommendation," <em>World Wide Web Consortium</em>, Jun. 2021. [Online]. Available: https://www.w3.org/TR/webaudio/</li>
        <li>W3C Speech API Community Group, "Web Speech API Specification," <em>World Wide Web Consortium</em>, Aug. 2020. [Online]. Available: https://wicg.github.io/speech-api/</li>
        <li>S. Kakumanu, K. S. Roy, and R. Chivukula, "Low-Bitrate Speech Communication in Resource-Constrained Rural Wireless Networks," <em>IEEE Trans. Consum. Electron.</em>, vol. 68, no. 3, pp. 245–254, Aug. 2022.</li>
        <li>A. Radford et al., "Robust Speech Recognition via Large-Scale Weak Supervision," in <em>Proc. Int. Conf. Mach. Learn. (ICML)</em>, 2023, pp. 28492–28518.</li>
        <li>B. A. Rao, P. V. Reddy, and M. Sivaram, "Architectural Analysis of WebRTC Selective Forwarding Units for Large-Scale Rural Broadcasting," <em>Int. J. Distrib. Syst. Commun.</em>, vol. 14, no. 2, pp. 112–126, 2024.</li>
        <li>United Nations, "Transforming Our World: The 2030 Agenda for Sustainable Development," <em>UN General Assembly Resolution A/RES/70/1</em>, Oct. 2015.</li>
        <li>International Telecommunication Union, "Perceptual Evaluation of Speech Quality (PESQ): An Objective Method for End-to-End Speech Quality Assessment of Narrow-Band Telephone Networks and Speech Codecs," <em>ITU-T Recommendation P.862</em>, Feb. 2001.</li>
        <li>Swecha Telangana Community, "Open Source Digital Solutions for Rural and Marginalized Civic Ecosystems," <em>Swecha Technical Whitepaper Series</em>, Hyderabad, India, Tech. Rep. ST-WP-2025-01, Jan. 2025.</li>
    </ol>
</div>


<!-- ================= APPENDIX A ================= -->
<div class="page-break">
    <h1 class="chapter-title">
        APPENDIX A<br>
        IMPLEMENTED DATA FIELDS AND STORAGE SCHEMAS
    </h1>

    <p>
        This appendix documents the implemented database schemas, field definitions, data types, and primary integrity constraints across the PostgreSQL 15 persistence tier:
    </p>

    <table class="report-table" style="font-size: 8pt;">
        <tr>
            <th style="width: 18%;">Entity Schema</th>
            <th style="width: 20%;">Field Attribute Name</th>
            <th style="width: 16%;">Data Type</th>
            <th style="width: 46%;">Constraints & Semantic Business Rule</th>
        </tr>
        <tr><td><code>stages</code></td><td><code>id</code></td><td>UUID</td><td>Primary Key; generated via <code>uuid_generate_v4()</code>.</td></tr>
        <tr><td><code>stages</code></td><td><code>title</code></td><td>VARCHAR(255)</td><td>NOT NULL; sanitized text descriptor of the live stage.</td></tr>
        <tr><td><code>stages</code></td><td><code>status</code></td><td>VARCHAR(32)</td><td>Enum: <code>draft</code>, <code>live</code>, <code>ended</code>; controls client access.</td></tr>
        <tr><td><code>stages</code></td><td><code>audio_bitrate</code></td><td>INTEGER</td><td>DEFAULT 32000; target Opus bitrate in bps (24000–64000).</td></tr>
        <tr><td><code>stages</code></td><td><code>language</code></td><td>VARCHAR(16)</td><td>DEFAULT 'te-IN'; ISO language-country code for transcription.</td></tr>
        <tr><td><code>qa_questions</code></td><td><code>id</code></td><td>UUID</td><td>Primary Key; unique identifier for audience inquiry.</td></tr>
        <tr><td><code>qa_questions</code></td><td><code>stage_id</code></td><td>UUID</td><td>Foreign Key referencing <code>stages.id</code>; CASCADE on delete.</td></tr>
        <tr><td><code>qa_questions</code></td><td><code>sender_channel</code></td><td>VARCHAR(16)</td><td>Enum: <code>web</code>, <code>whatsapp</code>; identifies provenance gateway.</td></tr>
        <tr><td><code>qa_questions</code></td><td><code>content</code></td><td>TEXT</td><td>NOT NULL; sanitized question body (max 500 characters).</td></tr>
        <tr><td><code>qa_questions</code></td><td><code>upvotes</code></td><td>INTEGER</td><td>DEFAULT 0; aggregate community upvote tally.</td></tr>
        <tr><td><code>polls</code></td><td><code>id</code></td><td>UUID</td><td>Primary Key; unique identifier for interactive poll.</td></tr>
        <tr><td><code>polls</code></td><td><code>options</code></td><td>JSONB</td><td>Array of string options, e.g. <code>["Agree", "Disagree", "Neutral"]</code>.</td></tr>
        <tr><td><code>polls</code></td><td><code>is_active</code></td><td>BOOLEAN</td><td>DEFAULT true; indicates whether votes are currently accepted.</td></tr>
        <tr><td><code>poll_votes</code></td><td><code>id</code></td><td>UUID</td><td>Primary Key; record of individual audience ballot.</td></tr>
        <tr><td><code>poll_votes</code></td><td><code>poll_id</code></td><td>UUID</td><td>Foreign Key referencing <code>polls.id</code>; CASCADE on delete.</td></tr>
        <tr><td><code>poll_votes</code></td><td><code>voter_identifier</code></td><td>VARCHAR(64)</td><td>Hash of IP or WhatsApp phone number; prevents duplicate voting.</td></tr>
        <tr><td><code>transcripts</code></td><td><code>id</code></td><td>UUID</td><td>Primary Key; timestamped caption segment.</td></tr>
        <tr><td><code>transcripts</code></td><td><code>timestamp_ms</code></td><td>BIGINT</td><td>Millisecond offset from session start time.</td></tr>
        <tr><td><code>transcripts</code></td><td><code>text_segment</code></td><td>TEXT</td><td>Transcribed vernacular speech string emitted by Web Speech API.</td></tr>
        <tr><td><code>recordings</code></td><td><code>storage_path</code></td><td>VARCHAR(512)</td><td>Filesystem URI for compressed Opus micro-podcast archive.</td></tr>
    </table>
</div>


<!-- ================= APPENDIX B ================= -->
<div class="page-break">
    <h1 class="chapter-title">
        APPENDIX B<br>
        REFERENCE API INVENTORY AND SIGNALING CONTRACTS
    </h1>

    <p>
        This appendix outlines the RESTful endpoints and WebSocket signaling contracts implemented in the Swecha Vedika backend service:
    </p>

    <table class="report-table" style="font-size: 8pt;">
        <tr>
            <th style="width: 14%;">Protocol / Verb</th>
            <th style="width: 28%;">Endpoint URI Path</th>
            <th style="width: 22%;">Request / Auth Payload</th>
            <th style="width: 36%;">Response Schema & Operational Behavior</th>
        </tr>
        <tr><td><code>POST</code></td><td><code>/api/stages/create</code></td><td>Bearer JWT; JSON body</td><td>Returns <code>{"stage_id": "...", "status": "draft"}</code>.</td></tr>
        <tr><td><code>GET</code></td><td><code>/api/stages/active</code></td><td>Public (No Auth)</td><td>Returns array of currently active live stage sessions.</td></tr>
        <tr><td><code>POST</code></td><td><code>/api/stages/{id}/start</code></td><td>Bearer JWT (Host)</td><td>Transitions stage status to <code>live</code>; enables WebRTC SFU.</td></tr>
        <tr><td><code>POST</code></td><td><code>/api/stages/{id}/end</code></td><td>Bearer JWT (Host)</td><td>Transitions stage to <code>ended</code>; triggers audio archiving.</td></tr>
        <tr><td><code>POST</code></td><td><code>/api/stages/{id}/questions</code></td><td>Public; JSON question</td><td>Appends question to stage queue; notifies WebSocket subscribers.</td></tr>
        <tr><td><code>POST</code></td><td><code>/api/stages/{id}/polls/create</code></td><td>Bearer JWT (Host)</td><td>Publishes poll prompt; broadcasts poll payload to listeners.</td></tr>
        <tr><td><code>POST</code></td><td><code>/api/stages/{id}/polls/vote</code></td><td>Public; voter hash + option</td><td>Records vote; returns updated live poll aggregate percentages.</td></tr>
        <tr><td><code>GET</code></td><td><code>/api/stages/{id}/archive</code></td><td>Public (No Auth)</td><td>Streams compressed 24 kbps Opus micro-podcast audio file.</td></tr>
        <tr><td><code>WS</code></td><td><code>/ws/signaling/{stage_id}</code></td><td>WebSocket handshake</td><td>Full-duplex SDP offer/answer exchanges and ICE candidate relay.</td></tr>
        <tr><td><code>WS</code></td><td><code>/ws/stage/{stage_id}/events</code></td><td>WebSocket handshake</td><td>Publishes real-time Q&A arrivals, poll tallies, and Telugu captions.</td></tr>
        <tr><td><code>POST</code></td><td><code>/api/internal/webhook/whatsapp</code></td><td>X-Internal-Secret header</td><td>Internal gateway endpoint ingesting WhatsApp FSM commands.</td></tr>
    </table>
</div>


<!-- ================= APPENDIX C ================= -->
<div class="page-break">
    <h1 class="chapter-title">
        APPENDIX C<br>
        EVALUATION REPRODUCIBILITY RECORD
    </h1>

    <p>
        To ensure scientific reproducibility, this appendix provides the complete manifest for recreating the experimental testbed and executing the verification benchmarks:
    </p>

    <h3 class="sub-heading">C.1 Containerized Deployment Deployment Manifest</h3>
    <p>
        The complete platform can be provisioned on any clean Ubuntu 22.04 LTS host using Docker and Docker Compose with the following sequence:
    </p>

    <div class="equation-box" style="font-size: 8pt;">
        <span>git clone https://github.com/swecha/vedika.git && cd vedika && docker-compose up -d --build</span>
        <span>(Terminal Command)</span>
    </div>

    <h3 class="sub-heading">C.2 Linux Kernel Traffic Control (tc-netem) Impairment Commands</h3>
    <p>
        Network emulation scripts utilized for Chapter 6 and Chapter 7 degradation benchmarks are reproducible using standard Linux <code>iproute2</code> commands:
    </p>

    <div class="equation-box" style="font-size: 8pt;">
        <span># Simulate 2G Network: 35% packet loss, 450ms delay, 120ms jitter<br>sudo tc qdisc add dev eth0 root netem loss 35% delay 450ms 120ms distribution normal</span>
        <span>(Netem 2G Profile)</span>
    </div>

    <div class="equation-box" style="font-size: 8pt;">
        <span># Clear all network impairments<br>sudo tc qdisc del dev eth0 root</span>
        <span>(Netem Reset)</span>
    </div>

    <h3 class="sub-heading">C.3 Concurrency and Load Testing Harness</h3>
    <p>
        Simulated multi-user load testing for the WhatsApp conversational gateway and WebRTC signaling server was executed using Locust 2.15:
    </p>

    <div class="equation-box" style="font-size: 8pt;">
        <span>locust -f tests/load/locustfile.py --headless -u 100 -r 10 --run-time 15m --host http://localhost:8000</span>
        <span>(Locust Execution)</span>
    </div>

    <p style="margin-top: 10pt;">
        All raw benchmark CSV data files, packet capture PCAP files, and PESQ speech evaluation logs are archived under the <code>benchmarks/results/</code> directory in the official project repository.
    </p>
</div>
"""
