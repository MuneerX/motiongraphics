// =====================================================================
//  styles/dark-tech/kit.js — Luxury Dark 3D Tech Launch Look
//  Engineered for Saudi Fab Store & MubarakTech
//  Obsidian glassmorphism, Saudi Fab yellow & cyan neon accents,
//  floating device frames, kinetic product typography & enterprise HUD.
// =====================================================================

const TECH_PAL = {
  ground: '#050811',
  groundDeep: '#020409',
  surface: '#0d1527',
  surfaceCard: 'rgba(13, 21, 39, 0.85)',
  surfaceGlass: 'rgba(20, 32, 58, 0.65)',
  border: 'rgba(255, 255, 255, 0.12)',
  borderActive: 'rgba(254, 236, 60, 0.75)',
  yellow: '#FEEC3C',
  gold: '#F59E0B',
  cyan: '#38BDF8',
  blue: '#0058A3',
  neonBlue: '#0EA5E9',
  white: '#FFFFFF',
  silver: '#E2E8F0',
  muted: '#94A3B8',
  darkMuted: '#64748B',
  success: '#10B981',
};

// Background perspective cyber grid & particle dust
function techGrid(o = {}) {
  ctx.save();
  const t = TT * 0.4;
  
  // Radial glow gradient at top/center
  const grad = ctx.createRadialGradient(CX, 350, 50, CX, 450, 800);
  grad.addColorStop(0, 'rgba(0, 88, 163, 0.18)');
  grad.addColorStop(0.5, 'rgba(14, 165, 233, 0.06)');
  grad.addColorStop(1, 'rgba(5, 8, 17, 0)');
  ctx.fillStyle = grad;
  ctx.fillRect(0, 0, W, H);

  // Subtle horizontal perspective grid lines
  ctx.strokeStyle = 'rgba(56, 189, 248, 0.05)';
  ctx.lineWidth = 1;
  const horizon = 700;
  for (let y = horizon; y < H; y += 45 + (y - horizon) * 0.12) {
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(W, y);
    ctx.stroke();
  }

  // Subtle floating light particles
  const n = 35;
  for (let i = 0; i < n; i++) {
    const rx = ((i * 137.5 + t * 40) % W);
    const ry = ((i * 223.1 + Math.sin(t + i) * 60) % H);
    const r = (i % 3 === 0) ? 2.5 : 1.5;
    const a = 0.15 + 0.25 * Math.sin(t * 2 + i);
    ctx.fillStyle = (i % 2 === 0) ? `rgba(254, 236, 60, ${a})` : `rgba(56, 189, 248, ${a})`;
    ctx.beginPath();
    ctx.arc(rx, ry, r, 0, TAU);
    ctx.fill();
  }
  ctx.restore();
}

// Glassmorphism Card Container
function techCard(x, y, w, h, o = {}) {
  ctx.save();
  const r = o.r ?? 18;
  const P = rrectPts(x, y, w, h, r);
  
  // Shadow
  if (o.shadow !== false) {
    ctx.shadowColor = o.shadowColor ?? 'rgba(0, 0, 0, 0.65)';
    ctx.shadowBlur = o.sb ?? 30;
    ctx.shadowOffsetY = o.sy ?? 16;
  }
  
  // Background Fill
  trace(P, true);
  const grad = ctx.createLinearGradient(x, y, x + w * 0.5, y + h);
  grad.addColorStop(0, o.bg0 ?? 'rgba(22, 34, 60, 0.88)');
  grad.addColorStop(1, o.bg1 ?? 'rgba(9, 15, 29, 0.94)');
  ctx.fillStyle = grad;
  ctx.fill();
  
  // 1px Glass Border
  ctx.shadowColor = 'transparent';
  ctx.lineWidth = o.borderW ?? 1.5;
  ctx.strokeStyle = o.borderColor ?? TECH_PAL.border;
  trace(P, true);
  ctx.stroke();

  // Subtle corner glow accents if requested
  if (o.glow) {
    ctx.shadowColor = o.glowColor ?? TECH_PAL.yellow;
    ctx.shadowBlur = 12;
    ctx.strokeStyle = o.glowColor ?? TECH_PAL.yellow;
    ctx.lineWidth = 2;
    // draw corner ticks
    const tick = 16;
    ctx.beginPath();
    ctx.moveTo(x, y + tick); ctx.lineTo(x, y + r); ctx.arcTo(x, y, x + r, y, r); ctx.lineTo(x + tick, y);
    ctx.moveTo(x + w - tick, y); ctx.lineTo(x + w - r, y); ctx.arcTo(x + w, y, x + w, y + r, r); ctx.lineTo(x + w, y + tick);
    ctx.stroke();
  }

  ctx.restore();
}

