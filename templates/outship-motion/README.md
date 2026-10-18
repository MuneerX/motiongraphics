# Outship Motion Graphics Starter Template

This folder contains a clean, modular starting template for building 1920×1080 motion graphics in the Outship design aesthetic.

## Files
* `template.html`: Fully configured composition root, Three.js WebGL canvas, GSAP timeline scaffolding, studio player, and automated headless render hooks.

## Quick Start
1. Copy `template.html` to your new film directory as `index.html`.
2. Add your scene layers inside `#root`.
3. Add your GSAP timeline tweens to `tl`.
4. Render with:
```bash
node "e:\MubarakTech\motiongraphics\.agents\skills\motionmaxxing\scripts\render.mjs" index.html film.mp4 --fps 30 --crf 18 --audio audio.wav
```
