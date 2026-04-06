"""
Generate 5 SVG logos / banner signs for Bayview Specialist Clinic.

Brand palette  (from index.html):
  --color-accent:       #2D5A4A
  --color-accent-light: #3D7A64
  --color-warm:         #C4A77D
  --color-warm-light:   #E8DCC8
  --color-bg:           #FAF9F7
  --color-border:       #E5E2DD

Fonts (from index.html):
  --font-display: 'Instrument Serif', Georgia, serif
  --font-body:    'DM Sans', -apple-system, sans-serif
"""

import os

OUT = os.path.dirname(os.path.abspath(__file__))

# Google Fonts import — same families/weights as index.html
FONTS = """\
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&amp;family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&amp;display=swap');
  </style>"""

SERIF = "'Instrument Serif', Georgia, serif"
SANS  = "'DM Sans', -apple-system, sans-serif"


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# LOGO 1 — Circle Monogram (kept from previous round)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
logo1 = f'''\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 500" width="400" height="500">
{FONTS}
  <defs>
    <linearGradient id="l1bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2D5A4A"/>
      <stop offset="100%" stop-color="#3D7A64"/>
    </linearGradient>
    <linearGradient id="l1gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#C4A77D"/>
      <stop offset="100%" stop-color="#A08968"/>
    </linearGradient>
  </defs>

  <circle cx="200" cy="195" r="175" fill="none" stroke="#2D5A4A" stroke-width="3"/>
  <circle cx="200" cy="195" r="158" fill="url(#l1bg)"/>
  <circle cx="200" cy="195" r="145" fill="none" stroke="#C4A77D" stroke-width="1" opacity="0.5"/>

  <text x="200" y="215" font-family="{SERIF}"
        font-size="170" fill="#FAF9F7"
        text-anchor="middle" font-style="italic">B</text>

  <g transform="translate(318, 62)">
    <rect x="-6" y="-20" width="12" height="40" rx="4" fill="url(#l1gold)"/>
    <rect x="-20" y="-6" width="40" height="12" rx="4" fill="url(#l1gold)"/>
  </g>

  <text x="200" y="405" font-family="{SERIF}"
        font-size="32" fill="#2D5A4A" text-anchor="middle"
        font-style="italic">Bayview</text>

  <line x1="120" y1="418" x2="280" y2="418" stroke="#C4A77D" stroke-width="1"/>

  <text x="200" y="442" font-family="{SANS}"
        font-size="13" fill="#3D7A64" text-anchor="middle"
        letter-spacing="6" font-weight="500">SPECIALIST CLINIC</text>

  <text x="200" y="470" font-family="{SANS}"
        font-size="9" fill="#A08968" text-anchor="middle"
        letter-spacing="3">PSYCHIATRY &amp; HOLISTIC HEALTH</text>
</svg>'''


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# LOGO 2 — Wordmark with Bay Wave (kept from previous round)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
logo2 = f'''\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 250" width="600" height="250">
{FONTS}
  <defs>
    <linearGradient id="l2wave" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#C4A77D"/>
      <stop offset="50%" stop-color="#2D5A4A"/>
      <stop offset="100%" stop-color="#C4A77D"/>
    </linearGradient>
  </defs>

  <!-- White background -->
  <rect width="600" height="250" fill="#FFFFFF"/>

  <text x="300" y="100" font-family="{SERIF}"
        font-size="78" fill="#2D5A4A" text-anchor="middle"
        font-style="italic" letter-spacing="3">Bayview</text>

  <path d="M 80,125 Q 140,110 190,125 T 300,125 T 410,125 T 520,125"
        stroke="url(#l2wave)" stroke-width="3" fill="none"
        stroke-linecap="round"/>

  <text x="300" y="165" font-family="{SANS}"
        font-size="20" fill="#3D7A64" text-anchor="middle"
        letter-spacing="10" font-weight="500">SPECIALIST CLINIC</text>

  <g transform="translate(300, 193)" opacity="0.7">
    <rect x="-1.5" y="-8" width="3" height="16" rx="1" fill="#C4A77D"/>
    <rect x="-8" y="-1.5" width="16" height="3" rx="1" fill="#C4A77D"/>
  </g>

  <text x="300" y="225" font-family="{SANS}"
        font-size="11" fill="#A08968" text-anchor="middle"
        letter-spacing="4" font-weight="400">PSYCHIATRY &amp; HOLISTIC HEALTH</text>
</svg>'''


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# BANNER 3 — "Green Billboard"
# Full deep-green background, huge white clinic name, gold accents,
# phone + address + services — readable from across the street
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
logo3 = f'''\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 360" width="1000" height="360">
{FONTS}
  <defs>
    <linearGradient id="b3bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2D5A4A"/>
      <stop offset="100%" stop-color="#244A3C"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="1000" height="360" fill="url(#b3bg)"/>

  <!-- Thin gold border inset -->
  <rect x="14" y="14" width="972" height="332" rx="4" fill="none"
        stroke="#C4A77D" stroke-width="1.5" opacity="0.4"/>

  <!-- Gold medical cross — left side accent -->
  <g transform="translate(80, 130)">
    <rect x="-8" y="-28" width="16" height="56" rx="4" fill="#C4A77D" opacity="0.7"/>
    <rect x="-28" y="-8" width="56" height="16" rx="4" fill="#C4A77D" opacity="0.7"/>
  </g>

  <!-- "Bayview" — large, dominant -->
  <text x="500" y="145" font-family="{SERIF}"
        font-size="110" fill="#FFFFFF" text-anchor="middle"
        font-style="italic" letter-spacing="5">Bayview</text>

  <!-- Gold divider line -->
  <line x1="200" y1="175" x2="800" y2="175" stroke="#C4A77D" stroke-width="2" opacity="0.6"/>

  <!-- "SPECIALIST CLINIC" -->
  <text x="500" y="218" font-family="{SANS}"
        font-size="30" fill="#FFFFFF" text-anchor="middle"
        letter-spacing="16" font-weight="500">SPECIALIST CLINIC</text>

  <!-- Services line -->
  <text x="500" y="262" font-family="{SANS}"
        font-size="15" fill="#C4A77D" text-anchor="middle"
        letter-spacing="4" font-weight="400">PSYCHIATRY &amp; HOLISTIC HEALTH</text>

  <!-- Bottom info bar -->
  <line x1="140" y1="288" x2="860" y2="288" stroke="#C4A77D" stroke-width="0.5" opacity="0.3"/>

  <!-- Phone -->
  <text x="340" y="320" font-family="{SANS}"
        font-size="18" fill="#FAF9F7" text-anchor="middle"
        letter-spacing="2" font-weight="500">(07) 3392 7078</text>

  <!-- Gold dot separator -->
  <circle cx="500" cy="315" r="3" fill="#C4A77D" opacity="0.6"/>

  <!-- Address -->
  <text x="670" y="320" font-family="{SANS}"
        font-size="14" fill="#FAF9F7" text-anchor="middle"
        letter-spacing="1" font-weight="300" opacity="0.8">10/120 Bloomfield St, Cleveland QLD 4163</text>
</svg>'''


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# BANNER 4 — "Split Panel"
# Left panel: solid green with large "B" monogram + gold cross
# Right panel: white with clinic name, services, contact
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
logo4 = f'''\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 360" width="1000" height="360">
{FONTS}
  <defs>
    <linearGradient id="b4green" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#3D7A64"/>
      <stop offset="100%" stop-color="#2D5A4A"/>
    </linearGradient>
  </defs>

  <!-- White background -->
  <rect width="1000" height="360" fill="#FFFFFF"/>

  <!-- Left green panel -->
  <rect width="300" height="360" fill="url(#b4green)"/>

  <!-- Gold trim on panel edge -->
  <line x1="300" y1="0" x2="300" y2="360" stroke="#C4A77D" stroke-width="3"/>

  <!-- "B" monogram in green panel -->
  <text x="150" y="200" font-family="{SERIF}"
        font-size="180" fill="#FFFFFF" text-anchor="middle"
        font-style="italic" opacity="0.95">B</text>

  <!-- Gold inner border on panel -->
  <rect x="12" y="12" width="276" height="336" rx="3" fill="none"
        stroke="#C4A77D" stroke-width="1" opacity="0.35"/>

  <!-- Gold cross in top-right of green panel -->
  <g transform="translate(252, 42)">
    <rect x="-5" y="-16" width="10" height="32" rx="3" fill="#C4A77D" opacity="0.7"/>
    <rect x="-16" y="-5" width="32" height="10" rx="3" fill="#C4A77D" opacity="0.7"/>
  </g>

  <!-- Right side: Clinic name -->
  <text x="650" y="120" font-family="{SERIF}"
        font-size="82" fill="#2D5A4A" text-anchor="middle"
        font-style="italic" letter-spacing="4">Bayview</text>

  <!-- Gold underline -->
  <line x1="400" y1="145" x2="900" y2="145" stroke="#C4A77D" stroke-width="2"/>

  <!-- "SPECIALIST CLINIC" -->
  <text x="650" y="192" font-family="{SANS}"
        font-size="26" fill="#2D5A4A" text-anchor="middle"
        letter-spacing="14" font-weight="500">SPECIALIST CLINIC</text>

  <!-- Services -->
  <text x="650" y="235" font-family="{SANS}"
        font-size="14" fill="#A08968" text-anchor="middle"
        letter-spacing="3" font-weight="400">PSYCHIATRY &amp; HOLISTIC HEALTH</text>

  <!-- Bottom info section -->
  <line x1="380" y1="265" x2="920" y2="265" stroke="#E5E2DD" stroke-width="1"/>

  <!-- Phone (prominent) -->
  <text x="505" y="305" font-family="{SANS}"
        font-size="22" fill="#2D5A4A" text-anchor="middle"
        letter-spacing="2" font-weight="600">(07) 3392 7078</text>

  <!-- Dot separator -->
  <circle cx="620" cy="300" r="3" fill="#C4A77D"/>

  <!-- Address -->
  <text x="780" y="300" font-family="{SANS}"
        font-size="13" fill="#5a5a5a" text-anchor="middle"
        letter-spacing="1" font-weight="400">10/120 Bloomfield St</text>
  <text x="780" y="320" font-family="{SANS}"
        font-size="13" fill="#5a5a5a" text-anchor="middle"
        letter-spacing="1" font-weight="400">Cleveland QLD 4163</text>
</svg>'''


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# BANNER 5 — "Elegant White"
# Clean white with strong green typography, gold accents,
# centered layout, green top/bottom border bars
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
logo5 = f'''\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 360" width="1000" height="360">
{FONTS}

  <!-- White background -->
  <rect width="1000" height="360" fill="#FAF9F7"/>

  <!-- Top green bar -->
  <rect width="1000" height="18" fill="#2D5A4A"/>
  <!-- Gold accent line below top bar -->
  <rect y="18" width="1000" height="3" fill="#C4A77D"/>

  <!-- Bottom green bar -->
  <rect y="339" width="1000" height="21" fill="#2D5A4A"/>
  <!-- Gold accent line above bottom bar -->
  <rect y="336" width="1000" height="3" fill="#C4A77D"/>

  <!-- Gold medical cross — left of clinic name -->
  <g transform="translate(175, 130)">
    <rect x="-6" y="-22" width="12" height="44" rx="3" fill="#C4A77D"/>
    <rect x="-22" y="-6" width="44" height="12" rx="3" fill="#C4A77D"/>
  </g>

  <!-- "Bayview" — huge, central -->
  <text x="500" y="155" font-family="{SERIF}"
        font-size="105" fill="#2D5A4A" text-anchor="middle"
        font-style="italic" letter-spacing="4">Bayview</text>

  <!-- Gold medical cross — right of clinic name -->
  <g transform="translate(825, 130)">
    <rect x="-6" y="-22" width="12" height="44" rx="3" fill="#C4A77D"/>
    <rect x="-22" y="-6" width="44" height="12" rx="3" fill="#C4A77D"/>
  </g>

  <!-- Gold divider lines flanking "SPECIALIST CLINIC" -->
  <line x1="120" y1="185" x2="330" y2="185" stroke="#C4A77D" stroke-width="1.5"/>
  <line x1="670" y1="185" x2="880" y2="185" stroke="#C4A77D" stroke-width="1.5"/>

  <!-- "SPECIALIST CLINIC" -->
  <text x="500" y="195" font-family="{SANS}"
        font-size="28" fill="#2D5A4A" text-anchor="middle"
        letter-spacing="18" font-weight="500">SPECIALIST CLINIC</text>

  <!-- Services -->
  <text x="500" y="240" font-family="{SANS}"
        font-size="16" fill="#3D7A64" text-anchor="middle"
        letter-spacing="5" font-weight="400">PSYCHIATRY &amp; HOLISTIC HEALTH</text>

  <!-- Thin separator -->
  <line x1="250" y1="262" x2="750" y2="262" stroke="#E5E2DD" stroke-width="1"/>

  <!-- Contact: Phone -->
  <text x="350" y="298" font-family="{SANS}"
        font-size="20" fill="#2D5A4A" text-anchor="middle"
        letter-spacing="2" font-weight="600">(07) 3392 7078</text>

  <!-- Gold dot -->
  <circle cx="500" cy="293" r="3" fill="#C4A77D"/>

  <!-- Contact: Address -->
  <text x="660" y="293" font-family="{SANS}"
        font-size="14" fill="#5a5a5a" text-anchor="middle"
        letter-spacing="1" font-weight="400">10/120 Bloomfield St</text>
  <text x="660" y="313" font-family="{SANS}"
        font-size="14" fill="#5a5a5a" text-anchor="middle"
        letter-spacing="1" font-weight="400">Cleveland QLD 4163</text>
</svg>'''


# ── Write all ────────────────────────────────────────────────────────
logos = {
    "logo1_monogram.svg":       logo1,
    "logo2_wordmark.svg":       logo2,
    "logo3_green_banner.svg":   logo3,
    "logo4_split_banner.svg":   logo4,
    "logo5_white_banner.svg":   logo5,
}

for name, svg in logos.items():
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"  OK  {path}")

print(f"\nDone -- {len(logos)} logos saved to {OUT}")