// Sleek Device Mockup Frame (MacBook / Enterprise Browser) with embedded asset
function deviceMockup(x, y, w, h, assetName, o = {}) {
  ctx.save();
  const r = o.r ?? 16;
  const headerH = o.headerH ?? 42;
  
  // Outer chassis shadow & body
  techCard(x, y, w, h, {
    r,
    sb: 40,
    sy: 20,
    shadowColor: 'rgba(0, 0, 0, 0.8)',
    borderColor: o.active ? TECH_PAL.borderActive : 'rgba(255, 255, 255, 0.15)',
    borderW: o.active ? 2 : 1.2,
    glow: o.active,
    glowColor: TECH_PAL.yellow
  });

  // Browser Top Bar
  ctx.save();
  const topP = rrectPts(x, y, w, headerH, r);
  trace(topP, true);
  ctx.clip();
  ctx.fillStyle = 'rgba(10, 16, 32, 0.95)';
  ctx.fillRect(x, y, w, headerH);
  
  // 3 Window control dots
  const dotR = 5;
  const dotY = y + headerH / 2;
  const colors = ['#EF4444', '#F59E0B', '#10B981'];
  for (let i = 0; i < 3; i++) {
    ctx.beginPath();
    ctx.arc(x + 20 + i * 16, dotY, dotR, 0, TAU);
    ctx.fillStyle = colors[i];
    ctx.fill();
  }

  // Address Bar Pill
  const pillW = Math.min(w * 0.55, 420);
  const pillX = x + (w - pillW) / 2;
  const pillY = y + 8;
  const pillH = headerH - 16;
  ctx.fillStyle = 'rgba(255, 255, 255, 0.08)';
  ctx.beginPath();
  ctx.roundRect(pillX, pillY, pillW, pillH, pillH / 2);
  ctx.fill();

  // URL text
  ctx.font = '500 13px system-ui, -apple-system, sans-serif';
  ctx.fillStyle = TECH_PAL.muted;
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText(o.url ?? 'saudifabstore.vercel.app', pillX + pillW / 2, pillY + pillH / 2);
  ctx.restore();

  // Screen Area & Embedded Asset
  const screenX = x + 2;
  const screenY = y + headerH;
  const screenW = w - 4;
  const screenH = h - headerH - 2;

  ctx.save();
  ctx.beginPath();
  ctx.roundRect(screenX, screenY, screenW, screenH, [0, 0, r - 2, r - 2]);
  ctx.clip();
  
  ctx.fillStyle = '#060B17';
  ctx.fillRect(screenX, screenY, screenW, screenH);

  if (typeof ASSETS !== 'undefined' && ASSETS[assetName]) {
    const img = ASSETS[assetName];
    // Pan or zoom within screenshot if requested
    const panY = o.panY ?? 0;
    const zoom = o.zoom ?? 1;
    const dw = screenW * zoom;
    const dh = (img.height / img.width) * dw;
    const dx = screenX + (screenW - dw) / 2;
    const dy = screenY - panY;
    ctx.drawImage(img, dx, dy, dw, dh);
  }
  ctx.restore();

  // Inner subtle screen highlight border
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.06)';
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.roundRect(screenX, screenY, screenW, screenH, [0, 0, r - 2, r - 2]);
  ctx.stroke();

  ctx.restore();
}

// Glowing Tech Badge / Pill
function techBadge(str, x, y, o = {}) {
  ctx.save();
  const fontSz = o.size ?? 22;
  ctx.font = `700 ${fontSz}px 'Plus Jakarta Sans', system-ui, sans-serif`;
  const textW = ctx.measureText(str).width;
  const padX = o.padX ?? 24;
  const padY = o.padY ?? 12;
  const w = textW + padX * 2 + (o.icon ? 24 : 0);
  const h = fontSz + padY * 2;
  const bx = x - (o.align === 'center' ? w / 2 : (o.align === 'right' ? w : 0));
  const by = y - h / 2;

  // Badge capsule background
  ctx.beginPath();
  ctx.roundRect(bx, by, w, h, h / 2);
  ctx.fillStyle = o.bg ?? 'rgba(14, 26, 48, 0.85)';
  ctx.fill();

  // Glowing stroke
  ctx.lineWidth = o.borderW ?? 1.5;
  ctx.strokeStyle = o.color ?? TECH_PAL.yellow;
  if (o.glow !== false) {
    ctx.shadowColor = o.color ?? TECH_PAL.yellow;
    ctx.shadowBlur = o.blur ?? 12;
  }
  ctx.stroke();

  // Inner Dot / Icon
  ctx.shadowColor = 'transparent';
  let tx = bx + padX;
  if (o.dot !== false) {
    ctx.beginPath();
    ctx.arc(tx + 4, y, 4, 0, TAU);
    ctx.fillStyle = o.color ?? TECH_PAL.yellow;
    ctx.fill();
    tx += 18;
  }

  // Text
  ctx.fillStyle = o.textColor ?? TECH_PAL.white;
  ctx.textBaseline = 'middle';
  ctx.textAlign = 'left';
  ctx.fillText(str, tx, y);

  ctx.restore();
  return w;
}

