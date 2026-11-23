"""Draw the 22 November 2026 world-news front page.

Run:  python3 generate.py

Writes entry.png next to this file: 1024 x 1024, deterministic
(no clock, no network, no randomness), so every run makes the
identical file. All 35 stories were checked against reporting
dated Sunday 22 November 2026.
"""

from PIL import Image, ImageDraw, ImageFont

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
SERIF_B = f"{FONT_DIR}/DejaVuSerif-Bold.ttf"
SANS_B = f"{FONT_DIR}/DejaVuSans-Bold.ttf"
SANS = f"{FONT_DIR}/DejaVuSans.ttf"

W, H = 1024, 1024
INK = (18, 18, 18)
RED = (158, 12, 12)
GREY = (96, 96, 96)
PAPER = (252, 251, 246)
MARGIN = 30

MASTHEAD = "THE WORLD IN ONE DAY"
DATE_LINE = "SUNDAY 22 NOVEMBER 2026"
SUB_LINE = "35 stories from every continent, in one page"

HEADLINES = [
    (
        "CLIMATE  ·  ANTALYA",
        "COP31 COLLAPSES WITHOUT A DEAL",
        "Climate talks end after two weeks with no agreement at all: "
        "the EU rejects a draft that never mentions fossil fuels. "
        "The longest COP ever — the first collapse since 2009.",
    ),
    (
        "UKRAINE  ·  KYIV REGION",
        "DRONE FLATTENS FLATS NEAR KYIV",
        "A Russian drone destroys part of a five-storey block in Dymer; "
        "at least six dead and 14 missing. Kyiv says 186 drones came "
        "overnight — 2,700 this week.",
    ),
]

