import os
import sys
from PIL import Image, ImageDraw, ImageFont

# Canvas size
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
DATE_CHECK_RED = (172, 62, 44)

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
    {"n": 1, "kick": "IRAN · GULF", "head": "Iran strikes back; US hits Qeshm", "summ": "US jets hit an IRGC site on Qeshm; Iran answered on Kuwait and Bahrain - Bahrain says it intercepted several.", "kind": "missiles", "continent": "Mideast", "tag": "STRIKES ON BOTH SIDES", "tag_color": ACCENT, "chip": "CONFIRMED · REUTERS/AP", "lon": 51.5, "lat": 26.5},
    {"n": 2, "kick": "ASIA · APEC SUMMIT", "head": "Xi and Putin meet in Shenzhen", "summ": "The two denounce protectionism and Western sanctions; the first Trump-Xi-Putin trilateral is set for Thursday.", "kind": "flags-skyline", "continent": "Asia", "tag": "THREE-WAY ON THURSDAY", "tag_color": NAVY, "chip": "CONFIRMED · JUST SECURITY", "lon": 114.0, "lat": 22.5},
    {"n": 3, "kick": "ASIA · QUAD", "head": "Quad meets; Trump lands in Manila", "summ": "First leader-level Quad meeting in 2+ years; Trump meets Marcos Jr. and announces a Philippines trade deal.", "kind": "harbour", "continent": "Asia", "tag": "MANILA FIRST", "tag_color": (16, 22, 34), "chip": "CONFIRMED · OPENCHRONICLE", "lon": 121.0, "lat": 14.6},
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

PIN_CONTINENTS = {
    1: "Mideast", 2: "Asia", 3: "Asia", 4: "Europe", 5: "Europe", 6: "Americas", 7: "Europe", 8: "Americas", 9: "Americas", 10: "Americas", 11: "Africa", 12: "Asia", 13: "Oceania", 14: "Mideast", 15: "Americas", 16: "Mideast", 17: "Mideast", 18: "Europe", 19: "Asia", 20: "Asia", 21: "Americas", 22: "Africa", 23: "Africa", 24: "Asia", 25: "Americas", 26: "Europe", 27: "Africa", 28: "Asia", 29: "Americas", 30: "Europe", 31: "Mideast", 32: "Africa", 33: "Americas", 34: "Americas", 35: "Americas", 36: "Africa", 37: "Oceania", 38: "Europe", 39: "Europe", 40: "Americas", 41: "Europe", 42: "Europe", 43: "Asia", 44: "Asia", 45: "Oceania", 46: "Europe", 47: "Mideast", 48: "Americas", 49: "Americas", 50: "Europe", 51: "Oceania", 52: "Africa", 53: "Americas", 54: "Europe", 55: "Africa",
}

PIN_COORDS_1_15 = {1: (51.5, 26.5, 0, 0), 2: (114.0, 22.5, 0, 0), 3: (121.0, 14.6, -6, -12), 4: (30.5, 50.4, 8, -2), 5: (4.35, 50.85, -8, -6), 6: (-74.0, 40.7, -4, -10), 7: (-0.1, 51.5, -12, -4), 8: (-122.4, 37.8, -8, -6), 9: (-118.1, 34.1, 0, 8), 10: (-98.0, 39.0, 0, 0), 11: (23.0, -2.0, 0, 0), 12: (86.0, 19.0, 6, 2), 13: (-160.0, -15.0, 0, 0), 14: (34.4, 31.45, -10, 8), 15: (-77.0, 38.9, -14, -8)}

DATE_CHECK_TEXT = "Left out on purpose - they broke on other days: the An-12 crash in Siberia, 19 killed (Tue 17 Nov) - Peltola's Alaska Senate call (Tue 17 Nov) - the Knesset speaker vote, Kahana 66-52 (Tue 17 Nov) - the Crimea Bridge collapse (overnight 16-17 Nov) - Nvidia's results (17 Nov). Not yet: the ICJ Rohingya judgment is due Thu 19 Nov."

