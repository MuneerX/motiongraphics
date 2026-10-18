import { chromium } from 'playwright';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

async function main() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1080, height: 1920 },
    deviceScaleFactor: 1
  });
  const page = await context.newPage();

  const htmlPath = path.resolve(__dirname, 'index.html');
  const fileUrl = `file://${htmlPath.replace(/\\/g, '/')}?render=true`;
  console.log(`Navigating to ${fileUrl}...`);
  await page.goto(fileUrl, { waitUntil: 'networkidle' });

  // Wait for window.__seek to be available
  await page.waitForFunction(() => typeof window.__seek === 'function');

  const stillsDir = path.resolve(__dirname, 'stills');
  if (!fs.existsSync(stillsDir)) {
    fs.mkdirSync(stillsDir, { recursive: true });
  }

  const timestamps = [
    { name: 'still_s1_2.00s.png', t: 2.00 },
    { name: 'still_s2_9.00s.png', t: 9.00 },
    { name: 'still_s3_16.00s.png', t: 16.00 },
    { name: 'still_s4_20.00s.png', t: 20.00 },
    { name: 'still_s5_25.00s.png', t: 25.00 },
    { name: 'still_s6_28.00s.png', t: 28.00 },
    { name: 'still_s7_32.00s.png', t: 32.00 },
    { name: 'still_s8_36.00s.png', t: 36.00 },
    { name: 'still_s9_40.00s.png', t: 40.00 },
    { name: 'still_s10_44.00s.png', t: 44.00 },
    { name: 'still_s11_49.00s.png', t: 49.00 },
    { name: 'still_s12_54.00s.png', t: 54.00 },
    { name: 'still_s13_58.00s.png', t: 58.00 },
    { name: 'still_s14_63.00s.png', t: 63.00 },
    { name: 'still_s15_68.00s.png', t: 68.00 },
    { name: 'still_s16_71.00s.png', t: 71.00 }
  ];

  for (const item of timestamps) {
    await page.evaluate((time) => {
      window.__seek(time);
    }, item.t);

    await page.waitForTimeout(100);

    const outPath = path.join(stillsDir, item.name);
    await page.screenshot({ path: outPath });
    console.log(`Captured: ${item.name} at t=${item.t}s`);
  }

  await browser.close();
  console.log('All stills captured successfully!');
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