# (section, title, body)
STORIES = [
    ("EUROPE",
     "EU budget talks stall",
     "Merz and Macron reject the \u20ac1.78tn compromise for the 2028\u201334 EU budget; farm pay splits the bloc."),
    ("EUROPE",
     "France tests M51.3 missile",
     "Paris fires an upgraded intercontinental missile from the submarine Le Vigilant, with Macron watching."),
    ("EUROPE",
     "Sparta II towed from Baltic",
     "A Russian rescue vessel tows the drone-hit cargo ship Sparta II out of Finnish waters; Finland blames Ukraine."),
    ("EUROPE",
     "Poland: two murder plots",
     "Warsaw says Russia twice tried to kill a Ukrainian-American rapper."),
    ("EUROPE",
     "Jet drone enters Moldova twice",
     "A Russian jet drone crosses into Moldovan airspace twice in one night."),
    ("EUROPE",
     "Odesa grid crippled",
     "Russian strikes knock out power lines serving Odesa and nearby districts, Ukrenergo says."),
    ("EUROPE",
     "Supermarket hit in Vyshneve",
     "A Russian drone kills two and hurts others at a supermarket south-west of Kyiv."),
    ("MIDDLE EAST & THE GULF",
     "Iran unveils missile city",
     "The Revolutionary Guards show off a new underground missile base as US bases in Bahrain stay under fire."),
    ("MIDDLE EAST & THE GULF",
     "Bahrain: two hurt in strike",
     "An Iranian attack hits a civilian industrial site in Sitra; Gulf states condemn it."),
    ("MIDDLE EAST & THE GULF",
     "Houthis strike Saudi Arabia",
     "Missiles are intercepted over Riyadh; falling debris damages a tower in the financial district."),
    ("MIDDLE EAST & THE GULF",
     "Gaza: food vehicle hit",
     "An Israeli strike kills three in Gaza City; World Central Kitchen says the vehicle was not its own."),
    ("MIDDLE EAST & THE GULF",
     "Settlers torch 12 vehicles",
     "Israeli settlers burn cars in four West Bank villages; Israel opens an inquiry and Eisenkot calls it terrorism."),
    ("MIDDLE EAST & THE GULF",
     "Lebanon seizes explosives",
     "The army finds 264 kg of C4 and TNT smuggled from Syria and arrests three suspects."),
    ("MIDDLE EAST & THE GULF",
     "Turkey: no Yemen troops decision",
     "Foreign minister Fidan says Ankara has not decided on sending troops to Yemen."),
    ("MIDDLE EAST & THE GULF",
     "Tehran: talks or war",
     "Iran's parliament speaker says Tehran is ready for \u201ceither negotiations or war\u201d."),
    ("AFRICA",
     "Drones hit Khartoum",
     "Four killed as drones strike homes and a UN building in Sudan's capital; the RSF is blamed."),
    ("AFRICA",
     "Mlambo-Ngcuka dies at 71",
     "South Africa's former deputy president and ex-UN Women chief dies."),
    ("ASIA-PACIFIC",
     "Factory fire in Indonesia",
     "A blaze at a candy factory in Cikande kills three workers; 36 are still missing."),
    ("ASIA-PACIFIC",
     "Quake shakes central Japan",
     "A magnitude 5.7 earthquake injures 22 and halts trains in Aichi and Shizuoka."),
    ("ASIA-PACIFIC",
     "Seoul minister quits",
     "South Korea's education minister resigns over an exam-cheating scandal."),
    ("ASIA-PACIFIC",
     "Marine held in Okinawa",
     "A US Marine is arrested on suspicion of murdering a local woman."),
    ("AMERICAS",
     "Democrats hit 258 seats",
     "Hubbard beats Foxx in North Carolina after a recount; Democrats take 258 seats, their biggest since 1992."),
    ("ASIA-PACIFIC",
     "Australia's economy stalls",
     "Business conditions shrink at the fastest pace in five years; flash PMI falls to 46.1."),
    ("ASIA-PACIFIC",
     "Canberra hits back on AUKUS",
     "Australia's defence minister criticises the US budget office over its AUKUS submarine report."),
    ("ASIA-PACIFIC",
     "\u2018Molly\u2019 Meldrum dies at 83",
     "The Australian music icon and Countdown host dies."),
    ("ASIA-PACIFIC",
     "Family tree rewrite?",
     "Monash researchers say the human family tree may need a major overhaul."),
    ("TECHNOLOGY & SCIENCE",
     "Mercury orbiter glitch",
     "ESA reports a thruster glitch as BepiColombo enters orbit around Mercury."),
    ("TECHNOLOGY & SCIENCE",
     "Germany tests kamikaze drones",
     "Germany starts first tactical tests of kamikaze drones in Lithuania and trials Helsing's AI targeting software."),
    ("TECHNOLOGY & SCIENCE",
     "FBI probes database hack",
     "The FBI investigates a reported breach of its national crime database."),
    ("SPORT",
     "Verstappen wins in Vegas",
     "A wild Las Vegas Grand Prix, 35 lead changes; Norris second, Piastri third."),
    ("SPORT",
     "Boca take Sudamericana",
     "Boca Juniors beat Atl\u00e9tico Mineiro 2\u20130 to win the Copa Sudamericana."),
    ("SPORT",
     "Marquez takes title No. 8",
     "Marc Marquez seals his eighth MotoGP world title in Portugal."),
    ("SPORT",
     "Van der Linde wins Macau GT",
     "Kelvin van der Linde takes the Macau GT Cup on the Guia circuit."),
]

