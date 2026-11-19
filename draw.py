import os
import sys
from PIL import Image, ImageDraw, ImageFont

WIDTH = 1024
HEIGHT = 1024

# Palette (RGB)
PAPER = (247, 243, 232)
CARD = (255, 253, 246)
INK = (22, 28, 26)
GREY = (104, 100, 90)
ACCENT = (27, 78, 66)
TEAL = (44, 96, 88)
NAVY = (38, 58, 92)
BORDER = (196, 190, 176)
DATE_RED = (172, 62, 44)

CONTINENT_COLORS = {
    "Americas": (168, 62, 44),
    "Europe": (58, 84, 128),
    "Mideast": (186, 122, 38),
    "Africa": (122, 106, 52),
    "Asia": (116, 80, 148),
    "Oceania": (44, 124, 134),
}

# Fonts
FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
font_serif_bold_path = os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf")
font_serif_path = os.path.join(FONT_DIR, "DejaVuSerif.ttf")
font_serif_italic_path = os.path.join(FONT_DIR, "DejaVuSerif-Italic.ttf")
if not os.path.exists(font_serif_italic_path):
    font_serif_italic_path = font_serif_path
font_sans_bold_path = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")
font_sans_path = os.path.join(FONT_DIR, "DejaVuSans.ttf")

def get_font(path, size):
    return ImageFont.truetype(path, size)

STORIES_FEATURED = [
    {
        "n": 1,
        "kick": "IRAN · GULF",
        "head": "Iran strikes back; US hits Qeshm",
        "summ": "US jets hit an IRGC site on Qeshm; Iran answered on Kuwait and Bahrain - Bahrain says it intercepted several.",
        "kind": "missiles over a gulf coastline",
        "continent": "Mideast",
        "tag": "STRIKES ON BOTH SIDES",
        "tag_color": ACCENT,
        "chip": "CONFIRMED · REUTERS/AP",
        "lon": 51.5, "lat": 26.5
    },
    {
        "n": 2,
        "kick": "ASIA · APEC SUMMIT",
        "head": "Xi and Putin meet in Shenzhen",
        "summ": "The two denounce protectionism and Western sanctions; the first Trump-Xi-Putin trilateral is set for Thursday.",
        "kind": "two flags over a skyline",
        "continent": "Asia",
        "tag": "THREE-WAY ON THURSDAY",
        "tag_color": NAVY,
        "chip": "CONFIRMED · JUST SECURITY",
        "lon": 114.0, "lat": 22.5
    },
    {
        "n": 3,
        "kick": "ASIA · QUAD",
        "head": "Quad meets; Trump lands in Manila",
        "summ": "First leader-level Quad meeting in 2+ years; Trump meets Marcos Jr. and announces a Philippines trade deal.",
        "kind": "four flags over a harbour",
        "continent": "Asia",
        "tag": "MANILA FIRST",
        "tag_color": (16, 22, 34),
        "chip": "CONFIRMED · OPENCHRONICLE",
        "lon": 121.0, "lat": 14.6
    },
]

STORIES_GRID = [
    {"n": 4, "kick": "UKRAINE · WAR", "head": "Russia fires 141 drones; 126 downed", "summ": "Overnight barrage, hits at 7 sites.", "kind": "drones", "continent": "Europe", "chip": "CLAIM · KYIV", "lon": 30.5, "lat": 50.4},
    {"n": 5, "kick": "EUROPE · UKRAINE AID", "head": "EU proposes a 45bn-euro Ukraine loan", "summ": "25bn military, 20bn budget for 2027.", "kind": "euro", "continent": "Europe", "chip": "CONFIRMED · REUTERS", "lon": 4.35, "lat": 50.85},
    {"n": 6, "kick": "US · MARKETS", "head": "Fed minutes back more hikes; Dow -561", "summ": "S and P 500 -0.23%, Nasdaq +0.42%.", "kind": "dow", "continent": "Americas", "chip": "CONFIRMED · REUTERS", "lon": -74.0, "lat": 40.7},
    {"n": 7, "kick": "MARKETS · GOLD", "head": "Gold sinks to a 14-month low", "summ": "Closed $3,725 an ounce, down 3.2%.", "kind": "gold", "continent": "Europe", "chip": "CONFIRMED · REUTERS", "lon": -0.1, "lat": 51.5},
    {"n": 8, "kick": "TECH · IPO", "head": "Anthropic prices IPO at $83", "summ": "Raising $81.3bn - a record listing.", "kind": "ipo", "continent": "Americas", "chip": "CONFIRMED · REUTERS", "lon": -122.4, "lat": 37.8},
    {"n": 9, "kick": "SCIENCE · SPACE", "head": "Voyager 1 reaches one light-day", "summ": "First human-made object to do so.", "kind": "voyager", "continent": "Americas", "chip": "CONFIRMED · NASA JPL", "lon": -118.1, "lat": 34.1},
    {"n": 10, "kick": "AMERICAS · HEALTH", "head": "US loses measles-free status after 26 years", "summ": "PAHO: endemic again; 5,412 cases in 2026.", "kind": "measles", "continent": "Americas", "chip": "CONFIRMED · PAHO", "lon": -98.0, "lat": 39.0},
    {"n": 11, "kick": "AFRICA · HEALTH", "head": "Ebola passes 11,000 cases in DR Congo", "summ": "More than doubled in three months.", "kind": "ebola", "continent": "Africa", "chip": "CONFIRMED · WHO", "lon": 23.0, "lat": -2.0},
    {"n": 12, "kick": "INDIA · WEATHER", "head": "Cyclone Akvan bears down on Odisha", "summ": "Severe storm; landfall expected ~20 Nov.", "kind": "cyclone", "continent": "Asia", "chip": "CONFIRMED · IMD", "lon": 86.0, "lat": 19.0},
    {"n": 13, "kick": "PACIFIC · WEATHER", "head": "Cyclone Xavier hits Category 5", "summ": "Briefly Cat 5 over the Cook Islands.", "kind": "xavier", "continent": "Oceania", "chip": "CONFIRMED · FIJI MET", "lon": -160.0, "lat": -15.0},
    {"n": 14, "kick": "GAZA · WAR", "head": "Israeli tanks cross Yellow Line at Nuseirat", "summ": "First such raid since the truce.", "kind": "gaza", "continent": "Mideast", "chip": "CONFIRMED · REUTERS", "lon": 34.4, "lat": 31.45},
    {"n": 15, "kick": "US · POLITICS", "head": "Jeffries wins Democrats' Speaker nod", "summ": "251-11; full House vote set for 3 January.", "kind": "vote", "continent": "Americas", "chip": "CONFIRMED · AP", "lon": -77.0, "lat": 38.9},
]

