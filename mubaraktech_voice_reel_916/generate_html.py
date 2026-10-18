# -*- coding: utf-8 -*-
"""
Generates the complete, high-fidelity mubaraktech_voice_reel_916/index.html
incorporating:
1. Smooth, overlapping scene transitions (cinematic cross-dissolves with directional lift).
   Eliminates sudden disappearances or popping frames.
2. GSAP TextPlugin kinetic typography and real-time typewriting animations:
   - S2 Audio quote types out in sync with audio scrubber
   - S6 Terminal command types out with live prompt
   - S8 WhatsApp message flow with typing indicator and response card
   - S15 Social comment box types 'VOICE' letter-by-letter with blinking cursor
   - Kinetic title reveals and spring-emphasis on editorial serif words across all 16 scenes
3. Rich staggered card appearing animations (cards slide up with back.out spring easing).
4. Deterministic GSAP background color tweening between Warm Cream (#FCF8F2) and Dark Obsidian (#0D0A09).
5. Continuous 24-point Hermite 3D camera trajectory syncing Three.js camera and DOM stage with real parallax.
6. 100% audio & script fidelity with natural English voiceover and tactile UI SFX.
"""

import os

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>MubarakTech — 2-Minute Voice Memo (9:16 Vertical Reel)</title>

  <!-- Google Fonts: Instrument Serif, Plus Jakarta Sans, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <!-- GSAP 3.12.5, TextPlugin & Three.js r128 -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/TextPlugin.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

  <style>
    :root {
      --cream: #FCF8F2;
      --cream-card: #FFFDF9;
      --obsidian: #0D0A09;
      --obsidian-card: #161210;
      --obsidian-glass: rgba(22, 18, 16, 0.95);
      --terracotta: #DF5A37;
      --terracotta-soft: #F4D7CE;
      --terracotta-glow: rgba(223, 90, 55, 0.45);
      --ink: #141210;
      --muted: #78716C;
      --purple-cursor: #7C3AED;
      --green-badge: #DCFCE7;
      --green-text: #15803D;
      --yellow-badge: #FEF9C3;
      --yellow-text: #A16207;
      --red-alert: #EF4444;
      --red-bg: #2B0C10;
      --stripe-purple: #635BFF;
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-serif: 'Instrument Serif', Georgia, serif;
      --font-mono: 'JetBrains Mono', monospace;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
    }

    html, body {
      width: 100%;
      height: 100%;
      background: #080706;
      color: #F5F2EB;
      font-family: var(--font-sans);
      overflow: hidden;
    }

    /* HEADLESS RENDER MODE (Clean 1080x1920 without UI chrome) */
    body.headless-render,
    body.headless-render .studio-shell,
    body.headless-render .viewport-area {
      width: 1080px !important;
      height: 1920px !important;
      margin: 0 !important;
      padding: 0 !important;
      overflow: hidden !important;
      background: transparent !important;
    }

    body.headless-render .studio-topbar,
    body.headless-render .scene-strip,
    body.headless-render .studio-controls {
      display: none !important;
    }

    body.headless-render #root {
      position: absolute !important;
      top: 0 !important;
      left: 0 !important;
      width: 1080px !important;
      height: 1920px !important;
      transform: none !important;
      box-shadow: none !important;
    }

    /* STUDIO SHELL */
    .studio-shell {
      display: flex;
      flex-direction: column;
      width: 100vw;
      height: 100vh;
    }

    .studio-topbar {
      height: 48px;
      background: #12100E;
      border-bottom: 1px solid rgba(255,255,255,0.08);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 16px;
      z-index: 100;
      flex-shrink: 0;
    }

    .studio-brand {
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 13px;
      font-weight: 600;
      letter-spacing: -0.01em;
    }

    .studio-logo-img {
      height: 22px;
      width: auto;
      object-fit: contain;
    }

    .studio-badge {
      background: rgba(223, 90, 55, 0.16);
      color: #FF7A59;
      border: 1px solid rgba(223, 90, 55, 0.35);
      padding: 2px 8px;
      border-radius: 99px;
      font-size: 11px;
      font-family: var(--font-mono);
    }

    /* SCENE JUMP STRIP */
    .scene-strip {
      height: 38px;
      background: #0D0B0A;
      border-bottom: 1px solid rgba(255,255,255,0.06);
      display: flex;
      align-items: center;
      gap: 4px;
      padding: 0 12px;
      overflow-x: auto;
      scrollbar-width: none;
      flex-shrink: 0;
    }
    .scene-strip::-webkit-scrollbar { display: none; }

    .scene-pill {
      background: rgba(255,255,255,0.04);
      border: 1px solid rgba(255,255,255,0.08);
      color: #A8A29E;
      font-size: 11px;
      padding: 4px 10px;
      border-radius: 6px;
      white-space: nowrap;
      cursor: pointer;
      font-family: var(--font-mono);
      transition: all 0.15s ease;
    }
    .scene-pill:hover {
      background: rgba(255,255,255,0.08);
      color: #fff;
    }
    .scene-pill.active {
      background: rgba(223, 90, 55, 0.2);
      border-color: var(--terracotta);
      color: #FF7A59;
      font-weight: 600;
    }

    /* VIEWPORT STAGE WRAPPER */
    .viewport-area {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #080706;
      position: relative;
      overflow: hidden;
    }

    /* HYPERFRAMES COMPOSITION ROOT (1080x1920 9:16 VERTICAL) */
    #root {
      position: relative;
      width: 1080px;
      height: 1920px;
      background-color: var(--cream);
      overflow: hidden;
      transform-origin: center center;
      box-shadow: 0 40px 100px rgba(0,0,0,0.9), 0 0 0 1px rgba(255,255,255,0.1);
      perspective: 1400px;
    }

    /* DYNAMIC FULL-BLEED CANVAS BACKGROUND */
    #canvas-bg {
      position: absolute;
      inset: 0;
      width: 1080px;
      height: 1920px;
      background-color: var(--cream);
      z-index: 0;
      overflow: hidden;
    }

    #three-stage {
      position: absolute;
      inset: 0;
      width: 1080px;
      height: 1920px;
      pointer-events: none;
      z-index: 2;
    }

    /* DYNAMIC 3D DOM STAGE */
    #dom-stage-3d {
      position: absolute;
      inset: 0;
      width: 1080px;
      height: 1920px;
      transform-style: preserve-3d;
      will-change: transform;
      z-index: 5;
    }

    /* SCENE LAYERS - Smooth cross-fade targets */
    .scene-layer {
      position: absolute;
      inset: 0;
      width: 1080px;
      height: 1920px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 180px 70px 260px 70px;
      opacity: 0;
      visibility: hidden;
      transform-style: preserve-3d;
      will-change: transform, opacity;
      background: transparent !important;
      pointer-events: none;
    }
    .scene-layer.active-layer {
      pointer-events: auto;
    }

    /* TYPOGRAPHY HELPERS */
    .editorial-serif {
      font-family: var(--font-serif);
      font-style: italic;
      font-weight: 400;
      display: inline-block;
      transform-origin: center center;
    }

    .hero-title {
      font-size: 60px;
      line-height: 1.22;
      letter-spacing: -0.03em;
      font-weight: 700;
      text-align: center;
      color: #F7F4EE;
      max-width: 880px;
      margin: 0 auto;
      word-break: keep-all;
      overflow-wrap: break-word;
      will-change: transform, opacity;
    }

    .hero-title.dark {
      color: var(--ink);
    }

    .hero-subtitle {
      font-size: 24px;
      color: #A8A29E;
      margin-top: 14px;
      max-width: 820px;
      line-height: 1.4;
      text-align: center;
      will-change: transform, opacity;
    }

    .hero-subtitle.dark {
      color: #78716C;
    }

    .category-badge {
      font-family: var(--font-mono);
      font-size: 15px;
      letter-spacing: 0.12em;
      font-weight: 700;
      margin-bottom: 16px;
      display: inline-block;
      will-change: transform, opacity;
    }

    .text-terracotta {
      color: var(--terracotta);
    }

    /* SUBTLE PIXEL PATTERNS */
    .pixel-grid-bg {
      position: absolute;
      inset: 0;
      background-image:
        linear-gradient(to right, rgba(20,18,16,0.035) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(20,18,16,0.035) 1px, transparent 1px);
      background-size: 32px 32px;
      pointer-events: none;
      transition: opacity 0.4s ease;
    }

    /* 3D GLASS SURFACES */
    .glass-card-obsidian {
      background: var(--obsidian-glass);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 36px;
      box-shadow: 0 30px 80px rgba(0,0,0,0.7), inset 0 1px 24px rgba(223, 90, 55, 0.22);
      backdrop-filter: blur(24px);
      color: #F5F2EB;
      position: relative;
    }

    .glass-card-cream {
      background: var(--cream-card);
      border: 1.5px solid rgba(20, 18, 16, 0.1);
      border-radius: 36px;
      box-shadow: 0 30px 70px rgba(20, 18, 16, 0.08), 0 10px 24px rgba(223, 90, 55, 0.05);
      color: var(--ink);
      position: relative;
    }

    /* 3D FLOAT TILTING CONTAINERS */
    .card-anim-wrapper {
      transform-style: preserve-3d;
      will-change: transform, opacity;
      width: 100%;
      display: flex;
      justify-content: center;
    }

    .card-3d-float {
      transform-style: preserve-3d;
      will-change: transform;
    }

    /* SPRING ALERT BADGES */
    .alert-badge {
      display: inline-flex;
      align-items: center;
      gap: 14px;
      background: var(--red-bg);
      border: 1.5px solid rgba(239, 68, 68, 0.65);
      color: #FCA5A5;
      font-family: var(--font-mono);
      font-size: 20px;
      font-weight: 600;
      padding: 16px 26px;
      border-radius: 999px;
      box-shadow: 0 16px 40px rgba(239, 68, 68, 0.45);
      transform-origin: center center;
      will-change: transform, opacity;
    }

    /* CORNER FRAMING BRACKETS */
    .corner-bracket {
      position: absolute;
      width: 60px;
      height: 60px;
      border-color: var(--terracotta);
      border-style: solid;
      pointer-events: none;
      will-change: transform, opacity;
    }
    .bracket-tl { top: -20px; left: -20px; border-width: 6px 0 0 6px; }
    .bracket-br { bottom: -20px; right: -20px; border-width: 0 6px 6px 0; }

    /* STUDIO PLAYBAR CONTROLS */
    .studio-controls {
      height: 52px;
      background: #12100E;
      border-top: 1px solid rgba(255,255,255,0.08);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 20px;
      z-index: 100;
      flex-shrink: 0;
    }

    .ctrl-group {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .ctrl-btn {
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.12);
      color: #F5F2EB;
      font-family: var(--font-mono);
      font-size: 12px;
      padding: 6px 14px;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .ctrl-btn:hover {
      background: rgba(255,255,255,0.12);
      border-color: rgba(255,255,255,0.25);
    }
    .ctrl-btn.primary {
      background: var(--terracotta);
      border-color: var(--terracotta);
      color: #fff;
      font-weight: 600;
    }

    .time-slider {
      flex: 1;
      max-width: 500px;
      margin: 0 16px;
      accent-color: var(--terracotta);
      cursor: pointer;
    }

    .time-readout {
      font-family: var(--font-mono);
      font-size: 13px;
      color: #A8A29E;
      min-width: 140px;
      text-align: right;
    }

    /* SCENE SPECIFIC STYLES */
    .s1-strikethrough {
      position: relative;
      display: inline;
      color: #9CA3AF;
    }
    .s1-strikethrough::after {
      content: '';
      position: absolute;
      left: -6px;
      right: -6px;
      top: 52%;
      height: 6px;
      background: var(--terracotta);
      transform: rotate(-6deg);
      border-radius: 3px;
    }

    .audio-waveform-container {
      display: flex;
      align-items: center;
      gap: 6px;
      height: 52px;
      margin-top: 32px;
    }
    .wave-bar {
      width: 6px;
      background: var(--terracotta);
      border-radius: 3px;
      transform-origin: bottom;
    }

    /* FLOATING APP CARDS (Scene 2) */
    .floating-tool-card {
      position: absolute;
      background: rgba(24, 18, 16, 0.94);
      border: 1px solid rgba(223, 90, 55, 0.35);
      border-radius: 20px;
      padding: 16px 22px;
      box-shadow: 0 16px 40px rgba(0,0,0,0.6), 0 0 24px rgba(223, 90, 55, 0.15);
      backdrop-filter: blur(16px);
      display: flex;
      align-items: center;
      gap: 14px;
      font-family: var(--font-mono);
      font-size: 14px;
      color: #E7E5E4;
      pointer-events: none;
      z-index: 10;
      will-change: transform, opacity;
    }

    /* SCENE 3: FATIGUE SYNTAX TOKENS */
    .fatigue-token {
      position: absolute;
      padding: 12px 20px;
      border-radius: 14px;
      font-family: var(--font-mono);
      font-size: 16px;
      font-weight: 700;
      pointer-events: none;
      box-shadow: 0 12px 30px rgba(0,0,0,0.08);
      z-index: 10;
      will-change: transform, opacity;
    }

    /* CARPLAY DASHBOARD (Scene 4) */
    .carplay-dashboard {
      width: 860px;
      background: #110E0C;
      border: 1px solid rgba(255,255,255,0.14);
      border-radius: 32px;
      box-shadow: 0 40px 100px rgba(0,0,0,0.85), inset 0 1px 20px rgba(223,90,55,0.15);
      overflow: hidden;
      will-change: transform, opacity;
    }

    /* LETTERBOX CURTAINS (Scene 5) */
    .pixel-curtain {
      position: absolute;
      left: 0;
      right: 0;
      height: 180px;
      background: var(--obsidian);
      z-index: 20;
      pointer-events: none;
      display: flex;
      align-items: center;
      justify-content: center;
      will-change: transform;
    }
    .curtain-top { top: 0; border-bottom: 3px solid var(--terracotta); }
    .curtain-bottom { bottom: 0; border-top: 3px solid var(--terracotta); }

    /* TERMINAL WINDOW (Scene 6) */
    .terminal-window {
      width: 860px;
      background: #110E0C;
      border: 1px solid rgba(255,255,255,0.14);
      border-radius: 28px;
      box-shadow: 0 40px 100px rgba(0,0,0,0.9), 0 0 60px rgba(239,68,68,0.2);
      overflow: hidden;
      font-family: var(--font-mono);
      text-align: left;
      will-change: transform, opacity;
    }
    .terminal-header {
      background: #1A1513;
      padding: 14px 22px;
      display: flex;
      align-items: center;
      gap: 12px;
      border-bottom: 1px solid rgba(255,255,255,0.08);
    }
    .terminal-dot {
      width: 12px;
      height: 12px;
      border-radius: 50%;
    }
    .terminal-dot.red { background: #EF4444; }
    .terminal-dot.yellow { background: #F59E0B; }
    .terminal-dot.green { background: #10B981; }

    /* WHATSAPP PHONE MOCKUP (Scene 8) */
    .phone-mockup-light {
      width: 820px;
      background: #FFFFFF;
      border-radius: 46px;
      border: 4px solid #D6D3CD;
      box-shadow: 0 40px 100px rgba(20,18,16,0.15), 0 0 50px rgba(223,90,55,0.1);
      overflow: hidden;
      margin-top: 26px;
      transform-style: preserve-3d;
      color: var(--ink);
      will-change: transform, opacity;
    }
    .phone-notch-light {
      width: 180px;
      height: 24px;
      background: #1F2937;
      border-radius: 0 0 16px 16px;
      margin: 0 auto;
    }

    /* SCENE 10: 3 STACKED ENGINEERING CARDS */
    .eng-stack-container {
      display: flex;
      flex-direction: column;
      gap: 18px;
      width: 860px;
      z-index: 6;
      margin-top: 36px;
    }
    .eng-signal-card {
      background: rgba(254, 252, 248, 0.98);
      border: 1.5px solid rgba(20, 18, 16, 0.08);
      border-radius: 22px;
      padding: 22px 32px;
      display: flex;
      align-items: center;
      gap: 22px;
      box-shadow: 0 16px 40px rgba(20, 18, 16, 0.08);
      text-align: left;
      will-change: transform, opacity;
    }
    .eng-signal-icon {
      width: 52px;
      height: 52px;
      border-radius: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      flex-shrink: 0;
    }

    /* SCENE 11: MACOS EMAIL WINDOW ON CREAM */
    .macos-mail-window {
      width: 860px;
      background: #FFFDF9;
      border: 1.5px solid rgba(20, 18, 16, 0.12);
      border-radius: 26px;
      box-shadow: 0 35px 80px rgba(20, 18, 16, 0.12);
      overflow: hidden;
      text-align: left;
      will-change: transform, opacity;
    }
    .macos-window-header {
      background: #F5EFE6;
      padding: 14px 22px;
      display: flex;
      align-items: center;
      gap: 12px;
      border-bottom: 1px solid rgba(20, 18, 16, 0.08);
    }

    /* TYPING INDICATOR DOTS */
    .typing-bubble {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #E2E8F0;
      padding: 14px 20px;
      border-radius: 18px 18px 18px 4px;
      align-self: flex-start;
      margin-top: 6px;
    }
    .typing-dot {
      width: 8px;
      height: 8px;
      background: #64748B;
      border-radius: 50%;
      animation: typingBounce 1.2s infinite ease-in-out;
    }
    .typing-dot:nth-child(2) { animation-delay: 0.2s; }
    .typing-dot:nth-child(3) { animation-delay: 0.4s; }
    @keyframes typingBounce {
      0%, 80%, 100% { transform: translateY(0); opacity: 0.4; }
      40% { transform: translateY(-6px); opacity: 1; }
    }

    /* AUTOMATION PIPELINE (Scene 9) */
    .pipeline-container {
      width: 860px;
      padding: 40px 36px;
      display: flex;
      flex-direction: column;
      gap: 24px;
      text-align: left;
    }
    .pipeline-stage {
      display: flex;
      align-items: center;
      gap: 20px;
      background: rgba(255,255,255,0.04);
      border: 1px solid rgba(255,255,255,0.08);
      padding: 18px 24px;
      border-radius: 20px;
      position: relative;
      overflow: hidden;
      will-change: transform, opacity;
    }
    .pipeline-stage.active {
      border-color: rgba(223,90,55,0.5);
      background: rgba(223,90,55,0.08);
      box-shadow: 0 0 30px rgba(223,90,55,0.2);
    }

    /* COMPARISON MATRIX (Scene 14) */
    .comparison-matrix {
      width: 880px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      margin-top: 32px;
    }
    .comparison-col {
      background: rgba(20, 16, 14, 0.95);
      border-radius: 28px;
      padding: 36px 30px;
      display: flex;
      flex-direction: column;
      gap: 18px;
      text-align: left;
      border: 1px solid rgba(255,255,255,0.1);
      will-change: transform, opacity;
    }
    .comparison-col.winner {
      border-color: rgba(223,90,55,0.5);
      background: rgba(28, 20, 17, 0.95);
      box-shadow: 0 0 60px rgba(223,90,55,0.25);
    }

    /* SOFTWARE CURSOR */
    .software-cursor {
      position: absolute;
      display: flex;
      align-items: center;
      gap: 10px;
      z-index: 1000;
      pointer-events: none;
      will-change: transform, opacity;
    }
    .cursor-tag {
      background: var(--purple-cursor);
      color: #fff;
      font-family: var(--font-mono);
      font-size: 15px;
      font-weight: 600;
      padding: 5px 12px;
      border-radius: 8px;
      box-shadow: 0 6px 16px rgba(124,58,237,0.4);
    }

    /* COMMENT INPUT BOX (Scene 15) */
    .comment-card-cream {
      width: 860px;
      background: #FFFDF9;
      border: 1.5px solid rgba(223,90,55,0.35);
      border-radius: 32px;
      padding: 48px 40px;
      box-shadow: 0 30px 80px rgba(20,18,16,0.1), 0 0 60px rgba(223,90,55,0.15);
      display: flex;
      flex-direction: column;
      gap: 24px;
      text-align: left;
      color: var(--ink);
      will-change: transform, opacity;
    }
    .comment-input-box-light {
      background: #F5EFE6;
      border: 2px solid rgba(223,90,55,0.5);
      border-radius: 18px;
      padding: 22px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-family: var(--font-mono);
      font-size: 26px;
      color: var(--ink);
      box-shadow: 0 4px 20px rgba(223,90,55,0.1);
    }
    .comment-cursor-blink {
      display: inline-block;
      width: 3px;
      height: 32px;
      background: var(--terracotta);
      vertical-align: middle;
      animation: blink 0.8s infinite;
    }
    @keyframes blink {
      0%, 100% { opacity: 1; }
      50% { opacity: 0; }
    }
  </style>
</head>
<body>

<div class="studio-shell">
  <!-- Topbar -->
  <header class="studio-topbar">
    <div class="studio-brand">
      <img src="assets/logo_light_text.png" alt="Mubarak Technologies" class="studio-logo-img" />
      <span style="color:rgba(255,255,255,0.3)">/</span>
      <span style="font-weight:400; color:#A8A29E">2-Minute Voice Memo</span>
      <span class="studio-badge">9:16 VERTICAL REEL</span>
    </div>
    <div style="font-size:12px; font-family:var(--font-mono); color:#78716C">
      1080×1920 • HyperFrames + Three.js
    </div>
  </header>

  <!-- Scene Jump Strip -->
  <nav class="scene-strip" id="scene-strip">
    <!-- Injected by JS -->
  </nav>

  <!-- Viewport Stage Wrapper -->
  <main class="viewport-area" id="viewport-area">
    <div id="root" data-composition-id="main" data-start="0" data-duration="73.08" data-width="1080" data-height="1920">
      <!-- Dynamic Full-Bleed Canvas Background -->
      <div id="canvas-bg">
        <div class="pixel-grid-bg" id="canvas-pixel-grid" style="opacity: 1;"></div>
      </div>

      <!-- Three.js Stage Background (Floating 3D Crystals, Rotating Torus Rings, Particle Motes) -->
      <div id="three-stage"></div>

      <!-- Synchronized Continuous 3D DOM Stage -->
      <div id="dom-stage-3d">

        <!-- ================= SCENE 1: HOOK (00:00.00 - 00:05.45) [CANVAS: WARM CREAM] ================= -->
        <section class="scene-layer" id="s1">
          <div class="card-anim-wrapper" id="s1-anim">
            <div class="card-3d-float glass-card-cream" id="s1-card" style="display:flex; flex-direction:column; align-items:center; text-align:center; width:860px; padding:48px 40px; border-color:rgba(20,18,16,0.12); position:relative;">
              <div class="corner-bracket bracket-tl" id="s1-br-tl" style="border-color:var(--terracotta);"></div>
              <div class="corner-bracket bracket-br" id="s1-br-br" style="border-color:var(--terracotta);"></div>
              <div style="margin-bottom:28px;" id="s1-logo">
                <img src="assets/logo.png" alt="Mubarak Technologies" style="height:48px; width:auto; object-fit:contain;" />
              </div>
              <div class="category-badge" id="s1-tag" style="color:var(--terracotta); background:rgba(223,90,55,0.1); border:1px solid rgba(223,90,55,0.25); padding:6px 20px; border-radius:99px; margin-bottom:24px;">
                CASE STUDY: AUTONOMOUS WORKFLOW
              </div>
              <h1 class="hero-title dark" id="s1-title" style="font-size: 64px; line-height: 1.22;">
                Steal the 2-minute <span class="editorial-serif text-terracotta" id="s1-serif-1" style="font-size: 84px;">voice&nbsp;memo</span> replacing our&nbsp;client's <span class="s1-strikethrough" id="s1-strike">$3,000</span> <span class="editorial-serif" id="s1-serif-2" style="font-size: 76px; color:var(--ink);">assistant.</span>
              </h1>
              <div class="audio-waveform-container" id="s1-waveform"></div>
            </div>
          </div>
        </section>

        <!-- ================= SCENE 2: 2 HOURS GRIND (00:05.45 - 00:15.35) [CANVAS: DARK OBSIDIAN] ================= -->
        <section class="scene-layer" id="s2">
          <div style="display:flex; flex-direction:column; align-items:center; text-align:center; width:100%; position:relative;">
            <div class="category-badge text-terracotta" id="s2-tag">
              THE FOUNDER GRIND
            </div>
            <h2 class="hero-title" id="s2-title" style="font-size: 58px; line-height: 1.28; max-width:820px;">
              Most agency founders lose<br/>
              <span class="editorial-serif text-terracotta" id="s2-serif" style="font-size: 82px;">two hours</span><br/>
              every single&nbsp;evening
            </h2>
            <p class="hero-subtitle" id="s2-sub">
              manually transcribing client audio notes and typing them into project&nbsp;management&nbsp;apps.
            </p>

            <!-- Central Audio Player Cockpit -->
            <div class="card-anim-wrapper" id="s2-anim" style="margin-top: 40px; position:relative;">
              <div class="card-3d-float glass-card-obsidian" id="s2-card" style="width: 860px; padding: 42px; text-align:left; position:relative; z-index:5;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
                  <div style="display:flex; align-items:center; gap:10px;">
                    <span style="font-size:22px;">🎙️</span>
                    <span style="font-family:var(--font-mono); font-size:14px; color:#A8A29E; letter-spacing:0.06em;">INCOMING CLIENT AUDIO</span>
                  </div>
                  <span style="font-family:var(--font-mono); font-size:14px; color:#EF4444; font-weight:700; background:rgba(239,68,68,0.15); padding:4px 12px; border-radius:99px; border:1px solid rgba(239,68,68,0.3);">
                    ● 02:14 UNPROCESSED
                  </span>
                </div>
                <div style="display:flex; align-items:center; gap:20px;">
                  <div style="width:64px; height:64px; border-radius:50%; background:var(--terracotta); display:flex; align-items:center; justify-content:center; font-size:26px; color:#fff; box-shadow:0 8px 24px rgba(223,90,55,0.4);">
                    ▶
                  </div>
                  <div style="flex:1;">
                    <div style="height:10px; background:rgba(255,255,255,0.15); border-radius:6px; position:relative; overflow:hidden;">
                      <div style="position:absolute; left:0; top:0; width:0%; height:100%; background:var(--terracotta);" id="s2-scrubber"></div>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-size:14px; font-family:var(--font-mono); color:#78716C; margin-top:10px;">
                      <span id="s2-time-cur">0:14</span>
                      <span>2:14</span>
                    </div>
                  </div>
                </div>
                <!-- Live Typewritten Audio Transcription -->
                <div style="margin-top:24px; font-size:18px; color:#E7E5E4; font-style:italic; line-height:1.5; min-height:54px;" id="s2-quote"></div>
              </div>

              <!-- 6 Floating Dark-Glass App Cards in 3D Space (Swarm effect) -->
              <div class="floating-tool-card" id="s2-tool-1" style="top: -45px; left: -25px;">
                <span style="font-size:20px;">📐</span>
                <div>
                  <div style="font-weight:700; color:#fff;">Linear Task #402</div>
                  <div style="font-size:12px; color:#A8A29E;">Pending Triage • P0</div>
                </div>
              </div>
              <div class="floating-tool-card" id="s2-tool-2" style="top: -45px; right: -25px;">
                <span style="font-size:20px;">💬</span>
                <div>
                  <div style="font-weight:700; color:#fff;">Slack Audio Note</div>
                  <div style="font-size:12px; color:#A8A29E;">Sarah: 02:14 m4a</div>
                </div>
              </div>
              <div class="floating-tool-card" id="s2-tool-3" style="bottom: -40px; left: -15px;">
                <span style="font-size:20px;">⏱️</span>
                <div>
                  <div style="font-weight:700; color:#F59E0B;">ClickUp Timer</div>
                  <div style="font-size:12px; color:#A8A29E;">01h 48m typing...</div>
                </div>
              </div>
              <div class="floating-tool-card" id="s2-tool-4" style="bottom: -40px; right: -15px;">
                <span style="font-size:20px;">📝</span>
                <div>
                  <div style="font-weight:700; color:#fff;">Notion Doc</div>
                  <div style="font-size:12px; color:#A8A29E;">Audio Transcription</div>
                </div>
              </div>
              <div class="floating-tool-card" id="s2-tool-5" style="top: 130px; left: -45px;">
                <span style="font-size:20px;">📋</span>
                <div>
                  <div style="font-weight:700; color:#fff;">Asana Sprint</div>
                  <div style="font-size:12px; color:#EF4444;">Overdue Backlog</div>
                </div>
              </div>
              <div class="floating-tool-card" id="s2-tool-6" style="top: 130px; right: -45px;">
                <span style="font-size:20px;">📱</span>
                <div>
                  <div style="font-weight:700; color:#4ADE80;">WhatsApp</div>
                  <div style="font-size:12px; color:#A8A29E;">14 unread memos</div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- ================= SCENE 3: EXHAUSTING (00:15.35 - 00:17.30) [CANVAS: WARM CREAM + SYNTAX SCATTER] ================= -->
        <section class="scene-layer" id="s3">
          <div class="card-anim-wrapper" id="s3-anim" style="position:relative; width:860px;">
            <div class="card-3d-float glass-card-cream" id="s3-card" style="display:flex; flex-direction:column; align-items:center; text-align:center; padding:64px 60px; border-color:rgba(239,68,68,0.3); box-shadow:0 30px 80px rgba(239,68,68,0.15); width:100%; position:relative; z-index:5;">
              <div class="corner-bracket bracket-tl" id="s3-br-tl" style="border-color:#EF4444;"></div>
              <div class="corner-bracket bracket-br" id="s3-br-br" style="border-color:#EF4444;"></div>
              <h2 class="hero-title dark" id="s3-title" style="font-size: 76px; line-height: 1.2;">
                It's completely <span class="editorial-serif text-terracotta" id="s3-serif" style="font-size: 114px; display:inline;">exhausting.</span>
              </h2>
              <div id="s3-badge" style="margin-top: 36px; padding:12px 28px; background:rgba(239,68,68,0.1); border:1px solid rgba(239,68,68,0.25); border-radius:99px; font-family:var(--font-mono); font-size:16px; color:#EF4444; font-weight:700;">
                ⚡ FOUNDER COGNITIVE LOAD: 98% [CRITICAL OVERLOAD]
              </div>
            </div>

            <!-- 5 Exploding 3D Fatigue / Burnout Tokens (Outship Scene 3 Syntax Scatter) -->
            <div class="fatigue-token" id="s3-tok-1" style="background:#FFF1F2; border:1.5px solid #FDA4AF; color:#E11D48; top:-40px; left:10px;">
              { burnout: true }
            </div>
            <div class="fatigue-token" id="s3-tok-2" style="background:#FEF2F2; border:1.5px solid #FCA5A5; color:#DC2626; top:-40px; right:10px;">
              !error: sleep_deprived
            </div>
            <div class="fatigue-token" id="s3-tok-3" style="background:#FFFBEB; border:1.5px solid #FCD34D; color:#D97706; bottom:-45px; left:20px;">
              [ 99+ unread voice notes ]
            </div>
            <div class="fatigue-token" id="s3-tok-4" style="background:#F5F3FF; border:1.5px solid #C4B5FD; color:#7C3AED; bottom:-45px; right:20px;">
              01:42 AM • Still typing...
            </div>
            <div class="fatigue-token" id="s3-tok-5" style="background:#FFF7ED; border:1.5px solid #FDBA74; color:#EA580C; top:110px; right:-50px;">
              ⚡ CPU: 99%
            </div>
          </div>
        </section>

        <!-- ================= SCENE 4: DRIVING HOME (00:17.30 - 00:24.35) [CANVAS: DARK OBSIDIAN + CARPLAY HUD] ================= -->
        <section class="scene-layer" id="s4">
          <div style="display:flex; flex-direction:column; align-items:center; text-align:center; width:100%;">
            <div class="category-badge" id="s4-tag" style="color:#A8A29E;">
              THE LATE-NIGHT PROMISE
            </div>
            <h2 class="hero-title" id="s4-title" style="font-size: 58px; line-height: 1.24; max-width:840px;">
              You're driving home, a client drops an <span class="editorial-serif text-terracotta" id="s4-serif" style="font-size: 76px;">urgent voice&nbsp;message,</span> and you promise yourself you'll deal with it tomorrow&nbsp;morning.
            </h2>

            <div class="card-anim-wrapper" id="s4-anim" style="margin-top:36px; flex-direction:column; align-items:center; gap:20px;">
              <!-- Apple CarPlay Dashboard HUD -->
              <div class="card-3d-float carplay-dashboard" id="s4-car-card" style="width:840px; padding:32px 36px; text-align:left;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
                  <div style="display:flex; align-items:center; gap:12px;">
                    <span style="font-size:26px;">🚗</span>
                    <span style="font-family:var(--font-mono); font-size:14px; color:#A8A29E;">APPLE CARPLAY • HIGHWAY 101</span>
                  </div>
                  <span style="font-family:var(--font-mono); font-size:13px; color:#EF4444; font-weight:700; background:rgba(239,68,68,0.2); padding:4px 12px; border-radius:99px;">
                    URGENT AUDIO MEMO
                  </span>
                </div>
                <div style="background:rgba(255,255,255,0.06); padding:20px; border-radius:18px; border:1px solid rgba(255,255,255,0.08); display:flex; align-items:center; gap:18px;">
                  <div style="width:48px; height:48px; border-radius:50%; background:#EF4444; display:flex; align-items:center; justify-content:center; font-size:22px; color:#fff;" id="s4-mic-pulse">
                    🎙️
                  </div>
                  <div style="flex:1;">
                    <div style="font-weight:700; font-size:18px; color:#fff;">Sarah (VIP Client) • 0:58 Audio Note</div>
                    <div style="font-size:13px; color:#A8A29E; font-family:var(--font-mono); margin-top:2px;">"Need the checkout overhauled and webhooks fixed today..."</div>
                  </div>
                </div>
              </div>

              <div style="font-size:32px; color:var(--terracotta); opacity:0.8;" id="s4-arrow">↓</div>

              <div class="card-3d-float glass-card-obsidian" id="s4-bubble-card" style="width:840px; padding:24px 36px; border-color:rgba(223,90,55,0.3); text-align:left; display:flex; align-items:center; gap:16px;">
                <span style="font-size:26px;">🧠</span>
                <div style="font-size:17px; color:#D6D3D1;">
                  "I'll deal with it tomorrow morning." <span style="color:#78716C;">(Zero tickets created, left in your head)</span>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- ================= SCENE 5: AND THEN YOU FORGET (00:24.35 - 00:25.85) [CANVAS: WARM CREAM + CURTAINS] ================= -->
        <section class="scene-layer" id="s5">
          <div class="pixel-curtain curtain-top" id="s5-curtain-t"></div>
          <div class="pixel-curtain curtain-bottom" id="s5-curtain-b"></div>

          <div class="card-anim-wrapper" id="s5-anim">
            <div class="card-3d-float glass-card-cream" id="s5-forget-card" style="width:860px; padding:60px 40px; border-color:rgba(223,90,55,0.4); box-shadow:0 30px 80px rgba(223,90,55,0.15); text-align:center; position:relative;">
              <div class="corner-bracket bracket-tl" id="s5-br-tl" style="border-color:var(--terracotta);"></div>
              <div class="corner-bracket bracket-br" id="s5-br-br" style="border-color:var(--terracotta);"></div>
              <h2 class="hero-title dark" id="s5-title" style="font-size: 78px;">
                <span class="editorial-serif text-terracotta" id="s5-serif" style="font-size: 104px;">And then you&nbsp;forget.</span>
              </h2>
              <div id="s5-sub" style="margin-top:20px; font-family:var(--font-mono); font-size:16px; color:#78716C;">
                ⏰ 3 DAYS ELAPSED • 0 ACTIONS TAKEN
              </div>
            </div>
          </div>
        </section>

        <!-- ================= SCENE 6: 3 DAYS CRISIS (00:25.85 - 00:30.70) [CANVAS: DARK OBSIDIAN + DEV TERMINAL] ================= -->
        <section class="scene-layer" id="s6">
          <div style="display:flex; flex-direction:column; align-items:center; text-align:center; width:100%;">
            <div class="category-badge" id="s6-tag" style="color:#EF4444;">
              THE INEVITABLE CRISIS
            </div>
            <h2 class="hero-title" id="s6-title" style="font-size: 60px; margin-top:12px; line-height: 1.24;">
              <span class="editorial-serif" id="s6-serif" style="color:#F87171; font-size:80px;">Three days&nbsp;later,</span> the client is furious because nobody started the&nbsp;job.
            </h2>

            <div class="card-anim-wrapper" id="s6-anim" style="position:relative; width:880px; height:460px; margin-top:36px;">
              <div class="card-3d-float" style="position:absolute; width:100%; height:100%; display:flex; justify-content:center;">
                <!-- Realistic Terminal Window -->
                <div class="terminal-window" id="s6-terminal">
                  <div class="terminal-header">
                    <span class="terminal-dot red"></span>
                    <span class="terminal-dot yellow"></span>
                    <span class="terminal-dot green"></span>
                    <span style="font-size:13px; color:#78716C; margin-left:12px;" id="s6-command"></span>
                  </div>
                  <div style="padding: 24px; font-size:14px; line-height:1.8; color:#D6D3D1;">
                    <div style="color:#78716C;" id="s6-log-1">$ checking sprint backlog for client memo MT-104...</div>
                    <div style="color:#EF4444; font-weight:700;" id="s6-log-2">[CRITICAL] 72.0 hours elapsed since voice message.</div>
                    <div style="color:#F59E0B;" id="s6-log-3">[WARNING] ZERO Linear tasks created. Engineering team is idle.</div>
                    <div style="color:#EF4444;" id="s6-log-4">[SLA BREACHED] Deliverable marked overdue by client.</div>
                  </div>
                </div>

                <!-- 4 Spring-Popping Red Alert Cards -->
                <div class="alert-badge" id="s6-alert-1" style="position:absolute; top:-20px; left:10px;">
                  <span>🚨</span> <span>"Where is the deliverable you promised??"</span>
                </div>
                <div class="alert-badge" id="s6-alert-2" style="position:absolute; top:80px; right:10px; background:#380C10; border-color:#EF4444;">
                  <span>⚠️</span> <span>Client: ESCALATED TO CRITICAL</span>
                </div>
                <div class="alert-badge" id="s6-alert-3" style="position:absolute; top:200px; left:30px;">
                  <span>🔥</span> <span>"Nobody started the job!"</span>
                </div>
                <div class="alert-badge" id="s6-alert-4" style="position:absolute; top:310px; right:20px; background:#380C10; border-color:#EF4444;">
                  <span>❌</span> <span>Threatening contract cancellation!</span>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- ================= SCENE 7: MUBARAKTECH INSTEAD (00:30.70 - 00:33.90) [CANVAS: WARM CREAM + GEOMETRIC PORTAL] ================= -->
        <section class="scene-layer" id="s7">
          <div class="card-anim-wrapper" id="s7-anim">
            <div class="card-3d-float" id="s7-container" style="display:flex; flex-direction:column; align-items:center; text-align:center;">
              <div style="position:relative; padding: 20px 64px; margin-bottom: 32px;" id="s7-bracket-target">
                <div class="corner-bracket bracket-tl" id="s7-br-tl" style="top:-14px; left:-14px; border-width:6px 0 0 6px;"></div>
                <div class="corner-bracket bracket-br" id="s7-br-br" style="bottom:-14px; right:-14px; border-width:0 6px 6px 0;"></div>
                <div style="font-family:var(--font-mono); font-size:32px; font-weight:800; color:var(--terracotta); letter-spacing:0.22em;">
                  INSTEAD
                </div>
              </div>

              <!-- Portal Lockup on Cream -->
              <div class="glass-card-cream" id="s7-portal" style="width:860px; padding:54px 44px; border-color:rgba(223,90,55,0.3); box-shadow: 0 30px 80px rgba(223,90,55,0.15);">
                <div style="margin-bottom:28px;" id="s7-logo">
                  <img src="assets/logo.png" alt="Mubarak Technologies" style="height:54px; width:auto; object-fit:contain;" />
                </div>
                <div class="category-badge" id="s7-badge" style="color:#78716C; background:rgba(20,18,16,0.06); padding:6px 20px; border-radius:99px; display:inline-block; border:1px solid rgba(20,18,16,0.1);">
                  AUTONOMOUS AGENCY WORKFLOWS
                </div>
                <h2 class="hero-title dark" id="s7-title" style="font-size: 54px; margin-top: 28px; line-height: 1.25;">
                  Here's what our clients at <span class="editorial-serif text-terracotta" id="s7-serif" style="font-size: 72px;">MubarakTech</span> do&nbsp;instead.
                </h2>
              </div>
            </div>
          </div>
        </section>

        <!-- ================= SCENE 8: WHATSAPP BOT (00:33.90 - 00:38.00) [CANVAS: WARM CREAM + LIGHT IPHONE MOCKUP] ================= -->
        <section class="scene-layer" id="s8">
          <div style="display:flex; flex-direction:column; align-items:center; text-align:center; width:100%;">
            <div class="category-badge text-terracotta" id="s8-tag">
              THE PRIVATE BOT
            </div>
            <h2 class="hero-title dark" id="s8-title" style="font-size: 56px; line-height: 1.22; max-width: 900px;">
              They forward that 60-second audio note to a <span style="white-space: nowrap;">private <span class="editorial-serif text-terracotta" id="s8-serif" style="font-size: 74px;">WhatsApp&nbsp;bot.</span></span>
            </h2>

            <!-- Interactive Light iPhone Mockup -->
            <div class="card-anim-wrapper" id="s8-anim">
              <div class="card-3d-float phone-mockup-light" id="s8-phone">
                <div class="phone-notch-light"></div>
                <div style="padding:16px 24px; background:#075E54; display:flex; align-items:center; justify-content:space-between; color:#fff;">
                  <div style="display:flex; align-items:center; gap:14px;">
                    <div style="width:44px; height:44px; border-radius:50%; background:var(--terracotta); display:flex; align-items:center; justify-content:center; font-size:20px; color:#fff; font-weight:700;">
                      🤖
                    </div>
                    <div style="text-align:left;">
                      <div style="font-weight:700; font-size:17px; color:#fff;">MubarakTech Dispatch Bot</div>
                      <div style="font-size:12px; color:#A7F3D0; font-family:var(--font-mono);">Online • Autonomous AI</div>
                    </div>
                  </div>
                  <span style="font-family:var(--font-mono); font-size:12px; color:#E0E7FF; background:rgba(255,255,255,0.15); padding:4px 10px; border-radius:6px;">PRIVATE BOT</span>
                </div>

                <!-- Chat Body on White -->
                <div style="padding:24px 28px; display:flex; flex-direction:column; gap:16px; background:#ECE5DD;">
                  <!-- Outgoing Audio Note -->
                  <div id="s8-user-msg" style="align-self:flex-end; background:#DCF8C6; padding:16px 22px; border-radius:18px 18px 4px 18px; max-width:560px; text-align:left; display:flex; align-items:center; gap:16px; box-shadow:0 2px 6px rgba(0,0,0,0.1); color:var(--ink);">
                    <span style="font-size:26px;">🎙️</span>
                    <div>
                      <div style="font-weight:600; font-size:16px; color:var(--ink);">Voice message forwarded (0:60)</div>
                      <div style="font-size:13px; color:#6B7280; font-family:var(--font-mono); margin-top:2px;">Audio memo from client Sarah</div>
                    </div>
                    <span style="font-family:var(--font-mono); font-size:11px; color:#3B82F6; margin-left:auto;" id="s8-ticks">08:34 PM ✓✓</span>
                  </div>

                  <!-- Bot Typing Bubble -->
                  <div class="typing-bubble" id="s8-typing" style="display:none;">
                    <span class="typing-dot"></span>
                    <span class="typing-dot"></span>
                    <span class="typing-dot"></span>
                    <span style="font-family:var(--font-mono); font-size:13px; color:#64748B; margin-left:6px;">Parsing audio memo...</span>
                  </div>

                  <!-- Bot Dispatched Card -->
                  <div id="s8-bot-msg" style="align-self:flex-start; background:#FFFFFF; padding:22px 24px; border-radius:18px 18px 18px 4px; max-width:680px; text-align:left; border:1px solid rgba(223,90,55,0.3); opacity:0; box-shadow:0 4px 12px rgba(0,0,0,0.08); color:var(--ink);">
                    <div style="display:flex; align-items:center; gap:8px; margin-bottom:12px;">
                      <span style="color:#F59E0B; font-size:16px;">⚡</span>
                      <span style="font-family:var(--font-mono); font-size:14px; font-weight:700; color:#15803D;">Parsed & Dispatched in 40 seconds</span>
                    </div>
                    <div style="font-size:15px; color:#4B5563; line-height:1.6; margin-bottom:14px;">
                      Transcribed client Sarah's 60s audio memo. Three autonomous actions triggered:
                    </div>
                    <div style="display:flex; flex-direction:column; gap:8px; font-family:var(--font-mono); font-size:13px;">
                      <div style="background:#F9FAFB; padding:8px 14px; border-radius:8px; border-left:3px solid var(--terracotta);" id="s8-pill-1">
                        [1] Task created: Lead engineering assigned (Hard deadline: Fri 5 PM)
                      </div>
                      <div style="background:#F9FAFB; padding:8px 14px; border-radius:8px; border-left:3px solid #3B82F6;" id="s8-pill-2">
                        [2] Client recap drafted: Prepared for 1-tap review
                      </div>
                      <div style="background:#F9FAFB; padding:8px 14px; border-radius:8px; border-left:3px solid var(--stripe-purple);" id="s8-pill-3">
                        [3] Stripe invoice generated: $1,500 link created
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- ================= SCENE 9: IN 40 SECONDS (00:38.00 - 00:41.90) [CANVAS: DARK OBSIDIAN + PIPELINE HUB] ================= -->
        <section class="scene-layer" id="s9">
          <div style="display:flex; flex-direction:column; align-items:center; text-align:center; width:100%;">
            <div class="category-badge text-terracotta" id="s9-tag" style="background:rgba(223,90,55,0.14); border:1px solid rgba(223,90,55,0.3); padding:8px 22px; border-radius:99px;">
              THE 40-SECOND PIPELINE
            </div>
            <h2 class="hero-title" id="s9-title" style="font-size: 58px; line-height: 1.24; max-width:860px;">
              In forty seconds, <span class="editorial-serif text-terracotta" id="s9-serif" style="font-size: 78px;">three things happen</span> automatically.
            </h2>

            <div class="card-anim-wrapper" id="s9-anim" style="margin-top:36px;">
              <div class="card-3d-float glass-card-obsidian pipeline-container" id="s9-hub">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                  <span style="font-family:var(--font-mono); font-size:14px; color:#A8A29E; letter-spacing:0.1em;">AUTONOMOUS EXECUTION ENGINE</span>
                  <span style="font-family:var(--font-mono); font-size:18px; color:var(--terracotta); font-weight:800; background:rgba(223,90,55,0.15); padding:6px 18px; border-radius:99px; border:1px solid rgba(223,90,55,0.3);" id="s9-countdown">
                    ⏱️ 00:40 SECONDS
                  </span>
                </div>

                <div class="pipeline-stage active" id="s9-stage-1">
                  <div style="width:42px; height:42px; border-radius:50%; background:var(--terracotta); display:flex; align-items:center; justify-content:center; font-weight:800; color:#fff; font-family:var(--font-mono);">01</div>
                  <div style="flex:1;">
                    <div style="font-weight:700; font-size:18px; color:#fff;">Extract Deliverables & Hard Deadline</div>
                    <div style="font-size:13px; color:#A8A29E; font-family:var(--font-mono); margin-top:3px;">Auto-dispatched straight to your lead engineer</div>
                  </div>
                  <span style="font-size:20px; color:#4ADE80;" id="s9-chk-1">✓</span>
                </div>

                <div class="pipeline-stage active" id="s9-stage-2">
                  <div style="width:42px; height:42px; border-radius:50%; background:#3B82F6; display:flex; align-items:center; justify-content:center; font-weight:800; color:#fff; font-family:var(--font-mono);">02</div>
                  <div style="flex:1;">
                    <div style="font-weight:700; font-size:18px; color:#fff;">Draft Client Recap for Review</div>
                    <div style="font-size:13px; color:#A8A29E; font-family:var(--font-mono); margin-top:3px;">Formatted update ready for 1-tap approval</div>
                  </div>
                  <span style="font-size:20px; color:#4ADE80;" id="s9-chk-2">✓</span>
                </div>

                <div class="pipeline-stage active" id="s9-stage-3">
                  <div style="width:42px; height:42px; border-radius:50%; background:var(--stripe-purple); display:flex; align-items:center; justify-content:center; font-weight:800; color:#fff; font-family:var(--font-mono);">03</div>
                  <div style="flex:1;">
                    <div style="font-weight:700; font-size:18px; color:#fff;">Generate Stripe Invoice Link</div>
                    <div style="font-size:13px; color:#A8A29E; font-family:var(--font-mono); margin-top:3px;">Created and linked straight into chat</div>
                  </div>
                  <span style="font-size:20px; color:#4ADE80;" id="s9-chk-3">✓</span>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- ================= SCENE 10: PILLAR 1 - EXTRACT & ASSIGN (00:41.90 - 00:47.80) [CANVAS: WARM CREAM + 3 STACKED CARDS] ================= -->
        <section class="scene-layer" id="s10">
          <div style="display:flex; flex-direction:column; align-items:center; text-align:center; width:100%;">
            <div class="category-badge text-terracotta" id="s10-tag" style="background:rgba(223,90,55,0.1); border:1px solid rgba(223,90,55,0.25); padding:8px 22px; border-radius:99px;">
              PILLAR 01 / 03
            </div>
            <h2 class="hero-title dark" id="s10-title" style="font-size: 58px; line-height: 1.22;">
              First, it extracts the deliverables and assigns them straight to your team with a <span class="editorial-serif text-terracotta" id="s10-serif" style="font-size: 76px;">hard&nbsp;deadline.</span>
            </h2>

            <!-- 3 Stacked Engineering Cards (Outship Scene 5 Style) -->
            <div class="card-anim-wrapper" id="s10-anim">
              <div class="eng-stack-container" id="s10-stack">
                <div class="eng-signal-card" id="s10-card-1">
                  <div class="eng-signal-icon" style="background:#DCFCE7; color:#15803D;">📐</div>
                  <div style="flex:1;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                      <span style="font-size:20px; font-weight:700; color:var(--ink);">Added Linear Task: Mobile Checkout UX Overhaul</span>
                      <span style="font-family:var(--font-mono); font-size:12px; color:#15803D; background:#DCFCE7; padding:4px 10px; border-radius:99px; font-weight:700;">P0 CRITICAL</span>
                    </div>
                    <div style="font-family:var(--font-mono); font-size:14px; color:#78716C; margin-top:4px;">
                      Assigned to <strong>Alex Rivera (Lead Engineer)</strong> • <span style="color:#EF4444; font-weight:700;">Due Today 5:00 PM</span>
                    </div>
                  </div>
                </div>

                <div class="eng-signal-card" id="s10-card-2">
                  <div class="eng-signal-icon" style="background:#DBEAFE; color:#1D4ED8;">⚡</div>
                  <div style="flex:1;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                      <span style="font-size:20px; font-weight:700; color:var(--ink);">Patched Webhook Listener 404 Retry</span>
                      <span style="font-family:var(--font-mono); font-size:12px; color:#1D4ED8; background:#DBEAFE; padding:4px 10px; border-radius:99px; font-weight:700;">AUTO-SCHEDULED</span>
                    </div>
                    <div style="font-family:var(--font-mono); font-size:14px; color:#78716C; margin-top:4px;">
                      Assigned to <strong>Elena Rostova</strong> • <span style="color:#EF4444; font-weight:700;">Due Today 6:00 PM</span>
                    </div>
                  </div>
                </div>

                <div class="eng-signal-card" id="s10-card-3">
                  <div class="eng-signal-icon" style="background:#FEF3C7; color:#B45309;">📅</div>
                  <div style="flex:1;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                      <span style="font-size:20px; font-weight:700; color:var(--ink);">Locked Google Calendar Sprint Block</span>
                      <span style="font-family:var(--font-mono); font-size:12px; color:#B45309; background:#FEF3C7; padding:4px 10px; border-radius:99px; font-weight:700;">SYNCED</span>
                    </div>
                    <div style="font-family:var(--font-mono); font-size:14px; color:#78716C; margin-top:4px;">
                      Sprint timeline verified • Zero dropped deliverables
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- ================= SCENE 11: PILLAR 2 - RECAP REVIEW (00:47.80 - 00:52.25) [CANVAS: WARM CREAM + MACOS WINDOW + PURPLE CURSOR] ================= -->
        <section class="scene-layer" id="s11">
          <div style="display:flex; flex-direction:column; align-items:center; text-align:center; width:100%;">
            <div class="category-badge text-terracotta" id="s11-tag" style="background:rgba(223,90,55,0.1); border:1px solid rgba(223,90,55,0.25); padding:8px 22px; border-radius:99px;">
              PILLAR 02 / 03
            </div>
            <h2 class="hero-title dark" id="s11-title" style="font-size: 58px; line-height: 1.22;">
              Second, it drafts a client recap for your <span class="editorial-serif text-terracotta" id="s11-serif" style="font-size: 76px;">one-tap&nbsp;review.</span>
            </h2>

            <!-- macOS Desktop Mail Window on Cream -->
            <div class="card-anim-wrapper" id="s11-anim" style="margin-top:36px;">
              <div class="card-3d-float macos-mail-window" id="s11-card" style="position:relative;">
                <div class="macos-window-header">
                  <span class="terminal-dot red"></span>
                  <span class="terminal-dot yellow"></span>
                  <span class="terminal-dot green"></span>
                  <span style="font-family:var(--font-mono); font-size:13px; color:#78716C; margin-left:12px;">Drafted Client Update • Ready for 1-Tap Review</span>
                </div>
                <div style="padding: 32px 36px;">
                  <div style="font-size:15px; color:var(--ink); line-height:1.6; background:#F5EFE6; padding:22px; border-radius:18px; margin-bottom:24px; border:1px solid rgba(20,18,16,0.06);">
                    <div style="margin-bottom:6px;"><strong>To:</strong> sarah@clientbrand.com</div>
                    <div style="margin-bottom:12px;"><strong>Subject:</strong> Update: Checkout Revamp & Webhook Resolution Underway</div>
                    <p style="color:#57534E; line-height:1.6;" id="s11-email-body">
                      "Hi Sarah, received your audio memo! Alex on our engineering team has been assigned and is addressing the mobile checkout layout and webhook listener today. Expected completion: Friday 5 PM."
                    </p>
                  </div>

                  <div style="display:flex; justify-content:flex-end;">
                    <button id="s11-approve-btn" style="background:var(--terracotta); border:none; color:#fff; font-family:var(--font-sans); font-size:17px; font-weight:700; padding:16px 36px; border-radius:99px; display:inline-flex; align-items:center; gap:10px; box-shadow:0 10px 30px rgba(223,90,55,0.35); cursor:pointer;">
                      <span id="s11-btn-text">Approve & Send to Client</span>
                      <span>➔</span>
                    </button>
                  </div>

                  <!-- Purple Founder Cursor -->
                  <div class="software-cursor" id="s11-cursor" style="left: 560px; top: 290px;">
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none">
                      <path d="M5.5 3.2L18.8 12.8L12.5 14.2L15.8 20.8L13.2 22L10 15.4L5.5 19.8V3.2Z" fill="#7C3AED" stroke="#FFFFFF" stroke-width="1.5"/>
                    </svg>
                    <div class="cursor-tag">You (1-Tap)</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- ================= SCENE 12: PILLAR 3 - STRIPE INVOICE (00:52.25 - 00:56.45) [CANVAS: DARK OBSIDIAN + STRIPE CARD] ================= -->
        <section class="scene-layer" id="s12">
          <div style="display:flex; flex-direction:column; align-items:center; text-align:center; width:100%;">
            <div class="category-badge text-terracotta" id="s12-tag" style="background:rgba(223,90,55,0.14); border:1px solid rgba(223,90,55,0.3); padding:8px 22px; border-radius:99px;">
              PILLAR 03 / 03
            </div>
            <h2 class="hero-title" id="s12-title" style="font-size: 58px; line-height: 1.24; max-width:840px;">
              Third, it generates the <span class="editorial-serif text-terracotta" id="s12-serif" style="font-size: 74px;">Stripe&nbsp;invoice</span> link&nbsp;automatically.
            </h2>

            <!-- Stripe Card -->
            <div class="card-anim-wrapper" id="s12-anim" style="margin-top:36px;">
              <div class="card-3d-float glass-card-obsidian" id="s12-card" style="width: 860px; padding: 42px; text-align: left; border-color: rgba(99,91,255,0.4); box-shadow:0 0 80px rgba(99,91,255,0.25);">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:24px;">
                  <div style="display:flex; align-items:center; gap:12px;">
                    <span style="font-size:28px; font-weight:800; color:#635BFF; font-family:var(--font-mono);">stripe</span>
                    <span style="font-size:14px; color:#A8A29E; font-family:var(--font-mono);">INVOICE GENERATOR</span>
                  </div>
                  <span style="background:rgba(34,197,94,0.15); color:#4ADE80; padding:6px 16px; border-radius:99px; font-size:14px; font-family:var(--font-mono); font-weight:600;" id="s12-status">
                    READY TO PAY
                  </span>
                </div>
                <div style="font-size:52px; font-weight:800; color:#fff; font-family:var(--font-sans); margin-bottom:10px;" id="s12-amount">
                  $1,500.00 <span style="font-size:20px; font-weight:400; color:#A8A29E;">USD</span>
                </div>
                <div style="font-size:15px; color:#A8A29E; font-family:var(--font-mono); margin-bottom:24px;">
                  Invoice #MT-2026-089 • Checkout optimization & webhook maintenance
                </div>
                <div style="background:rgba(255,255,255,0.06); padding:20px 24px; border-radius:16px; display:flex; justify-content:space-between; align-items:center; font-family:var(--font-mono); font-size:14px;" id="s12-url-box">
                  <span style="color:#D6D3D1;">https://buy.stripe.com/mb_voice_908f</span>
                  <span style="color:var(--terracotta); font-weight:700;">[ SENT TO WHATSAPP ]</span>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- ================= SCENE 13: RESULTS MONOLITHS (00:56.45 - 00:60.15) [CANVAS: WARM CREAM + TWIN MONOLITHS] ================= -->
        <section class="scene-layer" id="s13">
          <div style="display:flex; flex-direction:column; align-items:center; text-align:center; width:100%;">
            <div class="category-badge text-terracotta" id="s13-tag" style="background:rgba(223,90,55,0.1); border:1px solid rgba(223,90,55,0.25); padding:8px 22px; border-radius:99px; margin-bottom:32px;">
              THE RESULTS
            </div>

            <div class="card-anim-wrapper" id="s13-anim" style="flex-direction:column; gap:32px; width:860px;">
              <div class="card-3d-float glass-card-cream" id="s13-card-1" style="padding:42px; border-left:8px solid var(--ink); text-align:left;">
                <div style="font-size:68px; font-weight:800; color:var(--ink); line-height:1.1;">
                  Zero <span class="editorial-serif" style="font-size:68px; color:#44403C;">manual&nbsp;typing.</span>
                </div>
                <p style="margin-top:14px; font-size:20px; color:#78716C; line-height:1.4;">
                  Audio notes convert into actionable tasks, deadlines, and recaps in under 40&nbsp;seconds.
                </p>
              </div>

              <div class="card-3d-float glass-card-cream" id="s13-card-2" style="padding:42px; border-left:8px solid var(--terracotta); text-align:left;">
                <div style="font-size:68px; font-weight:800; color:var(--terracotta); line-height:1.1;">
                  Zero <span class="editorial-serif" style="font-size:68px; color:var(--ink);">dropped&nbsp;deadlines.</span>
                </div>
                <p style="margin-top:14px; font-size:20px; color:#78716C; line-height:1.4;">
                  Every client instruction is tracked, assigned, and delivered with 100% team accountability.
                </p>
              </div>
            </div>
          </div>
        </section>

        <!-- ================= SCENE 14: STOP PAYING $3,000 (00:60.15 - 00:66.50) [CANVAS: DARK OBSIDIAN + SPLIT MATRIX] ================= -->
        <section class="scene-layer" id="s14">
          <div class="card-anim-wrapper" id="s14-anim">
            <div class="card-3d-float glass-card-obsidian" id="s14-card" style="display:flex; flex-direction:column; align-items:center; text-align:center; width:880px; padding:48px 40px; border-color:rgba(223,90,55,0.45);">
              <div class="category-badge" id="s14-tag" style="color:#EF4444;">
                THE BOTTOM LINE
              </div>
              <h2 class="hero-title" id="s14-title" style="font-size: 56px; line-height: 1.25; max-width:840px;">
                Stop paying a <span class="s1-strikethrough" id="s14-strike" style="color:#9CA3AF; font-size:66px;">$3,000&nbsp;assistant</span> for tasks a smart automation <span style="white-space: nowrap;">finishes in <span class="editorial-serif text-terracotta" id="s14-serif" style="font-size: 78px;">seconds.</span></span>
              </h2>

              <!-- Contrast Comparison Matrix -->
              <div class="comparison-matrix" id="s14-matrix">
                <div class="comparison-col" id="s14-col-left">
                  <div style="font-family:var(--font-mono); font-size:14px; color:#EF4444; font-weight:700;">$3,000 / MO ASSISTANT</div>
                  <div style="font-size:15px; color:#D6D3D1;">❌ 2-3h delay typing audio notes</div>
                  <div style="font-size:15px; color:#D6D3D1;">❌ Missed scope & forgotten tasks</div>
                  <div style="font-size:15px; color:#D6D3D1;">❌ $36,000 annual recurring cost</div>
                </div>
                <div class="comparison-col winner" id="s14-col-right">
                  <div style="font-family:var(--font-mono); font-size:14px; color:#4ADE80; font-weight:700;">MUBARAKTECH AUTOMATION</div>
                  <div style="font-size:15px; color:#fff; font-weight:600;">⚡ 40-second autonomous turnaround</div>
                  <div style="font-size:15px; color:#fff; font-weight:600;">✓ 100% extraction accuracy</div>
                  <div style="font-size:15px; color:#fff; font-weight:600;">⚡ $0 recurring administrative labor</div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- ================= SCENE 15: COMMENT VOICE CTA (00:66.50 - 00:69.50) [CANVAS: WARM CREAM + SOCIAL CARD] ================= -->
        <section class="scene-layer" id="s15">
          <div class="card-anim-wrapper" id="s15-anim">
            <div class="card-3d-float comment-card-cream" id="s15-card">
              <div class="category-badge" id="s15-tag" style="color:#78716C;">
                CLAIM THE EXACT WORKFLOW
              </div>
              <h2 class="hero-title dark" id="s15-title" style="font-size: 54px; line-height: 1.25; text-align:left;">
                Comment <span class="editorial-serif text-terracotta" id="s15-serif" style="font-size: 74px;">VOICE</span> and I'll send you our exact&nbsp;template.
              </h2>
              <div class="comment-input-box-light" id="s15-input-box">
                <div>
                  <span id="s15-typed-text" style="color:var(--terracotta); font-weight:800; letter-spacing:0.1em;"></span>
                  <span class="comment-cursor-blink" id="s15-cursor"></span>
                </div>
                <span style="font-size:18px; color:#15803D; font-weight:700;" id="s15-post-btn">[ POST COMMENT ➔ ]</span>
              </div>
              <div style="font-family:var(--font-mono); font-size:14px; color:#78716C;" id="s15-toast">
                ⚡ Autonomous DM engine delivers the complete n8n / Make / WhatsApp blueprint in 10 seconds.
              </div>
            </div>
          </div>
        </section>

        <!-- ================= SCENE 16: OUTRO & BRAND LOCKUP (00:69.50 - 00:73.08) [CANVAS: DARK OBSIDIAN + PORTAL] ================= -->
        <section class="scene-layer" id="s16">
          <div class="card-anim-wrapper" id="s16-anim">
            <div class="card-3d-float glass-card-obsidian" id="s16-card" style="display:flex; flex-direction:column; align-items:center; text-align:center; position:relative; padding: 64px 60px; border-color:rgba(223,90,55,0.5); box-shadow: 0 0 160px rgba(223,90,55,0.4); width:880px;">
              <div class="corner-bracket bracket-tl" id="s16-br-tl" style="top:-20px; left:-20px; border-width:8px 0 0 8px;"></div>
              <div class="corner-bracket bracket-br" id="s16-br-br" style="bottom:-20px; right:-20px; border-width:0 8px 8px 0;"></div>

              <div style="margin-bottom:28px;" id="s16-logo">
                <img src="assets/logo_light_text.png" alt="Mubarak Technologies" style="height:58px; width:auto; object-fit:contain;" />
              </div>

              <div class="category-badge text-terracotta" id="s16-tag" style="letter-spacing:0.18em; margin-bottom:20px;">
                AUTONOMOUS AGENCY WORKFLOWS
              </div>

              <h1 class="hero-title" id="s16-title" style="font-size: 64px; line-height: 1.22;">
                Steal the 2-minute <span class="editorial-serif text-terracotta" id="s16-serif" style="font-size: 86px;">voice&nbsp;memo.</span>
              </h1>

              <div style="margin-top:24px; font-family:var(--font-mono); font-size:15px; color:#78716C;" id="s16-footer">
                AI-NATIVE SYSTEMS • MUBARAKTECH.COM
              </div>
            </div>
          </div>
        </section>

      </div><!-- /#dom-stage-3d -->
    </div>
  </main>

  <!-- Studio Playbar Controls -->
  <footer class="studio-controls">
    <div class="ctrl-group">
      <button class="ctrl-btn primary" id="btn-play">▶ Play</button>
      <button class="ctrl-btn" id="btn-restart">↺ Restart</button>
      <button class="ctrl-btn" id="btn-prev">⏮ Prev</button>
      <button class="ctrl-btn" id="btn-next">⏭ Next</button>
    </div>
    <input type="range" id="time-slider" class="time-slider" min="0" max="73.08" step="0.01" value="0" />
    <div class="ctrl-group">
      <span class="time-readout" id="time-readout">00:00.00 / 01:13.08</span>
      <button class="ctrl-btn" id="btn-fullscreen">⛶ Fullscreen</button>
    </div>
  </footer>
</div>

<!-- Audio Element -->
<audio id="master-audio" src="audio.wav" preload="auto"></audio>

<script>
  // Register GSAP TextPlugin
  if (window.gsap && window.TextPlugin) {
    gsap.registerPlugin(TextPlugin);
  }

  // Detect headless capture environment (CDP / render.mjs)
  if (navigator.webdriver || window.location.search.includes('render=true')) {
    document.body.classList.add('headless-render');
  }

  /* -------------------------------------------------------------
     THREE.JS DETERMINISTIC 3D STAGE (1080x1920)
     No 3D Grid lines! Luminous crystals, rotating Torus rings & depth motes
     ------------------------------------------------------------- */
  const threeStage = document.getElementById('three-stage');
  const domStage3D = document.getElementById('dom-stage-3d');
  const canvasBg = document.getElementById('canvas-bg');
  const canvasPixelGrid = document.getElementById('canvas-pixel-grid');
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(50, 1080 / 1920, 0.1, 3000);
  camera.position.set(0, 0, 800);

  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true });
  renderer.setSize(1080, 1920, false);
  renderer.setPixelRatio(1.0);
  threeStage.appendChild(renderer.domElement);

  // Floating 3D Depth Motes
  const particleCount = 120;
  const geomParticles = new THREE.BufferGeometry();
  const posParticles = new Float32Array(particleCount * 3);
  for (let i = 0; i < particleCount * 3; i += 3) {
    posParticles[i] = (Math.random() - 0.5) * 1200;
    posParticles[i+1] = (Math.random() - 0.5) * 1900;
    posParticles[i+2] = (Math.random() - 0.5) * 900;
  }
  geomParticles.setAttribute('position', new THREE.BufferAttribute(posParticles, 3));
  const matParticles = new THREE.PointsMaterial({
    color: 0xDF5A37,
    size: 4.0,
    transparent: true,
    opacity: 0.45
  });
  const particles = new THREE.Points(geomParticles, matParticles);
  scene.add(particles);

  // Rotating Concentric Torus Rings (Scene 7 & 16 Portal)
  const ringGeo1 = new THREE.TorusGeometry(260, 2.5, 16, 100);
  const ringMat1 = new THREE.MeshBasicMaterial({ color: 0xDF5A37, transparent: true, opacity: 0.45 });
  const ring1 = new THREE.Mesh(ringGeo1, ringMat1);
  ring1.rotation.x = Math.PI / 3;
  scene.add(ring1);

  const ringGeo2 = new THREE.TorusGeometry(320, 1.8, 16, 100);
  const ringMat2 = new THREE.MeshBasicMaterial({ color: 0xFF7A59, transparent: true, opacity: 0.3 });
  const ring2 = new THREE.Mesh(ringGeo2, ringMat2);
  ring2.rotation.y = Math.PI / 4;
  scene.add(ring2);

  // Floating 3D Polyhedra
  const objects3D = [];
  const crystalColors = [0xDF5A37, 0xF4D7CE, 0xDF5A37, 0xFF9E80, 0xC2410C];
  for (let i = 0; i < 8; i++) {
    const geo = i % 2 === 0 ? new THREE.OctahedronGeometry(22 + (i % 3) * 12, 0) : new THREE.IcosahedronGeometry(20 + (i % 3) * 10, 0);
    const mat = new THREE.MeshBasicMaterial({
      color: crystalColors[i % crystalColors.length],
      wireframe: true,
      transparent: true,
      opacity: 0.35
    });
    const mesh = new THREE.Mesh(geo, mat);
    const angle = (i / 8) * Math.PI * 2;
    const radius = 420 + (i % 3) * 60;
    mesh.position.set(Math.cos(angle) * radius, Math.sin(angle) * radius * 1.3, -150 + (i % 4) * 80);
    scene.add(mesh);
    objects3D.push({
      mesh,
      baseX: mesh.position.x,
      baseY: mesh.position.y,
      baseZ: mesh.position.z,
      rotSpeedX: 0.4 + (i * 0.1),
      rotSpeedY: 0.5 + (i * 0.08)
    });
  }

  /* -------------------------------------------------------------
     24-WAYPOINT HERMITE CONTINUOUS 3D CAMERA TRAJECTORY
     ------------------------------------------------------------- */
  const cameraTrajectory = [
    { t: 0.00,  x: 0,   y: 0,   z: 800, rx: 0,       ry: 0,       rz: 0 },
    { t: 3.50,  x: 20,  y: -15, z: 760, rx: 0.015,   ry: -0.02,   rz: 0.005 },
    { t: 5.45,  x: 0,   y: 0,   z: 780, rx: 0,       ry: 0,       rz: 0 },
    { t: 9.00,  x: -35, y: 25,  z: 740, rx: -0.02,   ry: 0.035,   rz: -0.01 },
    { t: 13.00, x: 25,  y: -20, z: 750, rx: 0.02,    ry: -0.025,  rz: 0.008 },
    { t: 15.35, x: 0,   y: 0,   z: 770, rx: 0,       ry: 0,       rz: 0 },
    { t: 17.30, x: 0,   y: -15, z: 730, rx: 0.03,    ry: 0,       rz: 0 },
    { t: 21.00, x: -30, y: 15,  z: 750, rx: -0.015,  ry: 0.03,    rz: -0.008 },
    { t: 24.35, x: 0,   y: 0,   z: 770, rx: 0,       ry: 0,       rz: 0 },
    { t: 25.85, x: 0,   y: 0,   z: 710, rx: 0.04,    ry: 0,       rz: 0 },
    { t: 28.50, x: 35,  y: -20, z: 750, rx: 0.02,    ry: -0.035,  rz: 0.01 },
    { t: 30.70, x: 0,   y: 0,   z: 790, rx: 0,       ry: 0,       rz: 0 },
    { t: 33.90, x: 0,   y: 10,  z: 760, rx: -0.015,  ry: 0,       rz: 0 },
    { t: 36.00, x: -25, y: -15, z: 740, rx: 0.02,    ry: 0.025,   rz: -0.006 },
    { t: 38.00, x: 0,   y: 0,   z: 770, rx: 0,       ry: 0,       rz: 0 },
    { t: 41.90, x: 20,  y: 20,  z: 750, rx: -0.02,   ry: -0.02,   rz: 0.006 },
    { t: 45.00, x: -20, y: -15, z: 760, rx: 0.015,   ry: 0.02,    rz: -0.005 },
    { t: 47.80, x: 0,   y: 0,   z: 770, rx: 0,       ry: 0,       rz: 0 },
    { t: 50.00, x: 25,  y: 15,  z: 740, rx: -0.015,  ry: -0.025,  rz: 0.008 },
    { t: 52.25, x: 0,   y: 0,   z: 760, rx: 0,       ry: 0,       rz: 0 },
    { t: 56.45, x: -25, y: -15, z: 780, rx: 0.015,   ry: 0.025,   rz: -0.006 },
    { t: 60.15, x: 0,   y: 0,   z: 770, rx: 0,       ry: 0,       rz: 0 },
    { t: 66.50, x: 20,  y: 15,  z: 750, rx: -0.015,  ry: -0.02,   rz: 0.006 },
    { t: 69.50, x: 0,   y: 0,   z: 780, rx: 0,       ry: 0,       rz: 0 },
    { t: 73.08, x: 0,   y: 0,   z: 750, rx: 0.01,    ry: 0,       rz: 0 }
  ];

  function evaluateCameraSpline(t) {
    if (t <= cameraTrajectory[0].t) return cameraTrajectory[0];
    const last = cameraTrajectory[cameraTrajectory.length - 1];
    if (t >= last.t) return last;

    let idx = 0;
    for (let i = 0; i < cameraTrajectory.length - 1; i++) {
      if (t >= cameraTrajectory[i].t && t <= cameraTrajectory[i+1].t) {
        idx = i;
        break;
      }
    }

    const p0 = cameraTrajectory[Math.max(0, idx - 1)];
    const p1 = cameraTrajectory[idx];
    const p2 = cameraTrajectory[idx + 1];
    const p3 = cameraTrajectory[Math.min(cameraTrajectory.length - 1, idx + 2)];

    const span = p2.t - p1.t;
    const u = span > 0 ? (t - p1.t) / span : 0;
    const u2 = u * u;
    const u3 = u2 * u;

    function catmull(v0, v1, v2, v3) {
      return 0.5 * (
        (2 * v1) +
        (-v0 + v2) * u +
        (2 * v0 - 5 * v1 + 4 * v2 - v3) * u2 +
        (-v0 + 3 * v1 - 3 * v2 + v3) * u3
      );
    }

    return {
      x: catmull(p0.x, p1.x, p2.x, p3.x),
      y: catmull(p0.y, p1.y, p2.y, p3.y),
      z: catmull(p0.z, p1.z, p2.z, p3.z),
      rx: catmull(p0.rx, p1.rx, p2.rx, p3.rx),
      ry: catmull(p0.ry, p1.ry, p2.ry, p3.ry),
      rz: catmull(p0.rz, p1.rz, p2.rz, p3.rz)
    };
  }

  // Pure time function: renderThreeAt(t)
  function renderThreeAt(t) {
    const cam = evaluateCameraSpline(t);
    camera.position.set(cam.x, cam.y, cam.z);
    camera.rotation.set(cam.rx, cam.ry, cam.rz);

    // Dynamic 3D DOM stage sync with camera
    if (domStage3D) {
      const pZ = (800 - cam.z) * 0.55;
      const pX = -cam.x * 0.5;
      const pY = cam.y * 0.5;
      const rX = -cam.rx * 32;
      const rY = -cam.ry * 32;
      const rZ = -cam.rz * 32;
      domStage3D.style.transform = `perspective(1400px) translate3d(${pX.toFixed(1)}px, ${pY.toFixed(1)}px, ${pZ.toFixed(1)}px) rotateX(${rX.toFixed(2)}deg) rotateY(${rY.toFixed(2)}deg) rotateZ(${rZ.toFixed(2)}deg)`;
    }

    // Physical 3D float tilt on cards
    const floatCards = document.querySelectorAll('.card-3d-float');
    floatCards.forEach((card, idx) => {
      const rx = Math.sin(t * 1.8 + idx * 1.3) * 4.2;
      const ry = Math.cos(t * 1.4 + idx * 1.1) * 5.0;
      const tz = Math.sin(t * 2.0 + idx * 1.5) * 8.0;
      card.style.transform = `rotateX(${rx.toFixed(2)}deg) rotateY(${ry.toFixed(2)}deg) translateZ(${tz.toFixed(1)}px)`;
    });

    // 3D Orbital rings active during Scene 7 and Scene 16
    const isHeroMoment = (t >= 30.7 && t <= 33.9) || (t >= 69.5 && t <= 73.08);
    ring1.visible = isHeroMoment;
    ring2.visible = isHeroMoment;
    if (isHeroMoment) {
      ring1.rotation.z = t * 0.9;
      ring2.rotation.z = -t * 0.7;
    }

    // Particle depth drift
    particles.rotation.y = t * 0.04;
    particles.rotation.x = t * 0.02;

    // Drift 3D crystals
    for (let i = 0; i < objects3D.length; i++) {
      const o = objects3D[i];
      o.mesh.position.x = o.baseX + Math.sin(t * 1.1 + i * 0.4) * 22;
      o.mesh.position.y = o.baseY + Math.cos(t * 0.9 + i * 0.3) * 26;
      o.mesh.rotation.x = t * o.rotSpeedX;
      o.mesh.rotation.y = t * o.rotSpeedY;

      if ((t >= 25.85 && t <= 30.70) || (t >= 33.90 && t <= 41.90)) {
        o.mesh.position.z = o.baseZ + Math.sin(t * 3.0 + i) * 40;
      } else {
        o.mesh.position.z = o.baseZ;
      }
    }
    renderer.render(scene, camera);
  }

  /* -------------------------------------------------------------
     SCENE TIMINGS MATCHED EXACTLY TO SPOKEN AUDIO (73.08s)
     ------------------------------------------------------------- */
  const scenes = [
    { id: 's1',  name: 'S1 Hook', t: 0.00, dur: 5.45, isCream: true },
    { id: 's2',  name: 'S2 2 Hours Grind', t: 5.45, dur: 9.90, isCream: false },
    { id: 's3',  name: 'S3 Exhausting', t: 15.35, dur: 1.95, isCream: true },
    { id: 's4',  name: 'S4 Driving Home', t: 17.30, dur: 7.05, isCream: false },
    { id: 's5',  name: 'S5 And Then Forget', t: 24.35, dur: 1.50, isCream: true },
    { id: 's6',  name: 'S6 3 Days Crisis', t: 25.85, dur: 4.85, isCream: false },
    { id: 's7',  name: 'S7 MubarakTech Instead', t: 30.70, dur: 3.20, isCream: true },
    { id: 's8',  name: 'S8 WhatsApp Bot', t: 33.90, dur: 4.10, isCream: true },
    { id: 's9',  name: 'S9 40s Pipeline Hub', t: 38.00, dur: 3.90, isCream: false },
    { id: 's10', name: 'S10 Pillar 1 Extract', t: 41.90, dur: 5.90, isCream: true },
    { id: 's11', name: 'S11 Pillar 2 Recap', t: 47.80, dur: 4.45, isCream: true },
    { id: 's12', name: 'S12 Pillar 3 Stripe', t: 52.25, dur: 4.20, isCream: false },
    { id: 's13', name: 'S13 Zero Typing', t: 56.45, dur: 3.70, isCream: true },
    { id: 's14', name: 'S14 $3K Comparison', t: 60.15, dur: 6.35, isCream: false },
    { id: 's15', name: 'S15 Comment VOICE', t: 66.50, dur: 3.00, isCream: true },
    { id: 's16', name: 'S16 Outro Lockup', t: 69.50, dur: 3.58, isCream: false }
  ];

  const TOTAL_DURATION = 73.08;
  window.__duration = TOTAL_DURATION;
  const tl = gsap.timeline({ paused: true });

  // Generate waveform bars in S1
  const waveContainer = document.getElementById('s1-waveform');
  const barCount = 32;
  for (let i = 0; i < barCount; i++) {
    const bar = document.createElement('div');
    bar.className = 'wave-bar';
    bar.style.height = `${12 + Math.sin(i * 0.35) * 32 + (i % 4) * 5}px`;
    waveContainer.appendChild(bar);
  }

  /* -------------------------------------------------------------
     DETERMINISTIC GSAP BACKGROUND COLOR TWEENS (Smooth Blending)
     ------------------------------------------------------------- */
  const bgTransitions = [
    { t: 5.05,  color: '#0D0A09', gridOpacity: 0 },
    { t: 14.95, color: '#FCF8F2', gridOpacity: 1 },
    { t: 16.90, color: '#0D0A09', gridOpacity: 0 },
    { t: 23.95, color: '#FCF8F2', gridOpacity: 1 },
    { t: 25.45, color: '#0D0A09', gridOpacity: 0 },
    { t: 30.30, color: '#FCF8F2', gridOpacity: 1 },
    { t: 37.60, color: '#0D0A09', gridOpacity: 0 },
    { t: 41.50, color: '#FCF8F2', gridOpacity: 1 },
    { t: 51.85, color: '#0D0A09', gridOpacity: 0 },
    { t: 56.05, color: '#FCF8F2', gridOpacity: 1 },
    { t: 59.75, color: '#0D0A09', gridOpacity: 0 },
    { t: 66.10, color: '#FCF8F2', gridOpacity: 1 },
    { t: 69.10, color: '#0D0A09', gridOpacity: 0 }
  ];
  bgTransitions.forEach(b => {
    tl.to(['#canvas-bg', '#root'], { backgroundColor: b.color, duration: 0.5, ease: 'power2.inOut' }, b.t);
    tl.to('#canvas-pixel-grid', { opacity: b.gridOpacity, duration: 0.45, ease: 'power2.inOut' }, b.t);
  });

  /* -------------------------------------------------------------
     SEAMLESS CROSS-FADE OVERLAPPING TRANSITIONS ACROSS ALL SCENES
     ------------------------------------------------------------- */
  scenes.forEach((sc, idx) => {
    const el = document.getElementById(sc.id);
    const startT = sc.t;
    const endT = sc.t + sc.dur;

    const fadeInT = startT > 0 ? startT - 0.4 : 0;
    const fadeOutT = endT - 0.45;

    // Smooth entrance for the entire scene layer
    tl.fromTo(el, 
      { autoAlpha: 0, y: 35, scale: 0.96 }, 
      { autoAlpha: 1, y: 0, scale: 1.0, duration: 0.55, ease: 'power2.out', zIndex: 10 + idx }, 
      fadeInT
    );

    // Smooth exit for the entire scene layer
    if (idx < scenes.length - 1) {
      tl.to(el, 
        { autoAlpha: 0, y: -35, scale: 0.96, duration: 0.5, ease: 'power2.inOut' }, 
        fadeOutT
      );
    }

    // ---------------- SCENE 1: HOOK ----------------
    if (sc.id === 's1') {
      tl.fromTo('#s1-anim', 
        { y: 60, scale: 0.92, opacity: 0 }, 
        { y: 0, scale: 1.0, opacity: 1, duration: 0.75, ease: 'back.out(1.5)' }, 
        startT + 0.1
      );
      tl.fromTo('#s1-tag', { y: -16, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4, ease: 'power2.out' }, startT + 0.2);
      tl.fromTo('#s1-title', { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: 'power3.out' }, startT + 0.3);
      tl.fromTo(['#s1-serif-1', '#s1-serif-2'], { scale: 0.86, opacity: 0 }, { scale: 1.0, opacity: 1, duration: 0.5, stagger: 0.15, ease: 'back.out(2.2)' }, startT + 0.45);
      tl.fromTo('.wave-bar', 
        { scaleY: 0.15 }, 
        { scaleY: 1.0, stagger: 0.02, duration: 0.6, ease: 'back.out(2.2)' }, 
        startT + 0.5
      );

    // ---------------- SCENE 2: 2 HOURS GRIND ----------------
    } else if (sc.id === 's2') {
      tl.fromTo('#s2-tag', { y: -16, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4 }, startT + 0.1);
      tl.fromTo('#s2-title', { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: 'power3.out' }, startT + 0.2);
      tl.fromTo('#s2-serif', { scale: 0.88, opacity: 0 }, { scale: 1.0, opacity: 1, duration: 0.5, ease: 'back.out(2.0)' }, startT + 0.35);
      tl.fromTo('#s2-sub', { y: 20, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5 }, startT + 0.45);

      tl.fromTo('#s2-anim', 
        { y: 70, scale: 0.92, opacity: 0 }, 
        { y: 0, scale: 1.0, opacity: 1, duration: 0.75, ease: 'back.out(1.6)' }, 
        startT + 0.3
      );
      tl.to('#s2-scrubber', { width: '92%', duration: 7.5, ease: 'none' }, startT + 0.8);

      // Typewriting transcription quote in real time
      tl.to('#s2-quote', { 
        text: '"Hey Mubarak, urgent update! We need the checkout redesigned and the Stripe webhook listener patched by Friday..."', 
        duration: 4.5, 
        ease: 'none' 
      }, startT + 1.0);

      // 6 Floating tool cards fly in with staggered springs
      tl.fromTo('#s2-tool-1', { x: -60, y: -20, opacity: 0, scale: 0.75 }, { x: 0, y: 0, opacity: 1, scale: 1, duration: 0.55, ease: 'back.out(1.8)' }, startT + 0.8);
      tl.fromTo('#s2-tool-2', { x: 60, y: -20, opacity: 0, scale: 0.75 }, { x: 0, y: 0, opacity: 1, scale: 1, duration: 0.55, ease: 'back.out(1.8)' }, startT + 1.1);
      tl.fromTo('#s2-tool-3', { y: 40, x: -30, opacity: 0, scale: 0.75 }, { y: 0, x: 0, opacity: 1, scale: 1, duration: 0.55, ease: 'back.out(1.8)' }, startT + 1.4);
      tl.fromTo('#s2-tool-4', { y: 40, x: 30, opacity: 0, scale: 0.75 }, { y: 0, x: 0, opacity: 1, scale: 1, duration: 0.55, ease: 'back.out(1.8)' }, startT + 1.7);
      tl.fromTo('#s2-tool-5', { x: -50, opacity: 0, scale: 0.75 }, { x: 0, opacity: 1, scale: 1, duration: 0.55, ease: 'back.out(1.8)' }, startT + 2.0);
      tl.fromTo('#s2-tool-6', { x: 50, opacity: 0, scale: 0.75 }, { x: 0, opacity: 1, scale: 1, duration: 0.55, ease: 'back.out(1.8)' }, startT + 2.3);

    // ---------------- SCENE 3: EXHAUSTING ----------------
    } else if (sc.id === 's3') {
      tl.fromTo('#s3-anim', 
        { scale: 0.82, opacity: 0, y: 30 }, 
        { scale: 1.0, opacity: 1, y: 0, duration: 0.55, ease: 'back.out(2.2)' }, 
        startT + 0.05
      );
      tl.fromTo('#s3-serif', { scale: 0.8, opacity: 0 }, { scale: 1.0, opacity: 1, duration: 0.45, ease: 'back.out(2.4)' }, startT + 0.15);
      tl.fromTo('#s3-badge', { scale: 0.7, opacity: 0 }, { scale: 1.0, opacity: 1, duration: 0.4, ease: 'back.out(2.0)' }, startT + 0.3);

      // Exploding fatigue syntax tokens
      tl.fromTo('#s3-tok-1', { x: -60, y: -45, scale: 0, opacity: 0 }, { x: 0, y: 0, scale: 1, opacity: 1, duration: 0.45, ease: 'back.out(2.2)' }, startT + 0.25);
      tl.fromTo('#s3-tok-2', { x: 60, y: -45, scale: 0, opacity: 0 }, { x: 0, y: 0, scale: 1, opacity: 1, duration: 0.45, ease: 'back.out(2.2)' }, startT + 0.35);
      tl.fromTo('#s3-tok-3', { x: -50, y: 40, scale: 0, opacity: 0 }, { x: 0, y: 0, scale: 1, opacity: 1, duration: 0.45, ease: 'back.out(2.2)' }, startT + 0.45);
      tl.fromTo('#s3-tok-4', { x: 50, y: 40, scale: 0, opacity: 0 }, { x: 0, y: 0, scale: 1, opacity: 1, duration: 0.45, ease: 'back.out(2.2)' }, startT + 0.55);
      tl.fromTo('#s3-tok-5', { x: 60, scale: 0, opacity: 0 }, { x: 0, scale: 1, opacity: 1, duration: 0.45, ease: 'back.out(2.2)' }, startT + 0.65);

    // ---------------- SCENE 4: DRIVING HOME ----------------
    } else if (sc.id === 's4') {
      tl.fromTo('#s4-tag', { y: -16, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4 }, startT + 0.1);
      tl.fromTo('#s4-title', { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: 'power3.out' }, startT + 0.2);
      tl.fromTo('#s4-serif', { scale: 0.88, opacity: 0 }, { scale: 1.0, opacity: 1, duration: 0.5, ease: 'back.out(1.8)' }, startT + 0.35);

      tl.fromTo('#s4-car-card', 
        { y: 70, scale: 0.94, opacity: 0 }, 
        { y: 0, scale: 1.0, opacity: 1, duration: 0.65, ease: 'back.out(1.5)' }, 
        startT + 0.3
      );
      tl.fromTo('#s4-arrow', 
        { scale: 0, opacity: 0 }, 
        { scale: 1, opacity: 1, duration: 0.35, ease: 'back.out(2.0)' }, 
        startT + 1.2
      );
      tl.fromTo('#s4-bubble-card', 
        { y: 40, opacity: 0 }, 
        { y: 0, opacity: 1, duration: 0.5, ease: 'power3.out' }, 
        startT + 1.5
      );

    // ---------------- SCENE 5: AND THEN YOU FORGET ----------------
    } else if (sc.id === 's5') {
      tl.fromTo('#s5-curtain-t', { y: -180 }, { y: 0, duration: 0.45, ease: 'power3.out' }, startT);
      tl.fromTo('#s5-curtain-b', { y: 180 }, { y: 0, duration: 0.45, ease: 'power3.out' }, startT);
      tl.fromTo('#s5-anim', 
        { scale: 1.2, opacity: 0 }, 
        { scale: 1.0, opacity: 1, duration: 0.5, ease: 'back.out(2.2)' }, 
        startT + 0.1
      );
      tl.fromTo('#s5-serif', { scale: 0.85, opacity: 0 }, { scale: 1.0, opacity: 1, duration: 0.45, ease: 'back.out(2.4)' }, startT + 0.2);
      tl.to('#s5-curtain-t', { y: -180, duration: 0.35, ease: 'power3.in' }, endT - 0.35);
      tl.to('#s5-curtain-b', { y: 180, duration: 0.35, ease: 'power3.in' }, endT - 0.35);

    // ---------------- SCENE 6: 3 DAYS CRISIS ----------------
    } else if (sc.id === 's6') {
      tl.fromTo('#s6-tag', { y: -16, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4 }, startT + 0.1);
      tl.fromTo('#s6-title', { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: 'power3.out' }, startT + 0.2);
      tl.fromTo('#s6-serif', { scale: 0.88, opacity: 0 }, { scale: 1.0, opacity: 1, duration: 0.5, ease: 'back.out(2.0)' }, startT + 0.35);

      tl.fromTo('#s6-terminal', 
        { scale: 0.9, y: 50, opacity: 0 }, 
        { scale: 1.0, y: 0, opacity: 1, duration: 0.6, ease: 'power3.out' }, 
        startT + 0.25
      );
      // Typewriting terminal command
      tl.to('#s6-command', { text: '$ sla-monitor --client=sarah --verify', duration: 1.0, ease: 'none' }, startT + 0.4);

      // Spring-popping alert pills
      tl.fromTo('#s6-alert-1', { scale: 0, rotation: -8, opacity: 0 }, { scale: 1, rotation: 0, opacity: 1, duration: 0.4, ease: 'back.out(2.6)' }, startT + 0.7);
      tl.fromTo('#s6-alert-2', { scale: 0, rotation: 8, opacity: 0 }, { scale: 1, rotation: 0, opacity: 1, duration: 0.4, ease: 'back.out(2.6)' }, startT + 1.3);
      tl.fromTo('#s6-alert-3', { scale: 0, rotation: -6, opacity: 0 }, { scale: 1, rotation: 0, opacity: 1, duration: 0.4, ease: 'back.out(2.6)' }, startT + 1.9);
      tl.fromTo('#s6-alert-4', { scale: 0, rotation: 6, opacity: 0 }, { scale: 1, rotation: 0, opacity: 1, duration: 0.4, ease: 'back.out(2.6)' }, startT + 2.5);

    // ---------------- SCENE 7: MUBARAKTECH INSTEAD ----------------
    } else if (sc.id === 's7') {
      tl.fromTo('#s7-bracket-target .bracket-tl', { x: -45, y: -45, opacity: 0 }, { x: 0, y: 0, opacity: 1, duration: 0.45, ease: 'power3.out' }, startT + 0.1);
      tl.fromTo('#s7-bracket-target .bracket-br', { x: 45, y: 45, opacity: 0 }, { x: 0, y: 0, opacity: 1, duration: 0.45, ease: 'power3.out' }, startT + 0.1);
      tl.fromTo('#s7-portal', { scale: 0.75, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.65, ease: 'back.out(1.8)' }, startT + 0.3);
      tl.fromTo('#s7-serif', { scale: 0.85, opacity: 0 }, { scale: 1.0, opacity: 1, duration: 0.5, ease: 'back.out(2.0)' }, startT + 0.45);

    // ---------------- SCENE 8: WHATSAPP BOT ----------------
    } else if (sc.id === 's8') {
      tl.fromTo('#s8-tag', { y: -16, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4 }, startT + 0.1);
      tl.fromTo('#s8-title', { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: 'power3.out' }, startT + 0.2);
      tl.fromTo('#s8-serif', { scale: 0.88, opacity: 0 }, { scale: 1.0, opacity: 1, duration: 0.5, ease: 'back.out(2.0)' }, startT + 0.35);

      tl.fromTo('#s8-anim', 
        { y: 120, scale: 0.94, opacity: 0 }, 
        { y: 0, scale: 1.0, opacity: 1, duration: 0.75, ease: 'power3.out' }, 
        startT + 0.25
      );
      tl.fromTo('#s8-user-msg', 
        { x: 60, opacity: 0 }, 
        { x: 0, opacity: 1, duration: 0.45, ease: 'back.out(1.8)' }, 
        startT + 0.5
      );
      tl.set('#s8-ticks', { textContent: '08:34 PM ✓✓' }, startT + 1.0);
      tl.set('#s8-typing', { display: 'inline-flex', opacity: 1 }, startT + 1.2);
      tl.set('#s8-typing', { display: 'none', opacity: 0 }, startT + 1.95);
      tl.fromTo('#s8-bot-msg', 
        { scale: 0.85, opacity: 0, y: 20 }, 
        { scale: 1.0, opacity: 1, y: 0, duration: 0.5, ease: 'back.out(1.9)' }, 
        startT + 2.0
      );
      tl.fromTo('#s8-pill-1', { x: -20, opacity: 0 }, { x: 0, opacity: 1, duration: 0.25 }, startT + 2.5);
      tl.fromTo('#s8-pill-2', { x: -20, opacity: 0 }, { x: 0, opacity: 1, duration: 0.25 }, startT + 2.85);
      tl.fromTo('#s8-pill-3', { x: -20, opacity: 0 }, { x: 0, opacity: 1, duration: 0.25 }, startT + 3.2);

    // ---------------- SCENE 9: IN 40 SECONDS ----------------
    } else if (sc.id === 's9') {
      tl.fromTo('#s9-tag', { y: -16, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4 }, startT + 0.1);
      tl.fromTo('#s9-title', { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: 'power3.out' }, startT + 0.2);
      tl.fromTo('#s9-serif', { scale: 0.88, opacity: 0 }, { scale: 1.0, opacity: 1, duration: 0.5, ease: 'back.out(2.0)' }, startT + 0.35);

      tl.fromTo('#s9-anim', 
        { y: 70, opacity: 0, scale: 0.92 }, 
        { y: 0, opacity: 1, scale: 1, duration: 0.7, ease: 'back.out(1.6)' }, 
        startT + 0.25
      );
      tl.fromTo('#s9-stage-1', { x: -30, opacity: 0 }, { x: 0, opacity: 1, duration: 0.4, ease: 'power2.out' }, startT + 0.6);
      tl.fromTo('#s9-stage-2', { x: -30, opacity: 0 }, { x: 0, opacity: 1, duration: 0.4, ease: 'power2.out' }, startT + 1.2);
      tl.fromTo('#s9-stage-3', { x: -30, opacity: 0 }, { x: 0, opacity: 1, duration: 0.4, ease: 'power2.out' }, startT + 1.8);

    // ---------------- SCENE 10: PILLAR 1 EXTRACT ----------------
    } else if (sc.id === 's10') {
      tl.fromTo('#s10-tag', { y: -16, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4 }, startT + 0.1);
      tl.fromTo('#s10-title', { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: 'power3.out' }, startT + 0.2);
      tl.fromTo('#s10-serif', { scale: 0.88, opacity: 0 }, { scale: 1.0, opacity: 1, duration: 0.5, ease: 'back.out(2.0)' }, startT + 0.35);

      tl.fromTo('#s10-anim', 
        { y: 70, opacity: 0 }, 
        { y: 0, opacity: 1, duration: 0.6, ease: 'power3.out' }, 
        startT + 0.2
      );
      // Cascading 3D stacked cards
      tl.fromTo('#s10-card-1', { y: 50, opacity: 0, scale: 0.92 }, { y: 0, opacity: 1, scale: 1, duration: 0.5, ease: 'back.out(1.6)' }, startT + 0.45);
      tl.fromTo('#s10-card-2', { y: 50, opacity: 0, scale: 0.92 }, { y: 0, opacity: 1, scale: 1, duration: 0.5, ease: 'back.out(1.6)' }, startT + 1.1);
      tl.fromTo('#s10-card-3', { y: 50, opacity: 0, scale: 0.92 }, { y: 0, opacity: 1, scale: 1, duration: 0.5, ease: 'back.out(1.6)' }, startT + 1.75);

    // ---------------- SCENE 11: PILLAR 2 RECAP ----------------
    } else if (sc.id === 's11') {
      tl.fromTo('#s11-tag', { y: -16, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4 }, startT + 0.1);
      tl.fromTo('#s11-title', { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: 'power3.out' }, startT + 0.2);
      tl.fromTo('#s11-serif', { scale: 0.88, opacity: 0 }, { scale: 1.0, opacity: 1, duration: 0.5, ease: 'back.out(2.0)' }, startT + 0.35);

      tl.fromTo('#s11-anim', 
        { y: 60, opacity: 0, scale: 0.93 }, 
        { y: 0, opacity: 1, scale: 1, duration: 0.7, ease: 'back.out(1.6)' }, 
        startT + 0.25
      );
      tl.fromTo('#s11-cursor', 
        { x: 180, y: 150, opacity: 0 }, 
        { x: 0, y: 0, opacity: 1, duration: 0.85, ease: 'power2.out' }, 
        startT + 0.8
      );
      tl.to('#s11-approve-btn', { scale: 0.92, duration: 0.15, yoyo: true, repeat: 1, ease: 'power1.inOut' }, startT + 1.9);
      tl.set('#s11-btn-text', { textContent: '✓ APPROVED & SENT' }, startT + 2.05);
      tl.to('#s11-approve-btn', { backgroundColor: '#15803D', duration: 0.25 }, startT + 2.05);

    // ---------------- SCENE 12: PILLAR 3 STRIPE ----------------
    } else if (sc.id === 's12') {
      tl.fromTo('#s12-tag', { y: -16, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4 }, startT + 0.1);
      tl.fromTo('#s12-title', { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: 'power3.out' }, startT + 0.2);
      tl.fromTo('#s12-serif', { scale: 0.88, opacity: 0 }, { scale: 1.0, opacity: 1, duration: 0.5, ease: 'back.out(2.0)' }, startT + 0.35);

      tl.fromTo('#s12-anim', 
        { y: 70, opacity: 0, scale: 0.92 }, 
        { y: 0, opacity: 1, scale: 1, duration: 0.7, ease: 'back.out(1.6)' }, 
        startT + 0.25
      );
      tl.fromTo('#s12-amount', { scale: 0.8, opacity: 0 }, { scale: 1.0, opacity: 1, duration: 0.5, ease: 'back.out(2.0)' }, startT + 0.65);

    // ---------------- SCENE 13: RESULTS MONOLITHS ----------------
    } else if (sc.id === 's13') {
      tl.fromTo('#s13-tag', { y: -16, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4 }, startT + 0.1);
      tl.fromTo('#s13-card-1', 
        { x: -80, opacity: 0, scale: 0.9 }, 
        { x: 0, opacity: 1, scale: 1, duration: 0.6, ease: 'back.out(1.8)' }, 
        startT + 0.2
      );
      tl.fromTo('#s13-card-2', 
        { x: 80, opacity: 0, scale: 0.9 }, 
        { x: 0, opacity: 1, scale: 1, duration: 0.6, ease: 'back.out(1.8)' }, 
        startT + 1.2
      );

    // ---------------- SCENE 14: STOP PAYING $3,000 ----------------
    } else if (sc.id === 's14') {
      tl.fromTo('#s14-tag', { y: -16, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4 }, startT + 0.1);
      tl.fromTo('#s14-title', { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: 'power3.out' }, startT + 0.2);
      tl.fromTo('#s14-serif', { scale: 0.88, opacity: 0 }, { scale: 1.0, opacity: 1, duration: 0.5, ease: 'back.out(2.0)' }, startT + 0.35);

      tl.fromTo('#s14-anim', 
        { scale: 0.88, opacity: 0, y: 30 }, 
        { scale: 1, opacity: 1, y: 0, duration: 0.65, ease: 'back.out(1.6)' }, 
        startT + 0.25
      );
      tl.fromTo('#s14-col-left', { x: -40, opacity: 0 }, { x: 0, opacity: 1, duration: 0.5, ease: 'power2.out' }, startT + 0.6);
      tl.fromTo('#s14-col-right', { x: 40, opacity: 0 }, { x: 0, opacity: 1, duration: 0.5, ease: 'power2.out' }, startT + 0.8);

    // ---------------- SCENE 15: COMMENT VOICE ----------------
    } else if (sc.id === 's15') {
      tl.fromTo('#s15-tag', { y: -16, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4 }, startT + 0.1);
      tl.fromTo('#s15-title', { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: 'power3.out' }, startT + 0.2);
      tl.fromTo('#s15-serif', { scale: 0.88, opacity: 0 }, { scale: 1.0, opacity: 1, duration: 0.5, ease: 'back.out(2.0)' }, startT + 0.35);

      tl.fromTo('#s15-anim', 
        { scale: 0.86, opacity: 0, y: 40 }, 
        { scale: 1, opacity: 1, y: 0, duration: 0.65, ease: 'back.out(1.8)' }, 
        startT + 0.25
      );
      // Typewriting 'VOICE' letter by letter in comment box
      tl.to('#s15-typed-text', { text: 'VOICE', duration: 0.8, ease: 'none' }, startT + 0.7);
      tl.fromTo('#s15-input-box', 
        { borderColor: 'rgba(223,90,55,0.2)' }, 
        { borderColor: 'rgba(223,90,55,1.0)', boxShadow: '0 0 50px rgba(223,90,55,0.3)', duration: 0.4 }, 
        startT + 1.2
      );

    // ---------------- SCENE 16: OUTRO LOCKUP ----------------
    } else if (sc.id === 's16') {
      tl.fromTo('#s16-card .bracket-tl', { x: -40, y: -40, opacity: 0 }, { x: 0, y: 0, opacity: 1, duration: 0.45, ease: 'power3.out' }, startT + 0.1);
      tl.fromTo('#s16-card .bracket-br', { x: 40, y: 40, opacity: 0 }, { x: 0, y: 0, opacity: 1, duration: 0.45, ease: 'power3.out' }, startT + 0.1);
      tl.fromTo('#s16-anim', 
        { scale: 0.85, opacity: 0, y: 30 }, 
        { scale: 1, opacity: 1, y: 0, duration: 0.7, ease: 'back.out(1.8)' }, 
        startT + 0.2
      );
      tl.fromTo('#s16-serif', { scale: 0.88, opacity: 0 }, { scale: 1.0, opacity: 1, duration: 0.5, ease: 'back.out(2.0)' }, startT + 0.4);
    }
  });

  // HyperFrames Seek API Contract
  window.__seek = function(t) {
    tl.seek(t, false);
    renderThreeAt(t);
    updateUI(t);
  };

  /* -------------------------------------------------------------
     STUDIO CONTROLS & TIMELINE INTERACTIVITY
     ------------------------------------------------------------- */
  const audio = document.getElementById('master-audio');
  const btnPlay = document.getElementById('btn-play');
  const btnRestart = document.getElementById('btn-restart');
  const btnPrev = document.getElementById('btn-prev');
  const btnNext = document.getElementById('btn-next');
  const timeSlider = document.getElementById('time-slider');
  const timeReadout = document.getElementById('time-readout');
  const sceneStrip = document.getElementById('scene-strip');

  // Populate Jump Strip
  scenes.forEach((sc, i) => {
    const pill = document.createElement('div');
    pill.className = `scene-pill ${i === 0 ? 'active' : ''}`;
    pill.textContent = sc.name;
    pill.onclick = () => {
      seekTo(sc.t);
      if (!audio.paused) audio.play();
    };
    sceneStrip.appendChild(pill);
  });

  function updateUI(t) {
    timeSlider.value = t;
    const m = Math.floor(t / 60);
    const s = (t % 60).toFixed(2);
    timeReadout.textContent = `${String(m).padStart(2,'0')}:${String(s).padStart(5,'0')} / 01:13.08`;

    // Highlight jump strip pill
    const pills = sceneStrip.querySelectorAll('.scene-pill');
    scenes.forEach((sc, i) => {
      if (t >= sc.t && t < sc.t + sc.dur) {
        pills.forEach(p => p.classList.remove('active'));
        if (pills[i]) pills[i].classList.add('active');
      }
    });
  }

  function seekTo(t) {
    t = Math.max(0, Math.min(TOTAL_DURATION, t));
    audio.currentTime = t;
    window.__seek(t);
  }

  btnPlay.onclick = () => {
    if (audio.paused) {
      if (audio.currentTime >= TOTAL_DURATION) audio.currentTime = 0;
      audio.play();
      btnPlay.textContent = '❚❚ Pause';
    } else {
      audio.pause();
      btnPlay.textContent = '▶ Play';
    }
  };

  btnRestart.onclick = () => {
    seekTo(0);
    if (!audio.paused) audio.play();
  };

  btnPrev.onclick = () => {
    const curT = audio.currentTime;
    for (let i = scenes.length - 1; i >= 0; i--) {
      if (scenes[i].t < curT - 0.5) {
        seekTo(scenes[i].t);
        return;
      }
    }
    seekTo(0);
  };

  btnNext.onclick = () => {
    const curT = audio.currentTime;
    for (let i = 0; i < scenes.length; i++) {
      if (scenes[i].t > curT + 0.2) {
        seekTo(scenes[i].t);
        return;
      }
    }
  };

  timeSlider.oninput = (e) => {
    seekTo(parseFloat(e.target.value));
  };

  audio.ontimeupdate = () => {
    if (!audio.paused) {
      window.__seek(audio.currentTime);
    }
  };

  audio.onended = () => {
    btnPlay.textContent = '▶ Play';
  };

  // Fullscreen support
  document.getElementById('btn-fullscreen').onclick = () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen();
    } else {
      document.exitFullscreen();
    }
  };

  // Auto-fit studio viewport
  function fit() {
    if (document.body.classList.contains('headless-render')) return;
    const vp = document.getElementById('viewport-area');
    const r = document.getElementById('root');
    const scale = Math.min((vp.clientWidth - 40) / 1080, (vp.clientHeight - 40) / 1920, 1.0);
    r.style.transform = `scale(${scale})`;
  }
  window.addEventListener('resize', fit);
  fit();

  // Initial seek
  window.__seek(0);
</script>

</body>
</html>
'''

def main():
    target_path = os.path.join(os.path.dirname(__file__), 'index.html')
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(HTML_CONTENT)
    print(f"Generated successfully: {target_path} ({len(HTML_CONTENT)} bytes)")

if __name__ == '__main__':
    main()