LAND_POLYGONS = [
    [(-168, 66), (-162, 71), (-140, 70), (-120, 71), (-95, 72), (-80, 70), (-60, 60), (-53, 47), (-66, 44), (-70, 41), (-75, 35), (-81, 25), (-84, 30), (-90, 29), (-97, 26), (-95, 18), (-87, 21), (-83, 9), (-79, 8), (-86, 15), (-92, 16), (-105, 20), (-115, 30), (-124, 40), (-125, 49), (-135, 58), (-150, 60)],
    [(-55, 60), (-45, 60), (-20, 70), (-20, 82), (-45, 84), (-60, 76)],
    [(-79, 9), (-75, 11), (-72, 12), (-68, 11.8), (-64, 10.8), (-62, 10), (-52, 5), (-50, 0), (-44, -2), (-35, -6), (-37, -10), (-38, -13), (-40, -20), (-40, -23), (-44, -23), (-48, -25), (-53, -34), (-58, -38), (-62, -40), (-65, -45), (-68, -50), (-68, -55), (-73, -53), (-75, -46), (-73, -37), (-71, -30), (-70, -18), (-71, -16), (-75, -14), (-77, -12), (-79, -6), (-81, -2), (-80, 1), (-78, 7)],
    [(-9, 37), (-9, 43), (-2, 48), (4, 52), (8, 58), (10, 57.5), (16, 58), (18, 59.5), (20, 60), (22, 66), (28, 71), (40, 70), (70, 74), (100, 78), (140, 73), (160, 70), (170, 66), (179, 65), (179, 60), (160, 58), (142, 52), (140, 44), (132, 46), (130, 42), (129, 38), (128, 38), (126, 38), (126, 35), (126, 34), (124, 35), (122, 30), (120, 25), (118, 24), (116.5, 24), (115.5, 23.2), (114.0, 22.0), (112.5, 21.2), (110, 20), (108, 18), (105, 10), (103, 1), (100, 6), (98, 12), (94, 16), (90, 22), (88, 22), (80, 8), (72, 18), (66, 25), (60, 25), (57, 22), (52, 17), (43, 12), (39, 20), (35, 28), (34, 31), (36, 36), (34, 36.5), (31, 36.5), (29, 37), (26, 38), (23, 38), (20, 40), (16, 41.5), (18, 40), (16, 38), (14, 40), (13, 45), (12, 45), (8, 44), (3, 43), (0, 38.5), (-6, 36), (-9, 37)],
    [(-17.6, 14.7), (-16, 21), (-10, 28), (0, 36.5), (10, 37.5), (20, 33), (32, 31), (35, 23), (43, 12), (51, 11), (48, 0), (41, -10), (35, -20), (32, -27), (26, -34), (20, -35), (18, -34.5), (15, -28), (12, -18), (9, -1), (3, 5), (-8, 4), (-13, 8)],
    [(114, -22), (113, -26), (115, -34), (129, -32), (138, -35), (146, -39), (150, -38), (152, -32), (153, -28), (146, -19), (142, -11), (132, -11), (126, -14), (122, -18)],
    [(-6, 50), (-6, 58), (-2, 58), (0, 53), (1, 51), (-2, 50)],
    [(-24, 63.5), (-13, 64.5), (-14, 66.5), (-22, 66.5)],
    [(130, 32), (133, 34), (136, 35), (139, 35), (141, 36), (142, 39), (141, 41), (143, 44), (145, 43), (142, 40), (139, 36), (136, 35), (133, 34), (131, 33)],
    [(120, 18), (124, 18), (126, 10), (122, 6), (120, 10)],
    [(95, 5), (105, 5), (115, 2), (120, -2), (130, -3), (140, -4), (140, -8), (120, -9), (114, -8.5), (105, -8), (105, -6), (100, -3), (100, 0)],
    [(44, -13), (50, -14), (50, -25), (45, -25), (43, -19)],
    [(172, -34), (178, -37), (176, -41), (173, -43), (167, -46), (170, -43), (172, -37)],
    [(177, -16), (180, -17), (180, -19), (177, -19)],
    [(-161, -20), (-159, -20), (-159, -22), (-161, -22)],
    [(-84, 22.5), (-74, 20), (-77, 23.5), (-84, 23.5)],
    [(80, 6), (82, 7), (82, 9), (80, 9)],
    [(6, 44), (10, 46), (13, 46), (13, 44), (16, 41.5), (18, 40), (16, 38), (15.5, 38), (13, 41), (12, 42), (10, 43), (8, 44)],
    [(124, 38.5), (127, 38.5), (129, 38), (129, 35), (126, 34), (125, 36)],
    [(145, -41), (148, -41), (148, -43), (145, -43)],
]