BRIEFS_DATA = [
    (16, "Houthis fire five drones at two pumping stations on Saudi pipeline", "Mideast", (46.7, 24.6, 0, 6)),
    (17, "Gaza winter: WHO counts 950,000 displaced on flood-prone ground", "Mideast", (34.3, 31.4, 6, 12)),
    (18, "Louvre workers vote to extend strike over staffing and the jewel heist", "Europe", (2.35, 48.9, -12, -4)),
    (19, "ASHA health workers' strike enters second day in Karnataka", "Asia", (77.6, 13.0, 8, 4)),
    (20, "Maharashtra court staff call off strike after talks with judges", "Asia", (72.8, 19.1, -8, -8)),
    (21, "Magnitude 6.0 quake off Peru's Ica region; tsunami ruled out", "Americas", (-75.4, -15.4, 0, 4)),
    (22, "Ghana's new $60m presidential jet sparks public outrage", "Africa", (-0.2, 5.6, 0, 6)),
    (23, "Nigeria's central bank and NNPC sign forex and energy deal", "Africa", (7.5, 9.1, 8, -4)),
    (24, "Malaysia Q3 GDP beats forecasts at 5.5%; AI boom to drive 2027", "Asia", (101.7, 3.1, 2, 10)),
    (25, "Fed's Waller calls for more aggressive inflation response", "Americas", (-77.0, 38.9, 10, 10)),
    (26, "UK inflation rises to 3.6%, highest in a year, on fuel prices", "Europe", (-0.1, 51.5, 10, 8)),
    (27, "Amnesty: RSF drone strikes in El Obeid killed 37 civilians", "Africa", (30.2, 13.2, 0, 6)),
    (28, "Bangladesh garment unrest: ~535 factories hit, ~300 arrested", "Asia", (90.4, 23.8, 8, -6)),
    (29, "GTA VI rolls out to rave reviews, Metacritic 99, ahead of launch", "Americas", (-74.0, 40.7, 12, 8)),
    (30, "Quake felt in Bucharest; EMSC 5.3, Romania's institute 5.7", "Europe", (26.1, 44.4, -6, -10)),
    (31, "Magnitude 4.1 quake strikes southwest Kuwait; no damage", "Mideast", (47.5, 29.3, 10, -6)),
    (32, "Migrant boat capsizes off Senegal, at least one dead", "Africa", (-17.4, 14.7, 0, -8)),
    (33, "Hegseth makes surprise Caracas trip, signs defence partnership", "Americas", (-66.9, 10.5, 0, -6)),
    (34, "Brazil Senate approves Lula's $10bn fiscal package", "Americas", (-47.9, -15.8, 0, 4)),
    (35, "Sheinbaum says Mexico-US trade talks 'very far along'", "Americas", (-99.1, 19.4, 0, -8)),
    (36, "Ethiopia and Eritrea mass troops near Badme; war fears rise", "Africa", (37.9, 14.7, -8, 4)),
    (37, "Tame Impala wins seven ARIAs, Album of the Year for Deadbeat", "Oceania", (151.2, -33.9, 0, -6)),
    (38, "Alcaraz beats Medvedev 6-2, 6-4 at ATP Finals, into semis", "Europe", (7.7, 45.1, 8, -12)),
    (39, "ECDC warns superbug infections surged; Klebsiella up 72% since 2019", "Europe", (18.1, 59.3, -6, -8)),
    (40, "Pew projects Islam will pass Christianity as largest religion by 2035", "Americas", (-77.0, 38.9, -2, 14)),
    (41, "Brent crude settles $91.95 a barrel, down $1.19 (-1.28%)", "Europe", (-0.1, 51.5, -2, -12)),
    (42, "Chelsea Women beat PSG 1-0, Buurman 87th-minute winner", "Europe", (-0.1, 51.5, 10, 14)),
    (43, "Japan exports hit record 11.8tn yen in Oct, +20.5%", "Asia", (139.7, 35.7, 0, -6)),
    (44, "Japan Oct visitors hit record 3.91m despite China arrivals -47%", "Asia", (139.7, 35.7, 12, -8)),
    (45, "Australia wages +1.1% in Sep quarter, fastest since Dec 2023", "Oceania", (149.1, -35.3, 0, -6)),
    (46, "EU Council authorises signing EU-Indonesia trade deal", "Europe", (4.35, 50.85, 12, 6)),
    (47, "COP31 launches second Global Stocktake; 21 issues unresolved", "Mideast", (30.7, 36.9, 4, -10)),
    (48, "Ella Langley wins record six CMAs, incl. Entertainer of the Year", "Americas", (-86.8, 36.2, 0, -6)),
    (49, "National Book Awards: Assadi fiction, ElGendy nonfiction", "Americas", (-74.0, 40.7, -12, 12)),
    (50, "First Ivors Composer Awards: Pemberton Composer of the Year", "Europe", (-0.1, 51.5, -10, -12)),
    (51, "Fiji declares state of disaster over El Nino drought", "Oceania", (178.4, -17.7, 0, -6)),
    (52, "Ruto gives State of the Nation address, unveils tax relief", "Africa", (36.8, -1.3, 0, -6)),
    (53, "Trump asks Supreme Court to block Venezuelan TPS restoration", "Americas", (-77.0, 38.9, 14, -4)),
    (54, "Qonto granted French/ECB banking licence", "Europe", (2.35, 48.9, 12, 10)),
    (55, "Cassava seeks $1bn to buy Nvidia chips for African AI centres", "Africa", (31.0, -17.8, 0, 4)),
]

