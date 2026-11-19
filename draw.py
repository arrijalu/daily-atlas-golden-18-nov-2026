import os
from PIL import Image, ImageDraw, ImageFont

# Canvas dimensions
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

# Story Data
STORIES_FEATURED = [
    {
        "n": 1,
        "kick": "IRAN - GULF",
        "head": "Iran strikes back; US hits Qeshm",
        "summ": "US struck an IRGC missile site on Qeshm Island on Tuesday; Iran answered early Wednesday with strikes on Kuwait's Ali Al Salem Air Base and Bahrain.",
        "kind": "missiles over a gulf coastline",
        "continent": "Mideast",
        "lon": 52, "lat": 27
    },
    {
        "n": 2,
        "kick": "ASIA - APEC SUMMIT",
        "head": "Xi and Putin meet in Shenzhen",
        "summ": "Xi Jinping and Vladimir Putin met on the APEC sidelines, denouncing protectionism and Western sanctions; trilateral with Trump set for Thursday.",
        "kind": "two flags over a skyline",
        "continent": "Asia",
        "lon": 114, "lat": 22
    },
    {
        "n": 3,
        "kick": "ASIA - QUAD IN MANILA",
        "head": "Quad meets; Trump lands in Manila",
        "summ": "First leader-level Quad meeting in over two years; Trump met Marcos Jr., announced a Philippines trade deal, then flies on to China.",
        "kind": "four flags over a harbour",
        "continent": "Asia",
        "lon": 121, "lat": 15
    },
]

STORIES_GRID = [
    {
        "n": 4,
        "kick": "UKRAINE - WAR",
        "head": "Russia fires 141 drones; 126 downed",
        "summ": "Overnight barrage across Ukraine; hits recorded at 7 sites. (ISW)",
        "kind": "drone barrage",
        "continent": "Europe",
        "lon": 32, "lat": 49
    },
    {
        "n": 5,
        "kick": "EUROPE - UKRAINE AID",
        "head": "EU proposes a 45bn-euro Ukraine loan",
        "summ": "25bn military and 20bn budget support for 2027, presented Wednesday.",
        "kind": "eu aid coin",
        "continent": "Europe",
        "lon": 5, "lat": 51
    },
    {
        "n": 6,
        "kick": "UNITED STATES - MARKETS",
        "head": "Fed minutes back more hikes; Dow -561",
        "summ": "Minutes put a bigger December hike in play; S and P 500 -0.23%, Nasdaq +0.42%.",
        "kind": "market chart down",
        "continent": "Americas",
        "lon": -74, "lat": 41
    },
    {
        "n": 7,
        "kick": "MARKETS - GOLD",
        "head": "Gold sinks to 14-month low",
        "summ": "Closed $3,725.18 an ounce, down 3.22 percent, on Wednesday.",
        "kind": "gold bar drop",
        "continent": "Americas",
    },
    {
        "n": 8,
        "kick": "TECH - IPO",
        "head": "Anthropic prices IPO at $83",
        "summ": "Raising $81.3bn - the largest listing on record, topping SpaceX's $75bn.",
        "kind": "tech IPO rise",
        "continent": "Americas",
        "lon": -122, "lat": 38
    },
    {
        "n": 9,
        "kick": "SCIENCE - SPACE",
        "head": "Voyager 1 reaches one light-day",
        "summ": "First human-made object to reach one light-day from Earth (16bn miles). NASA JPL.",
        "kind": "space probe signal",
        "continent": "Americas",
    },
    {
        "n": 10,
        "kick": "AMERICAS - HEALTH",
        "head": "US loses measles-free status after 26 years",
        "summ": "PAHO: measles endemic again; 5,412 cases in 2026, 10 deaths, highest since 1991.",
        "kind": "health cross alert",
        "continent": "Americas",
        "lon": -84, "lat": 34
    },
    {
        "n": 11,
        "kick": "AFRICA - HEALTH",
        "head": "Ebola passes 11,000 cases in DR Congo",
        "summ": "More than doubled in three months, second-largest on record; nearly 3 in 4 under-5s die. WHO.",
        "kind": "medical warning",
        "continent": "Africa",
        "lon": 23, "lat": -3
    },
    {
        "n": 12,
        "kick": "INDIA - WEATHER",
        "head": "Cyclone Akvan bears down on Odisha",
        "summ": "Severe storm 570 km east of Chennai; landfall expected near Andhra on 20 Nov. IMD.",
        "kind": "cyclone swirl",
        "continent": "Asia",
        "lon": 86, "lat": 20
    },
    {
        "n": 13,
        "kick": "PACIFIC - WEATHER",
        "head": "Cyclone Xavier hits Category 5",
        "summ": "Briefly Cat 5 (110 kt) over northern Cook Islands; wharves damaged on Manihiki.",
        "kind": "cyclone wave",
        "continent": "Oceania",
        "lon": -160, "lat": -21
    },
    {
        "n": 14,
        "kick": "GAZA - WAR",
        "head": "Israeli tanks cross Yellow Line at Nuseirat",
        "summ": "First such raid since the truce; three Palestinians killed, medics say.",
        "kind": "tank movement",
        "continent": "Mideast",
        "lon": 34, "lat": 31
    },
    {
        "n": 15,
        "kick": "UNITED STATES - POLITICS",
        "head": "Jeffries wins Democrats' Speaker nod",
        "summ": "Won the caucus vote 251-11; full House vote set for 3 January.",
        "kind": "gavel podium",
        "continent": "Americas",
    },
]