TIMELINE_DATA = [
    ("Overnight", "Russia fires 141 drones at Ukraine"),
    ("Before dawn", "Iran strikes Kuwait & Bahrain bases"),
    ("Asia daytime", "Xi-Putin summit; Quad meets in Manila"),
    ("10:16 UTC", "Voyager 1 reaches one light-day"),
    ("~19:00 UTC", "Fed minutes point to more hikes"),
    ("Evening", "Dow closes -561 on rate fears"),
]

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
    y = top
    drawn = 0
    for line in lines:
        bbox = draw.textbbox((x, y), line, font=font)
        if bbox[3] > bottom_limit:
            break
        draw.text((x, y), line, font=font, fill=INK)
        drawn += 1
        y += line_h
    return (drawn == len(lines)), y

def chip(draw, cx, cy, r, n):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=ACCENT)
    f_size = max(7, int(r * 1.12))
    font = get_font(font_sans_bold_path, f_size)
    text = str(n)
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((cx - tw/2 - bbox[0], cy - th/2 - bbox[1]), text, font=font, fill=(255, 255, 255))

def draw_banner(draw, x, y, w, h, kind, continent_color):
    muted_bg = (230, 240, 236)
    draw.rectangle([x, y, x + w, y + h], fill=muted_bg)
    c1 = ACCENT
    c2 = continent_color
    for i in range(4):
        draw.line([x + 20 + i * 50, y + 5, x + 40 + i * 50, y + h - 5], fill=c1, width=2)
        draw.ellipse([x + 10 + i * 50, y + 10, x + 30 + i * 50, y + 30], fill=c2)

def draw_scene(draw, x, y, w, h, kind):
    sky_color = (235, 240, 240)
    draw.rectangle([x, y, x + w, y + h], fill=sky_color)
    draw.ellipse([x + w - 30, y + 10, x + w - 10, y + 30], fill=(245, 200, 100))

    if kind == "missiles":
        draw.rectangle([x, y + 80, x + w, y + h], fill=(100, 150, 180))
        draw.polygon([x, y + 80, x + w/2, y + 70, x + w, y + 80, x + w, y + h, x, y + h], fill=(50, 50, 50))
        draw.rectangle([x + 20, y + 60, x + 50, y + 80], fill=(80, 80, 80))
        for i in range(3):
            draw.arc([x + 20 + i*60, y + 30, x + 150 + i*60, y + 70], 180, 270, fill=INK, width=2)
            draw.ellipse([x + 145 + i*60, y + 25, x + 155 + i*60, y + 35], fill=INK)
    elif kind == "flags-skyline":
        for i in range(5):
            h_b = 30 + (i % 3) * 20
            draw.rectangle([x + i * 60, y + h - h_b, x + i * 60 + 50, y + h], fill=(60, 60, 60))
        draw.rectangle([x + 100, y + 40, x + 105, y + 100], fill=INK)
        draw.rectangle([x + 200, y + 30, x + 205, y + 100], fill=INK)
        draw.polygon([x + 105, y + 40, x + 150, y + 50, x + 105, y + 60], fill=ACCENT)
        draw.polygon([x + 205, y + 30, x + 250, y + 40, x + 205, y + 50], fill=NAVY)
    elif kind == "harbour":
        draw.rectangle([x, y + 70, x + w, y + h], fill=(120, 170, 200))
        draw.rectangle([x + 50, y + 80, x + 200, y + 100], fill=INK)
        draw.line([x + 220, y + 100, x + 250, y + 50], fill=INK, width=3)
        draw.line([x + 250, y + 50, x + 270, y + 70], fill=INK, width=3)
        for i in range(4):
            draw.rectangle([x + 20 + i * 60, y + 50, x + 22 + i * 60, y + 70], fill=INK)
            draw.polygon([x + 22 + i * 60, y + 50, x + 40 + i * 60, y + 55, x + 22 + i * 60, y + 60], fill=ACCENT)

