const nodemailer = require('nodemailer');

async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const { contentHtml, signerName, agreementType, signDate } = req.body;

  if (!contentHtml) return res.status(400).json({ error: 'חסר תוכן הסכם' });

  try {
    const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: process.env.GMAIL_USER,
        pass: process.env.GMAIL_APP_PASSWORD
      }
    });

    const emailBody = `<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8">
<style>
  body { font-family: Arial, 'Arial Hebrew', sans-serif; direction: rtl; color: #1e2b3c; margin: 0; padding: 0; }
  .header { background: #0f2647; color: #fff; padding: 20px 30px; text-align: center; }
  .header h1 { margin: 0; font-size: 1.2rem; color: #c8a84b; }
  .meta-box { background: #f0f4f8; padding: 16px 30px; border-bottom: 2px solid #dde2ea; }
  .meta-box table { border-collapse: collapse; font-size: 14px; }
  .meta-box td { padding: 5px 14px 5px 0; }
  .meta-box td:first-child { font-weight: bold; }
  .print-bar { background: #1a3a6b; color: #fff; padding: 14px 30px; text-align: center; font-size: 0.95rem; }
  .print-bar strong { color: #f0d86e; }
  .doc-wrap { padding: 30px 40px; max-width: 794px; margin: 0 auto; }
  .doc-title { font-size: 16pt; font-weight: bold; text-align: center; margin-bottom: 20px; text-decoration: underline; }
  .clause { margin-bottom: 10px; line-height: 1.75; }
  .sig-line { border-top: 1.5px solid #333; padding-top: 6px; text-align: center; font-size: 0.88rem; min-width: 160px; }
  .sig-table { width: 100%; border-collapse: collapse; margin-top: 20px; }
  .sig-table td { width: 50%; padding: 10px; text-align: center; vertical-align: bottom; }
  .page-break { border-top: 2px dashed #ccc; margin: 30px 0; text-align: center; font-size: 0.8rem; color: #999; padding: 6px 0; }
  @media print {
    .header, .meta-box, .print-bar { display: none; }
    .doc-wrap { padding: 0; }
    body { font-size: 11pt; }
  }
</style>
</head>
<body>
<div class="header">
  <h1>Lock and Action – הסכם חתום התקבל</h1>
</div>
<div class="meta-box">
  <table>
    <tr><td>שם החותם:</td><td>${signerName}</td></tr>
    <tr><td>סוג הסכם:</td><td>${agreementType}</td></tr>
    <tr><td>תאריך חתימה:</td><td>${signDate}</td></tr>
  </table>
</div>
<div class="print-bar">
  🖨️ לשמירה כ-PDF: פתח מייל זה בדפדפן ולחץ <strong>Ctrl+P</strong> (Windows) או <strong>⌘+P</strong> (Mac) ← בחר "שמור כ-PDF"
</div>
<div class="doc-wrap">
  ${contentHtml}
</div>
</body>
</html>`;

    await transporter.sendMail({
      from: `"Lock and Action" <${process.env.GMAIL_USER}>`,
      to: 'roy2796@gmail.com, itay@lockandaction.co.il',
      subject: `✅ הסכם חתום התקבל – ${agreementType} | ${signerName}`,
      html: emailBody
    });

    res.status(200).json({ success: true });
  } catch (err) {
    console.error('Mail error:', err);
    res.status(500).json({ error: err.message || 'שגיאה בשליחת מייל' });
  }
}

handler.config = {
  api: { bodyParser: { sizeLimit: '15mb' } }
};

module.exports = handler;
