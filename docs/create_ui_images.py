from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('docs/screenshots', exist_ok=True)

# Try standard Windows fonts
try:
    font_bold_lg = ImageFont.truetype("arialbd.ttf", 22)
    font_bold_md = ImageFont.truetype("arialbd.ttf", 16)
    font_bold_sm = ImageFont.truetype("arialbd.ttf", 13)
    font_regular_md = ImageFont.truetype("arial.ttf", 15)
    font_regular_sm = ImageFont.truetype("arial.ttf", 13)
    font_regular_xs = ImageFont.truetype("arial.ttf", 11)
except:
    font_bold_lg = ImageFont.load_default()
    font_bold_md = ImageFont.load_default()
    font_bold_sm = ImageFont.load_default()
    font_regular_md = ImageFont.load_default()
    font_regular_sm = ImageFont.load_default()
    font_regular_xs = ImageFont.load_default()

# -------------------------------------------------------------
# IMAGE 1: LIVEKIT VIDEO STAGE & 2G LOW-DATA TELEMETRY (800 x 480)
# -------------------------------------------------------------
img1 = Image.new('RGB', (800, 480), color='#111111')
d1 = ImageDraw.Draw(img1)

# Navbar (height: 52)
d1.rectangle([(0, 0), (800, 52)], fill='#1c1511')
d1.line([(0, 52), (800, 52)], fill='#7A1F1A', width=2)
d1.text((16, 15), "🚩 Swecha Vedika", fill='#FFFFFF', font=font_bold_md)
d1.text((180, 16), "|  Rural Digital Empowerment Live Stage", fill='#E4D6C3', font=font_regular_sm)

# Stage Pill
d1.rounded_rectangle([(480, 12), (590, 40)], radius=6, fill='#C9962F')
d1.text((490, 18), "🎤 ON STAGE", fill='#FFFFFF', font=font_bold_sm)

# Low Data Button (active)
d1.rounded_rectangle([(600, 12), (720, 40)], radius=6, fill='#D9622B')
d1.text((608, 18), "📡 Low-Data (44k)", fill='#FFFFFF', font=font_bold_sm)

# Leave Button
d1.rounded_rectangle([(730, 12), (786, 40)], radius=6, fill='#B3261E')
d1.text((742, 18), "Leave", fill='#FFFFFF', font=font_bold_sm)

# 2G Frugal Mode Banner
d1.rounded_rectangle([(160, 64), (640, 92)], radius=14, fill='#D9622B')
d1.text((175, 70), "⚡ 2G Frugal Mode: Video tracks paused to prioritize 40kbps Opus audio", fill='#FFFFFF', font=font_bold_sm)

# Main Stage Area: 2 Video Tiles
# Speaker 1 Tile
d1.rounded_rectangle([(30, 106), (380, 360)], radius=12, fill='#222222', outline='#7A1F1A', width=2)
d1.ellipse([(165, 170), (245, 250)], fill='#7A1F1A')
d1.text((192, 195), "RK", fill='#FFFFFF', font=font_bold_lg)
d1.rounded_rectangle([(45, 318), (260, 348)], radius=6, fill='#111111')
d1.text((55, 324), "🎤 Ravi Kumar (Lead Host)", fill='#FFFFFF', font=font_bold_sm)

# Speaker 2 Tile
d1.rounded_rectangle([(400, 106), (750, 360)], radius=12, fill='#222222', outline='#C9962F', width=2)
d1.ellipse([(535, 170), (615, 250)], fill='#C9962F')
d1.text((562, 195), "PS", fill='#FFFFFF', font=font_bold_lg)
d1.rounded_rectangle([(415, 318), (620, 348)], radius=6, fill='#111111')
d1.text((425, 324), "🎤 Priya Sharma (KLUG Speaker)", fill='#FFFFFF', font=font_bold_sm)

# P2P Mesh Telemetry HUD (Bottom Left)
d1.rounded_rectangle([(30, 375), (340, 465)], radius=8, fill='#1c1511', outline='#C9962F', width=1)
d1.text((42, 382), "🌐 P2P Mesh Telemetry HUD", fill='#C9962F', font=font_bold_sm)
d1.text((42, 403), "Swarm State: 🟢 Active P2P Relay", fill='#55FF55', font=font_regular_xs)
d1.text((42, 421), "Bandwidth Saved: 68.4% (Origin Egress Slashed)", fill='#FFFFFF', font=font_bold_sm)
d1.text((42, 442), "Bitrate: 44.8 kbps (Audio-First) | 5 Peer Nodes", fill='#E4D6C3', font=font_regular_xs)