BRIEFS_DATA = [
    (16, "Houthis fire five drones at two pumping stations on Saudi East-West pipeline, Riyadh area.", "Mideast", (47, 25)),
    (17, "Gaza winter: WHO - 950,000 displaced Palestinians in flood-prone ground in Gaza's fourth winter.", "Mideast", None),
    (18, "Louvre workers vote to extend strike over understaffing and the October crown-jewels heist.", "Europe", (2, 49)),
    (19, "ASHA health workers' strike enters second day in Karnataka; demand 15,000 rupees/month honorarium.", "Asia", (77, 15)),
    (20, "Maharashtra district court employees call off strike after talks with four Bombay High Court judges.", "Asia", None),
    (21, "Magnitude 6.0 quake off Peru's Ica region; no casualties, tsunami ruled out.", "Americas", (-76, -13)),
    (22, "Ghana's new $60m presidential jet sparks public outrage amid austerity.", "Africa", (-2, 8)),
    (23, "Nigeria's central bank and NNPC sign forex and energy funding deal.", "Africa", (8, 10)),
    (24, "Malaysia Q3 GDP beats forecasts at 5.5 percent; AI boom to drive 2027 growth.", "Asia", (102, 4)),
    (25, "Fed's Waller calls for more aggressive inflation response - half-point hike in play for Dec.", "Americas", None),
    (26, "UK inflation rises to 3.6 percent, highest in a year, on record fuel prices.", "Europe", (0, 52)),
    (27, "Amnesty: RSF drone strikes in El Obeid killed 37 civilians, June-August.", "Africa", (30, 13)),
    (28, "Bangladesh garment unrest: about 535 factories hit, about 130 shut, about 300 arrested.", "Asia", (90, 24)),
    (29, "GTA VI rolls out to rave reviews, Metacritic 99, ahead of its 19 Nov launch.", "Americas", None),
    (30, "Quake felt in Bucharest; EMSC 5.3, Romania's institute 5.7.", "Europe", (26, 44)),
    (31, "Magnitude 4.1 quake strikes southwest Kuwait; no damage reported.", "Mideast", (48, 29)),
    (32, "Migrant boat capsizes off Senegal, at least one dead; search ongoing.", "Africa", (-17, 15)),
    (33, "Hegseth makes surprise Caracas trip, signs US-Venezuela defence partnership.", "Americas", (-67, 11)),
    (34, "Brazil Senate approves Lula's $10bn fiscal package; heads to lower house.", "Americas", (-48, -16)),
    (35, "Sheinbaum says Mexico-US trade talks 'very far along' after meeting Trump.", "Americas", None),
    (36, "Monitors say Ethiopia and Eritrea massed troops near Badme; war fears rise.", "Africa", (39, 15)),
    (37, "Tame Impala wins seven ARIAs, including Album of the Year for Deadbeat.", "Oceania", (151, -34)),
    (38, "Alcaraz beats Medvedev 6-2, 6-4 at ATP Finals, reaching the semi-finals.", "Europe", None),
    (39, "ECDC warns superbug infections surged; Klebsiella cases up 72 percent since 2019.", "Europe", (18, 59)),
    (40, "Pew projects Islam will pass Christianity as the world's largest religion by 2035.", "Mideast", None),
    (41, "Brent crude settles $91.95 a barrel, down $1.19 (-1.28 percent) on surplus fears.", "Mideast", None),
    (42, "Chelsea Women beat PSG 1-0, Buurman 87th-minute winner (UEFA UWCL, Matchday 5).", "Europe", None),
    (43, "Japan exports hit record 11.8tn yen in Oct, +20.5 percent, 14th straight monthly rise (Reuters).", "Asia", (140, 36)),
    (44, "Japan Oct visitors hit record 3.91m despite China arrivals falling 47 percent (JNTO).", "Asia", None),
    (45, "Australia wages +1.1 percent in Sep quarter, fastest since Dec 2023; real pay still falls (ABS).", "Oceania", None),
    (46, "EU Council authorises signing EU-Indonesia CEPA and investment deal (Consilium 18/11).", "Europe", None),
    (47, "COP31 launches second Global Stocktake; 21 issues still unresolved on Wed (Antalya).", "Europe", (31, 37)),
    (48, "Ella Langley wins record six CMAs in one night, incl. Entertainer of the Year (Nashville).", "Americas", (-87, 36)),
    (49, "National Book Awards: Assadi fiction, ElGendy nonfiction; Rushdie lifetime medal (NYC).", "Americas", None),
    (50, "First Ivors Composer Awards: Pemberton Composer of the Year, Einaudi Fellow (London).", "Europe", None),
    (51, "Fiji declares national state of disaster over El Nino drought, FJ$20m allocated (PM Rabuka).", "Oceania", (178, -18)),
    (52, "Ruto gives 4th State of the Nation address, unveils PAYE relief, KSh340bn fund (Nairobi).", "Africa", (37, -1)),
    (53, "Trump asks Supreme Court Wed to block Venezuelan TPS restoration for 600,000.", "Americas", None),
    (54, "Qonto granted French/ECB banking licence, serves 750,000+ European SMEs.", "Europe", None),
    (55, "Cassava seeks $1bn to buy Nvidia chips for AI data centres across Africa (TechCabal).", "Africa", (3, 6)),
]