FOOTER = ("Sources: Reuters \u00b7 AP \u00b7 CNN \u00b7 AFP \u00b7 Al Jazeera \u00b7 BBC \u00b7 ESA \u00b7 WRI"
          " \u2014 every story above happened or was first reported on Sunday 22 November 2026.")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Wrap text to lines that fit width pixels (greedy, by words)."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def render():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead ---
    f_title = font(SERIF_B, 58)
    d.text((W / 2, 24), MASTHEAD, font=f_title, fill=INK, anchor="ma")
    d.line([(MARGIN, 96), (W - MARGIN, 96)], fill=INK, width=3)
    f_date = font(SANS_B, 27)
    d.text((W / 2, 106), DATE_LINE, font=f_date, fill=RED, anchor="ma")
    f_sub = font(SANS, 14)
    d.text((W / 2, 142), SUB_LINE, font=f_sub, fill=GREY, anchor="ma")
    d.line([(MARGIN, 168), (W - MARGIN, 168)], fill=INK, width=1)

    # --- two headline stories ---
    hx0, hx1 = MARGIN, W / 2 + 8
    hw = W / 2 - MARGIN - 8
    hy = 180
    f_kick = font(SANS_B, 12)
    f_head = font(SERIF_B, 24)
    f_hbody = font(SANS, 13)
    for hx, (kick, head, body) in zip((hx0, hx1), HEADLINES):
        d.text((hx, hy), kick, font=f_kick, fill=RED, anchor="la")
        y = hy + 18
        for line in wrap(d, head, f_head, hw):
            d.text((hx, y), line, font=f_head, fill=INK, anchor="la")
            y += 29
        y += 2
        for line in wrap(d, body, f_hbody, hw)[:3]:
            d.text((hx, y), line, font=f_hbody, fill=INK, anchor="la")
            y += 17
    d.line([(MARGIN, 316), (W - MARGIN, 316)], fill=INK, width=2)

    # --- dense story columns, adaptive sizing so everything fits ---
    col_top, col_bottom = 330, 982
    col_w = 310
    col_x = [MARGIN, MARGIN + col_w + 17, MARGIN + 2 * (col_w + 17)]
    for title_size, body_size in ((13, 11), (12, 10), (11, 10)):
        f_sec = font(SANS_B, 14)
        f_t = font(SANS_B, title_size)
        f_b = font(SANS, body_size)
        t_lh = title_size + 4
        b_lh = body_size + 3
        # measure the whole flow into columns
        cols = [[], [], []]
        cur_col, cur_y = 0, col_top
        cur_section = None
        for section, title, body in STORIES:
            t_lines = wrap(d, title, f_t, col_w)
            b_lines = wrap(d, body, f_b, col_w)[:2]
            need = (26 if section != cur_section else 0) \
                + len(t_lines) * t_lh + len(b_lines) * b_lh + 8
            if cur_y + need > col_bottom and cur_col < 2:
                cur_col += 1
                cur_y = col_top
                cur_section = None
                need = (26 if section != cur_section else 0) \
                    + len(t_lines) * t_lh + len(b_lines) * b_lh + 8
            if cur_y + need > col_bottom:
                break
            cols[cur_col].append((section, title, body, t_lines, b_lines))
            cur_y += need
            cur_section = section
        else:
            # every story placed: draw this sizing
            for cx, items in zip(col_x, cols):
                y = col_top
                seen = None
                for section, title, body, t_lines, b_lines in items:
                    if section != seen:
                        d.text((cx, y), section, font=f_sec, fill=RED, anchor="la")
                        d.line([(cx, y + 19), (cx + col_w, y + 19)], fill=RED, width=1)
                        y += 26
                        seen = section
                    for line in t_lines:
                        d.text((cx, y), line, font=f_t, fill=INK, anchor="la")
                        y += t_lh
                    for line in b_lines:
                        d.text((cx, y), line, font=f_b, fill=INK, anchor="la")
                        y += b_lh
                    y += 8
            break
    else:
        raise RuntimeError("stories do not fit even at smallest size")

    # --- footer ---
    f_foot = font(SANS, 10)
    d.line([(MARGIN, 994), (W - MARGIN, 994)], fill=GREY, width=1)
    d.text((W / 2, 1000), FOOTER, font=f_foot, fill=GREY, anchor="ma")
    return img


def main():
    img = render()
    img.save("entry.png", format="PNG")


if __name__ == "__main__":
    main()