TIMELINE_DATA = [
    ("Overnight", "Russia fires 141 drones at Ukraine"),
    ("Before dawn", "Iran strikes Kuwait & Bahrain bases"),
    ("Asia daytime", "Xi-Putin summit; Quad meets in Manila"),
    ("10:16 UTC", "Voyager 1 reaches one light-day"),
    ("~19:00 UTC", "Fed minutes point to more hikes"),
    ("Evening", "Dow closes -561 on rate fears"),
]

DATE_CHECK_TEXT = "Left out on purpose - they broke on other days: the An-12 crash in Siberia, 19 killed (Tue 17 Nov) - Peltola's Alaska Senate call (Tue 17 Nov) - the Knesset speaker vote, Kahana 66-52 (Tue 17 Nov) - the Crimea Bridge collapse (overnight 16-17 Nov) - Nvidia's results (17 Nov). Not yet: the ICJ Rohingya judgment is due Thu 19 Nov."

LAND_POLYGONS = [
    # North America
    [(-168, 66), (-162, 71), (-140, 70), (-120, 71), (-95, 72),
     (-80, 70), (-60, 60), (-53, 47), (-66, 44), (-70, 41), (-75, 35),
     (-81, 25), (-84, 30), (-90, 29), (-97, 26), (-95, 18), (-87, 21),
     (-83, 9), (-79, 8), (-86, 15), (-92, 16), (-105, 20), (-115, 30),
     (-124, 40), (-125, 49), (-135, 58), (-150, 60)],
    # Greenland
    [(-55, 60), (-45, 60), (-20, 70), (-20, 82), (-45, 84), (-60, 76)],
    # South America
    [(-79, 9), (-75, 11), (-72, 12), (-68, 11.8), (-64, 10.8),
     (-62, 10), (-52, 5), (-50, 0), (-44, -2), (-35, -6), (-37, -10),
     (-38, -13), (-40, -20), (-40, -23), (-44, -23), (-48, -25),
     (-53, -34), (-58, -38), (-62, -40), (-65, -45), (-68, -50),
     (-68, -55), (-73, -53), (-75, -46), (-73, -37), (-71, -30),
     (-70, -18), (-71, -16), (-75, -14), (-77, -12), (-79, -6),
     (-81, -2), (-80, 1), (-78, 7)],
    # Eurasia
    [(-9, 37), (-9, 43), (-2, 48), (4, 52), (8, 58), (10, 57.5),
     (16, 58), (18, 59.5), (20, 60), (22, 66), (28, 71), (40, 70),
     (70, 74), (100, 78), (140, 73), (160, 70), (170, 66), (179, 65),
     (179, 60), (160, 58), (142, 52), (140, 44), (132, 46), (130, 42),
     (129, 38), (128, 38), (126, 38), (126, 35), (126, 34), (124, 35),
     (122, 30), (120, 25), (118, 24), (116.5, 24), (115.5, 23.2),
     (114.0, 22.0), (112.5, 21.2), (110, 20), (108, 18), (105, 10),
     (103, 1), (100, 6), (98, 12), (94, 16), (90, 22), (88, 22),
     (80, 8), (72, 18), (66, 25), (60, 25), (57, 22), (52, 17),
     (43, 12), (39, 20), (35, 28), (34, 31), (36, 36), (34, 36.5),
     (31, 36.5), (29, 37), (26, 38), (23, 38), (20, 40), (16, 41.5),
     (18, 40), (16, 38), (14, 40), (13, 45), (12, 45), (8, 44),
     (3, 43), (0, 38.5), (-6, 36), (-9, 37)],
    # Africa
    [(-17.6, 14.7), (-16, 21), (-10, 28), (0, 36.5), (10, 37.5),
     (20, 33), (32, 31), (35, 23), (43, 12), (51, 11), (48, 0),
     (41, -10), (35, -20), (32, -27), (26, -34), (20, -35),
     (18, -34.5), (15, -28), (12, -18), (9, -1), (3, 5), (-8, 4),
     (-13, 8)],
    # Australia
    [(114, -22), (113, -26), (115, -34), (129, -32), (138, -35),
     (146, -39), (150, -38), (152, -32), (153, -28), (146, -19),
     (142, -11), (132, -11), (126, -14), (122, -18)],
    # British Isles
    [(-6, 50), (-6, 58), (-2, 58), (0, 53), (1, 51), (-2, 50)],
    # Iceland
    [(-24, 63.5), (-13, 64.5), (-14, 66.5), (-22, 66.5)],
    # Japan
    [(130, 32), (133, 34), (136, 35), (139, 35), (141, 36), (142, 39),
     (141, 41), (143, 44), (145, 43), (142, 40), (139, 36), (136, 35),
     (133, 34), (131, 33)],
    # Philippines
    [(120, 18), (124, 18), (126, 10), (122, 6), (120, 10)],
    # Indonesia / PNG
    [(95, 5), (105, 5), (115, 2), (120, -2), (130, -3), (140, -4),
     (140, -8), (120, -9), (114, -8.5), (105, -8), (105, -6),
     (100, -3), (100, 0)],
    # Madagascar
    [(44, -13), (50, -14), (50, -25), (45, -25), (43, -19)],
    # New Zealand
    [(172, -34), (178, -37), (176, -41), (173, -43), (167, -46),
     (170, -43), (172, -37)],
    # Fiji
    [(177, -16), (180, -17), (180, -19), (177, -19)],
    # Cook Islands
    [(-161, -20), (-159, -20), (-159, -22), (-161, -22)],
    # Cuba / Caribbean
    [(-84, 22.5), (-74, 20), (-77, 23.5), (-84, 23.5)],
    # Sri Lanka
    [(80, 6), (82, 7), (82, 9), (80, 9)],
    # Italy
    [(6, 44), (10, 46), (13, 46), (13, 44), (16, 41.5), (18, 40),
     (16, 38), (15.5, 38), (13, 41), (12, 42), (10, 43), (8, 44)],
    # Korea
    [(124, 38.5), (127, 38.5), (129, 38), (129, 35), (126, 34), (125, 36)],
    # Tasmania
    [(145, -41), (148, -41), (148, -43), (145, -43)],
]

