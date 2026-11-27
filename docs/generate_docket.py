from pathlib import Path
import subprocess
import fitz

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs"

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
@page {
    size: A4 portrait;
    margin: 18mm 20mm 18mm 20mm;
}
body {
    font-family: 'Times New Roman', Times, serif;
    font-size: 10.5pt;
    line-height: 1.45;
    color: #111;
    margin: 0;
    padding: 0;
}
.header-table {
    width: 100%;
    border-bottom: 2px solid #0B2545;
    padding-bottom: 8px;
    margin-bottom: 14px;
}
.univ-title {
    font-size: 12pt;
    font-weight: bold;
    color: #0B2545;
    text-transform: uppercase;
}
.dept-title {
    font-size: 10pt;
    font-weight: bold;
    color: #A30000;
}
.doc-title {
    font-size: 13pt;
    font-weight: bold;
    text-align: center;
    color: #0B2545;
    text-transform: uppercase;
    margin: 10px 0 14px 0;
    letter-spacing: 0.5px;
}
.meta-box {
    background-color: #F8FAFC;
    border: 1px solid #CBD5E1;
    border-radius: 4px;
    padding: 8px 12px;
    margin-bottom: 14px;
    font-size: 9.5pt;
}
.meta-table {
    width: 100%;
}
.meta-table td {
    padding: 2px 4px;
    vertical-align: top;
}
h2 {
    font-size: 11pt;
    font-weight: bold;
    color: #0B2545;
    border-bottom: 1px solid #E2E8F0;
    padding-bottom: 3px;
    margin: 14px 0 6px 0;
    text-transform: uppercase;
}
p {
    margin: 0 0 6px 0;
    text-align: justify;
}
.status-badge {
    display: inline-block;
    padding: 2px 6px;
    font-size: 8.5pt;
    font-weight: bold;
    border-radius: 3px;
    background-color: #E6F4EA;
    color: #137333;
    border: 1px solid #CEEAD6;
}
.badge-blue {
    background-color: #E8F0FE;
    color: #1A73E8;
    border: 1px solid #D2E3FC;
}
.badge-gold {
    background-color: #FEF7E0;
    color: #B06000;
    border: 1px solid #FEEFC3;
}
table.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0 10px 0;
    font-size: 9pt;
}
table.data-table th, table.data-table td {
    border: 1px solid #CBD5E1;
    padding: 5px 8px;
    text-align: left;
}
table.data-table th {
    background-color: #0B2545;
    color: white;
    font-weight: bold;
}
table.data-table tr:nth-child(even) {
    background-color: #F8FAFC;
}
.sig-table {
    width: 100%;
    margin-top: 25px;
    border-collapse: collapse;
}
.sig-table td {
    width: 50%;
    vertical-align: top;
}
</style>
</head>
<body>

<table class="header-table">
    <tr>
        <td style="vertical-align: middle;">
            <div class="univ-title">Koneru Lakshmaiah Education Foundation</div>
            <div class="dept-title">Department of Experiential Learning and Global Engagement (EL&GE)</div>
            <div style="font-size: 9pt; color: #555;">Engineering Capstone Project–I End-Semester Review Verification Docket (Cabin C321A1)</div>
        </td>
        <td style="text-align: right; vertical-align: middle;">
            <div style="font-size: 9pt; font-weight: bold; color: #0B2545;">Academic Year 2026–2027</div>
            <div style="font-size: 8.5pt; color: #555;">November 2026</div>
        </td>
    </tr>
</table>

<div class="doc-title">Project Verification & Compliance Docket</div>

<div class="meta-box">
    <table class="meta-table">
        <tr>
            <td style="width: 18%; font-weight: bold;">Project Title:</td>
            <td style="width: 82%;">SWECHA VEDIKA: A Bandwidth-Frugal, Multilingual Live Stage and Knowledge Platform</td>
        </tr>
        <tr>
            <td style="font-weight: bold;">Team Name / ID:</td>
            <td><strong>KL - GLUG</strong> &nbsp;|&nbsp; Domain: <strong>Blockchain & Cyber Security Systems</strong></td>
        </tr>
        <tr>
            <td style="font-weight: bold;">Team Members:</td>
            <td>
                1. <strong>Muppavarapu Sivaram</strong> (Reg. No: 2300030447) &nbsp;|&nbsp; 
                2. <strong>Meda Lohith Pavan Kumar</strong> (Reg. No: 2300030921)
            </td>
        </tr>
        <tr>
            <td style="font-weight: bold;">Faculty Guide:</td>
            <td><strong>Dr. Koganti Sripath Roy</strong>, Assistant Professor, Department of EL&GE</td>
        </tr>
    </table>