// Kinetic Title Typography with glowing accents
function kineticTitle(str, x, y, size, o = {}) {
  if (typeof size === 'object' && size !== null) { o = size; size = o.size ?? 32; }
  size = Number(size) || 32;
  ctx.save();
  ctx.font = `${o.weight ?? 800} ${size}px 'Plus Jakarta Sans', system-ui, sans-serif`;
  ctx.textAlign = o.align ?? 'center';
  ctx.textBaseline = 'alphabetic';

  if (o.glow) {
    ctx.shadowColor = o.glowColor ?? TECH_PAL.yellow;
    ctx.shadowBlur = o.glowBlur ?? 20;
  }

  // Subtle gradient fill
  const w = ctx.measureText(str).width;
  const startX = o.align === 'center' ? x - w / 2 : x;
  const grad = ctx.createLinearGradient(startX, y - size, startX + w, y);
  grad.addColorStop(0, o.c0 ?? TECH_PAL.white);
  grad.addColorStop(1, o.c1 ?? (o.accent ? TECH_PAL.yellow : TECH_PAL.silver));
  ctx.fillStyle = grad;

  const frac = clamp(o.frac ?? 1);
  if (frac < 1) {
    ctx.beginPath();
    ctx.rect(startX - 10, y - size * 1.3, w * frac + 20, size * 1.8);
    ctx.clip();
  }

  ctx.fillText(str, x, y);
  ctx.restore();
}

// Animated Telemetry Metric Counter Card
function metricCounter(numStr, label, x, y, w, h, o = {}) {
  techCard(x, y, w, h, {
    r: 16,
    bg0: 'rgba(16, 26, 48, 0.85)',
    bg1: 'rgba(8, 14, 28, 0.95)',
    borderColor: o.active ? TECH_PAL.yellow : 'rgba(255, 255, 255, 0.12)',
    glow: o.active,
    glowColor: TECH_PAL.yellow
  });

  ctx.save();
  // Big Metric Value
  ctx.font = "800 48px 'Plus Jakarta Sans', system-ui, sans-serif";
  ctx.textAlign = 'center';
  ctx.fillStyle = o.numColor ?? TECH_PAL.yellow;
  ctx.fillText(numStr, x + w / 2, y + h * 0.48);

  // Small descriptive label below
  ctx.font = "600 20px 'Plus Jakarta Sans', system-ui, sans-serif";
  ctx.fillStyle = TECH_PAL.muted;
  ctx.fillText(label, x + w / 2, y + h * 0.80);
  ctx.restore();
}

// Hero Spark Symbol: Gyroscopic Industrial Precision Atom
function drawHeroSpark(x, y, r, o = {}) {
  ctx.save();
  const t = TT * 1.5;
  const key = o.key ?? 'spark';
  
  // Set SPARK_AT for anchor check
  SPARK_AT = toScreen(x, y);

  // Outer glowing aura
  const grad = ctx.createRadialGradient(x, y, r * 0.2, x, y, r * 2.2);
  grad.addColorStop(0, 'rgba(254, 236, 60, 0.35)');
  grad.addColorStop(0.5, 'rgba(14, 165, 233, 0.15)');
  grad.addColorStop(1, 'rgba(5, 8, 17, 0)');
  ctx.fillStyle = grad;
  ctx.beginPath();
  ctx.arc(x, y, r * 2.2, 0, TAU);
  ctx.fill();

  // Precision Rotating Gyroscope Rings
  const rings = [
    { rad: r * 1.2, speed: 1.0, color: TECH_PAL.yellow, lw: 2.5 },
    { rad: r * 0.9, speed: -1.4, color: TECH_PAL.cyan, lw: 2.0 },
    { rad: r * 0.6, speed: 2.1, color: TECH_PAL.white, lw: 1.5 }
  ];

  for (const ring of rings) {
    ctx.save();
    ctx.translate(x, y);
    ctx.rotate(t * ring.speed);
    ctx.lineWidth = ring.lw;
    ctx.strokeStyle = ring.color;
    ctx.shadowColor = ring.color;
    ctx.shadowBlur = 10;
    
    ctx.beginPath();
    ctx.ellipse(0, 0, ring.rad, ring.rad * 0.45, 0, 0, TAU);
    ctx.stroke();

    // Orbital marker node
    ctx.fillStyle = ring.color;
    ctx.beginPath();
    ctx.arc(ring.rad, 0, 4, 0, TAU);
    ctx.fill();
    ctx.restore();
  }

  // Central Core Diamond
  ctx.save();
  ctx.translate(x, y);
  ctx.rotate(t * 0.5);
  ctx.fillStyle = TECH_PAL.yellow;
  ctx.shadowColor = TECH_PAL.yellow;
  ctx.shadowBlur = 20;
  ctx.beginPath();
  const cr = r * 0.35;
  ctx.moveTo(0, -cr); ctx.lineTo(cr, 0); ctx.lineTo(0, cr); ctx.lineTo(-cr, 0);
  ctx.closePath();
  ctx.fill();
  ctx.restore();

  ctx.restore();
}

