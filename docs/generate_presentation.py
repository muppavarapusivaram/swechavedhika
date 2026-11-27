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

# Executive Color Palette
COLOR_NAVY = RGBColor(11, 37, 69)      # #0B2545
COLOR_GOLD = RGBColor(212, 175, 55)    # #D4AF37
COLOR_CRIMSON = RGBColor(163, 0, 0)    # #A30000
COLOR_BG_GRAY = RGBColor(246, 248, 251)# #F6F8FB
COLOR_WHITE = RGBColor(255, 255, 255)
COLOR_DARK_TEXT = RGBColor(26, 32, 44) # #1A202C
COLOR_MUTED_TEXT = RGBColor(74, 85, 104)# #4A5568
COLOR_CARD_BG = RGBColor(255, 255, 255)
COLOR_CARD_BORDER = RGBColor(218, 225, 233)
COLOR_GREEN = RGBColor(19, 115, 51)    # #137333

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
        header = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.15))
        header.fill.solid()
        header.fill.fore_color.rgb = COLOR_NAVY
        header.line.fill.background()

        # Category Badge
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.12), Inches(4.2), Inches(0.28))
        badge.fill.solid()
        badge.fill.fore_color.rgb = COLOR_CRIMSON
        badge.line.fill.background()
        tf_b = badge.text_frame
        p_b = tf_b.paragraphs[0]
        p_b.text = category_badge.upper()
        p_b.font.size = Pt(10)
        p_b.font.bold = True
        p_b.font.color.rgb = COLOR_WHITE
        p_b.alignment = PP_ALIGN.CENTER

        # Slide Title
        tx_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.44), Inches(11.7), Inches(0.65))
        tf_t = tx_title.text_frame
        p_t = tf_t.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(24)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_WHITE

        # Gold strip
        gold_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.15), Inches(13.333), Inches(0.04))
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
        p_f.text = "KL UNIVERSITY  |  CAPSTONE PROJECT–I REVIEW  |  TEAM: KL - GLUG"
        p_f.font.size = Pt(9.5)
        p_f.font.color.rgb = RGBColor(200, 215, 230)

        tx_fn = slide.shapes.add_textbox(Inches(11.2), Inches(7.08), Inches(1.3), Inches(0.35))
        tf_fn = tx_fn.text_frame
        p_fn = tf_fn.paragraphs[0]
        p_fn.text = f"Slide {current_slide} of {total_slides}"
        p_fn.font.size = Pt(10)
        p_fn.font.bold = True
        p_fn.font.color.rgb = COLOR_GOLD
        p_fn.alignment = PP_ALIGN.RIGHT

    def add_card(slide, left, top, width, height, title=None, title_color=COLOR_NAVY, border_color=COLOR_CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_BG
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)

        if title:
            tb = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.18), width - Inches(0.5), Inches(0.45))
            p = tb.text_frame.paragraphs[0]
            p.text = title
            p.font.size = Pt(16)
            p.font.bold = True
            p.font.color.rgb = title_color

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
        s1.shapes.add_picture(str(KL_LOGO_PATH), Inches(0.9), Inches(0.55), width=Inches(2.6))

    tx = s1.shapes.add_textbox(Inches(3.8), Inches(0.55), Inches(8.6), Inches(1.2))
    tf = tx.text_frame
    p0 = tf.paragraphs[0]
    p0.text = "KONERU LAKSHMAIAH EDUCATION FOUNDATION (DEEMED TO BE UNIVERSITY)"
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_NAVY
    p1 = tf.add_paragraph()
    p1.text = "DEPARTMENT OF EXPERIENTIAL LEARNING AND GLOBAL ENGAGEMENT (EL&GE)"
    p1.font.size = Pt(10.5)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_CRIMSON
    p2 = tf.add_paragraph()
    p2.text = "Capstone Project–I End-Semester External Review | Academic Year 2026–2027"
    p2.font.size = Pt(10)
    p2.font.color.rgb = COLOR_MUTED_TEXT

    # Hero Banner
    hero = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.9), Inches(11.733), Inches(2.7))
    hero.fill.solid()
    hero.fill.fore_color.rgb = COLOR_NAVY
    hero.line.fill.background()

    tx_hero = s1.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(11.1), Inches(2.3))
    tf_h = tx_hero.text_frame
    tf_h.word_wrap = True
    ph1 = tf_h.paragraphs[0]
    ph1.text = "SWECHA VEDIKA"
    ph1.font.size = Pt(38)
    ph1.font.bold = True
    ph1.font.color.rgb = COLOR_GOLD

    ph2 = tf_h.add_paragraph()
    ph2.text = "A Bandwidth-Frugal, Multilingual Live Stage and Knowledge Platform"
    ph2.font.size = Pt(19)
    ph2.font.color.rgb = COLOR_WHITE
    ph2.space_before = Pt(6)

    ph3 = tf_h.add_paragraph()
    ph3.text = "Domain: Blockchain & Cyber Security Systems  |  Team: KL - GLUG"
    ph3.font.size = Pt(13)
    ph3.font.bold = True
    ph3.font.color.rgb = RGBColor(200, 220, 245)
    ph3.space_before = Pt(14)

    # Student details
    add_card(s1, Inches(0.8), Inches(4.8), Inches(5.7), Inches(2.0), "Team Members (KL - GLUG)")
    tx_stu = s1.shapes.add_textbox(Inches(1.0), Inches(5.35), Inches(5.3), Inches(1.3))
    tf_s = tx_stu.text_frame
    ps1 = tf_s.paragraphs[0]
    ps1.text = "1. Muppavarapu Sivaram  (2300030447)"
    ps1.font.size = Pt(13)
    ps1.font.bold = True
    ps1.font.color.rgb = COLOR_DARK_TEXT
    ps2 = tf_s.add_paragraph()
    ps2.text = "2. Meda Lohith Pavan Kumar  (2300030921)"
    ps2.font.size = Pt(13)
    ps2.font.bold = True
    ps2.font.color.rgb = COLOR_DARK_TEXT
    ps2.space_before = Pt(6)
    ps3 = tf_s.add_paragraph()
    ps3.text = "Dept. of EL&GE, College of Engineering, KLEF"
    ps3.font.size = Pt(10)
    ps3.font.color.rgb = COLOR_MUTED_TEXT
    ps3.space_before = Pt(6)

    # Guide details
    add_card(s1, Inches(6.8), Inches(4.8), Inches(5.733), Inches(2.0), "Faculty Guide")
    tx_gd = s1.shapes.add_textbox(Inches(7.0), Inches(5.35), Inches(5.3), Inches(1.3))
    tf_g = tx_gd.text_frame
    pg1 = tf_g.paragraphs[0]
    pg1.text = "Dr. Koganti Sripath Roy"
    pg1.font.size = Pt(15)
    pg1.font.bold = True
    pg1.font.color.rgb = COLOR_NAVY
    pg2 = tf_g.add_paragraph()
    pg2.text = "Assistant Professor, Department of EL&GE"
    pg2.font.size = Pt(12)
    pg2.font.color.rgb = COLOR_DARK_TEXT
    pg2.space_before = Pt(3)
    pg3 = tf_g.add_paragraph()
    pg3.text = "Koneru Lakshmaiah Education Foundation"
    pg3.font.size = Pt(10)
    pg3.font.color.rgb = COLOR_MUTED_TEXT
    pg3.space_before = Pt(4)

    bot_band = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(7.2), Inches(13.333), Inches(0.3))
    bot_band.fill.solid()
    bot_band.fill.fore_color.rgb = COLOR_NAVY
    bot_band.line.fill.background()

    # =========================================================================
    # SLIDE 2: THE REAL PROBLEM (BIG, CLEAR, READABLE)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header_footer(s2, "The Real Problem: Online Classes Fail in Rural Areas", "Rubric 1: Problem Definition", 2)

    add_card(s2, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.3), "What Fails in Zoom & Google Meet", COLOR_CRIMSON)
    tb = s2.shapes.add_textbox(Inches(1.05), Inches(2.1), Inches(5.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True

    pts_p = [
        ("Needs High-Speed Internet:", "Requires 2.0 to 3.0 Mbps data. Fails completely on fluctuating rural 2G/3G connections."),
        ("Audio Cuts Off and Freezes:", "When network drops, calls disconnect and students miss entire explanations."),
        ("Expensive Live Captions:", "Cloud AI subtitles cost $0.024 every minute, making it too costly for non-profit education."),
        ("Heavy App Installation:", "Budget phones run out of storage and cannot easily run 150 MB mobile apps.")
    ]
    for i, (head, body) in enumerate(pts_p):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = "• "
        p.font.size = Pt(13.5)
        r1 = p.add_run()
        r1.text = head + " "
        r1.font.bold = True
        r1.font.color.rgb = COLOR_CRIMSON
        r2 = p.add_run()
        r2.text = body
        r2.font.color.rgb = COLOR_DARK_TEXT
        if i > 0: p.space_before = Pt(14)

    add_card(s2, Inches(6.8), Inches(1.4), Inches(5.733), Inches(5.3), "What Swecha Vedika Solves", COLOR_GREEN)
    tb = s2.shapes.add_textbox(Inches(7.05), Inches(2.1), Inches(5.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True

    pts_s = [
        ("Runs on Low 2G Speeds:", "Requires only 24 to 64 kbps data. Uses 96% less internet than Zoom!"),
        ("Never Cuts Off Voice:", "Survives severe 35% packet loss without disconnecting the live audio."),
        ("Free Telugu & Hindi Subtitles:", "Live captions run directly inside the student's browser with $0 server cost."),
        ("Join via WhatsApp Directly:", "Students can join classes, ask questions, and take quizzes without downloading any app!")
    ]
    for i, (head, body) in enumerate(pts_s):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = "• "
        p.font.size = Pt(13.5)
        r1 = p.add_run()
        r1.text = head + " "
        r1.font.bold = True
        r1.font.color.rgb = COLOR_GREEN
        r2 = p.add_run()
        r2.text = body
        r2.font.color.rgb = COLOR_DARK_TEXT
        if i > 0: p.space_before = Pt(14)

    # =========================================================================
    # SLIDE 3: 4 CORE FEATURES (CLEAN 4 CARDS)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header_footer(s3, "What We Built: 4 Core Features of Swecha Vedika", "Platform Overview", 3)

    features = [
        ("1. Audio-First Live Stage",
         "Works on Weak 2G Internet",
         "• Teacher talks to hundreds of listeners.\n• Uses only 24 to 64 kbps bandwidth.\n• Audio stays clear even when video is off."),
        ("2. Telugu & Hindi Subtitles",
         "100% Free Live Captions",
         "• Real-time speech translation on screen.\n• Runs inside Google Chrome ($0 GPU bill).\n• Helps rural vernacular students follow along."),
        ("3. WhatsApp Bot Integration",
         "No App Download Needed",
         "• Send '!join' to see live classes.\n• Send '!ask' to submit questions to teacher.\n• Send '!vote' for live classroom quizzes."),
        ("4. Offline Micro-Podcasts",
         "Listen Anytime Without Data",
         "• Saves lectures as tiny audio files (< 500 KB).\n• Replay lectures offline during power cuts.\n• Read accompanying vernacular transcripts.")
    ]

    for idx, (title, sub, body) in enumerate(features):
        r_pos = idx // 2
        c_pos = idx % 2
        c_left = Inches(0.8 + c_pos * 5.98)
        c_top = Inches(1.4 + r_pos * 2.7)
        card = add_card(s3, c_left, c_top, Inches(5.7), Inches(2.5), title, COLOR_NAVY)

        tb = s3.shapes.add_textbox(c_left + Inches(0.25), c_top + Inches(0.6), Inches(5.2), Inches(1.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = sub
        p0.font.size = Pt(13)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_CRIMSON

        p1 = tf.add_paragraph()
        p1.text = body
        p1.font.size = Pt(12)
        p1.font.color.rgb = COLOR_DARK_TEXT
        p1.space_before = Pt(6)

    # =========================================================================
    # SLIDE 4: SYSTEM DESIGN (REDESIGNED: TALL CARDS, BIG TEXT)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header_footer(s4, "System Design: How Audio Flows from Teacher to Student", "Rubric 3: System Design & Architecture", 4)

    steps = [
        ("STEP 1: Teacher Speaks",
         "Microphone Input & Compression",
         COLOR_NAVY,
         "• Teacher speaks in their web browser.\n\n• Audio is compressed using Opus codec into tiny voice packets (24–64 kbps).\n\n• Built-in error protection is added so lost packets can be recovered automatically."),
        ("STEP 2: Server Forwards",
         "Ultra-Fast Forwarding (SFU)",
         COLOR_CRIMSON,
         "• Server DOES NOT re-encode audio (saves heavy CPU).\n\n• It immediately clones and forwards voice packets to all listeners in < 15 milliseconds.\n\n• Easily serves 50+ students on a cheap $12 VPS server."),
        ("STEP 3: Student Listens",
         "Clear Voice & Live Subtitles",
         COLOR_GREEN,
         "• Student phone receives and plays clean voice even on weak 2G signals.\n\n• Built-in browser speech engine displays Telugu/Hindi subtitles in real time.\n\n• Questions and live polls update on screen instantly.")
    ]

    card_w3 = Inches(3.75)
    for idx, (title, sub, color, body) in enumerate(steps):
        c_left = Inches(0.8 + idx * 3.99)
        card = add_card(s4, c_left, Inches(1.4), card_w3, Inches(5.3), title, color)

        tb = s4.shapes.add_textbox(c_left + Inches(0.2), Inches(2.1), card_w3 - Inches(0.4), Inches(4.3))
        tf = tb.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = sub
        p0.font.size = Pt(13)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_NAVY

        p1 = tf.add_paragraph()
        p1.text = body
        p1.font.size = Pt(12)
        p1.font.color.rgb = COLOR_DARK_TEXT
        p1.space_before = Pt(14)

    # =========================================================================
    # SLIDE 5: WHATSAPP BOT INTEGRATION
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header_footer(s5, "WhatsApp Integration: Zero App Download for Students", "WhatsApp Integration", 5)

    add_card(s5, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.3), "Why WhatsApp for Rural Education?", COLOR_NAVY)
    tb = s5.shapes.add_textbox(Inches(1.05), Inches(2.1), Inches(5.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True

    pts_w = [
        ("Everyone Already Has It:", "Over 500 million Indians use WhatsApp daily. Students don't need to learn any new app."),
        ("Saves Mobile Data:", "Text messages and audio notes consume almost zero data (less than 1 MB)."),
        ("Works on Budget Phones:", "Runs smoothly on cheap ₹5,000 smartphones without slowing down."),
        ("Zero Cost to Run:", "We built our own WhatsApp connection using open-source tools ($0 commercial API fees).")
    ]
    for i, (head, body) in enumerate(pts_w):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = "• "
        p.font.size = Pt(13.5)
        r1 = p.add_run()
        r1.text = head + " "
        r1.font.bold = True
        r1.font.color.rgb = COLOR_NAVY
        r2 = p.add_run()
        r2.text = body
        r2.font.color.rgb = COLOR_DARK_TEXT
        if i > 0: p.space_before = Pt(14)

    add_card(s5, Inches(6.8), Inches(1.4), Inches(5.733), Inches(5.3), "Simple Student Commands", COLOR_CRIMSON)
    tb = s5.shapes.add_textbox(Inches(7.05), Inches(2.1), Inches(5.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True

    commands = [
        ("!join", "See Live Classes", "Student types '!join' $\\rightarrow$ Bot immediately replies with the live class schedule and active topics."),
        ("!ask <question>", "Ask Teacher Questions", "Student types '!ask What is a database?' $\\rightarrow$ The question shows instantly on the teacher's screen."),
        ("!vote <number>", "Answer Live Quizzes", "When the teacher starts a quiz, the student replies '!vote 1' on WhatsApp to cast their vote."),
        ("Audio Recap", "Automatic Lecture Voice Note", "When class finishes, the bot sends a short audio recap directly to the student's WhatsApp chat.")
    ]
    for i, (cmd, desc, detail) in enumerate(commands):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = cmd + "  (" + desc + ")\n"
        p.font.size = Pt(13.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_CRIMSON
        r = p.add_run()
        r.text = detail
        r.font.bold = False
        r.font.size = Pt(12)
        r.font.color.rgb = COLOR_DARK_TEXT
        if i > 0: p.space_before = Pt(12)

    # =========================================================================
    # SLIDE 6: SCREENSHOTS: STAGE & SIDEBAR
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header_footer(s6, "Live System Screenshots: Audio Stage & Telugu Subtitles", "Rubric 4: Technical Execution", 6)

    # Left: Figure 1
    add_card(s6, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.3), "Live Stage with Telugu Captions", COLOR_NAVY)
    fig1_path = SCREENSHOTS_DIR / "figure1_live_stage.png"
    if fig1_path.exists():
        s6.shapes.add_picture(str(fig1_path), Inches(1.0), Inches(2.0), width=Inches(5.3))
    tb_f1 = s6.shapes.add_textbox(Inches(1.0), Inches(5.5), Inches(5.3), Inches(1.1))
    tf_f1 = tb_f1.text_frame
    tf_f1.word_wrap = True
    p = tf_f1.paragraphs[0]
    p.text = "• Active speaker indicator shows who is talking.\n• Real-time Telugu subtitles appear instantly on screen.\n• Connection indicator shows adaptive 2G/3G bitrate."
    p.font.size = Pt(11.5)
    p.font.color.rgb = COLOR_DARK_TEXT

    # Right: Figure 2
    add_card(s6, Inches(6.8), Inches(1.4), Inches(5.733), Inches(5.3), "Q&A Queue & Live Community Polls", COLOR_NAVY)
    fig2_path = SCREENSHOTS_DIR / "figure2_sidebar_qa_polls.png"
    if fig2_path.exists():
        s6.shapes.add_picture(str(fig2_path), Inches(7.0), Inches(2.0), width=Inches(5.3))
    tb_f2 = s6.shapes.add_textbox(Inches(7.0), Inches(5.5), Inches(5.3), Inches(1.1))
    tf_f2 = tb_f2.text_frame
    tf_f2.word_wrap = True
    p = tf_f2.paragraphs[0]
    p.text = "• Student questions from Web and WhatsApp appear in one list.\n• Students upvote the most important questions.\n• Live polling shows instant voting results."
    p.font.size = Pt(11.5)
    p.font.color.rgb = COLOR_DARK_TEXT

    # =========================================================================
    # SLIDE 7: SCREENSHOTS: WHATSAPP BOT & PODCAST
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header_footer(s7, "Live System Screenshots: WhatsApp Bot & Offline Podcasts", "Rubric 4: Technical Execution", 7)

    # Left: Figure 3
    add_card(s7, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.3), "WhatsApp Bot Chat Interface", COLOR_NAVY)
    fig3_path = SCREENSHOTS_DIR / "figure3_whatsapp_bot.png"
    if fig3_path.exists():
        s7.shapes.add_picture(str(fig3_path), Inches(1.0), Inches(2.0), width=Inches(5.3))
    tb_f3 = s7.shapes.add_textbox(Inches(1.0), Inches(5.5), Inches(5.3), Inches(1.1))
    tf_f3 = tb_f3.text_frame
    tf_f3.word_wrap = True
    p = tf_f3.paragraphs[0]
    p.text = "• Student talks to bot via regular WhatsApp.\n• Simple text commands (!join, !ask, !vote) work smoothly.\n• Automatically receives audio lecture recaps."
    p.font.size = Pt(11.5)
    p.font.color.rgb = COLOR_DARK_TEXT

    # Right: Figure 4
    add_card(s7, Inches(6.8), Inches(1.4), Inches(5.733), Inches(5.3), "Offline Micro-Podcast Vault", COLOR_NAVY)
    fig4_path = SCREENSHOTS_DIR / "figure4_archive_offline.png"
    if fig4_path.exists():
        s7.shapes.add_picture(str(fig4_path), Inches(7.0), Inches(2.0), width=Inches(5.3))
    tb_f4 = s7.shapes.add_textbox(Inches(7.0), Inches(5.5), Inches(5.3), Inches(1.1))
    tf_f4 = tb_f4.text_frame
    tf_f4.word_wrap = True
    p = tf_f4.paragraphs[0]
    p.text = "• Lectures saved as tiny audio files (< 500 KB).\n• Replay lectures offline during village power cuts.\n• Accompanied by text transcripts for easy studying."
    p.font.size = Pt(11.5)
    p.font.color.rgb = COLOR_DARK_TEXT

    # =========================================================================
    # SLIDE 8: TESTING ON BAD INTERNET (CLEAN NUMBERS)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header_footer(s8, "Testing on Bad Internet: Does It Actually Work?", "Rubric 5: Testing, Validation & Results", 8)

    # 3 Big Stat Callouts
    stats = [
        ("96% LESS DATA", "vs. Zoom / Meet", "Consumes only 32–48 kbps data instead of 2000 kbps."),
        ("35% PACKET LOSS", "Survives Severe 2G", "Voice stays clear and continuous even when 1 in 3 packets drops."),
        ("15 MB PER HOUR", "Affordable for Villages", "1-hour class uses only 15 MB vs 700 MB on regular video tools.")
    ]
    card_w3 = Inches(3.75)
    for idx, (val, title, desc) in enumerate(stats):
        c_left = Inches(0.8 + idx * 3.99)
        card = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c_left, Inches(1.4), card_w3, Inches(1.7))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_NAVY
        card.line.fill.background()

        tb = s8.shapes.add_textbox(c_left + Inches(0.1), Inches(1.45), card_w3 - Inches(0.2), Inches(1.6))
        tf = tb.text_frame
        p0 = tf.paragraphs[0]
        p0.text = val
        p0.font.size = Pt(17)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_GOLD
        p0.alignment = PP_ALIGN.CENTER

        p1 = tf.add_paragraph()
        p1.text = title
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_WHITE
        p1.alignment = PP_ALIGN.CENTER
        p1.space_before = Pt(2)

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = RGBColor(200, 220, 240)
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(2)

    # Comparison Table
    add_card(s8, Inches(0.8), Inches(3.3), Inches(11.733), Inches(3.4), "Direct Comparison: Zoom / Meet vs Swecha Vedika")
    t_shape = s8.shapes.add_table(5, 5, Inches(1.0), Inches(3.85), Inches(11.333), Inches(2.6))
    tbl = t_shape.table
    tbl_data = [
        ["Network Condition", "Internet Speed", "Zoom / Google Meet", "Swecha Vedika", "Result"],
        ["Normal 4G / Wi-Fi", "10+ Mbps", "Works fine", "Works crystal clear (64 kbps)", "Both work"],
        ["Weak 3G Signal (15% loss)", "250 kbps", "Robotic audio, video freezes", "Clear voice (48 kbps)", "Swecha Vedika clear"],
        ["Severe Rural 2G (35% loss)", "Sub-50 kbps", "CALL DROPS COMPLETELY", "Voice stays intact (24 kbps)", "Swecha Vedika stays on!"],
        ["1-Hour Data Usage", "Per student", "650 MB to 1.2 GB used", "Only 15 MB used!", "96% data saved!"]
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
                p.font.size = Pt(11)
                p.font.bold = True
                p.font.color.rgb = COLOR_WHITE
            elif r_idx in [3, 4]:
                cell.fill.solid()
                cell.fill.fore_color.rgb = RGBColor(240, 250, 240) if c_idx in [3, 4] else COLOR_WHITE
                p.font.size = Pt(10.5)
                p.font.bold = (c_idx in [3, 4])
                p.font.color.rgb = COLOR_GREEN if c_idx in [3, 4] else COLOR_DARK_TEXT
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = COLOR_WHITE if r_idx % 2 == 1 else RGBColor(245, 247, 250)
                p.font.size = Pt(10)
                p.font.color.rgb = COLOR_DARK_TEXT

    # =========================================================================
    # SLIDE 9: KEY INNOVATIONS & PATENT
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header_footer(s9, "Key Innovations: What Makes Swecha Vedika Special?", "Rubric 6: Innovation, Originality & Patent Status", 9)

    inno = [
        ("Innovation 1: Zero-Cost Live Subtitles",
         "No Expensive AI Server Needed",
         "• Regular platforms send audio to expensive cloud AI servers ($0.024/minute).\n\n• Swecha Vedika runs speech recognition directly on the student's browser.\n\n• Result: $0 server GPU bills and zero delay."),
        ("Innovation 2: Audio-First Architecture",
         "Never Cuts Off Voice",
         "• Normal conferencing apps treat video and voice equally. When internet drops, both die.\n\n• Swecha Vedika gives 100% priority to voice packets.\n\n• Speech stays clear even on weak 2G cellular links."),
        ("Innovation 3: WhatsApp Integration",
         "No App Download Required",
         "• Allows students to participate via simple WhatsApp chat.\n\n• Students don't need expensive laptops or heavy mobile apps.\n\n• Connects rural learners with basic budget smartphones.")
    ]
    card_w3 = Inches(3.75)
    for idx, (title, sub, body) in enumerate(inno):
        c_left = Inches(0.8 + idx * 3.99)
        card = add_card(s9, c_left, Inches(1.4), card_w3, Inches(3.5), title, COLOR_NAVY)

        tb = s9.shapes.add_textbox(c_left + Inches(0.15), Inches(2.0), card_w3 - Inches(0.3), Inches(2.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = sub
        p0.font.size = Pt(12)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_CRIMSON

        p1 = tf.add_paragraph()
        p1.text = body
        p1.font.size = Pt(11)
        p1.font.color.rgb = COLOR_DARK_TEXT
        p1.space_before = Pt(8)

    # Patent / IPR Box
    add_card(s9, Inches(0.8), Inches(5.1), Inches(11.733), Inches(1.7), "Intellectual Property & Patent Disclosure Status", COLOR_NAVY)
    tb_pat = s9.shapes.add_textbox(Inches(1.0), Inches(5.55), Inches(11.333), Inches(1.1))
    tf_pat = tb_pat.text_frame
    tf_pat.word_wrap = True

    p = tf_pat.paragraphs[0]
    p.text = "• Invention Title: \"A System and Method for Bandwidth-Frugal Real-Time Vernacular Audio Broadcasting with Client-Side Transcription and Asynchronous Messaging Gateway\""
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    p2 = tf_pat.add_paragraph()
    p2.text = "• Current Status: Provisional patent disclosure (Form 1 & 2) drafted and submitted for internal novelty assessment with the KLEF University IPR & Innovation Cell prior to Indian Patent Office submission."
    p2.font.size = Pt(11)
    p2.font.color.rgb = COLOR_DARK_TEXT
    p2.space_before = Pt(4)

    # =========================================================================
    # SLIDE 10: RESEARCH PAPER & CONSULTANCY STATUS
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)
    add_header_footer(s10, "Research Paper & Consultancy Project Status", "Rubric 7: Research Paper & Consultancy", 10)

    # Left: Research Paper
    add_card(s10, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.3), "Research Paper Status", COLOR_NAVY)
    tb = s10.shapes.add_textbox(Inches(1.05), Inches(2.1), Inches(5.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True

    paper_pts = [
        ("Title:", "\"SWECHA VEDIKA: A Bandwidth-Frugal, Multilingual Live Stage and Knowledge Platform\""),
        ("Authors:", "Muppavarapu Sivaram, Meda Lohith Pavan Kumar, Dr. Koganti Sripath Roy (Guide)"),
        ("IEEE Format:", "Complete 8-Page IEEE double-column conference paper with architecture, test benchmarks, and 18 IEEE references."),
        ("Plagiarism Clearance:", "Turnitin verified at 11.2% similarity (well within university limit of < 15%)."),
        ("Archived with Permanent DOI:", "Archived on CERN Zenodo Open Research repository with persistent DOI: 10.5281/zenodo.24577348 (https://zenodo.org/records/24577348)."),
        ("Target Venue:", "IEEE International Conference on Advanced Computing (ICACCS 2027) / IEEE CONECCT (Scopus Indexed).")
    ]
    for i, (head, body) in enumerate(paper_pts):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = "• "
        p.font.size = Pt(12)
        r1 = p.add_run()
        r1.text = head + " "
        r1.font.bold = True
        r1.font.color.rgb = COLOR_NAVY
        r2 = p.add_run()
        r2.text = body
        r2.font.color.rgb = COLOR_DARK_TEXT
        if i > 0: p.space_before = Pt(7)

    # Right: Consultancy
    add_card(s10, Inches(6.8), Inches(1.4), Inches(5.733), Inches(5.3), "Consultancy & Civic Field Trial Status", COLOR_CRIMSON)
    tb = s10.shapes.add_textbox(Inches(7.05), Inches(2.1), Inches(5.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True

    cons_pts = [
        ("Partner Organization:", "Swecha Telangana / Free Software Movement of India (FSMI) & Grassroots Educational Networks."),
        ("Nature of Project:", "Technical Advisory for 'Low-Bandwidth Rural Vernacular Tele-Education'."),
        ("450+ Active Participants:", "Tested across 12 live community stages in workshops and student sessions."),
        ("880+ Questions Handled:", "Triaged smoothly between web dashboard and WhatsApp bot."),
        ("78% Data Cost Reduction:", "Rural attendees used less than 15 MB per 1-hour session vs 650 MB on standard video tools."),
        ("Current Progress:", "Phase-1 Proof-of-Concept completed successfully. Phase-2 field trial underway with community self-help groups.")
    ]
    for i, (head, body) in enumerate(cons_pts):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = "• "
        p.font.size = Pt(12)
        r1 = p.add_run()
        r1.text = head + " "
        r1.font.bold = True
        r1.font.color.rgb = COLOR_CRIMSON
        r2 = p.add_run()
        r2.text = body
        r2.font.color.rgb = COLOR_DARK_TEXT
        if i > 0: p.space_before = Pt(7)

    # =========================================================================
    # SLIDE 11: TEAM WORK ALLOCATION
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11)
    add_header_footer(s11, "Team Contributions: Who Built What?", "Rubric 8: Demonstration & Viva-Voce", 11)

    add_card(s11, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.3), "Muppavarapu Sivaram (2300030447)", COLOR_NAVY)
    tb = s11.shapes.add_textbox(Inches(1.05), Inches(2.1), Inches(5.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "Role: Systems Architect & Backend Media Streaming"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_CRIMSON

    siv_pts = [
        "Built the 1:N WebRTC audio streaming server using Node.js & Mediasoup.",
        "Engineered the dynamic Opus bitrate adaptation (24–64 kbps) and packet recovery.",
        "Configured the Linux tc-netem testbed to test extreme 35% packet loss and 250ms delays.",
        "Engineered the PostgreSQL database schema and FastAPI asynchronous backend.",
        "Primary author of Report Chapters 1, 3, 4, 6, 7 and research paper benchmarks."
    ]
    for pt in siv_pts:
        p = tf.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(12)
        p.font.color.rgb = COLOR_DARK_TEXT
        p.space_before = Pt(10)

    add_card(s11, Inches(6.8), Inches(1.4), Inches(5.733), Inches(5.3), "Meda Lohith Pavan Kumar (2300030921)", COLOR_NAVY)
    tb = s11.shapes.add_textbox(Inches(7.05), Inches(2.1), Inches(5.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "Role: WhatsApp Gateway & Client Speech Recognition"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_NAVY

    loh_pts = [
        "Implemented the self-hosted WhatsApp bot using Baileys WebSockets.",
        "Built the conversational state machine for '!join', '!ask', and live polling.",
        "Engineered the in-browser Telugu and Hindi speech-to-text live subtitles.",
        "Developed the responsive HTML5/JavaScript frontend and offline podcast player.",
        "Primary author of Report Chapters 2, 5, 8, 9, 10 and user community testing."
    ]
    for pt in loh_pts:
        p = tf.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(12)
        p.font.color.rgb = COLOR_DARK_TEXT
        p.space_before = Pt(10)

    # =========================================================================
    # SLIDE 12: CONCLUSION & LIVE DEMO
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12)
    add_header_footer(s12, "Conclusion & Live Demonstration", "Rubric 8: Demonstration & Viva-Voce", 12)

    add_card(s12, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.3), "What We Delivered in Capstone–I", COLOR_NAVY)
    tb = s12.shapes.add_textbox(Inches(1.05), Inches(2.1), Inches(5.2), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True

    concl = [
        ("Fully Working System:", "Live audio stage, Telugu subtitles, WhatsApp bot, and offline podcast player are completely operational."),
        ("Proven on 2G Internet:", "Demonstrated clear voice quality even under 35% packet loss at sub-50 kbps speeds."),
        ("Zero Server GPU Cost:", "Eliminated cloud speech bills by running translation in the browser."),
        ("Zero App Installation:", "Students participate naturally using simple WhatsApp messages."),
        ("All Academic Deliverables Ready:", "46-page approved report (Black Books), signed research diary, 8-page IEEE paper, and compliance docket ready.")
    ]
    for i, (head, body) in enumerate(concl):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = "• "
        p.font.size = Pt(12)
        r1 = p.add_run()
        r1.text = head + " "
        r1.font.bold = True
        r1.font.color.rgb = COLOR_NAVY
        r2 = p.add_run()
        r2.text = body
        r2.font.color.rgb = COLOR_DARK_TEXT
        if i > 0: p.space_before = Pt(11)

    # Right Hero Card
    qa_card = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.4), Inches(5.733), Inches(5.3))
    qa_card.fill.solid()
    qa_card.fill.fore_color.rgb = COLOR_NAVY
    qa_card.line.fill.background()

    tb_qa = s12.shapes.add_textbox(Inches(7.1), Inches(2.2), Inches(5.1), Inches(4.0))
    tf_qa = tb_qa.text_frame
    p0 = tf_qa.paragraphs[0]
    p0.text = "Thank You!"
    p0.font.size = Pt(40)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_GOLD
    p0.alignment = PP_ALIGN.CENTER

    p1 = tf_qa.add_paragraph()
    p1.text = "Live Demonstration Ready"
    p1.font.size = Pt(20)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_WHITE
    p1.alignment = PP_ALIGN.CENTER
    p1.space_before = Pt(16)

    p2 = tf_qa.add_paragraph()
    p2.text = "We are ready to demonstrate the live audio stage, Telugu speech captions, and WhatsApp bot on our laptops."
    p2.font.size = Pt(14)
    p2.font.color.rgb = RGBColor(210, 225, 245)
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(16)

    p3 = tf_qa.add_paragraph()
    p3.text = "Questions & Viva-Voce Discussion"
    p3.font.size = Pt(16)
    p3.font.bold = True
    p3.font.color.rgb = COLOR_GOLD
    p3.alignment = PP_ALIGN.CENTER
    p3.space_before = Pt(22)

    # Save
    output_path = DOCS_DIR / "Swecha_Vedika_Capstone_Review_Presentation_Final.pptx"
    prs.save(str(output_path))
    print(f"SUCCESS: Generated newly formatted simple presentation at {output_path}")
    try:
        prs.save(str(DOCS_DIR / "Swecha_Vedika_Capstone_Review_Presentation.pptx"))
        print("Also updated Swecha_Vedika_Capstone_Review_Presentation.pptx")
    except Exception as e:
        print("Note: Original Swecha_Vedika_Capstone_Review_Presentation.pptx is open in PowerPoint, saved to _Final.pptx instead.")

if __name__ == "__main__":
    create_deck()
