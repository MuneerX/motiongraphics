# MubarakTech — "Steal the 2-Minute Voice Memo" Motion Graphics Film

A deterministic, high-production motion graphics film created in the **Outship aesthetic** (editorial cream canvas `#FCF8F2`, deep obsidian `#0D0A09`, vibrant terracotta `#DF5A37`, *Instrument Serif italic* accents, floating glass squircles with rim glows, and deterministic Three.js pixel mosaics).

---

## 🎬 Project Overview

* **Title:** MubarakTech — Steal the 2-Minute Voice Memo
* **Aspect Ratio:** 16:9 Widescreen (1920×1080)
* **Frame Rate:** 30 fps
* **Duration:** 53.20 seconds (1,596 frames)
* **Audio Track:** Lossless 48kHz electronic motion graphics soundtrack with bass hits and risers
* **Runtime:** HyperFrames deterministic seek contract (`window.__seek(t)`) + GSAP 3.12.5 + Three.js r128

---

## 📜 Scene Breakdown & Narrative Arc

| Timecode | Scene | Background | Visual Elements & Narrative Beats |
|---|---|---|---|
| **00:00 – 00:03.5** | **S1 Hook** | Cream `#FCF8F2` | "Steal the 2-minute *voice memo* replacing our client's ~~$3,000~~ *assistant*." Terracotta corner pixel mosaics, price strikethrough badge. |
| **00:03.5 – 00:07.5** | **S2 The 2 Hours** | Obsidian `#0D0A09` | "Agency founders lose *two hours* every evening manually transcribing client audio notes." Floating glass voice memo card with active waveform and ClickUp/Notion/Slack chips. |
| **00:07.5 – 00:11.0** | **S3 Exhausting** | Obsidian `#0D0A09` | "It's completely *exhausting*." Driving home scenario $\rightarrow$ "I'll deal with it tomorrow" $\rightarrow$ *And then you forget.* |
| **00:11.0 – 00:14.5** | **S4 3 Days Later** | Obsidian `#0D0A09` | "Three days later... client is furious because nobody started the job." 4 spring-popping red alert pills (`back.out(2.2)`). |
| **00:14.5 – 00:18.0** | **S5 Instead** | Obsidian `#0D0A09` | Terracotta framing brackets `┏ ┛` snap inward around **INSTEAD** $\rightarrow$ Camera zooms into the glowing dark **MubarakTech** brand portal. |
| **00:18.0 – 00:22.5** | **S6 WhatsApp Bot** | Obsidian `#0D0A09` | "Forward that *60-second audio note* to a private bot. In 40s, 3 things happen automatically." Dark glass WhatsApp chat UI receiving audio note. |
| **00:22.5 – 00:27.5** | **S7 Extract & Assign** | Obsidian `#0D0A09` | **Pillar 01:** "Extracts deliverables & assigns with a *hard deadline*." Interactive task card with assignee Alex Rivera, P0 Critical tag, Friday 5 PM deadline. |
| **00:27.5 – 00:32.5** | **S8 Client Recap** | Obsidian `#0D0A09` | **Pillar 02:** "Drafts a client recap for your *one-tap review*." Prepared email modal $\rightarrow$ Purple founder cursor glides in and clicks `[ Approve & Send → ]`. |
| **00:32.5 – 00:37.5** | **S9 Stripe Invoice** | Obsidian `#0D0A09` | **Pillar 03:** "Generates the *Stripe invoice link* automatically." Dark glass Stripe card displaying Invoice #MT-2026-089 for $1,500.00 with live payment link. |
| **00:37.5 – 00:42.5** | **S10 Zero Typing** | Cream `#FCF8F2` | High-contrast split cards: **Zero** *manual typing* (left) and **Zero** *dropped deadlines* (right). |
| **00:42.5 – 00:47.5** | **S11 Comment VOICE** | Obsidian `#0D0A09` | "Stop paying a $3,000 assistant. Tasks a smart automation finishes in *seconds*." Glowing CTA pill: **Comment "VOICE"** to receive the exact template. |
| **00:47.5 – 00:53.2** | **S12 Outro Lockup** | Obsidian `#0D0A09` | Terracotta framing brackets `┏ ┛` framing final lockup: "Steal the *2-minute voice memo*." `mubaraktech.ai` AI-Native Systems & Autonomous Workflows. |

---

## 🛠️ How to View & Preview

### 1. In Browser (Interactive Studio Shell)
Simply open `index.html` in Chrome or Edge:
* **Interactive Player:** Play, pause, scrub with slider, toggle audio, and full-screen preview.
* **Scene Jump Strip:** One-click jump directly to any of the 12 scenes.
* **Responsive Scaling:** Auto-centers and scales the 1920×1080 canvas to any viewport size.

### 2. Headless Frame Capture (Broadcast MP4)
To re-render from source:
```bash
node "../.agents/skills/motionmaxxing/scripts/render.mjs" index.html mubaraktech_voice_master.mp4 --fps 30 --crf 18 --audio audio.wav
```

### 3. Extract Stills
```bash
node "../.agents/skills/motionmaxxing/scripts/render.mjs" index.html --still 1.0,5.0,12.5,16.0,20.0,25.0,30.0,35.0,40.0,45.0,50.0 stills
```

---

## 🎨 Design Rules Implemented
* **Cream Canvas (`#FCF8F2`):** Used for thesis statements, problem intro, and high-contrast result comparison.
* **Obsidian Surfaces (`#0D0A09`):** Used for deep focus, UI demo, and CTA cards.
* **Terracotta Brand Glow (`#DF5A37`):** Applied to keywords, bracket corners, active pills, and rim lighting (`inset 0 1px 18px rgba(223, 90, 55, 0.18)`).
* **Instrument Serif Italic:** Applied exclusively to emotional and punchy emphasis words (*voice memo*, *assistant*, *two hours*, *exhausting*, *hard deadline*, *one-tap review*, *seconds*).
* **Zero Frame Drift:** `renderThreeAt(t)` and `tl.seek(t, false)` guarantee identical pixels regardless of machine performance.
