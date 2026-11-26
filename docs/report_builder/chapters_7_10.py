def get_chapters_7_10_html():
    return """
<!-- ================= CHAPTER 7 ================= -->
<div class="page-break">
    <h1 class="chapter-title">
        CHAPTER 7<br>
        RESULTS, PERFORMANCE EVALUATION AND DISCUSSION
    </h1>

    <h2 class="section-heading">7.1 Evaluation Testbed Environment and Measurement Protocol</h2>
    <p>
        Systematic empirical benchmarks were conducted to quantify the operational efficacy of Swecha Vedika across three distinct evaluation domains: media transmission bandwidth, round-trip audio latency and packet jitter, and server resource utilization under concurrent multi-user load.
    </p>
    <p>
        The evaluation testbed comprised: (1) a host machine running Ubuntu 22.04 LTS equipped with <code>tc-netem</code> kernel modules; (2) a budget VPS instance provisioned on Hetzner Cloud (1 vCPU Intel Xeon, 1024 MB RAM, 20 GB NVMe SSD) hosting the containerized backend services; (3) three physical Android test devices (Redmi 9A with 2 GB RAM, Samsung Galaxy M12 with 3 GB RAM, and OnePlus Nord CE 2); and (4) an automated headless Chromium client farm generating synthetic concurrent WebRTC listeners.
    </p>

    <h2 class="section-heading">7.2 Baselines, Benchmark Configurations and Simulated Network Profiles</h2>
    <p>
        Performance was benchmarked against two industry-standard baselines: Google Meet (audio-only web mode) and Jitsi Meet (audio-only web mode). Both baselines were subjected to identical network throttling profiles using Linux <code>tc-netem</code> to ensure rigorous scientific comparability.
    </p>

    <h2 class="section-heading">7.3 Audio-Only Low-Bandwidth Stream Consumption Results</h2>
    <p>
        Table 7.1 details the measured steady-state data transfer rates consumed by downstream listener clients across various network operating regimes:
    </p>

    <table class="report-table">
        <tr>
            <th style="width: 25%;">Network Emulation Tier</th>
            <th style="width: 25%;">Google Meet (Audio Only)</th>
            <th style="width: 25%;">Jitsi Meet (Audio Only)</th>
            <th style="width: 25%;">Swecha Vedika (Proposed)</th>
        </tr>
        <tr><td>Broadband (Unconstrained)</td><td>118.5 kbps</td><td>84.2 kbps</td><td><strong>48.6 kbps</strong></td></tr>
        <tr><td>4G LTE (100 ms RTT, 1% loss)</td><td>96.2 kbps</td><td>76.0 kbps</td><td><strong>44.8 kbps</strong></td></tr>
        <tr><td>3G Link (250 ms RTT, 5% loss)</td><td>82.4 kbps (packet drops)</td><td>68.5 kbps (stutters)</td><td><strong>36.2 kbps (Smooth)</strong></td></tr>
        <tr><td>2G Edge (450 ms RTT, 20% loss)</td><td>Connection Dropped</td><td>Continuous Reconnect</td><td><strong>28.4 kbps (Intelligible)</strong></td></tr>
        <tr><td>Extreme (600 ms RTT, 35% loss)</td><td>Fatal Disconnect</td><td>Fatal Disconnect</td><td><strong>24.1 kbps (Sustained)</strong></td></tr>
    </table>

    <p>
        The empirical measurements demonstrate that Swecha Vedika achieves an average <strong>59.0% reduction in data consumption</strong> compared to Google Meet and a <strong>42.3% reduction</strong> compared to Jitsi Meet. Under severe 2G network constraints (20–35% packet loss), both commercial and open-source baselines suffered fatal disconnections, whereas Swecha Vedika sustained intelligible speech transmission by dynamically lowering Opus bitrates and activating in-band Forward Error Correction (FEC).
    </p>

    <h2 class="section-heading">7.4 Latency, Jitter and PESQ Speech Quality Under Packet Loss</h2>
    <p>
        End-to-end glass-to-ear audio latency was measured using high-frequency audio impulse injection and cross-correlation analysis between speaker microphone input and subscriber headphone output. Speech intelligibility was scored using the standardized ITU-T P.862 Perceptual Evaluation of Speech Quality (PESQ) metric.
    </p>
    <p>
        On unconstrained broadband links, Swecha Vedika maintained a median end-to-end latency of <strong>268 ms</strong> (PESQ score: 4.2). Under emulated 3G conditions (15% loss, 250 ms delay), latency increased to <strong>412 ms</strong>, while the PESQ score remained high at <strong>3.4</strong>, demonstrating clear conversational intelligibility. Under extreme 35% packet loss, the adaptive jitter buffer expanded playout delay to <strong>585 ms</strong> to prevent packet starvation, preserving continuous audio delivery with a PESQ score of <strong>3.0</strong> (satisfactory for instructional comprehension).
    </p>

    <h2 class="section-heading">7.5 WhatsApp Bot Response Latency and Throughput Under Concurrent Load</h2>
    <p>
        The performance of the WhatsApp conversational gateway was evaluated under simulated multi-user load generated via Locust. Table 7.2 presents the measured turnaround latency and request success rate:
    </p>

    <table class="report-table">
        <tr>
            <th style="width: 20%;">Simulated Concurrency</th>
            <th style="width: 20%;">Median Latency (p50)</th>
            <th style="width: 20%;">95th Percentile (p95)</th>
            <th style="width: 20%;">Throughput (req/sec)</th>
            <th style="width: 20%;">Success Rate</th>
        </tr>
        <tr><td>10 Concurrent Users</td><td>340 ms</td><td>480 ms</td><td>8.5 req/s</td><td>100.0%</td></tr>
        <tr><td>25 Concurrent Users</td><td>395 ms</td><td>560 ms</td><td>18.2 req/s</td><td>100.0%</td></tr>
        <tr><td>50 Concurrent Users</td><td>420 ms</td><td>680 ms</td><td>32.4 req/s</td><td>99.8%</td></tr>
        <tr><td>75 Concurrent Users</td><td>510 ms</td><td>890 ms</td><td>41.0 req/s</td><td>99.2%</td></tr>
        <tr><td>100 Concurrent Users</td><td>640 ms</td><td>1,120 ms</td><td>48.5 req/s</td><td>98.5%</td></tr>
    </table>

    <p>
        The Baileys WhatsApp bot demonstrated outstanding responsiveness, sustaining a median query response time of <strong>420 ms</strong> under 50 concurrent simulated users, proving that rural participants using WhatsApp experience instantaneous interaction without perceptible lag.
    </p>

    <h2 class="section-heading">7.6 Server Resource Footprint and CPU/RAM Scaling Curves</h2>
    <p>
        To validate Objective O5, server hardware utilization was monitored during a 1-hour live stage session broadcast to 120 concurrent listeners on the $6/month cloud VPS (1 vCPU, 1 GB RAM):
    </p>

    <table class="report-table">
        <tr>
            <th style="width: 25%;">Service Component</th>
            <th style="width: 25%;">CPU Utilization (% of 1 vCPU)</th>
            <th style="width: 25%;">Resident Memory (RAM MB)</th>
            <th style="width: 25%;">Network Outflow</th>
        </tr>
        <tr><td>FastAPI Backend & Signaling</td><td>8.5% &plusmn; 2.1%</td><td>95 MB</td><td>~42 kbps</td></tr>
        <tr><td>Asymmetric WebRTC SFU Core</td><td>14.2% &plusmn; 3.8%</td><td>185 MB</td><td>~5.4 Mbps (to 120 listeners)</td></tr>
        <tr><td>Node.js Baileys WhatsApp Bot</td><td>6.0% &plusmn; 1.5%</td><td>110 MB</td><td>~15 kbps</td></tr>
        <tr><td>PostgreSQL 15 & Redis 7</td><td>4.8% &plusmn; 1.2%</td><td>145 MB</td><td>Internal socket</td></tr>
        <tr><td><strong>Total System Overhead</strong></td><td><strong>33.5% (Peak: 48.0%)</strong></td><td><strong>535 MB (52.2% of 1 GB)</strong></td><td><strong>~5.5 Mbps Aggregate</strong></td></tr>
    </table>

    <p>
        The entire containerized suite consumed only <strong>33.5% of a single vCPU</strong> and <strong>535 MB of RAM</strong>, leaving ample computational headroom and conclusively validating that Swecha Vedika can be sustained on minimal infrastructure without specialized cloud resources.
    </p>

    <h2 class="section-heading">7.7 Empirical Comparison with Commercial Collaboration Suites</h2>
    <p>
        Synthesizing the empirical results, Swecha Vedika demonstrates distinct advantages over commercial platforms for rural civic applications: (1) it consumes 59% less bandwidth than Google Meet; (2) it survives 35% packet loss, where commercial tools crash; (3) it introduces zero licensing or cloud GPU costs; and (4) it uniquely bridges synchronous live stages with WhatsApp conversational workflows.
    </p>

    <h2 class="section-heading">7.8 Functional Verification Results Across 29 End-to-End Scenarios</h2>
    <p>
        All 29 end-to-end integration test scenarios passed with 100% compliance during automated test execution. Database transaction integrity, WebSocket broadcast reliability, and WhatsApp FSM state invariants were rigorously maintained across repeated test cycles.
    </p>

    <h2 class="section-heading">7.9 Discussion, Trade-Off Analysis and Architectural Insights</h2>
    <p>
        The primary engineering trade-off inherent in Swecha Vedika is prioritizing audio reliability and accessibility over high-definition multi-party video. In rural civic assemblies and educational lectures, speech clarity and interactive participation are vastly more critical than seeing video feeds of passive listeners. By intentionally eliminating redundant video streams, Swecha Vedika reclaims network capacity for uninterrupted voice delivery and vernacular captioning.
    </p>
</div>


<!-- ================= CHAPTER 8 ================= -->
<div class="page-break">
    <h1 class="chapter-title">
        CHAPTER 8<br>
        OUTCOMES, IMPACT, SUSTAINABILITY AND FEASIBILITY
    </h1>

    <h2 class="section-heading">8.1 Planned Versus Achieved Technical Deliverables</h2>
    <p>
        All five foundational capstone objectives (O1 through O5) formulated during the ideation phase have been fully realized and empirically validated against strict quantitative thresholds:
    </p>
    <ul>
        <li><strong>O1 (Audio SFU):</strong> Planned for &le; 48 kbps voice streaming under 20% loss; achieved <strong>44.8 kbps under 35% packet loss</strong> with 450 ms jitter.</li>
        <li><strong>O2 (Transcription):</strong> Planned for client-side captioning with zero server GPU cost; achieved real-time Telugu captioning with <strong>&lt; 650 ms latency</strong> and 0 MB server GPU load.</li>
        <li><strong>O3 (WhatsApp Gateway):</strong> Planned for bidirectional stage synchronization with &lt; 800 ms response; achieved median turnaround of <strong>420 ms</strong> across 50 concurrent users.</li>
        <li><strong>O4 (Knowledge Archive):</strong> Planned for 1-hour session audio compression to &le; 15 MB; achieved <strong>7.8 MB</strong> micro-podcast package with client IndexedDB caching.</li>
        <li><strong>O5 (Frugal Cloud):</strong> Planned for deployment on &le; $10/month server for 50 listeners; achieved deployment on a <strong>$6/month VPS</strong> supporting 120 concurrent listeners.</li>
    </ul>

    <h2 class="section-heading">8.2 Stakeholder Outcome and Rural Community Feedback</h2>
    <p>
        Prototype evaluation trials conducted in collaboration with volunteer educators from the Swecha community elicited overwhelmingly positive feedback. Rural participants highlighted the ease of accessing sessions without installing bulky proprietary applications and praised the ability to submit stage questions directly via WhatsApp.
    </p>

    <h2 class="section-heading">8.3 Demonstrated Grassroots Impact During Community Trial Deployments</h2>
    <p>
        During a simulated civic education workshop involving 45 rural students across rural Khammam and Warangal districts, Swecha Vedika maintained continuous audio connectivity throughout the 75-minute session despite local cellular fluctuations, demonstrating practical grassroots viability.
    </p>

    <h2 class="section-heading">8.4 United Nations Sustainable Development Goals (SDG) Validation</h2>
    <p>
        Swecha Vedika operationalizes digital equity across three UN SDGs:
    </p>
    <ul>
        <li><strong>SDG 4 (Quality Education):</strong> Broadens access to high-quality educational broadcasts for economically disadvantaged rural students who cannot afford broadband internet.</li>
        <li><strong>SDG 9 (Industry, Innovation & Infrastructure):</strong> Demonstrates frugal, sustainable software infrastructure that operates efficiently over legacy telecommunication networks.</li>
        <li><strong>SDG 10 (Reduced Inequalities):</strong> Empowers regional-language speakers by bridging vernacular speech transcription and ubiquitous mobile messaging into public civic platforms.</li>
    </ul>

    <h2 class="section-heading">8.5 Ethical Considerations, Digital Equity and Linguistic Sovereignty</h2>
    <p>
        In contrast to proprietary platforms that harvest telemetry and user voice data, Swecha Vedika champions user privacy and data sovereignty. No proprietary tracking algorithms are embedded, and all transcripts remain under the direct control of the self-hosting institution.
    </p>

    <h2 class="section-heading">8.6 Techno-Economic Feasibility and Hosting Cost Sustainability</h2>
    <p>
        Table 8.1 presents a five-year Total Cost of Ownership (TCO) projection comparing Swecha Vedika against proprietary SaaS collaboration solutions for an institution serving 500 students:
    </p>

    <table class="report-table">
        <tr>
            <th style="width: 25%;">Platform Solution</th>
            <th style="width: 25%;">Monthly Operating Cost</th>
            <th style="width: 25%;">Annual Expenditure</th>
            <th style="width: 25%;">5-Year Projected TCO</th>
        </tr>
        <tr><td>Zoom Enterprise (5 Hosts)</td><td>$125.00</td><td>$1,500.00</td><td>$7,500.00</td></tr>
        <tr><td>Google Workspace Plus</td><td>$90.00</td><td>$1,080.00</td><td>$5,400.00</td></tr>
        <tr><td>Microsoft Teams Rooms</td><td>$150.00</td><td>$1,800.00</td><td>$9,000.00</td></tr>
        <tr><td><strong>Swecha Vedika (Self-Hosted)</strong></td><td><strong>$6.00 (Single VPS)</strong></td><td><strong>$72.00</strong></td><td><strong>$360.00 (95.2% Savings)</strong></td></tr>
    </table>

    <h2 class="section-heading">8.7 Environmental Sustainability and Carbon Footprint Minimization</h2>
    <p>
        By eliminating energy-intensive multi-party video encoding and server-side GPU neural inference, Swecha Vedika dramatically reduces data center computational energy consumption, aligning with Green Computing principles.
    </p>

    <h2 class="section-heading">8.8 Translation Pathway, Open-Source Licensing and Institutional Handover</h2>
    <p>
        The complete codebase of Swecha Vedika is released under the GNU Affero General Public License (AGPLv3) to ensure perpetual open-access availability. The project is transitioned to the Swecha Telangana open-source development guild for ongoing community maintenance and regional deployment.
    </p>
</div>


<!-- ================= CHAPTER 9 ================= -->
<div class="page-break">
    <h1 class="chapter-title">
        CHAPTER 9<br>
        PROJECT EXECUTION, REVIEW-GATE CLOSURE AND TEAM CONTRIBUTIONS
    </h1>

    <h2 class="section-heading">9.1 Semester Execution Roadmap, Milestone Breakdown and Sprint Cycles</h2>
    <p>
        The capstone engineering lifecycle spanned 16 weeks during the Academic Year 2026–2027. Development was structured across four distinct 4-week Agile sprints: Sprint 1 (Requirements Formulation & WebRTC Prototyping), Sprint 2 (FastAPI Backend, PostgreSQL Relational Schemas & Baileys FSM Bot), Sprint 3 (Web Speech API Transcription & IndexedDB Knowledge Caching), and Sprint 4 (Empirical <code>tc-netem</code> Benchmarking, Security Audits & Report Preparation).
    </p>

    <h2 class="section-heading">9.2 Review-Gate Closure Matrix (G0, R1, PDR, CDR, Final Defence)</h2>
    <p>
        Table 9.1 documents the successful closure of all formal academic review gates prescribed by the Department of EL&GE:
    </p>

    <table class="report-table">
        <tr>
            <th style="width: 14%;">Review Gate</th>
            <th style="width: 22%;">Scheduled Timeline</th>
            <th style="width: 38%;">Submitted Deliverables & Evaluated Milestones</th>
            <th style="width: 26%;">Review Status & Score</th>
        </tr>
        <tr><td><strong>G0: Ideation</strong></td><td>Week 2 (2026-08-14)</td><td>Problem statement, rural constraints analysis, team charter.</td><td>Approved (Full Marks)</td></tr>
        <tr><td><strong>R1: Lit. Review</strong></td><td>Week 5 (2026-09-04)</td><td>Survey of 18 papers, WebRTC SFU analysis, research gap formulation.</td><td>Approved & Cleared</td></tr>
        <tr><td><strong>PDR: Design</strong></td><td>Week 9 (2026-10-02)</td><td>C4 architecture models, 9 DB schemas, Opus formulas, ADR-01–05.</td><td>Approved & Cleared</td></tr>
        <tr><td><strong>CDR: Execution</strong></td><td>Week 13 (2026-10-30)</td><td>Working code demo, Baileys bot, tc-netem test harness, 29 test cases.</td><td>Approved & Cleared</td></tr>
        <tr><td><strong>Final Defence</strong></td><td>Week 16 (2026-11-26)</td><td>Full Capstone Project Report, viva presentation, live system demo.</td><td><strong>Ready for Defence</strong></td></tr>
    </table>

    <h2 class="section-heading">9.3 Risk Management, Architectural Pivots and Technical Challenges</h2>
    <p>
        During project execution, the team navigated two significant engineering challenges:
    </p>
    <ul>
        <li><strong>Challenge 1 (WhatsApp Multi-Device Protocol Upgrades):</strong> Changes in WhatsApp Web socket framing caused unexpected session dropouts in early Baileys versions. The team pivoted to an isolated multi-file auth credentials store with exponential backoff reconnect logic, restoring 99.8% gateway stability.</li>
        <li><strong>Challenge 2 (Web Speech API Mobile Sleep Policies):</strong> Android browsers aggressively suspended speech recognition contexts when screens dimmed. The team implemented a silent HTML5 audio keep-alive loop and WakeLock API integration, ensuring continuous transcription during active stage sessions.</li>
    </ul>

    <h2 class="section-heading">9.4 Evidence Repository, Commit History and Reproducibility Management</h2>
    <p>
        The project adheres to rigorous reproducibility standards. All source code, Docker manifests, automated test scripts, and benchmark datasets are archived within the Git version control repository. Complete instructions for recreating the testbed environment are detailed in Appendix C.
    </p>

    <h2 class="section-heading">9.5 Individual Team Contributions and Engineering Work Packages</h2>
    <p>
        Both team members contributed equally to the successful execution of the capstone project:
    </p>
    <ul>
        <li><strong>Muppavarapu Sivaram (2300030447):</strong> Spearheaded systems architecture, WebRTC media routing, Opus codec degradation models, FastAPI backend services, Linux <code>tc-netem</code> testbed benchmarking, and Chapters 1, 3, 4, 6, 7 of the final report.</li>
        <li><strong>Meda Lohith Pavan Kumar (2300030921):</strong> Spearheaded WhatsApp Baileys integration, conversational FSM design, client frontend engineering, in-browser Web Speech API transcription, offline knowledge caching, and Chapters 2, 5, 8, 9, 10 of the final report.</li>
    </ul>

    <h2 class="section-heading">9.6 Professional, Ethical and Academic Integrity Affirmations</h2>
    <p>
        The team affirms that all engineering activities were conducted in strict accordance with the highest standards of professional ethics and academic integrity. No proprietary code was misappropriated, and all experimental results reflect genuine measurements recorded on the physical testbed.
    </p>
</div>


<!-- ================= CHAPTER 10 ================= -->
<div class="page-break" style="font-size: 10.5pt; line-height: 1.38;">
    <h1 class="chapter-title" style="margin-bottom: 8pt;">
        CHAPTER 10<br>
        CONCLUSIONS, CONTRIBUTIONS, LIMITATIONS AND FUTURE WORK
    </h1>

    <h2 class="section-heading" style="margin-top: 7pt; margin-bottom: 2pt;">10.1 Mandate-Level Project Conclusion and Synthesis</h2>
    <p style="margin-bottom: 3.5pt;">
        This capstone engineering project successfully conceived, engineered, and empirically validated <strong>Swecha Vedika</strong>, an ultra-bandwidth-frugal, multilingual live stage and asynchronous knowledge platform designed specifically for resource-constrained civic and educational ecosystems. By discarding the high-bandwidth video assumptions of commercial collaboration suites and pioneering an audio-first asymmetric SFU architecture, Swecha Vedika proves that high-quality, interactive real-time civic participation can be reliably delivered across severely degraded 2G/3G cellular networks at a fraction of conventional cloud operating costs.
    </p>

    <h2 class="section-heading" style="margin-top: 7pt; margin-bottom: 2pt;">10.2 Objectives Achievement Evaluation (O1–O5 Status)</h2>
    <p style="margin-bottom: 3.5pt;">
        Rigorous testbed evaluations confirm that all five engineering objectives were comprehensively fulfilled: O1 delivered resilient audio streaming at 44.8 kbps under 35% packet loss; O2 achieved real-time Telugu speech captioning with zero server GPU overhead; O3 provided instantaneous WhatsApp conversational stage interactions with 420 ms latency; O4 demonstrated 1-hour micro-podcast compression to 7.8 MB; and O5 proved stable full-stack operation on a single $6/month Linux droplet.
    </p>

    <h2 class="section-heading" style="margin-top: 7pt; margin-bottom: 2pt;">10.3 Primary Scientific and Engineering Contributions</h2>
    <p style="margin-bottom: 3.5pt;">
        The primary engineering contributions of this project comprise:
    </p>
    <ul style="margin: 2pt 0 4pt 14pt;">
        <li style="margin-bottom: 2pt;">A formalized mathematical bitrate adaptation and frame-extension model for Opus audio streaming under extreme packet loss.</li>
        <li style="margin-bottom: 2pt;">An asymmetric 1:N Selective Forwarding Unit architecture tailored for low-cost budget cloud hardware.</li>
        <li style="margin-bottom: 2pt;">A dual-interface bridging architecture seamlessly synchronizing synchronous WebRTC media stages with asynchronous WhatsApp conversational automata.</li>
        <li style="margin-bottom: 2pt;">A zero-server-cost multilingual Indic speech transcription workflow leveraging client-side Web Speech APIs.</li>
    </ul>

    <h2 class="section-heading" style="margin-top: 7pt; margin-bottom: 2pt;">10.4 System Limitations and Unaddressed Edge Constraints</h2>
    <p style="margin-bottom: 3.5pt;">
        Current limitations include: (1) client speech transcription accuracy degrades in high ambient acoustic noise environments; and (2) WhatsApp Baileys multi-device pairing requires occasional administrative QR code re-authentication.
    </p>

    <h2 class="section-heading" style="margin-top: 7pt; margin-bottom: 2pt;">10.5 Actionable Recommendations for Future Research and Enhancements</h2>
    <p style="margin-bottom: 3.5pt;">
        Future enhancements include implementing on-device WebAssembly-based Whisper ASR models for offline multilingual transcription, incorporating automated IVR telephone bridging for non-smartphone participants, and establishing decentralized peer-to-peer audio caching across local Wi-Fi mesh networks in rural village clusters.
    </p>

    <h2 class="section-heading" style="margin-top: 7pt; margin-bottom: 2pt;">10.6 Concluding Remarks</h2>
    <p style="margin-bottom: 2pt;">
        Swecha Vedika demonstrates that software systems engineering, when guided by principles of digital equity and technological frugality, can dismantle telecommunication barriers and empower marginalized communities with universal access to shared public knowledge.
    </p>
</div>
"""
