const nodemailer = require('nodemailer');
const chromium   = require('@sparticuz/chromium-min');
const puppeteer  = require('puppeteer-core');

async function generatePdf(contentHtml) {
  const html = `<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
  <meta charset="UTF-8">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Heebo', Arial, sans-serif;
      font-size: 10.5pt;
      line-height: 1.6;
      color: #111;
      direction: rtl;
      background: #fff;
    }
    .doc-title { text-align:center; font-size:17px; font-weight:700; text-decoration:underline; margin-bottom:16px; }
    .clause { margin-bottom:8px; text-align:justify; unicode-bidi:embed; }
    .fv { font-weight:600; }
    .fv.empty { color:#bbb; }
    .dynamic-val { font-weight:bold; }
    .sig-table { width:100%; margin-top:28px; border-collapse:collapse; }
    .sig-table td { width:50%; text-align:center; vertical-align:bottom; padding:10px; }
    .sig-line { margin-top:18px; border-top:1.5px solid #333; width:65%; margin-left:auto; margin-right:auto; padding-top:6px; font-size:10pt; color:#444; }
    .page-break { page-break-before:always; }
  </style>
</head>
<body>${contentHtml}</body>
</html>`;

  const executablePath = await chromium.executablePath(
    'https://github.com/Sparticuz/chromium/releases/download/v131.0.0/chromium-v131.0.0-pack.tar'
  );

  const browser = await puppeteer.launch({
    args: chromium.args,
    defaultViewport: { width: 794, height: 1123 },
    executablePath,
    headless: 'new',
  });

  const page = await browser.newPage();
  await page.setContent(html, { waitUntil: 'domcontentloaded' });
  await page.evaluateHandle('document.fonts.ready');

  const pdfBuffer = await page.pdf({
    format: 'A4',
    printBackground: true,
    margin: { top: '20mm', right: '20mm', bottom: '20mm', left: '20mm' },
  });

  await browser.close();
  return pdfBuffer;
}

async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const { contentHtml, signerName, agreementType, signDate } = req.body;
  if (!contentHtml) return res.status(400).json({ error: 'חסר תוכן הסכם' });

  try {
    const pdfBuffer = await generatePdf(contentHtml);

    const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: process.env.GMAIL_USER,
        pass: process.env.GMAIL_APP_PASSWORD
      }
    });

    const safeDate = (signDate || '').replace(/\//g, '-');
    const safeName = (signerName || 'לא_ידוע').replace(/[^\u05D0-\u05EAa-zA-Z0-9_\- ]/g, '');
    const filename = `הסכם_${safeName}_${safeDate}.pdf`;

    const emailBody = `<!DOCTYPE html>
<html lang="he" dir="rtl">
<head><meta charset="UTF-8">
<style>
  body { font-family: Arial, sans-serif; direction: rtl; color: #1e2b3c; margin: 0; padding: 0; }
  .header { background:#0f2647; color:#fff; padding:16px 28px; }
  .header h1 { margin:0; font-size:1.1rem; color:#c8a84b; }
  .meta-box { background:#f0f4f8; padding:12px 28px; border-bottom:2px solid #dde2ea; font-size:13px; }
  .meta-box table { border-collapse:collapse; }
  .meta-box td { padding:4px 14px 4px 0; }
  .meta-box td:first-child { font-weight:bold; }
</style>
</head>
<body>
  <div class="header"><h1>Lock and Action – הסכם חתום התקבל</h1></div>
  <div class="meta-box">
    <table>
      <tr><td>שם החותם:</td><td>${signerName}</td></tr>
      <tr><td>סוג הסכם:</td><td>${agreementType}</td></tr>
      <tr><td>תאריך חתימה:</td><td>${signDate}</td></tr>
    </table>
  </div>
  <p style="padding:16px 28px;font-size:14px;">ההסכם החתום מצורף כקובץ PDF.</p>
</body>
</html>`;

    await transporter.sendMail({
      from: `"Lock and Action" <${process.env.GMAIL_USER}>`,
      to: 'roy2796@gmail.com, itay@lockandaction.co.il',
      subject: `✅ הסכם חתום התקבל – ${agreementType} | ${signerName}`,
      html: emailBody,
      attachments: [{
        filename,
        content: pdfBuffer,
        contentType: 'application/pdf'
      }]
    });

    res.status(200).json({ success: true });
  } catch (err) {
    console.error('Error:', err);
    res.status(500).json({ error: err.message || 'שגיאה בשליחת מייל' });
  }
}

handler.config = {
  api: { bodyParser: { sizeLimit: '15mb' } }
};

module.exports = handler;