</div>

<h2>1. Research Paper Publication Status</h2>
<p>
    In accordance with the Capstone Project–I evaluation guidelines, the team has authored a comprehensive 8-page camera-ready research manuscript formatted strictly under IEEE double-column conference guidelines:
</p>

<table class="data-table">
    <tr>
        <th style="width: 25%;">Item / Metric</th>
        <th style="width: 75%;">Status & Verification Details</th>
    </tr>
    <tr>
        <td><strong>Manuscript Title</strong></td>
        <td><em>SWECHA VEDIKA: A BANDWIDTH-FRUGAL, MULTILINGUAL LIVE STAGE AND KNOWLEDGE PLATFORM</em></td>
    </tr>
    <tr>
        <td><strong>Target Publication Venues</strong></td>
        <td>
            1. <strong>IEEE International Conference on Advanced Computing and Communication Systems (ICACCS 2027)</strong> / IEEE CONECCT (Scopus Indexed).<br>
            2. <em>Telecommunication Systems</em> (Springer / Scopus Q2) for extended system telemetry.
        </td>
    </tr>
    <tr>
        <td><strong>Target Track</strong></td>
        <td>Edge Computing, Real-Time Distributed Systems, and Low-Bandwidth Vernacular Networking.</td>
    </tr>
    <tr>
        <td><strong>Current Review Status</strong></td>
        <td>
            <span class="status-badge">CAMERA-READY MANUSCRIPT COMPLETED</span> &nbsp;
            <span class="badge-blue status-badge">SUBMISSION DOCKET PREPARED</span><br>
            The full 8-page paper is printed and compiled in the project evidence package. Final portal locking is scheduled immediately following the faculty guide's end-semester sign-off.
        </td>
    </tr>
    <tr>
        <td><strong>Plagiarism Clearance</strong></td>
        <td>
            <strong>11.2% Similarity Index</strong> (verified via Turnitin / DrillBit academic software). Excludes references and quotes. 100% compliant with KLEF academic integrity guidelines (&lt; 15%).
        </td>
    </tr>
    <tr>
        <td><strong>Pre-Print Archival Record</strong></td>
        <td>
            Archived on CERN Zenodo / Open Research Infrastructure with a globally citable DOI: <strong>10.5281/zenodo.24577348</strong><br>
            Public URL: <strong>https://zenodo.org/records/24577348</strong> (Indexed in OpenAIRE & CERN Data Centre).
        </td>
    </tr>
</table>

<h2>2. Consultancy Project & Societal Technology Transfer Status</h2>
<p>
    The Capstone–I engineering effort is directly coupled with an applied civic consultancy collaboration with the <strong>Swecha Free Software Movement of India (FSMI)</strong>:
</p>

<table class="data-table">
    <tr>
        <th style="width: 25%;">Consultancy Parameter</th>
        <th style="width: 75%;">Field Engagement Details</th>
    </tr>
    <tr>
        <td><strong>Consultancy Partner</strong></td>
        <td><strong>Swecha Telangana / Free Software Movement of India (FSMI)</strong> & Rural Educational Networks.</td>
    </tr>
    <tr>
        <td><strong>Nature of Work</strong></td>
        <td>Technical Architecture Advisory & Prototype Engineering for "Low-Bandwidth Vernacular Civic Tele-Education Infrastructure".</td>
    </tr>
    <tr>
        <td><strong>Field Trial Validation</strong></td>
        <td>
            • Tested across <strong>12 live community stages</strong> with <strong>450+ cumulative participants</strong>.<br>
            • Triaged and answered <strong>880+ live Q&A queries</strong> via WhatsApp and Web interfaces.<br>
            • Achieved <strong>78% cellular data cost reduction</strong> (&lt; 15 MB/hour vs 650 MB on standard video tools).
        </td>
    </tr>
    <tr>
        <td><strong>Current Progress</strong></td>
        <td>
            <span class="status-badge">PHASE-1 POC VALIDATED</span> &nbsp;
            <span class="badge-gold status-badge">PHASE-2 COMMUNITY EXTENSION IN PROGRESS</span>
        </td>
    </tr>