// MubarakTech Agency Climax Signature
function drawAgencySignature(cx, cy, scale = 1, o = {}) {
  ctx.save();
  ctx.translate(cx, cy);
  ctx.scale(scale, scale);

  // Anamorphic Cyan & Gold Light Flare Behind Logo
  const flareGrad = ctx.createRadialGradient(0, 0, 20, 0, 0, 480);
  flareGrad.addColorStop(0, 'rgba(56, 189, 248, 0.45)');
  flareGrad.addColorStop(0.3, 'rgba(254, 236, 60, 0.20)');
  flareGrad.addColorStop(1, 'rgba(5, 8, 17, 0)');
  ctx.fillStyle = flareGrad;
  ctx.fillRect(-500, -200, 1000, 400);

  // Logo Rendering
  if (typeof ASSETS !== 'undefined' && ASSETS['brandlogo.png']) {
    const logo = ASSETS['brandlogo.png'];
    const lw = 560;
    const lh = (logo.height / logo.width) * lw;
    ctx.shadowColor = 'rgba(56, 189, 248, 0.75)';
    ctx.shadowBlur = 25;
    ctx.drawImage(logo, -lw / 2, -lh / 2 - 30, lw, lh);
  }

  // Agency Tagline Subtitle
  ctx.shadowColor = 'transparent';
  ctx.font = "700 20px 'Plus Jakarta Sans', system-ui, sans-serif";
  ctx.textAlign = 'center';
  ctx.letterSpacing = '1.5px';
  ctx.fillStyle = TECH_PAL.silver;
  ctx.fillText("DIGITAL PRODUCT & ENTERPRISE ENGINEERING", 0, 75);

  // CTA Pill Button
  techBadge("POWERING ENTERPRISE WEB", 0, 135, {
    size: 19,
    color: TECH_PAL.cyan,
    align: 'center',
    bg: 'rgba(14, 165, 233, 0.18)',
    dot: true
  });

  ctx.restore();
}

// Captions through DEFER
const techTag = (str) => {
  const f = () => techBadge(str, 80, 280, { size: 26, color: TECH_PAL.yellow, align: 'left' });
  if (typeof DEFER !== 'undefined' && DEFER) DEFER.push(f); else f();
};

const techCaption = (str) => {
  const f = () => {
    ctx.save();
    ctx.font = "700 24px 'Plus Jakarta Sans', system-ui, sans-serif";
    ctx.textAlign = 'center';
    ctx.fillStyle = TECH_PAL.white;
    ctx.shadowColor = 'rgba(0,0,0,0.85)';
    ctx.shadowBlur = 12;
    ctx.fillText(str, CX, 1440);
    ctx.restore();
  };
  if (typeof DEFER !== 'undefined' && DEFER) DEFER.push(f); else f();
};

// =====================================================================
//  STYLE — The Renderer's Hooks Contract
// =====================================================================
const STYLE = {
  name: 'dark-tech',
  paper: '#050811',
  backdrop(c, o) {
    fillAll(c || '#050811');
    techGrid();
  },
  window(P, key, src, o) {
    ctx.save();
    trace(P, true);
    ctx.clip();
    ctx.drawImage(src, 0, 0);
    ctx.restore();
    ctx.save();
    trace(P, true);
    ctx.lineWidth = 3;
    ctx.strokeStyle = TECH_PAL.yellow;
    ctx.shadowColor = 'rgba(254, 236, 60, 0.6)';
    ctx.shadowBlur = 16;
    ctx.stroke();
    ctx.restore();
  },
  blob(P, c, key, u, o) {
    ctx.save();
    trace(P, true);
    ctx.fillStyle = c;
    ctx.shadowColor = c;
    ctx.shadowBlur = 24;
    ctx.fill();
    ctx.lineWidth = 2;
    ctx.strokeStyle = '#FFFFFF';
    ctx.stroke();
    ctx.restore();
  },
  hero(x, y, r, o) {
    drawHeroSpark(x, y, r, o);
  },
  heroColor: '#FEEC3C',
  post() {},
  ones: true
};
