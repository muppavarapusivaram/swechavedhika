import os
import subprocess
from pathlib import Path

BASE_DIR = Path(r"C:\Users\Victus\Documents\swecha\prototype")
DOCS_DIR = BASE_DIR / "docs"

def get_base64_image(image_path):
    import base64
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"
    return ""

kl_logo_b64 = get_base64_image(DOCS_DIR / "kl_logo.png")

HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Swecha Vedika - End-Semester External Review Defense Guide (8 Rubrics)</title>
<style>
@page {{
    size: A4 portrait;
    margin: 20mm 18mm 20mm 18mm;
}}
body {{
    font-family: Arial, Helvetica, sans-serif;
    font-size: 10pt;
    line-height: 1.45;
    color: #111;
}}
.header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2pt solid #800000;
    padding-bottom: 8px;
    margin-bottom: 14px;
}}
h1 {{
    font-size: 14pt;
    color: #800000;
    margin: 0 0 4px 0;
    text-transform: uppercase;
}}
.meta-box {{
    background: #fdfaf6;
    border: 1pt solid #ebd5c1;
    border-left: 4pt solid #d9622b;
    padding: 8px 12px;
    margin-bottom: 14px;
    font-size: 9pt;
}}
.rubric-card {{
    border: 1pt solid #d0d7de;
    border-radius: 4px;
    margin-bottom: 12px;
    page-break-inside: avoid;
    overflow: hidden;
}}
.rubric-header {{
    background-color: #800000;
    color: #fff;
    padding: 6px 10px;
    font-weight: bold;
    font-size: 10pt;
    display: flex;
    justify-content: space-between;
}}
.rubric-body {{
    padding: 8px 12px;
    background-color: #ffffff;
}}
.q-title {{
    font-weight: bold;
    color: #0b3954;
    margin-top: 4px;
    margin-bottom: 2px;
}}
ul {{
    margin: 3px 0 6px 18px;
    padding: 0;
}}
li {{
    margin-bottom: 2px;
}}
.badge {{
    background-color: #2e7d32;
    color: #fff;
    padding: 1px 6px;
    border-radius: 3px;
    font-size: 8pt;
}}
</style>
</head>
<body>

<div class="header">
    <div>
        <img src="{kl_logo_b64}" style="height: 50px;" alt="KL Logo">
    </div>
    <div style="text-align: right;">
        <div style="font-weight: bold; color: #800000; font-size: 11pt;">K L DEEMED TO BE UNIVERSITY</div>
        <div style="font-size: 8.5pt; color: #555;">DEPARTMENT OF EXPERIENTIAL LEARNING AND GLOBAL ENGAGEMENT</div>
        <div style="font-size: 8.5pt; font-weight: bold; color: #333;">Capstone Project–I End-Semester External Review Defense Guide</div>
    </div>
</div>

<div class="meta-box">
    <strong>Project Title:</strong> SWECHA VEDIKA: A BANDWIDTH-FRUGAL, MULTILINGUAL LIVE STAGE AND KNOWLEDGE PLATFORM<br>
    <strong>Students:</strong> Muppavarapu Sivaram (2300030447) &nbsp;|&nbsp; Meda Lohith Pavan Kumar (2300030921)<br>
    <strong>Supervisor & Guide:</strong> Dr. Koganti Sripath Roy, Assistant Professor, Department of EL&GE &nbsp;|&nbsp; <strong>Date:</strong> November 2026
</div>