# Quick Controls Bar (Bottom Center)
d1.rounded_rectangle([(450, 395), (690, 445)], radius=25, fill='#2b211a', outline='#E4D6C3', width=1)
d1.ellipse([(465, 405), (495, 435)], fill='#2E6B3E')
d1.text((475, 412), "🎤", fill='#FFFFFF', font=font_regular_sm)
d1.ellipse([(515, 405), (545, 435)], fill='#B3261E')
d1.text((525, 412), "📷", fill='#FFFFFF', font=font_regular_sm)
d1.ellipse([(565, 405), (595, 435)], fill='#C9962F')
d1.text((575, 412), "✋", fill='#FFFFFF', font=font_regular_sm)
d1.ellipse([(615, 405), (645, 435)], fill='#D9622B')
d1.text((625, 412), "💬", fill='#FFFFFF', font=font_regular_sm)

img1.save('docs/screenshots/figure1_live_stage.png')


# -------------------------------------------------------------
# IMAGE 2: INTERACTIVE SIDEBAR: Q&A, POLLS & CHAT (800 x 480)
# -------------------------------------------------------------
img2 = Image.new('RGB', (800, 480), color='#FFFFFF')
d2 = ImageDraw.Draw(img2)

# Left Side: Live Q&A Queue (width: 390)
d2.rounded_rectangle([(10, 10), (390, 468)], radius=10, fill='#FBF5EA', outline='#E4D6C3', width=1)
d2.text((24, 20), "❓ Live Q&A Stage Queue (3)", fill='#7A1F1A', font=font_bold_md)
d2.text((24, 42), "Real-time upvoting & host moderation", fill='#5C4C3E', font=font_regular_xs)

# Question 1 (Answered)
d2.rounded_rectangle([(24, 65), (376, 175)], radius=8, fill='#F3FBF5', outline='#2E6B3E', width=1)
d2.text((36, 75), "Guntur Volunteer  •  ✔ Answered", fill='#2E6B3E', font=font_bold_sm)
d2.text((36, 95), "How does the 2G low-data mode handle", fill='#2B211A', font=font_regular_sm)
d2.text((36, 115), "packet loss in remote village networks?", fill='#2B211A', font=font_regular_sm)
d2.rounded_rectangle([(36, 140), (145, 165)], radius=12, fill='#D9622B')
d2.text((46, 145), "▲ 14 Upvotes", fill='#FFFFFF', font=font_bold_sm)

# Question 2 (Active from WhatsApp)
d2.rounded_rectangle([(24, 188), (376, 298)], radius=8, fill='#FFFFFF', outline='#E4D6C3', width=1)
d2.text((36, 198), "💬 [WhatsApp from Village Volunteer]", fill='#075e54', font=font_bold_sm)
d2.text((36, 218), "Can we deploy Swecha Vedika on a", fill='#2B211A', font=font_regular_sm)
d2.text((36, 238), "low-cost Raspberry Pi 4 locally?", fill='#2B211A', font=font_regular_sm)
d2.rounded_rectangle([(36, 263), (140, 288)], radius=12, fill='#FAF3E6', outline='#D9622B', width=1)
d2.text((46, 268), "▲ 9 Upvotes", fill='#D9622B', font=font_bold_sm)

# Question 3
d2.rounded_rectangle([(24, 310), (376, 410)], radius=8, fill='#FFFFFF', outline='#E4D6C3', width=1)
d2.text((36, 320), "KLUG Student Contributor", fill='#5C4C3E', font=font_bold_sm)
d2.text((36, 340), "Is the Telugu speech corpus export", fill='#2B211A', font=font_regular_sm)
d2.text((36, 360), "open-weights for Indic AI research?", fill='#2B211A', font=font_regular_sm)
d2.rounded_rectangle([(36, 380), (140, 402)], radius=12, fill='#FAF3E6', outline='#D9622B', width=1)
d2.text((46, 383), "▲ 7 Upvotes", fill='#D9622B', font=font_bold_sm)

# Input Bar
d2.rounded_rectangle([(24, 424), (376, 458)], radius=6, fill='#FFFFFF', outline='#7A1F1A', width=1)
d2.text((36, 432), "Ask live stage question (Telugu/English)...", fill='#888888', font=font_regular_sm)