clip_failures = 0
# (label, undrawn remainder) for every headline/summary that was not drawn whole
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
    """Draw wrapped text from `top` down to `bottom_limit`.

    Returns (complete, remainder, next_y). `complete` is True only when every
    wrapped line was drawn AND its ink stays above `bottom_limit`; in that case
    `remainder` is the empty string. Otherwise `remainder` is the exact text
    that was not drawn, so callers can prove the clip by construction instead
    of trusting a line budget.
    """
    lines = wrap(text, font, max_width, draw)
    # wrap() must not lose or alter words
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
    f_size = max(7, int(r * 1.15))
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
    if "missile" in kind or "drone" in kind or "tank" in kind:
        for i in range(4):
            dx = x + 20 + i * 70
            draw.line([dx, y + h - 10, dx + 40, y + 10], fill=c1, width=2)
            draw.polygon([dx+30, y+15, dx+45, y+10, dx+40, y+25], fill=c2)
    elif "skyline" in kind or "harbour" in kind or "gavel" in kind or "podium" in kind:
        for i in range(5):
            bw = 25
            bh = 20 + (i * 13) % 40
            bx = x + 15 + i * 60
            by = y + h - bh
            draw.rectangle([bx, by, bx + bw, y + h], fill=c1 if i % 2 == 0 else c2)
    elif "flag" in kind or "eu" in kind or "aid" in kind:
        draw.rectangle([x + 30, y + 15, x + 100, y + h - 15], fill=c1)
        draw.rectangle([x + 110, y + 20, x + 180, y + h - 10], fill=c2)
        draw.ellipse([x + 200, y + 20, x + 250, y + h - 20], fill=c1)
    else:
        for i in range(3):
            rx = x + 30 + i * 90
            ry = y + h // 2
            draw.ellipse([rx, ry - 15, rx + 40, ry + 15], outline=c1, width=2)
            draw.arc([rx + 10, ry - 25, rx + 60, ry + 25], 0, 180, fill=c2, width=2)

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
    draw.text((24, 4), "THE WORLD'S NEWS IN ONE PICTURE", font=font_top_left, fill=ACCENT)

    right_text = "55 STORIES · ONE PAGE"
    bbox = draw.textbbox((0, 0), right_text, font=font_top_right)
    rw = bbox[2] - bbox[0]
    draw.text((1000 - rw, 4), right_text, font=font_top_right, fill=INK)

    title_size = 58
    font_title = get_font(font_serif_bold_path, title_size)
    while draw.textlength("THE DAILY ATLAS", font=font_title) > 900 and title_size > 40:
        title_size -= 2
        font_title = get_font(font_serif_bold_path, title_size)

    draw.text((512, 16), "THE DAILY ATLAS", font=font_title, fill=INK, anchor="ma")

    r1 = 16 + title_size + 7
    draw.line([24, r1, 1000, r1], fill=ACCENT, width=3)
    draw.line([24, r1 + 5, 1000, r1 + 5], fill=ACCENT, width=1)

    dy = r1 + 10
    font_date = get_font(font_serif_bold_path, 23)
    draw.text((512, dy), "Wednesday 18 November 2026", font=font_date, fill=ACCENT, anchor="ma")

    sy = dy + 31
    font_sub_left = get_font(font_sans_path, 10.5)
    font_sub_right = get_font(font_sans_bold_path, 11)
    draw.text((24, sy), "EVERY STORY REPORTED ON THE DAY", font=font_sub_left, fill=GREY)

    sub_right_text = "WEDNESDAY EDITION - NO. 18"
    bbox = draw.textbbox((0, 0), sub_right_text, font=font_sub_right)
    srw = bbox[2] - bbox[0]
    draw.text((1000 - srw, sy), sub_right_text, font=font_sub_right, fill=INK)

    fy = sy + 18

    # 2. Featured Row (3 cards, 317 wide, 180 high, x = 24 + i*329)
    font_kicker_feat = get_font(font_sans_bold_path, 12)
    font_kicker_feat_sm = get_font(font_sans_bold_path, 10.5)
    font_head_feat = get_font(font_serif_bold_path, 16)
    font_summ_feat = get_font(font_serif_path, 9)

    for i, story in enumerate(STORIES_FEATURED):
        x = 24 + i * 329
        w = 317
        h = 180

        draw.rectangle([x, fy, x + w, fy + h], fill=CARD, outline=BORDER, width=1)

        banner_h = 84
        c_color = CONTINENT_COLORS.get(story["continent"], ACCENT)
        draw_banner(draw, x, fy, w, banner_h, story["kind"], c_color)

        tag_y = fy + banner_h - 26
        draw.rectangle([x, tag_y, x + w, fy + banner_h], fill=c_color)
        draw.rectangle([x, tag_y, x + 5, fy + banner_h], fill=ACCENT)

        draw.text((x + 14, tag_y + 13), story["kick"], font=font_kicker_feat, fill=(255, 255, 255), anchor="lm")

        chip_cy = fy + 98
        chip(draw, x + 20, chip_cy, 10, story["n"], ACCENT)
        drawn_numbers.add(story["n"])

        draw.text((x + 38, chip_cy), story["kick"], font=font_kicker_feat_sm, fill=ACCENT, anchor="lm")

        head_y = fy + 110
        h_ok, h_rem, head_next = block(
            draw, story["head"], font_head_feat, x + 10, head_y, 297, 17,
            fy + 144)
        check_block(f"featured #{story['n']} headline", h_ok, h_rem)

        summ_y = max(head_next + 3, fy + 146)
        s_ok, s_rem, _ = block(
            draw, story["summ"], font_summ_feat, x + 10, summ_y, 297, 10.6,
            fy + 180)
        check_block(f"featured #{story['n']} summary", s_ok, s_rem)

    feat_bottom = fy + 180

    # 3. Grid (12 cards, 4 cols x 3 rows; card 238 wide, 92 high; x = 24 + col*246)
    grid_rule_y = feat_bottom + 8
    draw.line([24, grid_rule_y, 1000, grid_rule_y], fill=INK, width=1)

    grid_start_y = grid_rule_y + 8
    row_pitch = 102

    font_kicker_grid = get_font(font_sans_bold_path, 8.5)
    font_head_grid = get_font(font_serif_bold_path, 9)
    font_summ_grid = get_font(font_serif_path, 8.5)

    for idx, story in enumerate(STORIES_GRID):
        col = idx % 4
        row = idx // 4
        x = 24 + col * 246
        y0 = grid_start_y + row * row_pitch
        w = 238
        h = 92

        draw.rectangle([x, y0, x + w, y0 + h], fill=CARD, outline=BORDER, width=1)

        banner_h = 40
        c_color = CONTINENT_COLORS.get(story["continent"], ACCENT)
        draw_banner(draw, x, y0, w, banner_h, story["kind"], c_color)

        chip_cy = y0 + 48
        chip(draw, x + 14, chip_cy, 6.5, story["n"], ACCENT)
        drawn_numbers.add(story["n"])

        draw.text((x + 26, chip_cy), story["kick"], font=font_kicker_grid, fill=ACCENT, anchor="lm")

        head_y = y0 + 54
        h_ok, h_rem, head_next = block(
            draw, story["head"], font_head_grid, x + 8, head_y, 222, 11,
            y0 + 68)
        check_block(f"grid #{story['n']} headline", h_ok, h_rem)

        summ_y = head_next + 2
        s_ok, s_rem, _ = block(
            draw, story["summ"], font_summ_grid, x + 8, summ_y, 226, 9.5,
            y0 + 90)
        check_block(f"grid #{story['n']} summary", s_ok, s_rem)

    grid_bottom = grid_start_y + 3 * row_pitch - (row_pitch - 92)

    # 4. Bottom Band
    bottom_rule_y = grid_bottom + 8
    draw.line([24, bottom_rule_y, 1000, bottom_rule_y], fill=INK, width=1)

    bb_top = bottom_rule_y + 8

    map_x = 580
    map_y = bb_top
    map_w = 420
    map_h = 245

    draw.rectangle([map_x, map_y, map_x + map_w, map_y + map_h], fill=CARD, outline=BORDER, width=1)

    def lon_lat_to_xy(lon, lat):
        px = map_x + (lon + 180) / 360.0 * map_w
        py = map_y + (90 - lat) / 180.0 * map_h
        return px, py

    # Graticule first, land on top so the landmasses read as solid shapes.
    for lon in range(-120, 180, 60):
        lx, _ = lon_lat_to_xy(lon, 0)
        draw.line([lx, map_y, lx, map_y + map_h], fill=(225, 220, 210), width=1)
    for lat in range(-60, 90, 30):
        _, ly = lon_lat_to_xy(0, lat)
        draw.line([map_x, ly, map_x + map_w, ly], fill=(225, 220, 210), width=1)

    # Simplified coastlines on a real-world layout: the Americas on the left,
    # Europe/Africa in the centre, Asia on the right, Australia lower right.
    LAND_POLYGONS = [
        # North America (Alaska to Panama)
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
        # Eurasia (Iberia to Chukotka, with Arabia, India and SE Asia)
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
        # Japan (Honshu)
        [(130, 32), (133, 34), (136, 35), (139, 35), (141, 36), (142, 39),
         (141, 41), (143, 44), (145, 43), (142, 40), (139, 36), (136, 35),
         (133, 34), (131, 33)],
        # Kyushu / Shikoku
        [(129, 31), (132, 33), (134, 33), (131, 30)],
        # Hokkaido
        [(140, 42), (145, 44), (145, 45), (140, 44)],
        # Philippines
        [(120, 18), (124, 18), (126, 10), (122, 6), (120, 10)],
        # Indonesia and New Guinea
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
        # Cook Islands (Rarotonga)
        [(-161, -20), (-159, -20), (-159, -22), (-161, -22)],
        # Cuba / Hispaniola
        [(-84, 22.5), (-74, 20), (-77, 23.5), (-84, 23.5)],
        # Sri Lanka
        [(80, 6), (82, 7), (82, 9), (80, 9)],
        # Italy
        [(6, 44), (10, 46), (13, 46), (13, 44), (16, 41.5), (18, 40),
         (16, 38), (15.5, 38), (13, 41), (12, 42), (10, 43), (8, 44)],
        # Korea
        [(124, 38.5), (127, 38.5), (129, 38), (129, 35), (126, 34),
         (125, 36)],
        # Tasmania
        [(145, -41), (148, -41), (148, -43), (145, -43)],
    ]

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
    CELL = 3.0  # degrees per cell
    SUBS = 3    # subsamples per cell axis, so small islands are not missed
    cols = int(round(360.0 / CELL))
    rows = int(round(180.0 / CELL))
    land_cells = 0
    for row in range(rows):
        for col in range(cols):
            hit = False
            for sy in range(SUBS):
                lat_s = 90.0 - (row + (sy + 0.5) / SUBS) * CELL
                for sx in range(SUBS):
                    lon_s = -180.0 + (col + (sx + 0.5) / SUBS) * CELL
                    if any(point_in_poly(lon_s, lat_s, p) for p in LAND_POLYGONS):
                        hit = True
                        break
                if hit:
                    break
            if hit:
                x0, y0 = lon_lat_to_xy(-180.0 + col * CELL,
                                       90.0 - row * CELL)
                x1, y1 = lon_lat_to_xy(-180.0 + (col + 1) * CELL,
                                       90.0 - (row + 1) * CELL)
                # full-cell squares so neighbouring cells merge into solid land
                draw.rectangle([x0, y0, x1, y1], fill=LAND)
                land_cells += 1

    land_pct = 100.0 * land_cells / (cols * rows)
    print(f"Map land cells: {land_cells}/{cols * rows} ({land_pct:.1f}%)")
    assert 20.0 <= land_pct <= 35.0, f"Implausible land coverage: {land_pct:.1f}%"

    all_pins = []
    for s in STORIES_FEATURED:
        if "lon" in s and "lat" in s:
            all_pins.append((s["n"], s["lon"], s["lat"], s["continent"]))
    for s in STORIES_GRID:
        if "lon" in s and "lat" in s:
            all_pins.append((s["n"], s["lon"], s["lat"], s["continent"]))
    for b_num, b_text, b_cont, b_coord in BRIEFS_DATA:
        if b_coord is not None:
            all_pins.append((b_num, b_coord[0], b_coord[1], b_cont))

    font_pin = get_font(font_sans_bold_path, 8)
    for p_num, plon, plat, pcont in all_pins:
        px, py = lon_lat_to_xy(plon, plat)
        ccolor = CONTINENT_COLORS.get(pcont, ACCENT)
        draw.ellipse([px - 5.5, py - 5.5, px + 5.5, py + 5.5], fill=ccolor, outline=(255, 255, 255), width=1)
        t_str = str(p_num)
        tb = draw.textbbox((0, 0), t_str, font=font_pin)
        tw = tb[2] - tb[0]
        th = tb[3] - tb[1]
        draw.text((px - tw/2 - tb[0], py - th/2 - tb[1]), t_str, font=font_pin, fill=(255, 255, 255))

    legend_y = map_y + map_h + 6
    font_legend = get_font(font_sans_bold_path, 8.5)
    lx_curr = map_x
    for c_name, c_col in CONTINENT_COLORS.items():
        draw.rectangle([lx_curr, legend_y, lx_curr + 8, legend_y + 8], fill=c_col)
        draw.text((lx_curr + 11, legend_y - 1), c_name, font=font_legend, fill=INK)
        lx_curr += len(c_name) * 6 + 22

    # Briefs on the LEFT
    briefs_heading_y = bb_top
    font_briefs_head = get_font(font_sans_bold_path, 11)
    draw.text((24, briefs_heading_y), "ALSO ON WEDNESDAY", font=font_briefs_head, fill=ACCENT)

    briefs_start_y = briefs_heading_y + 12
    font_brief = get_font(font_sans_path, 7.2) # font size 7.2
    font_brief_bold = get_font(font_sans_bold_path, 7.2)

    col_width = 126
    col_gap = 10
    briefs_left = 24

    for c_idx in range(4):
        col_x = briefs_left + c_idx * (col_width + col_gap)
        col_items = BRIEFS_DATA[c_idx * 10 : (c_idx + 1) * 10]

        curr_y = briefs_start_y
        for b_num, b_text, b_cont, b_coord in col_items:
            drawn_numbers.add(b_num)
            num_str = f"{b_num}. "
            full_text = f"{b_num}. {b_text}"
            lines = wrap(full_text, font_brief, col_width, draw)
            for line_idx, line in enumerate(lines):
                if curr_y + 8.5 > 965:
                    clip_failures += 1
                if line_idx == 0:
                    draw.text((col_x, curr_y), num_str, font=font_brief_bold, fill=INK)
                    num_w = draw.textlength(num_str, font=font_brief_bold)
                    rest_text = line[len(num_str):]
                    draw.text((col_x + num_w, curr_y), rest_text, font=font_brief, fill=INK)
                else:
                    draw.text((col_x, curr_y), line, font=font_brief, fill=INK)
                curr_y += 8.5
            curr_y += 1.2

    # 5. Footer
    font_footer_1 = get_font(font_serif_italic_path, 10)
    font_footer_2 = get_font(font_sans_path, 8.5)

    footer_text_1 = "Deliberately not today: Peltola's Senate call, the Knesset speaker vote and the Kerch Bridge collapse all happened on 17 November."
    draw.text((512, 970), footer_text_1, font=font_footer_1, fill=INK, anchor="ma")

    footer_text_2 = "Every story happened or was first reported on Wednesday 18 November 2026 · Disputed claims are attributed · Sources: Reuters · AP · AFP · BBC · Al Jazeera · CNN · WHO · UN News"
    draw.text((512, 995), footer_text_2, font=font_footer_2, fill=GREY, anchor="ma")

    print(f"Clip failures (briefs): {clip_failures}")
    print(f"Text blocks checked: {text_blocks_checked}")
    print(f"Text clip failures: {len(text_clip_failures)}")
    print(f"Total stories drawn: {len(drawn_numbers)}")

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

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out_path, "PNG")

    file_size = os.path.getsize(out_path)
    print(f"Saved entry.png: {file_size} bytes")
    assert img.size == (1024, 1024), f"Invalid size {img.size}"
    assert file_size <= 1048576, f"File too large: {file_size} bytes"

if __name__ == "__main__":
    main()