<!-- RUBRIC 1 -->
<div class="rubric-card">
    <div class="rubric-header">
        <span>1. Problem Definition & Objectives</span>
        <span class="badge">100% Ready</span>
    </div>
    <div class="rubric-body">
        <div class="q-title">What to say to Evaluator:</div>
        <p style="margin: 0 0 4px 0;">
            <em>"Existing commercial platforms (Zoom, Google Meet) impose heavy recurring per-host fees (\$150-\$300/yr), require high-speed broadband (>600 kbps), and drop out completely under rural 2G/EDGE cellular constraints. Swecha Vedika solves this by building an open-source, bandwidth-frugal conferencing platform tailored for rural civic-tech outreach with zero licensing cost."</em>
        </p>
        <div class="q-title">Key Objectives (O1–O5):</div>
        <ul>
            <li><strong>O1:</strong> Role-Scoped LiveKit SFU routing (saves server egress by separating stage speakers from viewers).</li>
            <li><strong>O2:</strong> Extreme 2G Low-Data fallback mode (&le; 48 kbps downlink; 85% bandwidth reduction).</li>
            <li><strong>O3:</strong> Meta WhatsApp FSM gateway for zero-data RSVP, stage Q&A, and AI digests.</li>
            <li><strong>O4:</strong> Synchronized Replay-as-Live broadcasting clock (t_offset) with real-time live chat and polls.</li>
            <li><strong>O5:</strong> Bilingual speech-to-text live captions (Telugu & English) and standalone offline learning packs (.zip).</li>
        </ul>
    </div>
</div>

<!-- RUBRIC 2 -->
<div class="rubric-card">
    <div class="rubric-header">
        <span>2. Literature Review & Research Gap</span>
        <span class="badge">100% Ready</span>
    </div>
    <div class="rubric-body">
        <div class="q-title">How Swecha Vedika addresses the Research Gap:</div>
        <ul>
            <li><strong>Commercial SaaS (Zoom/Meet/Teams):</strong> Proprietary closed licensing; bandwidth hungry (600–1800 kbps); no WhatsApp integration; no offline-playable bundles.</li>
            <li><strong>Open-Source SFUs (Jitsi Meet/BigBlueButton):</strong> Heavy server hardware requirements; high egress bandwidth per viewer; no automated Telugu corpus archiving.</li>
            <li><strong>Swecha Vedika Innovation:</strong> Runs on a modest \$10/mo dual-core VPS via Docker Compose; 44.8 kbps 2G mode; WhatsApp front-door bot; time-indexed Telugu Whisper search.</li>
        </ul>
    </div>
</div>

<!-- RUBRIC 3 -->
<div class="rubric-card">
    <div class="rubric-header">
        <span>3. System Design & Methodology</span>
        <span class="badge">100% Ready</span>
    </div>
    <div class="rubric-body">
        <div class="q-title">Architecture & Tech Stack:</div>
        <ul>
            <li><strong>Frontend:</strong> React 18, Vite, LiveKit Components React, Web Speech API (in-browser speech-to-text).</li>
            <li><strong>Backend:</strong> FastAPI (Python 3.11), SQLAlchemy ORM, Alembic migrations, LiveKit Server SDK, bcrypt auth.</li>
            <li><strong>Database:</strong> PostgreSQL 16 (9 relational tables: users, events, attendance, questions, question_upvotes, polls, poll_votes, chat_messages, alembic_version).</li>
            <li><strong>Media SFU:</strong> LiveKit Server (Go) operating across Ports 7880 (WS signaling), 7881 (TCP), 7882/udp (SRTP media).</li>
        </ul>
    </div>
</div>

<!-- RUBRIC 4 -->
<div class="rubric-card">
    <div class="rubric-header">
        <span>4. Implementation & Technical Execution</span>
        <span class="badge">100% Functional</span>
    </div>
    <div class="rubric-body">
        <div class="q-title">5 Major Live Working Modules:</div>
        <ul>
            <li><strong>Live Video Stage:</strong> Multi-speaker stage with mic, camera, screen share, and low-latency audio/video.</li>
            <li><strong>2G Low-Data Mode:</strong> 1-click toggle that disables heavy video and switches to Opus DTX audio at 44.8 kbps.</li>
            <li><strong>Interactive Sidebar:</strong> Stage hand-raising, in-room live chat with Telugu reactions, Q&A upvotes, and real-time polls.</li>
            <li><strong>WhatsApp Bot:</strong> FSM webhook parsing EVENTS, RSVP &lt;id&gt;, ASK &lt;id&gt;: &lt;question&gt;, and SUMMARY &lt;id&gt;.</li>
            <li><strong>Bilingual Speech-to-Text & Offline Bundler:</strong> Real-time Telugu/English live captions and 1-click offline ZIP pack export.</li>
        </ul>
    </div>
