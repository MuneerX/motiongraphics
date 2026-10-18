# MubarakTech — "Steal the 2-Minute Voice Memo" (9:16 Vertical Reel)

A deterministic, high-production 9:16 vertical motion graphics reel built in the **Outship aesthetic** (`#FCF8F2` cream canvas, `#0D0A09` obsidian, `#DF5A37` terracotta, and *Instrument Serif italic* accents) with enhanced 3D perspective, natural English voiceover, and electronic backing audio.

---

## 🎬 Reel Specifications

* **Format:** 9:16 Vertical Reel / Shorts / Story
* **Canvas Resolution:** 1080×1920 portrait
* **Safe Zones:** Top: 220px, Bottom: 320px, Sides: 70px (optimized for Instagram Reels, TikTok, and YouTube Shorts UI overlays)
* **Frame Rate:** 30 fps
* **Duration:** 62.00 seconds (1,860 frames)
* **Voiceover:** Natural English speaking (`en-US-ChristopherNeural`, +22% rate, -1Hz pitch)
* **Soundtrack Bed:** Deep ocean electronic pulse score (`pieces/deep-ocean-pulse/renders/stem-music.wav`), sidechain ducked under the voiceover
* **Audio Master:** 48kHz Stereo Master WAV (`audio.wav`)

---

## 🚀 Enhanced Motion Graphics & 3D Features

1. **Deterministic Three.js 3D Crystals & Polyhedra:**
   * 36 floating 3D faceted icosahedrons and cubes rendered in terracotta (`#DF5A37`) and obsidian glass with specular rim lighting and continuous organic drift.
   * Frame-accurate mathematical positioning `renderThreeAt(t)` with seeded PRNG (`mulberry32`), guaranteeing zero frame drift during headless capture.
2. **Audio Waveform Dynamic Visualizer:**
   * Responsive terracotta waveform equalizer bars that react to voice energy in Scene 1 and Scene 2.
3. **3D Perspective Tilt Cards:**
   * Floating cards and device frames rendered with CSS 3D perspective (`perspective: 1200px; transform: rotateX(...) rotateY(...)`) for depth.
4. **Interactive Software Cursor:**
   * Purple founder cursor (`#7C3AED`) gliding with ease and triggering click ripples on the one-tap recap approval button.
5. **Spring-Physics Alert Pills:**
   * 4 red alert badges popping in with GSAP `back.out(2.5)` spring bounce.

---

## 📜 Scene Breakdown & Timings

| Timecode | Scene | Canvas Ground | Spoken Narration & Motion Graphics |
|---|---|---|---|
| **00:00.10 – 00:04.54** | **S1: Hook** | Cream (`#FCF8F2`) | *"Steal the 2-minute voice memo replacing our client's $3,000 assistant."* Terracotta strikethrough and animated audio waveform bars. |
| **00:04.54 – 00:11.76** | **S2: The 2 Hours** | Obsidian (`#0D0A09`) | *"Agency founders lose two hours every single evening manually transcribing client audio notes..."* 3D tilted card with active audio scrubber and app chips. |
| **00:11.76 – 00:13.77** | **S3: Exhausting** | Obsidian (`#0D0A09`) | *"It's completely exhausting."* Bold kinetic title reveal. |
| **00:13.77 – 00:21.11** | **S4: Driving Home** | Obsidian (`#0D0A09`) | *"You're driving home, a client drops an urgent voice message... And then you forget."* |
| **00:21.11 – 00:25.26** | **S5: 3 Days Later** | Obsidian (`#0D0A09`) | *"Three days later, the client is furious because nobody started the job."* 4 spring-popping red alert pills. |
| **00:25.26 – 00:28.17** | **S6: Instead** | Obsidian (`#0D0A09`) | Terracotta corner framing brackets `┏ ┛` snapping around **INSTEAD** $\rightarrow$ camera zoom into glowing **MubarakTech** portal card. |
| **00:28.17 – 00:35.20** | **S7: WhatsApp Bot** | Obsidian (`#0D0A09`) | *"They forward that 60-second audio note to a private WhatsApp bot..."* 3D phone mockup receiving and parsing the memo in 40s. |
| **00:35.20 – 00:39.92** | **S8: Extract & Assign** | Obsidian (`#0D0A09`) | **Pillar 01:** *"Extracts deliverables and assigns them straight to your team with a hard deadline."* Auto-assigned card with checklist. |
| **00:39.92 – 00:43.49** | **S9: Client Recap** | Obsidian (`#0D0A09`) | **Pillar 02:** *"Drafts a client recap for your one-tap review."* Purple cursor clicks `[ Approve & Send → ]`. |
| **00:43.49 – 00:47.05** | **S10: Stripe Invoice** | Obsidian (`#0D0A09`) | **Pillar 03:** *"Generates the Stripe invoice link automatically."* Dark-glass Stripe card for $1,500.00 ready to pay. |
| **00:47.05 – 00:50.94** | **S11: Zero Typing** | Cream (`#FCF8F2`) | High-contrast split vertical cards: **Zero** *manual typing* & **Zero** *dropped deadlines*. |
| **00:50.94 – 00:55.99** | **S12: $3K Assistant** | Obsidian (`#0D0A09`) | *"Stop paying a $3,000 assistant for tasks a smart automation finishes in seconds."* |
| **00:55.99 – 00:58.79** | **S13: Comment VOICE** | Obsidian (`#0D0A09`) | Glowing pulsating CTA box: **Comment "VOICE"** for the exact template. |
| **00:58.79 – 00:62.00** | **S14: Outro Lockup** | Obsidian (`#0D0A09`) | Terracotta brackets `┏ ┛` framing final lockup: *"Steal the 2-minute voice memo."* `mubaraktech.ai`. |

---

## 🛠️ Viewing & Re-Rendering

* **Interactive Preview:** Open `index.html` in Chrome/Edge. Auto-fits 1080×1920 to window size with interactive scrub bar, scene pills, and audio toggle.
* **Headless Capture:**
  ```bash
  node "../.agents/skills/motionmaxxing/scripts/render.mjs" index.html mubaraktech_voice_reel_916_master.mp4 --width 1080 --height 1920 --fps 30 --crf 18 --audio audio.wav
  ```