# Right Side: Live Polls & In-Room Chat (width: 385)
d2.rounded_rectangle([(405, 10), (790, 468)], radius=10, fill='#FBF5EA', outline='#E4D6C3', width=1)
d2.text((420, 20), "📊 Live Community Poll", fill='#7A1F1A', font=font_bold_md)

# Active Poll Card
d2.rounded_rectangle([(420, 50), (775, 240)], radius=8, fill='#FFFFFF', outline='#E4D6C3', width=1)
d2.text((432, 60), "What is your typical village/college speed?", fill='#2B211A', font=font_bold_sm)

# Option 1 (48% - Selected)
d2.rounded_rectangle([(432, 85), (763, 125)], radius=6, fill='#FFEADA', outline='#D9622B', width=1)
d2.rounded_rectangle([(432, 85), (590, 125)], radius=6, fill='#FFCCA8')
d2.text((442, 95), "✔ < 1 Mbps (2G/3G Edge)", fill='#2B211A', font=font_bold_sm)
d2.text((680, 95), "48% (24)", fill='#7A1F1A', font=font_bold_sm)

# Option 2 (36%)
d2.rounded_rectangle([(432, 135), (763, 175)], radius=6, fill='#FFFFFF', outline='#E4D6C3', width=1)
d2.rounded_rectangle([(432, 135), (550, 175)], radius=6, fill='#EFEFEF')
d2.text((442, 145), "1 - 10 Mbps (4G Data)", fill='#2B211A', font=font_regular_sm)
d2.text((680, 145), "36% (18)", fill='#5C4C3E', font=font_bold_sm)

# Option 3 (16%)
d2.rounded_rectangle([(432, 185), (763, 225)], radius=6, fill='#FFFFFF', outline='#E4D6C3', width=1)
d2.rounded_rectangle([(432, 185), (485, 225)], radius=6, fill='#EFEFEF')
d2.text((442, 195), "> 50 Mbps (Fiber / 5G)", fill='#2B211A', font=font_regular_sm)
d2.text((680, 195), "16% (8)", fill='#5C4C3E', font=font_bold_sm)

# Chat & Telugu Reaction Chips
d2.text((420, 255), "💬 Live Chat & Telugu Reactions", fill='#7A1F1A', font=font_bold_md)
d2.rounded_rectangle([(420, 280), (775, 460)], radius=8, fill='#FFFFFF', outline='#E4D6C3', width=1)

# Chat items
d2.text((432, 290), "Sivaram: Switched to 2G Low-Data mode, audio is crystal clear!", fill='#2B211A', font=font_regular_xs)
d2.text((432, 310), "Guntur Volunteer: నమస్కారం! Watching from rural community center.", fill='#7A1F1A', font=font_regular_xs)
d2.text((432, 330), "Host: Welcome all! Polling is active on the right.", fill='#2E6B3E', font=font_regular_xs)

# Quick Telugu Reaction Chips
chips = ["👏 నమస్కారం", "💡 అద్భుతం", "✊ జై స్వేచ్ఛ", "❓ సందేహం", "❤️ ధన్యవాదాలు"]
x_c = 430
for c in chips:
    d2.rounded_rectangle([(x_c, 360), (x_c + 64, 386)], radius=12, fill='#FBF5EA', outline='#D9622B', width=1)
    d2.text((x_c + 6, 366), c, fill='#7A1F1A', font=font_regular_xs)
    x_c += 68

# Chat Input Bar
d2.rounded_rectangle([(430, 400), (765, 442)], radius=6, fill='#FAF7F2', outline='#E4D6C3', width=1)
d2.text((440, 412), "Type message or select Telugu reaction...", fill='#888888', font=font_regular_xs)

img2.save('docs/screenshots/figure2_sidebar_qa_polls.png')


# -------------------------------------------------------------
# IMAGE 3: WHATSAPP BOT CONVERSATIONAL GATEWAY (800 x 480)
# -------------------------------------------------------------
img3 = Image.new('RGB', (800, 480), color='#ECE5DD')
d3 = ImageDraw.Draw(img3)

# Phone Container (centered, width: 440)
x0, x1 = 180, 620
d3.rounded_rectangle([(x0, 0), (x1, 480)], radius=16, fill='#ECE5DD', outline='#CCCCCC', width=2)

# WhatsApp Top Bar
d3.rectangle([(x0, 0), (x1, 58)], fill='#075E54')
d3.ellipse([(x0 + 16, 12), (x0 + 50, 46)], fill='#C9962F')
d3.text((x0 + 26, 18), "🚩", fill='#FFFFFF', font=font_regular_sm)
d3.text((x0 + 60, 12), "Swecha Vedika Official Bot", fill='#FFFFFF', font=font_bold_sm)
d3.text((x0 + 60, 32), "Automated Rural Helpline  •  Online", fill='#D5F0DC', font=font_regular_xs)