clip_failures = 0
text_clip_failures = []
text_blocks_checked = 0

def wrap(text, font, max_width, draw):
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        test_line = " ".join(current_line + [word])
        if draw.textlength(test_line, font=font) <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
                current_line = [word]
            else:
                lines.append(word)
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def block(draw, text, font, x, top, max_width, line_h, bottom_limit):
    lines = wrap(text, font, max_width, draw)
    assert " ".join(lines) == " ".join(text.split()), f"wrap() altered text: {text!r}"
    y = top
    drawn = 0
    for line in lines:
        bbox = draw.textbbox((x, y), line, font=font)
        if bbox[3] > bottom_limit:
            break
        draw.text((x, y), line, font=font, fill=INK)
        drawn += 1
        y += line_h
    remainder = " ".join(lines[drawn:])
    complete = (drawn == len(lines)) and (remainder == "")
    return complete, remainder, y

def check_block(label, complete, remainder):
    global text_blocks_checked
    text_blocks_checked += 1
    if not complete:
        text_clip_failures.append((label, remainder))

def chip(draw, cx, cy, r, n, fill):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill)
    f_size = max(7, int(r * 1.12))
    font = get_font(font_sans_bold_path, f_size)
    text = str(n)
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((cx - tw/2 - bbox[0], cy - th/2 - bbox[1]), text, font=font, fill=(255, 255, 255))

def source_chip_featured(draw, x, fy, text):
    font = get_font(font_sans_bold_path, 8)
    bbox = draw.textbbox((0, 0), text, font=font)
    pw = (bbox[2] - bbox[0]) + 14
    chip_x1 = x + 309 - pw
    chip_y1 = fy + 78
    chip_x2 = x + 309
    chip_y2 = fy + 94
    draw.rounded_rectangle([chip_x1, chip_y1, chip_x2, chip_y2], radius=7, fill=(90, 88, 80))
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    cx = chip_x1 + pw / 2
    cy = chip_y1 + 8
    draw.text((cx - tw/2 - bbox[0], cy - th/2 - bbox[1]), text, font=font, fill=(255, 255, 255))

def source_chip_grid(draw, x, y0, text):
    font = get_font(font_sans_bold_path, 7)
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    rx = x + 230
    ry = y0 + 41
    color = DATE_RED if text.startswith("CLAIM") else GREY
    draw.text((rx - tw - bbox[0], ry - th/2 - bbox[1]), text, font=font, fill=color)

