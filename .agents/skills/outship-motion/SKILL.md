---
name: outship-motion
description: Direct and build premium, deterministic motion graphics films in the Outship design aesthetic (warm cream canvas #FCF8F2, deep obsidian #0D0A09, vibrant terracotta #DF5A37, editorial Instrument Serif italic accents, floating glass squircles with rim glows, spring alert pills, and deterministic Three.js pixel mosaics). Use whenever creating product launch films, SaaS explainers, or brand kinetic typography in this signature high-taste style.
---

# Outship Motion Graphics Design System & Skill

## 1. Aesthetic DNA & Visual Language

The Outship motion design language pairs the warmth and editorial elegance of print with modern devtool precision and punchy motion timing.

### Color Palette
* `--cream: #FCF8F2` — Main canvas background for light scenes (warm editorial cream, never stark #FFFFFF).
* `--cream-card: #FFFDF9` — Foreground card surfaces on cream grounds.
* `--obsidian: #0D0A09` — Primary dark transition background (rich black with warm undertone).
* `--obsidian-card: #161210` — Dark glass squircle surfaces.
* `--terracotta: #DF5A37` — Signature hero brand accent (used on key words, brackets, pills, and active states).
* `--terracotta-soft: #F4D7CE` — Secondary warm accent / badge backgrounds.
* `--terracotta-glow: rgba(223, 90, 55, 0.38)` — Rim lighting on dark glass cards.
* `--ink: #141210` — Primary body text on cream.
* `--muted: #78716C` — Supporting copy, subtitles, file extensions.
* `--alert-red: #F43F5E` — Spring warning badges (`#2D0A0E` background, `#FB7185` text).
* `--badge-green: #DCFCE7` — Success tags (`#15803D` text).
* `--badge-purple: #7C3AED` — Candidate / developer cursors and tags.

### Typography Hierarchy
* **Headlines & Interface:** `Plus Jakarta Sans` (or `Inter`) at 500–700 weight.
* **Editorial Emphasis:** `Instrument Serif` *italic* at 400 weight (applied selectively to verbs, qualifiers, and punchlines like *everyday*, *actually*, *engineering*, *vibe-coding*, *everything*, *analyze*, *best*).
* **Code & Telemetry:** `JetBrains Mono` for file names, prompt typing, terminal commands, and tags.

---

## 2. Deterministic Technical Architecture

To guarantee 100% frame accuracy during headless capture (no frame drops, no audio drift):

1. **Pure Time Function (`renderThreeAt(t)`):**
   * Never accumulate state using `requestAnimationFrame` or `clock.getDelta()`.
   * Mesh coordinates, rotations, and opacities must be pure mathematical functions of timestamp `t` in seconds.
   * Use a seeded PRNG (`mulberry32`) for particle initialization.

2. **Dual-Mode Studio Shell:**
   * **In Browser:** Renders a rich Studio shell with timecode readout, playback transport, audio toggle, and scene jump pills.
   * **In Headless Render (`render.mjs` / Chrome CDP):** Automatically activates `body.headless-render` via `navigator.webdriver`, cleanly hiding all studio UI chrome and rendering the exact 1920×1080 `#root` canvas.

3. **Seek Hooks:**
   * Expose `window.__seek(t)` that seeks the master GSAP timeline `tl.seek(t, false)` and calls `renderThreeAt(t)`.
   * Register `window.__timelines['main'] = tl` and `window.__duration = <seconds>`.
   * Listen for `window.addEventListener('hf-seek', e => window.__seek(e.detail.time))`.

---

## 3. Standard Scene Patterns & Motifs

1. **Floating AI Tool / Integration Squircles:**
   * Dark glass cards (`width: 180-230px`, `border-radius: 42px`) with warm terracotta rim lighting:
     `box-shadow: 0 24px 60px rgba(0,0,0,0.7), inset 0 1px 18px rgba(223, 90, 55, 0.2);`
   * Gentle sinusoidal drift across multiple Z-planes.

2. **Corner Framing Brackets:**
   * Terracotta corner brackets (`┏` and `┛`, `26px` solid) snapping inward to frame a thesis word.

3. **Stacked Signal Cards:**
   * Cascading cards from bottom with category icons and pill subtitles.

4. **Terminal & Spring Alert Badges:**
   * Dark monospace terminal window with `claude code` or automation logs.
   * High-contrast warning pills popping in with `back.out(2.0)` bounce.

5. **Typewriter Prompt & Pixel Mascot:**
   * 8-bit terracotta pixel mascot + monospace prompt bar typing letter-by-letter with a blinking cursor.

6. **Split Showcase Grid:**
   * Left navigation with active terracotta dot indicator gliding vertically between tabs.
   * Right stage displaying interactive UI cards, code diffs, or rubric scores.

7. **Convergence Outro:**
   * Calendar or profile blocks swarming and accelerating outward, leaving a centered terracotta bordered pill (*only the best.*), transitioning into the final brand lockup.

---

## 4. Vertical Reel (9:16) Architecture & Enhanced Techniques

For vertical formats (1080×1920 for Reels, Shorts, and TikTok):

1. **Layout & Safe Margins:**
   * Canvas: `width: 1080px; height: 1920px;`
   * Padding: `padding: 180px 70px 260px;` (260px bottom margin protects against TikTok/Reels captions and UI icons; 180px top margin clears app headers).
   * Intelligent line-balancing: Never leave a single orphaned serif word (e.g. keep `private WhatsApp bot.` together).

2. **Overlapping Scene Transitions:**
   * Avoid sudden 1-frame cuts. Use a 0.4s – 0.55s overlapping cross-fade and directional glide:
     ```javascript
     const fadeInT = isFirst ? sc.start : Math.max(0, sc.start - 0.4);
     const fadeOutT = isLast ? sc.end : sc.end - 0.45;
     tl.fromTo(el, { autoAlpha: 0, y: 35, scale: 0.96 }, { autoAlpha: 1, y: 0, scale: 1.0, duration: 0.55, ease: 'power2.out' }, fadeInT);
     if (!isLast) tl.to(el, { autoAlpha: 0, y: -35, scale: 0.96, duration: 0.5, ease: 'power2.in' }, fadeOutT);
     ```

3. **Deterministic Background Blending:**
   * CSS `transition` does not fire in headless frame-by-frame renders. Animate canvas background colors deterministically via GSAP:
     ```javascript
     tl.to(['#canvas-bg', '#root'], { backgroundColor: sc.bg, duration: 0.5, ease: 'power2.inOut' }, sc.start - 0.25);
     ```

4. **Real-Time Typewriting (GSAP TextPlugin):**
   * Import `TextPlugin.min.js` and register `gsap.registerPlugin(TextPlugin)`.
   * Type quotes, terminal commands, or comment inputs:
     ```javascript
     tl.to('#cmd-line', { text: { value: '$ n8n-dispatch --live', delimiter: '' }, ease: 'none', duration: 1.8 }, startTime);
     ```

5. **Tactile Spring Card Appearances:**
   * Animate hero cards with spring physics:
     ```javascript
     tl.fromTo(card, { scale: 0.88, y: 55, opacity: 0 }, { scale: 1.0, y: 0, opacity: 1, duration: 0.75, ease: 'back.out(1.6)' }, startTime);
     ```

---

## 5. Ready Templates

- **Landscape 16:9 Master Template:** `templates/outship-motion/template.html`
- **Vertical 9:16 Reel Starter Template:** `templates/outship-vertical-reel-916/template.html`
- **Vertical 9:16 Full Production Master:** `templates/outship-vertical-reel-916/mubaraktech_voice_reel_master.html`
- **Vertical 9:16 Code Generator:** `templates/outship-vertical-reel-916/generate_html.py`

---

## 6. Re-rendering Command

Render any composition created with this style into broadcast MP4:
```bash
# For Landscape 16:9:
node "e:\MubarakTech\motiongraphics\.agents\skills\motionmaxxing\scripts\render.mjs" index.html output.mp4 --fps 30 --crf 18 --audio audio.wav

# For Vertical 9:16:
node "e:\MubarakTech\motiongraphics\.agents\skills\motionmaxxing\scripts\render.mjs" index.html output_916.mp4 --width 1080 --height 1920 --fps 30 --crf 18 --audio audio.wav
```
