const nodemailer = require('nodemailer');

module.exports.config = {
  api: { bodyParser: { sizeLimit: '15mb' } }
};

module.exports = async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const { pdfBase64, signerName, agreementType, signDate } = req.body;

  if (!pdfBase64) return res.status(400).json({ error: 'חסר קובץ PDF' });

  const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: process.env.GMAIL_USER,
      pass: process.env.GMAIL_APP_PASSWORD
    }
  });

  const safeDate = (signDate || '').replace(/\//g, '-');
  const safeName = (signerName || 'לא_ידוע').replace(/[^א-תa-zA-Z0-9_\- ]/g, '');
  const filename = `הסכם_${safeName}_${safeDate}.pdf`;

  await transporter.sendMail({
    from: `"Lock and Action" <${process.env.GMAIL_USER}>`,
    to: 'roy2796@gmail.com, itay@lockandaction.co.il',
    subject: `✅ הסכם חתום התקבל – ${agreementType} | ${signerName}`,
    html: `
      <div dir="rtl" style="font-family:Arial,sans-serif;padding:24px;color:#1e2b3c;">
        <h2 style="color:#1a3a6b;border-bottom:2px solid #c8a84b;padding-bottom:10px;">
          התקבל הסכם חתום – Lock and Action
        </h2>
        <p>שלום,<br>מצורף הסכם חתום כקובץ PDF.</p>
        <table style="border-collapse:collapse;margin:16px 0;font-size:14px;">
          <tr style="background:#f0f4f8;">
            <td style="padding:8px 14px;font-weight:bold;border:1px solid #dde2ea;">שם החותם</td>
            <td style="padding:8px 14px;border:1px solid #dde2ea;">${signerName}</td>
          </tr>
          <tr>
            <td style="padding:8px 14px;font-weight:bold;border:1px solid #dde2ea;">סוג ההסכם</td>
            <td style="padding:8px 14px;border:1px solid #dde2ea;">${agreementType}</td>
          </tr>
          <tr style="background:#f0f4f8;">
            <td style="padding:8px 14px;font-weight:bold;border:1px solid #dde2ea;">תאריך חתימה</td>
            <td style="padding:8px 14px;border:1px solid #dde2ea;">${signDate}</td>
          </tr>
        </table>
        <p style="color:#888;font-size:12px;">נשלח אוטומטית ממערכת ההסכמים של Lock and Action</p>
      </div>
    `,
    attachments: [{
      filename,
      content: pdfBase64,
      encoding: 'base64'
    }]
  });

  res.status(200).json({ success: true });
};
