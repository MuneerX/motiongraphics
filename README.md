# Outship Motion Graphics Engine & Templates

A procedural, deterministic motion graphics production system built for high-taste product launch videos, feature reveals, and social reels in the signature **Outship design aesthetic**.

---

## Visual & Motion Design System

- **Color Palette**:
  - Warm Cream Canvas: `#FCF8F2` (editorial print warmth, never stark `#FFFFFF`)
  - Dark Obsidian: `#0D0A09` (deep obsidian ground for technical contrast)
  - Terracotta Brand Accent: `#DF5A37` (hero thesis words, framing brackets, active states)
  - Soft Terracotta: `#F4D7CE`
  - Surfaces: `#FFFDF9` (cream card) and `#161210` (dark glass squircle with terracotta rim glows)
  - Muted Stone: `#78716C`
- **Typography Hierarchy**:
  - Primary UI & Titles: `Plus Jakarta Sans` / `Inter` (500–700 weight)
  - Editorial Accents: `Instrument Serif` (italic 400 weight) for verbs and punchlines
  - Telemetry & Terminal: `JetBrains Mono` for code, tags, and typing metrics
- **Runtime Dynamics**:
  - GSAP 3.12.5 + `TextPlugin` for real-time live typewriting (terminal commands, transcripts, comments)
  - Three.js r128 deterministic particles, pixel mosaic motes, and floating 3D elements
  - Tactile spring physics (`back.out(1.6 - 1.8)`) on badges, alert pills, and card entries
  - Overlapping cross-dissolves and directional glides (`fadeInT = startT - 0.4s`, `fadeOutT = endT - 0.45s`)
  - Deterministic headless background color tweening across `#canvas-bg` and `#root`

---

## Directory Overview

| Directory / File | Description |
|---|---|
| [`templates/`](templates/) | Modular, production-ready templates for both **Vertical 9:16** reels and **Landscape 16:9** films, complete with interactive studio shells and code generators. |
| [`mubaraktech_voice_reel_916/`](mubaraktech_voice_reel_916/) | **Confirmed Production Master**: 73-second 1080×1920 vertical reel ("Steal the 2-minute voice memo replacing our client's $3,000 assistant"), with live terminal telemetry, WhatsApp dispatch UI, and kinetic CTA. Includes `mubaraktech_voice_reel_916_master.mp4`. |
| [`outship_recreation/`](outship_recreation/) | **Original Product Launch Recreation**: 52-second 1920×1080 landscape film ("Hire AI-Native Engineers") with floating tool glass cards, terminal error logs, and candidate perspective IDE. Includes `outship_recreation_master.mp4`. |
| [`.agents/skills/`](.agents/skills/) | Autonomous motion graphics agent skills: `outship-motion` (design system & architecture), `motionmaxxing` (deterministic frame-by-frame renderer and physics curves), and `animate`. |
| [`recordings/`](recordings/) | Screen captures and test recordings. |
| [`fonts/`](fonts/) & [`sfx/`](sfx/) | Bundled typography licenses and procedural audio sound effects. |

---

## Setup & Prerequisites

Ensure [Node.js](https://nodejs.org/) (v18+) is installed. Install Playwright browser dependencies:

```bash
npm install
npx playwright install chromium
```

---

## How to Render

To render any composition deterministically frame-by-frame into broadcast MP4:

### 1. Vertical 9:16 Reel (1080×1920 @ 30 FPS)
```bash
node ".agents/skills/motionmaxxing/scripts/render.mjs" mubaraktech_voice_reel_916/index.html mubaraktech_voice_reel_916/output.mp4 --width 1080 --height 1920 --fps 30 --crf 18 --audio mubaraktech_voice_reel_916/audio.wav
```

### 2. Landscape 16:9 Film (1920×1080 @ 30 FPS)
```bash
node ".agents/skills/motionmaxxing/scripts/render.mjs" outship_recreation/index.html outship_recreation/output.mp4 --width 1920 --height 1080 --fps 30 --crf 18 --audio outship_recreation/audio.wav
```

### 3. Quick Still Previews (No Video Encoding)
```bash
node ".agents/skills/motionmaxxing/scripts/render.mjs" templates/outship-vertical-reel-916/template.html --still 2.0,6.0,12.0 preview_stills --width 1080 --height 1920
```

---

## Interactive Browser Studio

Every composition (`index.html` or `template.html`) is completely self-contained. Open any file directly in Google Chrome, Edge, or Safari to scrub through the timeline, inspect scenes, and preview audio in real time.
