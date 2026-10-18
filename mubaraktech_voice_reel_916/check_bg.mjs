import { chromium } from 'playwright';

async function main() {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto("file:///e:/MubarakTech/motiongraphics/mubaraktech_voice_reel_916/index.html?render=true");
  await page.waitForFunction(() => typeof window.__seek === 'function');
  
  await page.evaluate(() => {
    const bg = document.getElementById("canvas-bg");
    bg.style.transition = 'none';
    window.__seek(9.0);
  });

  const info = await page.evaluate(() => {
    const bg = document.getElementById("canvas-bg");
    return {
      bgStyle: bg.style.backgroundColor,
      bgComputed: window.getComputedStyle(bg).backgroundColor
    };
  });
  console.log("Without transition at t=9.0s:", info);
  await browser.close();
}
main();