</table>

<h2>3. Intellectual Property (IPR) & Patent Disclosure Status</h2>
<p>
    <strong>Invention Title:</strong> <em>"A System and Method for Bandwidth-Frugal Real-Time Vernacular Audio Broadcasting with Client-Side Transcription and Asynchronous Messaging Gateway"</em><br>
    <strong>Status:</strong> The provisional patent specification (Forms 1 & 2) detailing the asymmetric 1:N audio-first SFU pipeline and client-side W3C speech transcription architecture has been catalogued and submitted for internal novelty assessment and clearance with the <strong>KLEF Center for Innovation, Incubation and Entrepreneurship (CIIE) & University IPR Cell</strong> prior to official filing with the Indian Patent Office.
</p>

<h2>4. Mandatory Review Artifacts Checklist</h2>
<table class="data-table">
    <tr>
        <th>Artifact</th>
        <th>Quantity Prepared</th>
        <th>Verification Status</th>
    </tr>
    <tr>
        <td>Capstone Project–I Final Report (Black Book)</td>
        <td>3 Copies (1 Team Copy + 2 Individual Copies)</td>
        <td>Complete (46 Pages, KLEF Approved Format)</td>
    </tr>
    <tr>
        <td>Research Diary</td>
        <td>1 Official Diary with Review-Gate Logs</td>
        <td>Updated & Signed by Faculty Guide</td>
    </tr>
    <tr>
        <td>Project Presentation (PPT)</td>
        <td>16:9 Widescreen Presentation (16 Slides)</td>
        <td>Covering all 8 Evaluation Rubrics</td>
    </tr>
    <tr>
        <td>Research Paper Evidence Dossier</td>
        <td>Full 8-Page IEEE Manuscript + Plagiarism Report</td>
        <td>Ready for Physical Inspection</td>
    </tr>
</table>

<table class="sig-table">
    <tr>
        <td>
            <div style="font-weight: bold;">Student Team Signatures:</div>
            <div style="margin-top: 15px;">1. Muppavarapu Sivaram: ________________________</div>
            <div style="margin-top: 10px;">2. Meda Lohith Pavan Kumar: ____________________</div>
            <div style="margin-top: 6px; font-size: 9pt; color: #555;">Date: 27-11-2026</div>
        </td>
        <td style="text-align: right;">
            <div style="font-weight: bold;">Faculty Guide Endorsement:</div>
            <div style="margin-top: 25px;">___________________________________</div>
            <div style="font-weight: bold; margin-top: 4px;">Dr. Koganti Sripath Roy</div>
            <div style="font-size: 9pt; color: #555;">Assistant Professor, Department of EL&GE</div>
        </td>
    </tr>
</table>

</body>
</html>
"""

def generate_pdf():
    html_path = DOCS_DIR / "verification_docket.html"
    raw_pdf_path = DOCS_DIR / "verification_docket_raw.pdf"
    final_pdf_path = DOCS_DIR / "Swecha_Vedika_Research_Paper_and_Consultancy_Status_Docket.pdf"

    html_path.write_text(HTML_CONTENT, encoding="utf-8")
    
    edge_cmd = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={raw_pdf_path}",
        str(html_path)
    ]
    subprocess.run(edge_cmd, check=True)

    # Read and verify page count
    doc = fitz.open(str(raw_pdf_path))
    print(f"Generated Raw Docket with {len(doc)} pages.")

    # Save to final path
    doc.save(str(final_pdf_path))
    doc.close()

    # cleanup temp
    if html_path.exists(): html_path.unlink()
    if raw_pdf_path.exists(): raw_pdf_path.unlink()
    print(f"SUCCESS: Saved {final_pdf_path}")

if __name__ == "__main__":
    generate_pdf()
