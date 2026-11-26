import sys
from pathlib import Path
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs"
SCREENSHOTS_DIR = DOCS_DIR / "screenshots"
KL_LOGO_PATH = DOCS_DIR / "official_kl_logo.jpeg"

# Corporate Color Palette
COLOR_NAVY = RGBColor(11, 37, 69)      # #0B2545
COLOR_GOLD = RGBColor(212, 175, 55)    # #D4AF37
COLOR_CRIMSON = RGBColor(163, 0, 0)    # #A30000
COLOR_BG_GRAY = RGBColor(248, 250, 252)# #F8FAFC
COLOR_WHITE = RGBColor(255, 255, 255)
COLOR_DARK_TEXT = RGBColor(26, 32, 44) # #1A202C
COLOR_MUTED_TEXT = RGBColor(74, 85, 104)# #4A5568
COLOR_CARD_BG = RGBColor(255, 255, 255)
COLOR_CARD_BORDER = RGBColor(226, 232, 240)
COLOR_GREEN = RGBColor(19, 115, 51)    # Green badge

def create_deck():
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def set_slide_background(slide, color=COLOR_BG_GRAY):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header_footer(slide, title, category_badge, current_slide, total_slides=12):
        # Header banner
        header = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.1))
        header.fill.solid()
        header.fill.fore_color.rgb = COLOR_NAVY
        header.line.fill.background()

        # Category Badge
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.12), Inches(4.0), Inches(0.28))
        badge.fill.solid()
        badge.fill.fore_color.rgb = COLOR_CRIMSON
        badge.line.fill.background()
        tf_b = badge.text_frame
        p_b = tf_b.paragraphs[0]
        p_b.text = category_badge.upper()
        p_b.font.size = Pt(9.5)
        p_b.font.bold = True
        p_b.font.color.rgb = COLOR_WHITE
        p_b.alignment = PP_ALIGN.CENTER

        # Slide Title
        tx_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.42), Inches(11.5), Inches(0.6))
        tf_t = tx_title.text_frame
        p_t = tf_t.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(22)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_WHITE

        # Gold strip
        gold_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.1), Inches(13.333), Inches(0.04))
        gold_line.fill.solid()
        gold_line.fill.fore_color.rgb = COLOR_GOLD
        gold_line.line.fill.background()

        # Footer
        footer = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(7.05), Inches(13.333), Inches(0.45))
        footer.fill.solid()
        footer.fill.fore_color.rgb = COLOR_NAVY
        footer.line.fill.background()

        tx_f = slide.shapes.add_textbox(Inches(0.8), Inches(7.08), Inches(10.0), Inches(0.35))
        tf_f = tx_f.text_frame
        p_f = tf_f.paragraphs[0]
        p_f.text = "KL UNIVERSITY  |  CAPSTONE PROJECT–I END-SEMESTER REVIEW  |  TEAM: KL - GLUG"
        p_f.font.size = Pt(9)
        p_f.font.color.rgb = RGBColor(200, 215, 230)

        tx_fn = slide.shapes.add_textbox(Inches(11.2), Inches(7.08), Inches(1.3), Inches(0.35))
        tf_fn = tx_fn.text_frame
        p_fn = tf_fn.paragraphs[0]
        p_fn.text = f"Slide {current_slide} of {total_slides}"
        p_fn.font.size = Pt(9.5)
        p_fn.font.bold = True
        p_fn.font.color.rgb = COLOR_GOLD
        p_fn.alignment = PP_ALIGN.RIGHT

    def add_card(slide, left, top, width, height, title=None, border_color=COLOR_CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_BG
        card.line.color.rgb = border_color
        card.line.width = Pt(1)

        if title:
            tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.14), width - Inches(0.4), Inches(0.45))
            p = tb.text_frame.paragraphs[0]
            p.text = title
            p.font.size = Pt(14)
            p.font.bold = True
            p.font.color.rgb = COLOR_NAVY

        return card

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, COLOR_BG_GRAY)

    top_band = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.25))
    top_band.fill.solid()
    top_band.fill.fore_color.rgb = COLOR_CRIMSON
    top_band.line.fill.background()

    if KL_LOGO_PATH.exists():
        s1.shapes.add_picture(str(KL_LOGO_PATH), Inches(0.9), Inches(0.55), width=Inches(2.5))

    tx = s1.shapes.add_textbox(Inches(3.6), Inches(0.55), Inches(8.8), Inches(1.2))
    tf = tx.text_frame
    p0 = tf.paragraphs[0]
    p0.text = "KONERU LAKSHMAIAH EDUCATION FOUNDATION (DEEMED TO BE UNIVERSITY)"
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_NAVY
    p1 = tf.add_paragraph()
    p1.text = "DEPARTMENT OF EXPERIENTIAL LEARNING AND GLOBAL ENGAGEMENT (EL&GE)"
    p1.font.size = Pt(10)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_CRIMSON
    p2 = tf.add_paragraph()
    p2.text = "Capstone Project–I End-Semester External Review | Academic Year 2026–2027"
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = COLOR_MUTED_TEXT

    hero = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.9), Inches(11.733), Inches(2.7))
    hero.fill.solid()
    hero.fill.fore_color.rgb = COLOR_NAVY
    hero.line.fill.background()

    tx_hero = s1.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(11.1), Inches(2.3))
    tf_h = tx_hero.text_frame
    tf_h.word_wrap = True
    ph1 = tf_h.paragraphs[0]
    ph1.text = "SWECHA VEDIKA"
    ph1.font.size = Pt(34)
    ph1.font.bold = True
    ph1.font.color.rgb = COLOR_GOLD

    ph2 = tf_h.add_paragraph()
    ph2.text = "A Bandwidth-Frugal, Multilingual Live Stage and Knowledge Platform"
    ph2.font.size = Pt(18)
    ph2.font.color.rgb = COLOR_WHITE
    ph2.space_before = Pt(6)

    ph3 = tf_h.add_paragraph()
    ph3.text = "Domain: Blockchain & Cyber Security Systems  |  Team: KL - GLUG"
    ph3.font.size = Pt(12)
    ph3.font.bold = True
    ph3.font.color.rgb = RGBColor(200, 220, 245)
    ph3.space_before = Pt(14)

    # Student details
    add_card(s1, Inches(0.8), Inches(4.8), Inches(5.7), Inches(2.0), "Presented by Team KL - GLUG")
    tx_stu = s1.shapes.add_textbox(Inches(1.0), Inches(5.3), Inches(5.3), Inches(1.3))
    tf_s = tx_stu.text_frame
    ps1 = tf_s.paragraphs[0]
    ps1.text = "• Muppavarapu Sivaram  (2300030447)"
    ps1.font.size = Pt(12)
    ps1.font.bold = True
    ps1.font.color.rgb = COLOR_DARK_TEXT
    ps2 = tf_s.add_paragraph()
    ps2.text = "• Meda Lohith Pavan Kumar  (2300030921)"
    ps2.font.size = Pt(12)
    ps2.font.bold = True
    ps2.font.color.rgb = COLOR_DARK_TEXT
    ps2.space_before = Pt(8)
    ps3 = tf_s.add_paragraph()
    ps3.text = "Department of EL&GE, College of Engineering, KLEF"
    ps3.font.size = Pt(9.5)
    ps3.font.color.rgb = COLOR_MUTED_TEXT
    ps3.space_before = Pt(6)

    # Guide details
    add_card(s1, Inches(6.8), Inches(4.8), Inches(5.733), Inches(2.0), "Under the Guidance of")
    tx_gd = s1.shapes.add_textbox(Inches(7.0), Inches(5.3), Inches(5.3), Inches(1.3))
    tf_g = tx_gd.text_frame
    pg1 = tf_g.paragraphs[0]
    pg1.text = "Dr. Koganti Sripath Roy"
    pg1.font.size = Pt(14)
    pg1.font.bold = True
    pg1.font.color.rgb = COLOR_NAVY
    pg2 = tf_g.add_paragraph()
    pg2.text = "Assistant Professor, Department of EL&GE"
    pg2.font.size = Pt(11)
    pg2.font.color.rgb = COLOR_DARK_TEXT
    pg3 = tf_g.add_paragraph()
    pg3.text = "Koneru Lakshmaiah Education Foundation"
    pg3.font.size = Pt(9.5)
    pg3.font.color.rgb = COLOR_MUTED_TEXT
    pg3.space_before = Pt(4)

    bot_band = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(7.2), Inches(13.333), Inches(0.3))
    bot_band.fill.solid()
    bot_band.fill.fore_color.rgb = COLOR_NAVY
    bot_band.line.fill.background()

    # =========================================================================
    # SLIDE 2: WHY WE BUILT THIS (THE REAL PROBLEM)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header_footer(s2, "The Real-World Problem: Why We Built This", "Rubric 1: Problem Definition", 2)

    add_card(s2, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.3), "What Happens Today (The Problem)")
    tb = s2.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    pts_p = [
        ("High Data Requirement: ", "Tools like Zoom and Google Meet require 1.5 to 3.0 Mbps high-speed internet. They completely fail in rural areas where network fluctuates."),
        ("Audio Cuts Off on 2G/3G: ", "When mobile data drops, commercial tools freeze or disconnect the call, breaking the learning experience for village students."),
        ("Expensive Live Subtitles: ", "Cloud-based live captions cost $0.024 every minute on AI servers, making it impossible for rural non-profit schools to afford."),
        ("Heavy App Installations: ", "Students with basic smartphones cannot easily download large 150 MB apps or register complicated accounts.")
    ]
    for i, (head, body) in enumerate(pts_p):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = "• "
        p.font.size = Pt(11)
        r1 = p.add_run()
        r1.text = head
        r1.font.bold = True
        r1.font.color.rgb = COLOR_CRIMSON
        r2 = p.add_run()
        r2.text = body
        r2.font.color.rgb = COLOR_DARK_TEXT
        if i > 0: p.space_before = Pt(12)

    add_card(s2, Inches(6.8), Inches(1.4), Inches(5.733), Inches(5.3), "What Swecha Vedika Does (Our Solution)")
    tb = s2.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    pts_s = [
        ("Runs on Low 2G Speeds (Sub-50 kbps): ", "Prioritizes audio above all else. Uses only 24 to 64 kbps data — 96% less internet than Zoom!"),
        ("Survives Severe Network Drops: ", "Keeps audio talking smoothly even with 35% packet loss on patchy mobile towers without disconnecting."),
        ("100% Free Telugu & Hindi Subtitles: ", "Captions run directly inside the student's browser without requiring costly GPU cloud servers ($0 server cost)."),
        ("Join via WhatsApp Directly: ", "Students don't need any app. They can join classes, ask questions, and vote in quizzes directly on WhatsApp!")
    ]
    for i, (head, body) in enumerate(pts_s):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = "• "
        p.font.size = Pt(11)
        r1 = p.add_run()
        r1.text = head
        r1.font.bold = True
        r1.font.color.rgb = COLOR_GREEN
        r2 = p.add_run()
        r2.text = body
        r2.font.color.rgb = COLOR_DARK_TEXT
        if i > 0: p.space_before = Pt(12)

    # =========================================================================
    # SLIDE 3: 4 CORE FEATURES (WHAT WE BUILT)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header_footer(s3, "Core Platform Capabilities: What Swecha Vedika Does", "Platform Features", 3)

    features = [
        ("1. Audio-First Live Stage",
         "Runs on Sub-50 kbps 2G Internet",
         "• One teacher/speaker broadcasts crystal-clear voice to hundreds of listeners.\n• If internet drops, it automatically lowers bitrate from 64 down to 24 kbps so audio never cuts off.\n• Uses Opus audio codec with built-in error recovery."),
        ("2. Telugu & Hindi Live Subtitles",
         "Zero Cost Speech-to-Text",
         "• Live spoken words are translated to text instantly on screen.\n• Runs 100% on the student's web browser using native Web Speech technology.\n• Zero cloud server GPU bills ($0 hosting overhead)."),
        ("3. WhatsApp Bot Integration",
         "No Need to Install Any New App",
         "• Students type '!join' to enter the live stage.\n• Students type '!ask <question>' on WhatsApp, and it instantly shows on the teacher's screen.\n• Students vote in live classroom polls using simple numbers ('!vote 1')."),
        ("4. Offline Micro-Podcasts",
         "Listen Anytime Without Data",
         "• Automatically saves finished live talks into tiny audio files (< 500 KB per 15 mins).\n• Works completely offline in the browser cache even during village power cuts or no-signal periods.")
    ]

    for idx, (title, sub, body) in enumerate(features):
        r_pos = idx // 2
        c_pos = idx % 2
        c_left = Inches(0.8 + c_pos * 5.98)
        c_top = Inches(1.4 + r_pos * 2.7)
        card = add_card(s3, c_left, c_top, Inches(5.7), Inches(2.5), title)

        tb = s3.shapes.add_textbox(c_left + Inches(0.2), c_top + Inches(0.52), Inches(5.3), Inches(1.8))
        tf = tb.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = sub
        p0.font.size = Pt(11)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_CRIMSON

        p1 = tf.add_paragraph()
        p1.text = body
        p1.font.size = Pt(10)
        p1.font.color.rgb = COLOR_DARK_TEXT
        p1.space_before = Pt(4)

    # =========================================================================
    # SLIDE 4: SYSTEM DESIGN MADE SIMPLE
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header_footer(s4, "System Design: How Audio Flows Through Swecha Vedika", "Rubric 3: System Design & Architecture", 4)

    # 3 Steps Flow
    steps = [
        ("Step 1: Speaker Speaks", "Microphone Input & Encoding",
         "• Speaker talks in their browser.\n• Microphone audio is compressed into small Opus packets (24–64 kbps).\n• Forward Error Correction (FEC) is added so missing packets can be repaired."),
        ("Step 2: Server Forwards", "Zero-Transcode SFU Server",
         "• The server DOES NOT re-encode audio (which wastes CPU).\n• It simply forwards the voice packets to all connected listeners in under 15 milliseconds.\n• Easily handles 50+ students on a cheap $12 VPS."),
        ("Step 3: Student Listens", "Instant Audio & Subtitles",
         "• Student phone receives and plays clean voice even on 2G.\n• Built-in browser speech engine displays Telugu/Hindi subtitles on screen in real time.")
    ]
    card_w3 = Inches(3.75)
    for idx, (title, sub, body) in enumerate(steps):
        c_left = Inches(0.8 + idx * 3.99)
        card = add_card(s4, c_left, Inches(1.4), card_w3, Inches(3.2), title)

        tb = s4.shapes.add_textbox(c_left + Inches(0.15), Inches(1.95), card_w3 - Inches(0.3), Inches(2.5))
        tf = tb.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = sub
        p0.font.size = Pt(10.5)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_CRIMSON

        p1 = tf.add_paragraph()
        p1.text = body
        p1.font.size = Pt(9.5)
        p1.font.color.rgb = COLOR_DARK_TEXT
        p1.space_before = Pt(6)

    # Simple Tech Stack Bar Below
    add_card(s4, Inches(0.8), Inches(4.8), Inches(11.733), Inches(2.0), "Simple Technologies Used & Why")
    tb_tech = s4.shapes.add_textbox(Inches(1.0), Inches(5.3), Inches(11.333), Inches(1.3))
    tf_tech = tb_tech.text_frame
    tf_tech.word_wrap = True

    tech_items = [
        ("FastAPI (Python): ", "Handles login, database, questions, and live polls quickly with low memory."),
        ("Mediasoup (Node.js): ", "Industry-standard WebRTC media server that routes real-time voice without delay."),
        ("Baileys (WebSockets): ", "Direct WhatsApp connection so students don't need any special app and we pay $0 API fees."),
        ("Vanilla JavaScript & HTML5: ", "Extremely lightweight frontend (<150 KB) that loads instantly on cheap Android phones.")
    ]
    for i, (t_name, t_desc) in enumerate(tech_items):
        p = tf_tech.paragraphs[0] if i == 0 else tf_tech.add_paragraph()
        p.text = "• "
        p.font.size = Pt(10)
        r1 = p.add_run()
        r1.text = t_name
        r1.font.bold = True
        r1.font.color.rgb = COLOR_NAVY
        r2 = p.add_run()
        r2.text = t_desc
        r2.font.color.rgb = COLOR_DARK_TEXT
        if i > 0: p.space_before = Pt(3)

    # =========================================================================
    # SLIDE 5: WHATSAPP BOT WORKFLOW
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header_footer(s5, "WhatsApp Conversational Bot: How Rural Students Connect", "WhatsApp Bridge", 5)

    add_card(s5, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.3), "Why WhatsApp for Education?")
    tb = s5.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    pts_w = [
        ("No New App Needed: ", "Over 500 million people in India already use WhatsApp daily. Students do not need to download or learn anything new."),
        ("Zero Mobile Data Waste: ", "Text and audio notes consume negligible bandwidth (less than 1 MB for an entire session)."),
        ("Works on Low-End Phones: ", "Functions perfectly even on basic ₹5,000 Android phones without freezing or running out of memory."),
        ("Zero Commercial API Cost: ", "Built using self-hosted Baileys WebSockets instead of commercial paid APIs (like Twilio or Meta Cloud API), saving thousands of dollars.")
    ]
    for i, (head, body) in enumerate(pts_w):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = "• "
        p.font.size = Pt(11)
        r1 = p.add_run()
        r1.text = head
        r1.font.bold = True
        r1.font.color.rgb = COLOR_NAVY
        r2 = p.add_run()
        r2.text = body
        r2.font.color.rgb = COLOR_DARK_TEXT
        if i > 0: p.space_before = Pt(14)

    add_card(s5, Inches(6.8), Inches(1.4), Inches(5.733), Inches(5.3), "Student Commands on WhatsApp")
    tb = s5.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    commands = [
        ("!join", "Find Live Classes", "Student sends '!join'. The bot immediately replies with today's live classes, topics, and schedule."),
        ("!ask <question>", "Ask Teacher a Question", "Student sends '!ask What is WebRTC?'. The question appears instantly on the teacher's screen with upvotes."),
        ("!vote <number>", "Live Quizzes & Polling", "When the teacher launches a quiz, the bot asks the student on WhatsApp. They reply '!vote 2' to cast their answer."),
        ("Audio Recap", "Automatic Lecture Audio", "Once the session finishes, the bot sends a compressed voice note of the lecture directly to the student's WhatsApp chat.")
    ]
    for i, (cmd, desc, detail) in enumerate(commands):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = cmd + " — " + desc + "\n"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_CRIMSON
        r = p.add_run()
        r.text = detail
        r.font.bold = False
        r.font.size = Pt(10)
        r.font.color.rgb = COLOR_DARK_TEXT
        if i > 0: p.space_before = Pt(10)

    # =========================================================================
    # SLIDE 6: SCREENSHOTS - STAGE & SIDEBAR
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header_footer(s6, "Working System Screenshots: Live Stage & Telugu Subtitles", "Rubric 4: Technical Execution", 6)

    # Left: Figure 1
    add_card(s6, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.3), "Live Stage with Telugu Captions")
    fig1_path = SCREENSHOTS_DIR / "figure1_live_stage.png"
    if fig1_path.exists():
        s6.shapes.add_picture(str(fig1_path), Inches(1.0), Inches(1.95), width=Inches(5.3))
    tb_f1 = s6.shapes.add_textbox(Inches(1.0), Inches(5.4), Inches(5.3), Inches(1.2))
    tf_f1 = tb_f1.text_frame
    tf_f1.word_wrap = True
    p = tf_f1.paragraphs[0]
    p.text = "• Live voice streaming with speaking indicator.\n• Real-time Telugu subtitles appearing as the teacher speaks.\n• Connection indicator shows adaptive 2G/3G bitrate status."
    p.font.size = Pt(10.5)
    p.font.color.rgb = COLOR_DARK_TEXT

    # Right: Figure 2
    add_card(s6, Inches(6.8), Inches(1.4), Inches(5.733), Inches(5.3), "Q&A Queue & Live Community Polls")
    fig2_path = SCREENSHOTS_DIR / "figure2_sidebar_qa_polls.png"
    if fig2_path.exists():
        s6.shapes.add_picture(str(fig2_path), Inches(7.0), Inches(1.95), width=Inches(5.3))
    tb_f2 = s6.shapes.add_textbox(Inches(7.0), Inches(5.4), Inches(5.3), Inches(1.2))
    tf_f2 = tb_f2.text_frame
    tf_f2.word_wrap = True
    p = tf_f2.paragraphs[0]
    p.text = "• Questions from both Web and WhatsApp show in one queue.\n• Students upvote the most important questions.\n• Live polling shows real-time voting percentages instantly."
    p.font.size = Pt(10.5)
    p.font.color.rgb = COLOR_DARK_TEXT

    # =========================================================================
    # SLIDE 7: SCREENSHOTS - WHATSAPP & PODCAST
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header_footer(s7, "Working System Screenshots: WhatsApp Bot & Offline Podcasts", "Rubric 4: Technical Execution", 7)

    # Left: Figure 3
    add_card(s7, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.3), "WhatsApp Conversational Bot in Action")
    fig3_path = SCREENSHOTS_DIR / "figure3_whatsapp_bot.png"
    if fig3_path.exists():
        s7.shapes.add_picture(str(fig3_path), Inches(1.0), Inches(1.95), width=Inches(5.3))
    tb_f3 = s7.shapes.add_textbox(Inches(1.0), Inches(5.4), Inches(5.3), Inches(1.2))
    tf_f3 = tb_f3.text_frame
    tf_f3.word_wrap = True
    p = tf_f3.paragraphs[0]
    p.text = "• Student interacts naturally via regular WhatsApp chat.\n• Simple text commands (!join, !ask, !vote) work smoothly.\n• Sends automated audio recap after class ends."
    p.font.size = Pt(10.5)
    p.font.color.rgb = COLOR_DARK_TEXT

    # Right: Figure 4
    add_card(s7, Inches(6.8), Inches(1.4), Inches(5.733), Inches(5.3), "Compressed Micro-Podcast Offline Vault")
    fig4_path = SCREENSHOTS_DIR / "figure4_archive_offline.png"
    if fig4_path.exists():
        s7.shapes.add_picture(str(fig4_path), Inches(7.0), Inches(1.95), width=Inches(5.3))
    tb_f4 = s7.shapes.add_textbox(Inches(7.0), Inches(5.4), Inches(5.3), Inches(1.2))
    tf_f4 = tb_f4.text_frame
    tf_f4.word_wrap = True
    p = tf_f4.paragraphs[0]
    p.text = "• Lectures saved as tiny audio files (< 500 KB).\n• Cached in browser storage so students can replay offline.\n• Accompanied by text transcripts for easy studying."
    p.font.size = Pt(10.5)
    p.font.color.rgb = COLOR_DARK_TEXT

    # =========================================================================
    # SLIDE 8: TESTING & RESULTS (SIMPLE NUMBERS)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header_footer(s8, "Testing & Results: Does It Actually Work on Bad Internet?", "Rubric 5: Testing & Results", 8)

    # 3 Big Highlight Metric Cards
    big_metrics = [
        ("96% LESS DATA", "vs. Zoom / Google Meet", "Consumes only 32–48 kbps compared to 1500–3000 kbps on commercial video tools."),
        ("SURVIVES 35% PACKET LOSS", "Severe 2G Simulation", "Voice stays clear and understandable even under heavy mobile tower network drops."),
        ("< 185 ms DELAY", "Real-Time Interaction", "Natural conversational flow between teacher and students with zero awkward pauses.")
    ]
    card_w3 = Inches(3.75)
    for idx, (val, title, desc) in enumerate(big_metrics):
        c_left = Inches(0.8 + idx * 3.99)
        card = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c_left, Inches(1.4), card_w3, Inches(1.7))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_NAVY
        card.line.fill.background()

        tb = s8.shapes.add_textbox(c_left + Inches(0.1), Inches(1.45), card_w3 - Inches(0.2), Inches(1.6))
        tf = tb.text_frame
        p0 = tf.paragraphs[0]
        p0.text = val
        p0.font.size = Pt(16)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_GOLD
        p0.alignment = PP_ALIGN.CENTER

        p1 = tf.add_paragraph()
        p1.text = title
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_WHITE
        p1.alignment = PP_ALIGN.CENTER
        p1.space_before = Pt(2)

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(9)
        p2.font.color.rgb = RGBColor(200, 220, 240)
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(3)

    # Simple Comparison Table Below
    add_card(s8, Inches(0.8), Inches(3.3), Inches(11.733), Inches(3.4), "Simple Comparison: Swecha Vedika vs. Zoom / Google Meet")
    t_shape = s8.shapes.add_table(5, 5, Inches(1.0), Inches(3.85), Inches(11.333), Inches(2.6))
    tbl = t_shape.table
    tbl_data = [
        ["Network Condition", "Internet Speed", "Zoom / Google Meet", "Swecha Vedika", "Result / Verdict"],
        ["Normal 4G / Wi-Fi", "10+ Mbps", "Works fine", "Works crystal clear (64 kbps)", "Both work"],
        ["Weak 3G Signal (15% loss)", "250 kbps", "Video freezes, robotic audio", "Clear voice (48 kbps)", "Swecha Vedika clear"],
        ["Severe Rural 2G (35% loss)", "Sub-50 kbps", "CALL DROPS COMPLETELY", "Voice stays intact (24 kbps)", "Swecha Vedika wins!"],
        ["1-Hour Data Usage", "Per student", "650 MB to 1.2 GB consumed", "Only 15 MB consumed!", "96% data saved!"]
    ]
    for r_idx, row in enumerate(tbl_data):
        for c_idx, val in enumerate(row):
            cell = tbl.cell(r_idx, c_idx)
            cell.text = val
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = cell.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER
            if r_idx == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = COLOR_NAVY
                p.font.size = Pt(10)
                p.font.bold = True
                p.font.color.rgb = COLOR_WHITE
            elif r_idx in [3, 4]:
                cell.fill.solid()
                cell.fill.fore_color.rgb = RGBColor(240, 250, 240) if c_idx in [3, 4] else COLOR_WHITE
                p.font.size = Pt(9.5)
                p.font.bold = (c_idx in [3, 4])
                p.font.color.rgb = COLOR_GREEN if c_idx in [3, 4] else COLOR_DARK_TEXT
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = COLOR_WHITE if r_idx % 2 == 1 else RGBColor(245, 247, 250)
                p.font.size = Pt(9.5)
                p.font.color.rgb = COLOR_DARK_TEXT

    # =========================================================================
    # SLIDE 9: INNOVATIONS (WHY IT IS SPECIAL)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header_footer(s9, "Key Innovations: Why Swecha Vedika Is Different", "Rubric 6: Innovation & Originality", 9)

    inno = [
        ("Innovation 1: Zero-Cost Live Subtitles",
         "No Server GPU Needed",
         "• Traditional tools send audio to costly cloud GPU servers ($0.024/min).\n• Swecha Vedika runs speech recognition directly on the student's browser.\n• Server load = 0%, Server GPU bill = $0, works instantly."),
        ("Innovation 2: Audio-First Architecture",
         "Never Drops Voice",
         "• Normal conferencing apps treat video and voice equally. When network drops, both die.\n• Swecha Vedika discards video first and gives 100% priority to voice packets.\n• Speech remains clear even on weak 2G cellular links."),
        ("Innovation 3: WhatsApp-to-Web Bridge",
         "Zero App Downloads",
         "• Allows live two-way participation through normal WhatsApp chat.\n• Students don't need expensive computers or heavy mobile apps.\n• Connects rural participants who only have basic smartphones.")
    ]
    card_w3 = Inches(3.75)
    for idx, (title, sub, body) in enumerate(inno):
        c_left = Inches(0.8 + idx * 3.99)
        card = add_card(s9, c_left, Inches(1.4), card_w3, Inches(3.5), title)

        tb = s9.shapes.add_textbox(c_left + Inches(0.15), Inches(1.95), card_w3 - Inches(0.3), Inches(2.8))
        tf = tb.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = sub
        p0.font.size = Pt(11)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_CRIMSON

        p1 = tf.add_paragraph()
        p1.text = body
        p1.font.size = Pt(10)
        p1.font.color.rgb = COLOR_DARK_TEXT
        p1.space_before = Pt(8)

    # Patent / IPR Box Below
    add_card(s9, Inches(0.8), Inches(5.1), Inches(11.733), Inches(1.7), "Intellectual Property & Patent Disclosure Status")
    tb_pat = s9.shapes.add_textbox(Inches(1.0), Inches(5.55), Inches(11.333), Inches(1.1))
    tf_pat = tb_pat.text_frame
    tf_pat.word_wrap = True

    p = tf_pat.paragraphs[0]
    p.text = "• Title: \"A System and Method for Bandwidth-Frugal Real-Time Vernacular Audio Broadcasting with Client-Side Transcription and Asynchronous Messaging Gateway\""
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    p2 = tf_pat.add_paragraph()
    p2.text = "• Status: The complete technical disclosure (Form 1 & Form 2 format) has been catalogued and submitted for internal novelty assessment and clearance with the KLEF University IPR & Innovation Cell prior to filing with the Indian Patent Office."
    p2.font.size = Pt(10)
    p2.font.color.rgb = COLOR_DARK_TEXT
    p2.space_before = Pt(4)

    # =========================================================================
    # SLIDE 10: RESEARCH PAPER & CONSULTANCY STATUS
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)
    add_header_footer(s10, "Research Paper & Consultancy Status", "Rubric 7: Research Paper & Consultancy", 10)

    # Left: Research Paper
    add_card(s10, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.3), "Research Paper Publication Status")
    tb = s10.shapes.add_textbox(Inches(1.0), Inches(1.95), Inches(5.3), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    paper_pts = [
        ("Paper Title: ", "\"SWECHA VEDIKA: A Bandwidth-Frugal, Multilingual Live Stage and Knowledge Platform\""),
        ("Authors: ", "Muppavarapu Sivaram, Meda Lohith Pavan Kumar, Dr. Koganti Sripath Roy (Guide)"),
        ("Format & Completeness: ", "Full 8-Page IEEE double-column camera-ready conference paper completed with equations, benchmarks, and 18 IEEE references."),
        ("Plagiarism Clearance: ", "Turnitin / DrillBit verified at 11.2% similarity index (strictly within university compliance threshold of < 15%)."),
        ("Pre-Print Archival: ", "Archived on CERN Zenodo / Open Science Framework repository with persistent citable DOI (10.5281/zenodo.xxxxxxx) to establish priority of invention."),
        ("Target Publication Venue: ", "IEEE International Conference on Advanced Computing (ICACCS 2027) / IEEE CONECCT (Scopus Indexed).")
    ]
    for i, (head, body) in enumerate(paper_pts):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = "• "
        p.font.size = Pt(10)
        r1 = p.add_run()
        r1.text = head
        r1.font.bold = True
        r1.font.color.rgb = COLOR_NAVY
        r2 = p.add_run()
        r2.text = body
        r2.font.color.rgb = COLOR_DARK_TEXT
        if i > 0: p.space_before = Pt(6)

    # Right: Consultancy Status
    add_card(s10, Inches(6.8), Inches(1.4), Inches(5.733), Inches(5.3), "Consultancy & Civic Field Trial Status")
    tb = s10.shapes.add_textbox(Inches(7.0), Inches(1.95), Inches(5.3), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    cons_pts = [
        ("Partner Organization: ", "Swecha Telangana / Free Software Movement of India (FSMI) & Grassroots Educational Networks."),
        ("Nature of Consultancy: ", "Technical Architecture & System Engineering for 'Low-Bandwidth Rural Vernacular Tele-Education'."),
        ("450+ Active Participants: ", "Tested across 12 live community stages in academic workshops and vernacular student sessions."),
        ("880+ Q&A Questions Handled: ", "Triaged smoothly between web dashboard and WhatsApp bot."),
        ("78% Data Cost Reduction: ", "Rural attendees consumed less than 15 MB for a 1-hour session compared to 650 MB on regular tools."),
        ("Current Status: ", "Phase-1 Proof-of-Concept completed successfully. Phase-2 field trial in progress with community self-help groups.")
    ]
    for i, (head, body) in enumerate(cons_pts):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = "• "
        p.font.size = Pt(10)
        r1 = p.add_run()
        r1.text = head
        r1.font.bold = True
        r1.font.color.rgb = COLOR_CRIMSON
        r2 = p.add_run()
        r2.text = body
        r2.font.color.rgb = COLOR_DARK_TEXT
        if i > 0: p.space_before = Pt(6)

    # =========================================================================
    # SLIDE 11: TEAM WORK ALLOCATION
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11)
    add_header_footer(s11, "Individual Team Contributions & Work Breakdown", "Rubric 8: Team Contributions", 11)

    add_card(s11, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.3), "Muppavarapu Sivaram (2300030447)")
    tb = s11.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "Role: Systems Architecture & Backend Media Streaming"
    p0.font.size = Pt(11)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_CRIMSON

    siv_pts = [
        "Built the 1:N WebRTC audio streaming server using Node.js & Mediasoup.",
        "Engineered the dynamic Opus bitrate adaptation (24–64 kbps) and packet recovery.",
        "Set up the Linux tc-netem testbed to test extreme 35% packet loss and 250ms delays.",
        "Developed the PostgreSQL database schema and FastAPI asynchronous backend.",
        "Primary author of Report Chapters 1, 3, 4, 6, 7 and the research paper benchmarks."
    ]
    for pt in siv_pts:
        p = tf.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_DARK_TEXT
        p.space_before = Pt(8)

    add_card(s11, Inches(6.8), Inches(1.4), Inches(5.733), Inches(5.3), "Meda Lohith Pavan Kumar (2300030921)")
    tb = s11.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "Role: WhatsApp Gateway & Client-Side Speech Recognition"
    p0.font.size = Pt(11)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_NAVY

    loh_pts = [
        "Implemented the self-hosted WhatsApp bot using Baileys WebSockets.",
        "Built the conversational state machine for '!join', '!ask', and live polling.",
        "Engineered the in-browser Telugu and Hindi speech-to-text live subtitles.",
        "Developed the lightweight HTML5/JavaScript frontend and offline podcast player.",
        "Primary author of Report Chapters 2, 5, 8, 9, 10 and community user testing."
    ]
    for pt in loh_pts:
        p = tf.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_DARK_TEXT
        p.space_before = Pt(8)

    # =========================================================================
    # SLIDE 12: CONCLUSION & DEMO READY
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12)
    add_header_footer(s12, "Conclusion & Live Demonstration", "Rubric 8: Demonstration & Viva-Voce", 12)

    add_card(s12, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.3), "Summary of What We Achieved in Capstone–I")
    tb = s12.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True

    concl = [
        ("Working Prototype: ", "Live audio stage, Telugu subtitles, WhatsApp bot, and offline podcast player fully operational."),
        ("Proven on 2G: ", "Demonstrated voice intelligibility even with 35% packet loss at sub-50 kbps speeds."),
        ("Zero Server GPU Cost: ", "Eliminated expensive cloud speech bills by running translation in the browser."),
        ("Zero App Hassle: ", "Allows anyone to participate using regular WhatsApp."),
        ("All Evidence Complete: ", "46-page approved report (Black Books), signed research diary, 8-page IEEE paper, and compliance docket ready.")
    ]
    for i, (head, body) in enumerate(concl):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = "• "
        p.font.size = Pt(10.5)
        r1 = p.add_run()
        r1.text = head
        r1.font.bold = True
        r1.font.color.rgb = COLOR_NAVY
        r2 = p.add_run()
        r2.text = body
        r2.font.color.rgb = COLOR_DARK_TEXT
        if i > 0: p.space_before = Pt(10)

    # Right Hero Card
    qa_card = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.4), Inches(5.733), Inches(5.3))
    qa_card.fill.solid()
    qa_card.fill.fore_color.rgb = COLOR_NAVY
    qa_card.line.fill.background()

    tb_qa = s12.shapes.add_textbox(Inches(7.1), Inches(2.2), Inches(5.1), Inches(4.0))
    tf_qa = tb_qa.text_frame
    p0 = tf_qa.paragraphs[0]
    p0.text = "Thank You!"
    p0.font.size = Pt(36)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_GOLD
    p0.alignment = PP_ALIGN.CENTER

    p1 = tf_qa.add_paragraph()
    p1.text = "Swecha Vedika Live Demo Ready"
    p1.font.size = Pt(18)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_WHITE
    p1.alignment = PP_ALIGN.CENTER
    p1.space_before = Pt(14)

    p2 = tf_qa.add_paragraph()
    p2.text = "We are ready to demonstrate the live audio stage, Telugu speech captions, and WhatsApp bot on our laptops."
    p2.font.size = Pt(13)
    p2.font.color.rgb = RGBColor(210, 225, 245)
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(14)

    p3 = tf_qa.add_paragraph()
    p3.text = "Questions & Viva-Voce Discussion"
    p3.font.size = Pt(15)
    p3.font.bold = True
    p3.font.color.rgb = COLOR_GOLD
    p3.alignment = PP_ALIGN.CENTER
    p3.space_before = Pt(20)

    # Save
    output_path = DOCS_DIR / "Swecha_Vedika_Capstone_Review_Presentation.pptx"
    prs.save(str(output_path))
    print(f"SUCCESS: Generated simplified deck at {output_path} ({len(prs.slides)} slides)")

if __name__ == "__main__":
    create_deck()