def draw_banner(draw, x, y, w, h, kind, continent_color):
    muted_bg = (230, 240, 236)
    draw.rectangle([x, y, x + w, y + h], fill=muted_bg)
    c1 = ACCENT
    c2 = continent_color
    if "missile" in kind or "drone" in kind or "tank" in kind or "cyclone" in kind or "wave" in kind:
        for i in range(4):
            dx = x + 20 + i * 50
            y_top = max(y + 2, y + 6)
            y_bot = min(y + h - 2, y + h - 6)
            if y_bot > y_top:
                draw.line([dx, y_bot, dx + 25, y_top], fill=c1, width=2)
                draw.polygon([dx+20, y_top+2, dx+30, y_top, dx+25, y_top+8], fill=c2)
    elif "skyline" in kind or "harbour" in kind or "gavel" in kind or "podium" in kind or "ipo" in kind:
        for i in range(5):
            bw = 18
            bh = max(5, min(int(h - 6), 10 + (i * 9) % 30))
            bx = x + 12 + i * 45
            by = y + h - bh
            draw.rectangle([bx, by, bx + bw, y + h], fill=c1 if i % 2 == 0 else c2)
    elif "flag" in kind or "eu" in kind or "aid" in kind or "gold" in kind or "voyager" in kind or "measles" in kind or "health" in kind:
        dh = max(4, h - 10)
        draw.rectangle([x + 20, y + 5, x + 70, y + 5 + dh], fill=c1)
        draw.rectangle([x + 80, y + 5, x + 130, y + 5 + dh], fill=c2)
        if h > 20:
            draw.ellipse([x + 140, y + 5, x + min(w - 10, x + 180), y + h - 5], fill=c1)
    else:
        for i in range(3):
            rx = x + 20 + i * 70
            ry = y + h // 2
            r_val = max(3, min(10, h // 3))
            if ry - r_val < ry + r_val:
                draw.ellipse([rx, ry - r_val, rx + 2*r_val, ry + r_val], outline=c1, width=2)

def main():
    global clip_failures, text_blocks_checked
    clip_failures = 0
    text_blocks_checked = 0
    text_clip_failures.clear()
    img = Image.new("RGB", (WIDTH, HEIGHT), PAPER)
    draw = ImageDraw.Draw(img)

    drawn_numbers = set()

    # 1. Masthead
    font_top_left = get_font(font_sans_bold_path, 12.5)
    font_top_right = get_font(font_sans_bold_path, 12.5)
    draw.text((24, 3), "THE WORLD'S NEWS IN ONE PICTURE", font=font_top_left, fill=ACCENT)

    right_text = "55 STORIES - ONE PAGE"
    bbox = draw.textbbox((0, 0), right_text, font=font_top_right)
    rw = bbox[2] - bbox[0]
    draw.text((1000 - rw, 3), right_text, font=font_top_right, fill=INK)

    title_size = 54
    font_title = get_font(font_serif_bold_path, title_size)
    while draw.textlength("THE DAILY ATLAS", font=font_title) > 900 and title_size > 40:
        title_size -= 2
        font_title = get_font(font_serif_bold_path, title_size)

    draw.text((512, 13), "THE DAILY ATLAS", font=font_title, fill=INK, anchor="ma")

    r1 = 13 + title_size + 6
    draw.line([24, r1, 1000, r1], fill=ACCENT, width=3)
    draw.line([24, r1 + 5, 1000, r1 + 5], fill=ACCENT, width=1)

    dy = r1 + 9
    font_date = get_font(font_serif_bold_path, 21)
    draw.text((512, dy), "Wednesday 18 November 2026", font=font_date, fill=ACCENT, anchor="ma")

    sy = dy + 27
    font_sub_left = get_font(font_sans_path, 10.5)
    font_sub_right = get_font(font_sans_bold_path, 11)
    draw.text((24, sy), "EVERY STORY REPORTED ON THE DAY", font=font_sub_left, fill=GREY)

    sub_right_text = "WEDNESDAY EDITION - NO. 18"
    bbox = draw.textbbox((0, 0), sub_right_text, font=font_sub_right)
    srw = bbox[2] - bbox[0]
    draw.text((1000 - srw, sy), sub_right_text, font=font_sub_right, fill=INK)

    # 2. UTC timeline strip (NEW device 1)
    tl_y = sy + 13
    draw.rectangle([24, tl_y, 1000, tl_y + 46], fill=CARD, outline=BORDER, width=1)
    draw.rectangle([24, tl_y, 24 + 62, tl_y + 46], fill=ACCENT)
    font_tl_label = get_font(font_sans_bold_path, 10)
    draw.text((55, tl_y + 13), "THE DAY", font=font_tl_label, fill=(255, 255, 255), anchor="ma")
    draw.text((55, tl_y + 26), "IN UTC", font=font_tl_label, fill=(255, 255, 255), anchor="ma")

    seg_w = 914 / 6.0
    font_seg_lbl = get_font(font_sans_bold_path, 10)
    font_seg_txt = get_font(font_sans_path, 8.5)

    timeline_segments_drawn = 0
    for seg_idx, (seg_title, seg_desc) in enumerate(TIMELINE_DATA):
        seg_x0 = 24 + 62 + seg_idx * seg_w
        if seg_idx > 0:
            draw.line([seg_x0, tl_y + 5, seg_x0, tl_y + 41], fill=BORDER, width=1)

        draw.text((seg_x0 + 8, tl_y + 4), seg_title, font=font_seg_lbl, fill=ACCENT)
        desc_lines = wrap(seg_desc, font_seg_txt, seg_w - 14, draw)
        dy_txt = tl_y + 19
        for line in desc_lines:
            bbox = draw.textbbox((seg_x0 + 8, dy_txt), line, font=font_seg_txt)
            if bbox[3] > tl_y + 46:
                clip_failures += 1
            draw.text((seg_x0 + 8, dy_txt), line, font=font_seg_txt, fill=INK)
            dy_txt += 10
        timeline_segments_drawn += 1

    # 3. Featured row (three cards, each 317 wide, 162 high)
    fy = tl_y + 54
    font_kicker_feat = get_font(font_sans_bold_path, 12)
    font_kicker_feat_sm = get_font(font_sans_bold_path, 10.5)
    font_head_feat = get_font(font_serif_bold_path, 17)
    font_summ_feat = get_font(font_serif_path, 9.5)

    for i, story in enumerate(STORIES_FEATURED):
        x = 24 + i * 329
        w = 317
        h = 162
        draw.rectangle([x, fy, x + w, fy + h], fill=CARD, outline=BORDER, width=1)

        banner_h = 74
        c_color = CONTINENT_COLORS.get(story["continent"], ACCENT)
        draw_banner(draw, x, fy, w, banner_h, story["kind"], c_color)

        tag_y = fy + 48
        tag_col = story["tag_color"]
        draw.rectangle([x, tag_y, x + w, fy + 74], fill=tag_col)
        strip_col = INK if tag_col == ACCENT else ACCENT
        draw.rectangle([x, tag_y, x + 5, fy + 74], fill=strip_col)
        draw.text((x + 14, fy + 61), story["tag"], font=font_kicker_feat, fill=(255, 255, 255), anchor="lm")

        chip_cy = fy + 86
        chip(draw, x + 18, chip_cy, 9.5, story["n"], ACCENT)
        drawn_numbers.add(story["n"])

        draw.text((x + 34, chip_cy), story["kick"], font=font_kicker_feat_sm, fill=ACCENT, anchor="lm")
        source_chip_featured(draw, x, fy, story["chip"])

        head_y = fy + 96
        h_ok, h_rem, head_next = block(
            draw, story["head"], font_head_feat, x + 10, head_y, 297, 18,
            fy + 133)
        check_block(f"featured #{story['n']} headline", h_ok, h_rem)

        summ_y = max(head_next + 2, fy + 135)
        s_ok, s_rem, _ = block(
            draw, story["summ"], font_summ_feat, x + 10, summ_y, 297, 11.5,
            fy + 160)
        check_block(f"featured #{story['n']} summary", s_ok, s_rem)

    feat_bottom = fy + 162

    # 4. Grid (12 cards, 4 cols x 3 rows; card 238 wide, 84 high)
    grid_rule_y = feat_bottom + 8
    draw.line([24, grid_rule_y, 1000, grid_rule_y], fill=INK, width=1)

    gy = feat_bottom + 16
    row_pitch = 92

    font_kicker_grid = get_font(font_sans_bold_path, 8)
    font_head_grid = get_font(font_serif_bold_path, 12)
    font_summ_grid = get_font(font_serif_path, 8.5)

    for idx, story in enumerate(STORIES_GRID):
        col = idx % 4
        row = idx // 4
        x = 24 + col * 246
        y0 = gy + row * row_pitch
        w = 238
        h = 84

        draw.rectangle([x, y0, x + w, y0 + h], fill=CARD, outline=BORDER, width=1)

        banner_h = 34
        c_color = CONTINENT_COLORS.get(story["continent"], ACCENT)
        draw_banner(draw, x, y0, w, banner_h, story["kind"], c_color)

        chip_cy = y0 + 41
        chip(draw, x + 13, chip_cy, 6, story["n"], ACCENT)
        drawn_numbers.add(story["n"])

        draw.text((x + 24, chip_cy), story["kick"], font=font_kicker_grid, fill=ACCENT, anchor="lm")
        source_chip_grid(draw, x, y0, story["chip"])

        head_y = y0 + 46
        h_ok, h_rem, head_next = block(
            draw, story["head"], font_head_grid, x + 8, head_y, 222, 11.5,
            y0 + 74)
        check_block(f"grid #{story['n']} headline", h_ok, h_rem)

        summ_y = head_next + 1
        s_ok, s_rem, _ = block(
            draw, story["summ"], font_summ_grid, x + 8, summ_y, 222, 9.5,
            y0 + 83)
        check_block(f"grid #{story['n']} summary", s_ok, s_rem)

    grid_bottom = gy + 3 * row_pitch - (row_pitch - 84)

    # 5. Bottom Band
    by = gy + 3 * 84 + 2 * 8 + 12
    draw.line([24, by, 1000, by], fill=INK, width=1)
    hy = by + 8

    font_head_left = get_font(font_sans_bold_path, 12)
    font_head_right = get_font(font_sans_bold_path, 12)
    draw.text((24, hy), "ALSO ON WEDNESDAY 18 NOVEMBER", font=font_head_left, fill=INK)
    draw.text((700, hy), "WHERE IT HAPPENED", font=font_head_right, fill=ACCENT)

    # Legend centred on x=512 in header row
    font_legend = get_font(font_sans_path, 8.5)
    legend_items = list(CONTINENT_COLORS.items())
    dummy_img = Image.new("RGB", (10, 10))
    dummy_draw = ImageDraw.Draw(dummy_img)
    total_legend_w = 0
    for c_name, c_col in legend_items:
        tb = dummy_draw.textbbox((0, 0), c_name, font=font_legend)
        total_legend_w += 9 + (tb[2] - tb[0]) + 16
    total_legend_w -= 16
    leg_x = 512 - total_legend_w / 2
    for c_name, c_col in legend_items:
        draw.rectangle([leg_x, hy + 4, leg_x + 7, hy + 11], fill=c_col)
        tb = draw.textbbox((0, 0), c_name, font=font_legend)
        tw = tb[2] - tb[0]
        draw.text((leg_x + 10, hy + 2), c_name, font=font_legend, fill=INK)
        leg_x += 9 + tw + 16

    briefs_start_y = hy + 22

    # Auto-fit briefs layout
    col_width = 150
    col_lefts = [24, 196, 368, 540]

    partitions = []
    for c1 in range(8, 13):
        for c2 in range(8, 13):
            for c3 in range(8, 13):
                c4 = 40 - (c1 + c2 + c3)
                if 8 <= c4 <= 12:
                    partitions.append((c1, c2, c3, c4))

    font_sizes = [9.5, 9.25, 9.0, 8.75, 8.5, 8.25, 8.0]
    best_layout = None

    for f_size in font_sizes:
        f_reg = get_font(font_sans_path, f_size)
        f_bld = get_font(font_sans_bold_path, f_size)
        line_h = f_size + 2.0

        for part in partitions:
            max_h = 0
            curr_idx = 0
            for count in part:
                col_items = BRIEFS_DATA[curr_idx : curr_idx + count]
                curr_idx += count
                col_h = 0
                for b_num, b_text, _, _ in col_items:
                    full_text = f"{b_num}. {b_text}"
                    lines = wrap(full_text, f_reg, col_width, draw)
                    col_h += len(lines) * line_h + 2.0
                if col_h > max_h:
                    max_h = col_h
            if briefs_start_y + max_h <= 930:
                best_layout = (f_size, part, max_h)
                break
        if best_layout:
            break

    if not best_layout:
        best_layout = (8.0, (10, 10, 10, 10), 0)

    chosen_size, chosen_part, band_h = best_layout
    f_reg = get_font(font_sans_path, chosen_size)
    f_bld = get_font(font_sans_bold_path, chosen_size)
    line_h = chosen_size + 2.0

    curr_idx = 0
    for c_idx, count in enumerate(chosen_part):
        col_x = col_lefts[c_idx]
        col_items = BRIEFS_DATA[curr_idx : curr_idx + count]
        curr_idx += count
        curr_y = briefs_start_y
        for b_num, b_text, b_cont, b_coord in col_items:
            drawn_numbers.add(b_num)
            num_str = f"{b_num}. "
            full_text = f"{b_num}. {b_text}"
            lines = wrap(full_text, f_reg, col_width, draw)
            for line_idx, line in enumerate(lines):
                if curr_y + line_h > 930:
                    clip_failures += 1
                if line_idx == 0:
                    draw.text((col_x, curr_y), num_str, font=f_bld, fill=INK)
                    num_w = draw.textlength(num_str, font=f_bld)
                    rest_text = line[len(num_str):]
                    draw.text((col_x + num_w, curr_y), rest_text, font=f_reg, fill=INK)
                else:
                    draw.text((col_x, curr_y), line, font=f_reg, fill=INK)
                curr_y += line_h
            curr_y += 1.0
            draw.line([col_x, curr_y, col_x + col_width, curr_y], fill=(225, 220, 210), width=1)
            curr_y += 1.0

    map_x = 700
    map_y = briefs_start_y
    map_w = 300
    map_h = int(band_h)

    draw.rectangle([map_x, map_y, map_x + map_w, map_y + map_h], fill=CARD, outline=BORDER, width=1)

    def lon_lat_to_xy(lon, lat):
        px = map_x + (lon + 180) / 360.0 * map_w
        py = map_y + (90 - lat) / 180.0 * map_h
        return px, py

    for lon in range(-120, 180, 60):
        lx, _ = lon_lat_to_xy(lon, 0)
        draw.line([lx, map_y, lx, map_y + map_h], fill=(225, 220, 210), width=1)
    for lat in range(-60, 90, 30):
        _, ly = lon_lat_to_xy(0, lat)
        draw.line([map_x, ly, map_x + map_w, ly], fill=(225, 220, 210), width=1)

    def point_in_poly(lon, lat, poly):
        inside = False
        n = len(poly)
        j = n - 1
        for i in range(n):
            xi, yi = poly[i]
            xj, yj = poly[j]
            if ((yi > lat) != (yj > lat)) and (
                    lon < (xj - xi) * (lat - yi) / (yj - yi) + xi):
                inside = not inside
            j = i
        return inside

    LAND = (195, 205, 215)
    CELL = 3.0
    SUBS = 3
    cols_grid = int(round(360.0 / CELL))
    rows_grid = int(round(180.0 / CELL))
    land_cells = 0
    for row in range(rows_grid):
        for col in range(cols_grid):
            hit = False
            for sy_sub in range(SUBS):
                lat_s = 90.0 - (row + (sy_sub + 0.5) / SUBS) * CELL
                for sx_sub in range(SUBS):
                    lon_s = -180.0 + (col + (sx_sub + 0.5) / SUBS) * CELL
                    if any(point_in_poly(lon_s, lat_s, p) for p in LAND_POLYGONS):
                        hit = True
                        break
                if hit:
                    break
            if hit:
                x0, y0 = lon_lat_to_xy(-180.0 + col * CELL, 90.0 - row * CELL)
                x1, y1 = lon_lat_to_xy(-180.0 + (col + 1) * CELL, 90.0 - (row + 1) * CELL)
                draw.rectangle([x0, y0, x1, y1], fill=LAND)
                land_cells += 1

    all_pins = []
    for s in STORIES_FEATURED:
        if "lon" in s and "lat" in s:
            all_pins.append((s["n"], s["lon"], s["lat"], s["continent"], 0, 0))
    for s in STORIES_GRID:
        if "lon" in s and "lat" in s:
            all_pins.append((s["n"], s["lon"], s["lat"], s["continent"], 0, 0))
    for b_num, b_text, b_cont, b_coord in BRIEFS_DATA:
        if b_coord is not None:
            all_pins.append((b_num, b_coord[0], b_coord[1], b_cont, b_coord[2], b_coord[3]))

    font_pin = get_font(font_sans_bold_path, 8)
    for p_num, plon, plat, pcont, pdx, pdy in all_pins:
        px, py = lon_lat_to_xy(plon, plat)
        px += pdx
        py += pdy
        ccolor = CONTINENT_COLORS.get(pcont, ACCENT)
        draw.ellipse([px - 5.5, py - 5.5, px + 5.5, py + 5.5], fill=ccolor, outline=(255, 255, 255), width=1)
        t_str = str(p_num)
        tb = draw.textbbox((0, 0), t_str, font=font_pin)
        tw = tb[2] - tb[0]
        th = tb[3] - tb[1]
        draw.text((px - tw/2 - tb[0], py - th/2 - tb[1]), t_str, font=font_pin, fill=(255, 255, 255))

    # 6. DATE CHECK box (NEW device 2)
    dc_y = map_y + map_h + 8
    draw.rectangle([24, dc_y, 1000, dc_y + 36], fill=CARD, outline=DATE_RED, width=2)
    draw.rectangle([24, dc_y, 24 + 62, dc_y + 36], fill=DATE_RED)
    font_dc_lbl = get_font(font_sans_bold_path, 10.5)
    draw.text((55, dc_y + 6), "DATE", font=font_dc_lbl, fill=(255, 255, 255), anchor="ma")
    draw.text((55, dc_y + 19), "CHECK", font=font_dc_lbl, fill=(255, 255, 255), anchor="ma")

    font_dc_txt = get_font(font_sans_path, 9)
    dc_lines = wrap(DATE_CHECK_TEXT, font_dc_txt, 896, draw)
    assert len(dc_lines) <= 2, f"DATE CHECK text took {len(dc_lines)} lines (max 2): {dc_lines}"
    dc_y_txt = dc_y + 5
    for line in dc_lines:
        draw.text((96, dc_y_txt), line, font=font_dc_txt, fill=INK)
        dc_y_txt += 12

    # 7. Footer
    fy2 = dc_y + 42
    draw.line([24, fy2, 1000, fy2], fill=INK, width=1)
    font_footer_1 = get_font(font_serif_italic_path, 9.5)
    font_footer_2 = get_font(font_sans_path, 8.5)

    draw.text((512, fy2 + 5), "CLAIM = one side's account, not independently confirmed.", font=font_footer_1, fill=INK, anchor="ma")
    footer_text_2 = "Every story happened or was first reported on Wednesday 18 November 2026 - Disputed claims are attributed - Sources: Reuters - AP - AFP - BBC - Al Jazeera - CNN - WHO - UN News"
    draw.text((512, fy2 + 21), footer_text_2, font=font_footer_2, fill=GREY, anchor="ma")

    # Verifications & Assertions
    print(f"Clip failures (briefs): {clip_failures}")
    print(f"Text blocks checked: {text_blocks_checked}")
    print(f"Text clip failures: {len(text_clip_failures)}")
    print(f"Total stories drawn: {len(drawn_numbers)}")
    print(f"Timeline segments drawn: {timeline_segments_drawn}")

    expected_text_blocks = 2 * (len(STORIES_FEATURED) + len(STORIES_GRID))
    assert text_blocks_checked == expected_text_blocks, (
        f"Expected {expected_text_blocks} headline/summary blocks, "
        f"checked {text_blocks_checked}")
    if text_clip_failures:
        detail = "\n".join(
            f"  {label}: undrawn remainder {rem!r}"
            for label, rem in text_clip_failures)
        raise AssertionError(
            f"{len(text_clip_failures)} text block(s) were not drawn in full:\n"
            + detail)
    assert clip_failures == 0, f"Found {clip_failures} clip failures!"
    assert len(drawn_numbers) == 55, f"Expected 55 drawn stories, got {len(drawn_numbers)}: {sorted(drawn_numbers)}"
    assert timeline_segments_drawn == 6, f"Expected 6 timeline segments, got {timeline_segments_drawn}"

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out_path, "PNG")

    file_size = os.path.getsize(out_path)
    print(f"Saved entry.png: {file_size} bytes")
    assert img.size == (1024, 1024), f"Invalid size {img.size}"
    assert file_size <= 1048576, f"File too large: {file_size} bytes"

if __name__ == "__main__":
    main()