# Message 1 (Bot: Greeting)
d3.rounded_rectangle([(x0 + 20, 75), (x0 + 380, 135)], radius=8, fill='#FFFFFF', outline='#E0E0E0', width=1)
d3.text((x0 + 30, 85), "నమస్కారం! Swecha Vedika Helpline.", fill='#000000', font=font_bold_sm)
d3.text((x0 + 30, 105), "Reply EVENTS for upcoming live sessions.", fill='#333333', font=font_regular_xs)

# Message 2 (User: EVENTS)
d3.rounded_rectangle([(x0 + 280, 145), (x0 + 420, 180)], radius=8, fill='#DCF8C6')
d3.text((x0 + 295, 153), "EVENTS", fill='#000000', font=font_bold_sm)

# Message 3 (Bot: Event List)
d3.rounded_rectangle([(x0 + 20, 192), (x0 + 400, 275)], radius=8, fill='#FFFFFF', outline='#E0E0E0', width=1)
d3.text((x0 + 30, 200), "📅 Upcoming Sessions:", fill='#075E54', font=font_bold_sm)
d3.text((x0 + 30, 220), "1. Rural Digital Empowerment (WebRTC 2G)", fill='#000000', font=font_regular_xs)
d3.text((x0 + 30, 240), "Reply: RSVP c71cc603 to register & get link.", fill='#7A1F1A', font=font_bold_sm)

# Message 4 (User: ASK)
d3.rounded_rectangle([(x0 + 100, 290), (x0 + 420, 345)], radius=8, fill='#DCF8C6')
d3.text((x0 + 110, 298), "ASK c71cc603: Can we run this on a", fill='#000000', font=font_regular_xs)
d3.text((x0 + 110, 318), "low-cost Raspberry Pi 4 locally?", fill='#000000', font=font_regular_xs)

# Message 5 (Bot: Confirmation)
d3.rounded_rectangle([(x0 + 20, 360), (x0 + 400, 420)], radius=8, fill='#FFFFFF', outline='#075E54', width=1)
d3.text((x0 + 30, 368), "👍 Question submitted to live stage queue!", fill='#075E54', font=font_bold_sm)
d3.text((x0 + 30, 390), "Speakers will answer live during Q&A.", fill='#333333', font=font_regular_xs)

# WhatsApp Input Bar (Bottom)
d3.rectangle([(x0, 432), (x1, 480)], fill='#F0F0F0')
d3.rounded_rectangle([(x0 + 12, 440), (x1 - 60, 472)], radius=16, fill='#FFFFFF')
d3.text((x0 + 25, 448), "Type message (RSVP, ASK, SUMMARY)...", fill='#888888', font=font_regular_xs)
d3.ellipse([(x1 - 50, 440), (x1 - 18, 472)], fill='#075E54')
d3.text((x1 - 38, 447), "➤", fill='#FFFFFF', font=font_bold_sm)

# Outside Phone Annotations (Left & Right)
d3.text((20, 150), "📱 Zero-Install Mobile Access", fill='#075E54', font=font_bold_md)
d3.text((20, 180), "• Low-literacy volunteer outreach", fill='#2B211A', font=font_regular_sm)
d3.text((20, 205), "• Works on basic 2G mobile data", fill='#2B211A', font=font_regular_sm)
d3.text((20, 230), "• Automated FSM webhook parser", fill='#2B211A', font=font_regular_sm)

d3.text((640, 150), "⚡ Instant Stage Injection", fill='#7A1F1A', font=font_bold_md)
d3.text((640, 180), "• Questions sent over WhatsApp", fill='#2B211A', font=font_regular_sm)
d3.text((640, 205), "• Instantly show on stage Q&A", fill='#2B211A', font=font_regular_sm)
d3.text((640, 230), "• AI summaries returned via SMS", fill='#2B211A', font=font_regular_sm)

img3.save('docs/screenshots/figure3_whatsapp_bot.png')


# -------------------------------------------------------------
# IMAGE 4: SEARCHABLE ARCHIVE & OFFLINE PACK (.ZIP) (800 x 480)
# -------------------------------------------------------------
img4 = Image.new('RGB', (800, 480), color='#FBF5EA')
d4 = ImageDraw.Draw(img4)