</div>

<!-- RUBRIC 5 -->
<div class="rubric-card">
    <div class="rubric-header">
        <span>5. Testing, Validation & Results</span>
        <span class="badge">15/15 Tests Passed</span>
    </div>
    <div class="rubric-body">
        <div class="q-title">Empirical Results:</div>
        <ul>
            <li><strong>Automated Test Suite:</strong> 15 automated test modules in Docker (<code>test_all_features.py</code>) passed 100%.</li>
            <li><strong>Bandwidth Reduction:</strong> 44.8 kbps in 2G mode vs 303 kbps standard (85.21% savings) and 68.4% savings vs SFU video.</li>
            <li><strong>Packet Loss Resilience:</strong> Voice remains fully intelligible up to <strong>35% simulated packet loss</strong> using Linux netem.</li>
            <li><strong>API Performance:</strong> Concurrency stress test (N=50) showed mean latencies of 2.9–18.2 ms and p99 &lt; 27 ms.</li>
        </ul>
    </div>
</div>

<!-- RUBRIC 6 -->
<div class="rubric-card">
    <div class="rubric-header">
        <span>6. Innovation, Originality & Patent Status</span>
        <span class="badge">100% Ready</span>
    </div>
    <div class="rubric-body">
        <ul>
            <li><strong>Original Architectural Contributions:</strong> Dynamic role-scoped asymmetric media token minting combined with WhatsApp stage Q&A bridging, master epoch synchronized replays, and automated offline HTML package bundling.</li>
            <li><strong>Patent / IPR Status:</strong> Developed under Free & Open Source Software (FOSS) principles (AGPLv3 licence). Source code and architectural documentation prepared for institutional copyright registration at KL University.</li>
        </ul>
    </div>
</div>

<!-- RUBRIC 7 -->
<div class="rubric-card">
    <div class="rubric-header">
        <span>7. Research Paper & Consultancy Status</span>
        <span class="badge">Paper Ready</span>
    </div>
    <div class="rubric-body">
        <ul>
            <li><strong>Research Paper Title:</strong> <em>SWECHA VEDIKA: A BANDWIDTH-FRUGAL, MULTILINGUAL LIVE STAGE AND KNOWLEDGE PLATFORM</em>.</li>
            <li><strong>Format:</strong> Fully written and formatted to IEEE/ACM conference standards with mathematical models, benchmarks, and 9 citations.</li>
            <li><strong>Consultancy / Outreach Status:</strong> Deployed in field collaboration with Swecha AP and Free Software Movement India (FSMI) for rural village community center literacy sessions.</li>
        </ul>
    </div>
</div>

<!-- RUBRIC 8 -->
<div class="rubric-card">
    <div class="rubric-header">
        <span>8. Demonstration & Viva-Voce Readiness</span>
        <span class="badge">Live & Functional</span>
    </div>
    <div class="rubric-body">
        <div class="q-title">Role Distribution in Viva:</div>
        <ul>
            <li><strong>Muppavarapu Sivaram (2300030447):</strong> Leads project context, distributed architecture, LiveKit SFU design, 2G bandwidth calculations, and answers backend/infrastructure technical queries.</li>
            <li><strong>Meda Lohith Pavan Kumar (2300030921):</strong> Operates live demonstration (video call, 2G toggle, WhatsApp simulator, live captions, polls, offline pack extraction), and explains frontend/testing results.</li>
        </ul>
    </div>
</div>

</body>
</html>
"""

def main():
    html_path = DOCS_DIR / "review_viva_guide.html"
    pdf_path = DOCS_DIR / "Swecha_Vedika_Review_Rubrics_Viva_Guide.pdf"

    print("Generating Review Viva Guide HTML...")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)

    edge_bin = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    file_uri = "file:///" + str(html_path).replace("\\", "/")
    cmd = [
        edge_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        file_uri
    ]
    print("Compiling Review Viva Guide PDF...")
    subprocess.run(cmd, check=True)
    if pdf_path.exists():
        print(f"SUCCESS: Created {pdf_path.name} ({pdf_path.stat().st_size} bytes)")

if __name__ == "__main__":
    main()
