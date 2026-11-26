import os
import subprocess
import base64
import pymupdf
from pathlib import Path

from styles import CSS_STYLES
from front_matter import get_front_matter_html
from preliminaries import get_preliminary_sections_html
from chapters_1_3 import get_chapters_1_3_html
from chapters_4_6 import get_chapters_4_6_html
from chapters_7_10 import get_chapters_7_10_html
from back_matter import get_references_and_appendices_html

BASE_DIR = Path(r"C:\Users\Victus\Documents\swecha\prototype")
DOCS_DIR = BASE_DIR / "docs"
SCREENSHOTS_DIR = DOCS_DIR / "screenshots"

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"
    return ""

def build_html(target, kl_logo_b64, fig1_b64, fig2_b64, fig3_b64, fig4_b64):
    front_matter = get_front_matter_html(target, kl_logo_b64)
    preliminaries = get_preliminary_sections_html(target)
    chap_1_3 = get_chapters_1_3_html()
    chap_4_6 = get_chapters_4_6_html(fig1_b64, fig2_b64, fig3_b64, fig4_b64)
    chap_7_10 = get_chapters_7_10_html()
    back_matter = get_references_and_appendices_html()

    target_title = {
        "team": "Team Copy",
        "sivaram": "Individual Copy - Muppavarapu Sivaram (2300030447)",
        "lohith": "Individual Copy - Meda Lohith Pavan Kumar (2300030921)"
    }.get(target, "Team Copy")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Swecha Vedika - Capstone Project-I Final Report ({target_title})</title>
<style>
{CSS_STYLES}
</style>
</head>
<body>
{front_matter}
{preliminaries}
{chap_1_3}
{chap_4_6}
{chap_7_10}
{back_matter}
</body>
</html>
"""

def stamp_headers_and_footers(raw_pdf_path, final_pdf_path):
    doc = pymupdf.open(raw_pdf_path)
    total_pages = len(doc)
    print(f"Stamping headers and footers on {total_pages} pages...")

    for page_idx in range(total_pages):
        # Page 1 (Cover Page): NO header, NO footer
        if page_idx == 0:
            continue

        page = doc[page_idx]
        page_num = page_idx + 1

        # Running Header (pages 2 to N)
        rect_header = pymupdf.Rect(54, 24, 595 - 54, 45)
        page.insert_textbox(
            rect_header,
            "KL UNIVERSITY   |   CAPSTONE FINAL REPORT   |   CLUSTER A - SOFTWARE SYSTEMS ENGINEERING",
            fontsize=7.5,
            fontname="helv",
            align=pymupdf.TEXT_ALIGN_CENTER,
            color=(0.35, 0.35, 0.35)
        )

        # Running Footer (Page X at bottom right)
        rect_footer = pymupdf.Rect(595 - 120, 842 - 40, 595 - 54, 842 - 20)
        page.insert_textbox(
            rect_footer,
            f"Page {page_num}",
            fontsize=9.5,
            fontname="times-roman",
            align=pymupdf.TEXT_ALIGN_RIGHT,
            color=(0, 0, 0)
        )

    doc.save(final_pdf_path)
    doc.close()
    return total_pages

def compile_reports():
    kl_logo_b64 = get_base64_image(DOCS_DIR / "kl_logo.png")
    fig1_b64 = get_base64_image(SCREENSHOTS_DIR / "figure1_live_stage.png")
    fig2_b64 = get_base64_image(SCREENSHOTS_DIR / "figure2_sidebar_qa_polls.png")
    fig3_b64 = get_base64_image(SCREENSHOTS_DIR / "figure3_whatsapp_bot.png")
    fig4_b64 = get_base64_image(SCREENSHOTS_DIR / "figure4_archive_offline.png")

    targets = [
        ("team", "capstone_report_team.html", "Swecha_Vedika_Capstone_Report_Team.pdf"),
        ("sivaram", "capstone_report_sivaram.html", "Swecha_Vedika_Capstone_Report_Sivaram_2300030447.pdf"),
        ("lohith", "capstone_report_lohith.html", "Swecha_Vedika_Capstone_Report_Lohith_2300030921.pdf"),
    ]

    edge_bin = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

    for target, html_name, pdf_name in targets:
        html_path = DOCS_DIR / html_name
        raw_pdf_path = DOCS_DIR / f"raw_{pdf_name}"
        final_pdf_path = DOCS_DIR / pdf_name

        print(f"\n==========================================")
        print(f"Building {target.upper()} Report...")
        print(f"==========================================")

        html_content = build_html(target, kl_logo_b64, fig1_b64, fig2_b64, fig3_b64, fig4_b64)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Written HTML: {html_name} ({html_path.stat().st_size} bytes)")

        # Compile raw PDF via Microsoft Edge headless
        file_uri = "file:///" + str(html_path.resolve()).replace("\\", "/")
        cmd = [
            edge_bin,
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={raw_pdf_path.resolve()}",
            file_uri
        ]
        print(f"Invoking Microsoft Edge headless for {html_name}...")
        subprocess.run(cmd, check=True)

        if not raw_pdf_path.exists():
            print(f"ERROR: Failed to generate {raw_pdf_path}")
            continue

        # Post-process with PyMuPDF
        pages = stamp_headers_and_footers(raw_pdf_path, final_pdf_path)
        print(f"SUCCESS: Generated {pdf_name} with {pages} pages ({final_pdf_path.stat().st_size} bytes)")

        # Cleanup raw PDF
        if raw_pdf_path.exists():
            os.remove(raw_pdf_path)

if __name__ == "__main__":
    compile_reports()
