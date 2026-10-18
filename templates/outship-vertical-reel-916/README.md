# Outship Vertical Reel (9:16) Motion Graphics Template

A modular, deterministic template for building broadcast-quality 1080×1920 (9:16 vertical) product launch, SaaS explainer, and brand reels in the Outship design aesthetic.

---

## Architecture & Specifications

- **Dimensions**: `1080×1920` (9:16 vertical widescreen reel for Reels, Shorts, and TikTok)
- **Framerate**: 30 FPS progressive
- **Color Palette**:
  - Warm Editorial Cream: `#FCF8F2` (primary light canvas)
  - Dark Obsidian: `#0D0A09` (primary dark transition canvas)
  - Signature Terracotta: `#DF5A37` (brand accents, editorial emphasis, active states)
  - Card Surfaces: `#FFFDF9` (cream card) and `#161210` (obsidian dark glass)
  - Stone Muted: `#78716C`
- **Typography**:
  - Headlines & UI: `Plus Jakarta Sans` (500–700 weight)
  - Editorial Accents: `Instrument Serif` (italic 400 weight)
  - Monospace / Terminal / Metrics: `JetBrains Mono`
- **Animation Engine**:
  - GSAP 3.12.5 + `TextPlugin` for real-time letter-by-letter typewriting
  - Three.js r128 deterministic motes & pixel mosaic stage
  - Spring-physics card appearances (`back.out(1.6 - 1.8)`)
  - Smooth overlapping cross-dissolve & directional glide scene transitions (`fadeInT = startT - 0.4s`, `fadeOutT = endT - 0.45s`)
  - Deterministic headless background color tweening across `#canvas-bg` and `#root`

---

## Template Files in this Directory

| File | Description |
|---|---|
| [`template.html`](file:///e:/MubarakTech/motiongraphics/templates/outship-vertical-reel-916/template.html) | Clean, reusable 3-scene starter scaffold with built-in interactive Studio shell, scrubber, and headless render mode. |
| [`generate_html.py`](file:///e:/MubarakTech/motiongraphics/templates/outship-vertical-reel-916/generate_html.py) | Full Python generator script demonstrating how to programmatically compile complex multi-scene vertical compositions. |
| [`mubaraktech_voice_reel_master.html`](file:///e:/MubarakTech/motiongraphics/templates/outship-vertical-reel-916/mubaraktech_voice_reel_master.html) | Production 16-scene 73-second master composition complete with voiceover sync, terminal logs, interactive mockup cards, and kinetic CTA. |
| [`mubaraktech_voice_reel_checkpoint.html`](file:///e:/MubarakTech/motiongraphics/templates/outship-vertical-reel-916/mubaraktech_voice_reel_checkpoint.html) | Initial development snapshot preserved for historical reference. |

---

## How to Render

To render any composition in this template to a broadcast MP4 video using the deterministic headless renderer:

```bash
node "e:/MubarakTech/motiongraphics/.agents/skills/motionmaxxing/scripts/render.mjs" index.html output_master.mp4 --width 1080 --height 1920 --fps 30 --crf 18 --audio audio.wav
```

### Previewing in Browser
Simply open any of the HTML files directly in your web browser. You can play, pause, scrub through the interactive timeline, and jump directly to any scene using the scene pill strip.
