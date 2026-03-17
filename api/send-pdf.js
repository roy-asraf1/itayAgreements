const nodemailer = require('nodemailer');

async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const { contentHtml, pdfBase64, signerName, agreementType, signDate } = req.body;

  if (!contentHtml) return res.status(400).json({ error: 'חסר תוכן הסכם' });

  try {
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
  body { font-family: Arial, 'Arial Hebrew', sans-serif; direction: rtl; color: #1e2b3c; margin: 0; padding: 0; }
  .header { background:#0f2647; color:#fff; padding:16px 28px; }
  .header h1 { margin:0; font-size:1.1rem; color:#c8a84b; }
  .meta-box { background:#f0f4f8; padding:12px 28px; border-bottom:2px solid #dde2ea; font-size:13px; }
  .meta-box table { border-collapse:collapse; }
  .meta-box td { padding:4px 14px 4px 0; }
  .meta-box td:first-child { font-weight:bold; }
  .doc-wrap { padding:28px 36px; max-width:794px; margin:0 auto; }
  .doc-title { font-size:15pt; font-weight:bold; text-align:center; margin-bottom:18px; text-decoration:underline; }
  .clause { margin-bottom:10px; line-height:1.75; }
  .sig-line { border-top:1.5px solid #333; padding-top:6px; text-align:center; font-size:0.85rem; min-width:160px; }
  .sig-table { width:100%; border-collapse:collapse; margin-top:18px; }
  .sig-table td { width:50%; padding:10px; text-align:center; vertical-align:bottom; }
  .page-break { border-top:2px dashed #ccc; margin:28px 0; text-align:center; font-size:0.8rem; color:#999; padding:4px 0; }
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
<div class="doc-wrap">${contentHtml}</div>
</body></html>`;

    const mailOptions = {
      from: `"Lock and Action" <${process.env.GMAIL_USER}>`,
      to: 'roy2796@gmail.com, itay@lockandaction.co.il',
      subject: `✅ הסכם חתום התקבל – ${agreementType} | ${signerName}`,
      html: emailBody
    };

    if (pdfBase64) {
      mailOptions.attachments = [{
        filename,
        content: pdfBase64,
        encoding: 'base64'
      }];
    }

    await transporter.sendMail(mailOptions);

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