def source_chip(draw, x, y, text):
    font = get_font(font_sans_bold_path, 8)
    bbox = draw.textbbox((0, 0), text, font=font)
    pw = (bbox[2] - bbox[0]) + 14
    draw.rounded_rectangle([x + 309 - pw, y, x + 309, y + 16], radius=7, fill=(90, 88, 80))
    draw.text((x + 309 - pw/2, y + 8), text, font=font, fill=(255, 255, 255), anchor="mm")

def pack_briefs(draw, size, briefs_data, briefs_top, band_limit):
    col_x_list = [24, 192, 360, 528]
    brief_font = get_font(font_sans_path, size)
    line_h = size + 1.75

    column = 0
    y = briefs_top
    placements = []
    col_heights = [0, 0, 0, 0]

    for n, text, continent, coords in briefs_data:
        lines = wrap(text, brief_font, 142, draw)
        h = len(lines) * line_h + 3
        if y + h > briefs_top + band_limit:
            if column < 3:
                column += 1
                y = briefs_top
            else:
                return None, None
        placements.append((n, text, col_x_list[column], y, h, len(lines), size))
        y += h
        col_heights[column] = max(col_heights[column], y - briefs_top)

    band_h = max(col_heights)
    return placements, band_h

def main():
    img = Image.new("RGB", (WIDTH, HEIGHT), PAPER)
    draw = ImageDraw.Draw(img)

    reclamation_configs = [
        (192, 112, 94, 56),
        (184, 104, 94, 56),
        (184, 104, 90, 56),
        (184, 104, 90, 52),
    ]

    chosen_layout = None
    best_size = None
    placements = None
    band_h = None

    for cfg in reclamation_configs:
        feat_card_h, scene_h, row_pitch, title_size = cfg
        r1 = 18 + title_size + 10
        sy = r1 + 12
        tl_y = sy + 16
        fy = tl_y + 54
        gy = fy + feat_card_h + 16
        by = gy + 3 * row_pitch + 8
        hy = by + 8

        briefs_top = hy + 22
        band_limit = 940 - briefs_top

        for size in [9.5, 9.25, 9.0, 8.75, 8.5]:
            p, bh = pack_briefs(draw, size, BRIEFS_DATA, briefs_top, band_limit)
            if p is not None:
                best_size = size
                placements = p
                band_h = bh
                chosen_layout = cfg
                break
        if chosen_layout is not None:
            break

    if chosen_layout is None:
        chosen_layout = reclamation_configs[-1]
        feat_card_h, scene_h, row_pitch, title_size = chosen_layout
        r1 = 18 + title_size + 10
        sy = r1 + 12
        tl_y = sy + 16
        fy = tl_y + 54
        gy = fy + feat_card_h + 16
        by = gy + 3 * row_pitch + 8
        hy = by + 8
        briefs_top = hy + 22
        band_limit = 940 - briefs_top
        best_size = 8.5
        placements, band_h = pack_briefs(draw, 8.5, BRIEFS_DATA, briefs_top, band_limit)

    feat_card_h, scene_h, row_pitch, title_size = chosen_layout
    r1 = 18 + title_size + 10
    sy = r1 + 12
    tl_y = sy + 16
    fy = tl_y + 54
    gy = fy + feat_card_h + 16
    by = gy + 3 * row_pitch + 8
    hy = by + 8

    tag_bar_y = fy + (74 if feat_card_h == 184 else 82)
    chip_y = fy + (116 if feat_card_h == 184 else 124)
    source_chip_y = fy + (108 if feat_card_h == 184 else 116)
    head_y = fy + (130 if feat_card_h == 184 else 136)
    head_bottom = fy + (166 if feat_card_h == 184 else 174)
    summ_y = fy + (151 if feat_card_h == 184 else 157)
    summ_bottom = fy + (182 if feat_card_h == 184 else 190)
    box_h = row_pitch - 8

    # Masthead
    draw.text((24, 6), "THE WORLD'S NEWS IN ONE PICTURE", font=get_font(font_sans_bold_path, 12.5), fill=ACCENT)
    draw.text((1000, 6), "55 STORIES · 6 CONTINENTS · ONE PAGE", font=get_font(font_sans_bold_path, 12.5), fill=INK, anchor="rm")
    draw.text((512, 18), "Wednesday 18 November 2026", font=get_font(font_serif_bold_path, title_size), fill=INK, anchor="ma")
    draw.line([24, r1, 1000, r1], fill=ACCENT, width=3)
    draw.line([24, r1 + 5, 1000, r1 + 5], fill=ACCENT, width=1)
    draw.text((24, sy), "THE DAILY ATLAS · WEDNESDAY EDITION NO. 18", font=get_font(font_sans_bold_path, 11), fill=INK)
    draw.text((1000, sy), "EVERY STORY REPORTED ON THE DAY", font=get_font(font_sans_path, 10.5), fill=GREY, anchor="rm")

    # UTC Timeline
    draw.rectangle([24, tl_y, 1000, tl_y + 46], fill=CARD, outline=BORDER)
    draw.rectangle([24, tl_y, 24 + 62, tl_y + 46], fill=ACCENT)
    draw.text((55, tl_y + 13), "THE DAY", font=get_font(font_sans_bold_path, 10), fill=(255, 255, 255), anchor="ma")
    draw.text((55, tl_y + 26), "IN UTC", font=get_font(font_sans_bold_path, 10), fill=(255, 255, 255), anchor="ma")
    seg_w = (976 - 62) / 6
    for i in range(6):
        seg_x = 24 + 62 + i * seg_w
        if i > 0: draw.line([seg_x, tl_y + 5, seg_x, tl_y + 41], fill=BORDER, width=1)
        label, event = TIMELINE_DATA[i]
        draw.text((seg_x + 8, tl_y + 4), label, font=get_font(font_sans_bold_path, 10), fill=ACCENT)
        block(draw, event, get_font(font_sans_path, 8.5), seg_x + 4, tl_y + 19, seg_w - 14, 10, tl_y + 46)

    # Featured Row
    drawn_stories = set()
    for i, story in enumerate(STORIES_FEATURED):
        x = 24 + i * 329
        draw.rectangle([x, fy, x + 317, fy + feat_card_h], fill=CARD, outline=BORDER)
        draw_scene(draw, x, fy, 317, scene_h, story["kind"])
        draw.rectangle([x, tag_bar_y, x + 317, tag_bar_y + 30], fill=story["tag_color"])
        strip_color = INK if story["tag_color"] == ACCENT else ACCENT
        draw.rectangle([x, tag_bar_y, x + 5, tag_bar_y + 30], fill=strip_color)
        draw.text((x + 14, tag_bar_y + 15), story["tag"], font=get_font(font_sans_bold_path, 12.5), fill=(255, 255, 255), anchor="lm")
        chip(draw, x + 18, chip_y, 9.5, story["n"])
        drawn_stories.add(story["n"])
        draw.text((x + 34, chip_y), story["kick"], font=get_font(font_sans_bold_path, 10.5), fill=ACCENT, anchor="lm")
        source_chip(draw, x, source_chip_y, story["chip"])
        h_size = 16.0
        while h_size > 13.5:
            if len(wrap(story["head"], get_font(font_serif_bold_path, h_size), 297, draw)) == 1: break
            h_size -= 0.5
        ok1, _ = block(draw, story["head"], get_font(font_serif_bold_path, h_size), x + 10, head_y, 297, 19, head_bottom)
        assert ok1 and len(wrap(story["head"], get_font(font_serif_bold_path, h_size), 297, draw)) == 1, f"Story {story['n']} headline error"
        ok2, _ = block(draw, story["summ"], get_font(font_serif_path, 9.5), x + 10, summ_y, 297, 10.5, summ_bottom)
        assert ok2, f"Story {story['n']} summary clipped"

    # Grid
    draw.line([24, gy - 8, 1000, gy - 8], fill=INK, width=1)
    for i, story in enumerate(STORIES_GRID):
        row = i // 4
        col = i % 4
        x = 24 + col * 246
        y0 = gy + row * row_pitch
        draw.rectangle([x, y0, x + 238, y0 + box_h], fill=CARD, outline=BORDER)
        draw_banner(draw, x, y0, 238, 32, story["kind"], CONTINENT_COLORS.get(story["continent"], ACCENT))
        chip(draw, x + 13, y0 + 38, 6, story["n"])
        drawn_stories.add(story["n"])
        draw.text((x + 24, y0 + 38), story["kick"], font=get_font(font_sans_bold_path, 8), fill=ACCENT, anchor="lm")
        chip_text = story["chip"]
        c_fill = DATE_CHECK_RED if chip_text.startswith("CLAIM") else GREY
        draw.text((x + 230, y0 + 38), chip_text, font=get_font(font_sans_bold_path, 7), fill=c_fill, anchor="rm")
        ok1, _ = block(draw, story["head"], get_font(font_serif_bold_path, 11), x + 8, y0 + 44, 222, 13, y0 + 70)
        assert ok1, f"Story {story['n']} headline clipped"
        f_size = 8.0
        ok2 = False
        while f_size >= 7.5:
            ok2, _ = block(draw, story["summ"], get_font(font_serif_path, f_size), x + 8, y0 + 67, 222, 8.5, y0 + 84)
            if ok2:
                break
            f_size -= 0.5
        assert ok2, f"Story {story['n']} summary clipped"

    # Bottom Band
    draw.line([24, by, 1000, by], fill=INK, width=1)
    draw.text((700, hy), "WHERE IT HAPPENED", font=get_font(font_sans_bold_path, 12), fill=ACCENT)
    draw.text((24, hy), "ALSO ON WEDNESDAY 18 NOVEMBER", font=get_font(font_sans_bold_path, 12), fill=INK)

    # Legend
    legend_start = 338
    for i, (name, color) in enumerate(CONTINENT_COLORS.items()):
        draw.ellipse([legend_start + i*58, hy + 4, legend_start + i*58 + 7, hy + 11], fill=color)
        draw.text((legend_start + i*58 + 10, hy + 4), name, font=get_font(font_sans_path, 8.5), fill=INK)

    # Briefs Columns
    brief_font = get_font(font_sans_path, best_size)
    brief_num_font = get_font(font_sans_bold_path, best_size)
    brief_lh = best_size + 1.75
    drawn_brief_nums = set()

    for n, text, cx, y, h, num_lines, size in placements:
        draw.text((cx, y), str(n), font=brief_num_font, fill=INK)
        ok, _ = block(draw, text, brief_font, cx + 15, y, 142, brief_lh, y + num_lines * brief_lh)
        assert ok, f"Brief {n} clipped"
        drawn_stories.add(n)
        drawn_brief_nums.add(n)

        # Dotted separator
        sep_y = y + h - 2
        for sx in range(cx + 15, cx + 15 + 142, 4):
            draw.point((sx, sep_y), fill=BORDER)

    assert drawn_brief_nums == set(range(16, 56))

    # Map
    map_x = 700
    map_y = hy + 22
    for poly in LAND_POLYGONS:
        scaled_poly = []
        for lon, lat in poly:
            mx = map_x + (lon + 180) / 360 * 300
            my = map_y + (90 - lat) / 180 * band_h
            scaled_poly.append((mx, my))
        draw.polygon(scaled_poly, fill=(200, 200, 200))

    # Pins
    drawn_pins = set()
    for n, _, _, (lon, lat, dx, dy) in BRIEFS_DATA:
        mx = map_x + (lon + 180) / 360 * 300 + dx
        my = map_y + (90 - lat) / 180 * band_h + dy
        c = CONTINENT_COLORS.get(PIN_CONTINENTS.get(n), INK)
        draw.ellipse([mx - 7, my - 7, mx + 7, my + 7], fill=c)
        font = get_font(font_sans_bold_path, 7.8)
        draw.text((mx, my), str(n), font=font, fill=(255, 255, 255), anchor="mm")
        drawn_pins.add(n)

    for n, (lon, lat, dx, dy) in PIN_COORDS_1_15.items():
        mx = map_x + (lon + 180) / 360 * 300 + dx
        my = map_y + (90 - lat) / 180 * band_h + dy
        c = CONTINENT_COLORS.get(PIN_CONTINENTS.get(n), INK)
        draw.ellipse([mx - 7, my - 7, mx + 7, my + 7], fill=c)
        font = get_font(font_sans_bold_path, 7.8)
        draw.text((mx, my), str(n), font=font, fill=(255, 255, 255), anchor="mm")
        drawn_pins.add(n)
    assert drawn_pins == set(range(1, 56))

    # DATE CHECK box
    dc_y = hy + band_h + 20
    draw.rectangle([24, dc_y, 1000, dc_y + 40], fill=CARD, outline=DATE_CHECK_RED, width=2)
    draw.rectangle([24, dc_y, 24 + 62, dc_y + 40], fill=DATE_CHECK_RED)
    draw.text((55, dc_y + 7), "DATE", font=get_font(font_sans_bold_path, 10.5), fill=(255, 255, 255), anchor="ma")
    draw.text((55, dc_y + 21), "CHECK", font=get_font(font_sans_bold_path, 10.5), fill=(255, 255, 255), anchor="ma")
    ok_dc, _ = block(draw, DATE_CHECK_TEXT, get_font(font_sans_path, 9.5), 96, dc_y + 6, 888, 12.5, dc_y + 40)
    assert ok_dc, "DATE CHECK text exceeds 2 lines"

    # Footer
    fy2 = dc_y + 46
    draw.line([24, fy2, 1000, fy2], fill=INK, width=1)
    draw.text((512, fy2 + 5), "CLAIM = one side's account, not independently confirmed.", font=get_font(font_serif_italic_path, 9.5), fill=INK, anchor="ma")
    draw.text((512, fy2 + 21), "Every story happened or was first reported on Wednesday 18 November 2026 - Disputed claims are attributed - Sources: Reuters · AP · AFP · BBC · Al Jazeera · CNN · WHO · UN News", font=get_font(font_sans_path, 8.5), fill=GREY, anchor="ma")
    assert (fy2 + 21) <= 1022, f"Footer second line at y={fy2 + 21}, exceeds 1022"

    assert len(drawn_stories) == 55, f"Not all 55 stories drawn, only {len(drawn_stories)}"

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out_path, "PNG")
    print(f"Saved {out_path}")

if __name__ == "__main__":
    main()