# Top Bar
d4.rectangle([(0, 0), (800, 50)], fill='#7A1F1A')
d4.text((20, 14), "🏛️ Swecha Digital Knowledge Archive  •  Bilingual Telugu/English", fill='#FFFFFF', font=font_bold_md)

# Search Bar
d4.rounded_rectangle([(20, 62), (540, 96)], radius=6, fill='#FFFFFF', outline='#E4D6C3', width=1)
d4.text((32, 70), "🔍 Search query: 'WebRTC'  (Matched in Telugu ASR transcript)", fill='#2B211A', font=font_bold_sm)

# Export Corpus Button
d4.rounded_rectangle([(555, 62), (780, 96)], radius=6, fill='#C9962F')
d4.text((568, 71), "📥 Export Telugu Corpus (JSON)", fill='#FFFFFF', font=font_bold_sm)

# Video Player with Synchronized Seeker (width: 440, height: 260)
d4.rounded_rectangle([(20, 110), (460, 360)], radius=8, fill='#000000')
d4.ellipse([(215, 210), (265, 260)], fill='#FFFFFF')
d4.polygon([(233, 223), (233, 247), (253, 235)], fill='#000000')
d4.text((35, 125), "🔴 Synchronized Whisper Video Playback", fill='#FFFFFF', font=font_bold_sm)
d4.text((35, 335), "⏱️ 00:19.0 / 01:25.0  [Seeking to matched segment]", fill='#E4D6C3', font=font_regular_xs)

# Right: Synchronized Whisper Transcript Segments
d4.rounded_rectangle([(475, 110), (780, 360)], radius=8, fill='#FFFFFF', outline='#E4D6C3', width=1)
d4.text((488, 120), "🎙️ Whisper Multilingual Segments", fill='#7A1F1A', font=font_bold_sm)

# Segment 1 (Jump Link)
d4.rounded_rectangle([(488, 145), (768, 205)], radius=6, fill='#FAF7F2', outline='#E4D6C3', width=1)
d4.text((498, 152), "Ravi Kumar (Host)  •  [00:00 - 00:08]", fill='#7A1F1A', font=font_bold_sm)
d4.text((498, 172), "అందరికీ నమస్కారం! స్వేచ్ఛ వేదిక ఈరోజు వెబినార్‌కి స్వాగతం.", fill='#2B211A', font=font_regular_xs)

# Segment 2 (Active Matched Segment)
d4.rounded_rectangle([(488, 215), (768, 285)], radius=6, fill='#FFEADA', outline='#D9622B', width=2)
d4.text((498, 222), "Priya Sharma (Speaker)  •  [00:19 - 00:28]  ✔ Active", fill='#D9622B', font=font_bold_sm)
d4.text((498, 242), "WebRTC పీర్-టు-పీర్ మెష్ ద్వారా మనం సర్వర్ భారాన్ని", fill='#2B211A', font=font_regular_xs)
d4.text((498, 260), "70 శాతం తగ్గించవచ్చు (Bandwidth saved).", fill='#2B211A', font=font_regular_xs)

# Segment 3
d4.rounded_rectangle([(488, 295), (768, 350)], radius=6, fill='#FAF7F2', outline='#E4D6C3', width=1)
d4.text((498, 302), "Priya Sharma (English)  •  [00:29 - 00:39]", fill='#5C4C3E', font=font_bold_sm)
d4.text((498, 322), "Low-data mode operates seamlessly under 50 kbps.", fill='#2B211A', font=font_regular_xs)

# Bottom: Offline Pack (.zip) Feature Ribbon
d4.rounded_rectangle([(20, 375), (780, 465)], radius=8, fill='#FFFFFF', outline='#2E6B3E', width=2)
d4.rounded_rectangle([(35, 395), (280, 445)], radius=6, fill='#2E6B3E')
d4.text((48, 410), "📦 Download Offline Pack (.zip)", fill='#FFFFFF', font=font_bold_md)

d4.text((300, 395), "Self-Contained Offline Learning Bundle for Rural Classrooms", fill='#7A1F1A', font=font_bold_sm)
d4.text((300, 415), "• Bundles standalone zero-dependency index.html reader (works 100% offline)", fill='#2B211A', font=font_regular_xs)
d4.text((300, 435), "• Includes Markdown summary, JSON transcript, and audio segments on USB flash drives", fill='#5C4C3E', font=font_regular_xs)

img4.save('docs/screenshots/figure4_archive_offline.png')

print("All 4 UI screenshot graphics generated successfully!")
