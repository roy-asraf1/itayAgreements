import os

INDEX_CODE = """<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>איתי ראובני – יצירת הסכמים</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root { --navy: #0f2647; --blue: #1a3a6b; --gold: #c8a84b; --goldlt: #f0d86e; --bg: #0d1c35; --white: #ffffff; --muted: #6b7a8d; --border: #dde2ea; --radius: 16px; --shadow: 0 8px 40px rgba(0,0,0,.22); }
    body { font-family: 'Segoe UI', 'Arial Hebrew', Arial, sans-serif; background: linear-gradient(160deg, var(--bg) 0%, var(--blue) 100%); min-height: 100vh; color: #1e2b3c; direction: rtl; }
    .site-header { position: sticky; top: 0; display: flex; align-items: center; padding: 14px 32px; background: rgba(15,38,71,.88); border-bottom: 1px solid rgba(200,168,75,.25); z-index: 100; }
    .logo { display: flex; align-items: center; gap: 12px; text-decoration: none; }
    .logo-icon { width: 46px; height: 46px; background: linear-gradient(135deg, var(--gold), var(--goldlt)); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 22px; }
    .logo-title { color: var(--white); font-size: 18px; font-weight: 700; }
    .logo-sub { color: var(--gold); font-size: 12px; }
    .home-hero { text-align: center; padding: 50px 16px 36px; }
    .home-hero h2 { color: var(--white); font-size: 2.5rem; margin-bottom: 12px; font-weight: 800; }
    .home-hero p { color: rgba(255,255,255,.68); font-size: 1.05rem; }
    .cards-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 26px; max-width: 1060px; margin: 0 auto; padding: 0 10px; }
    .card { background: var(--white); border-radius: var(--radius); padding: 30px 26px 24px; position: relative; overflow: hidden; border: 2px solid transparent; text-decoration: none; display: block; color: inherit; box-shadow: var(--shadow); transition: transform .25s, box-shadow .25s, border-color .25s; }
    .card:hover { transform: translateY(-7px); box-shadow: 0 20px 55px rgba(0,0,0,.32); border-color: var(--gold); }
    .card-badge { position: absolute; top: 16px; left: 16px; font-size: 11px; font-weight: 700; padding: 3px 11px; border-radius: 20px; background: #27ae60; color: #fff; }
    .card-icon { width: 60px; height: 60px; background: linear-gradient(135deg, var(--blue), #2a5298); border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 26px; margin-bottom: 18px; }
    .card h3 { font-size: 1.2rem; color: var(--blue); margin-bottom: 8px; }
    .card p { color: var(--muted); font-size: .92rem; line-height: 1.6; }
    .card-cta { margin-top: 18px; color: var(--gold); font-weight: 700; font-size: .95rem; }
    #loginOverlay { position:fixed; inset:0; z-index:9999; background: linear-gradient(160deg, var(--bg) 0%, var(--blue) 100%); display:flex; align-items:center; justify-content:center; }
    #loginOverlay.hidden { display:none; }
    .login-box { background:var(--white); border-radius:var(--radius); padding:40px 36px; box-shadow: 0 20px 60px rgba(0,0,0,.35); text-align:center; max-width:380px; width:90%; }
    .login-box h2 { color:var(--blue); font-size:1.3rem; margin-top: 15px;}
    .login-box input { width:100%; padding:11px 14px; border:1.5px solid var(--border); border-radius:10px; font-size:1.05rem; text-align:center; direction:ltr; margin-top: 20px; outline:none; }
    .login-box button { width:100%; margin-top:14px; padding:12px; background:linear-gradient(135deg, var(--blue), #2a5298); color:#fff; border:none; border-radius:10px; font-size:.95rem; font-weight:700; cursor:pointer; }
    .login-err { color:#e00; font-size:.82rem; margin-top:10px; min-height:1.2em; }
  </style>
</head>
<body>
  <div id="loginOverlay">
    <div class="login-box">
      <div class="logo-icon" style="margin:0 auto">🔒</div>
      <h2>איתי ראובני</h2>
      <p style="color:#6b7a8d;font-size:0.9rem;margin-top:5px;">הכנס קוד גישה למערכת</p>
      <input id="loginCode" type="password" placeholder="קוד גישה" maxlength="20" onkeydown="if(event.key==='Enter')checkLogin()" />
      <button onclick="checkLogin()">כניסה</button>
      <div class="login-err" id="loginErr"></div>
    </div>
  </div>
  <script>
    function checkLogin(){
      if(document.getElementById('loginCode').value.trim()==='0547351024'){
        document.getElementById('loginOverlay').classList.add('hidden');
        try { sessionStorage.setItem('auth','1'); } catch(e){}
      } else { document.getElementById('loginErr').textContent='קוד שגוי, נסה שנית'; }
    }
    try { if(sessionStorage.getItem('auth')==='1') document.getElementById('loginOverlay').classList.add('hidden'); } catch(e){}
  </script>

  <header class="site-header">
    <a href="index.html" class="logo">
      <div class="logo-icon">📋</div>
      <div><div class="logo-title">איתי ראובני</div><div class="logo-sub">יצירת הסכמים</div></div>
    </a>
  </header>

  <div class="home-hero">
    <h2>יצירת הסכמים מקצועיים</h2>
    <p>תפריט ראשי - בחר את ההסכם הרצוי מהרשימה</p>
  </div>

  <div class="cards-grid">
    <a href="agreement1.html" class="card">
      <span class="card-badge ok">זמין</span>
      <div class="card-icon">🏠</div>
      <h3>הסכם בין בעל נכס למזמין</h3>
      <p>הסכם המסדיר את ביצוע הצילומים בנכס בין בעל הנכס לבין מזמין השירות</p>
      <div class="card-cta">לחץ ליצירה ←</div>
    </a>
    <a href="agreement2.html" class="card">
      <span class="card-badge ok">זמין</span>
      <div class="card-icon">📸</div>
      <h3>הסכם בין בעל נכס לאיתי</h3>
      <p>הסכם שירותי צילום נדל"ן בין בעל הנכס לבין הצלם איתי ראובני</p>
      <div class="card-cta">לחץ ליצירה ←</div>
    </a>
    <a href="agreement3.html" class="card">
      <span class="card-badge ok">זמין</span>
      <div class="card-icon">🤝</div>
      <h3>הסכם בין לקוח לאיתי</h3>
      <p>הסכם שירותי צילום בין הלקוח לבין איתי ראובני (Lock and Action)</p>
      <div class="card-cta">לחץ ליצירה ←</div>
    </a>
  </div>
</body>
</html>
"""

AG1_CODE = """<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>הסכם 1 - בעל נכס למזמין</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css" />
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root { --navy:#0f2647; --blue:#1a3a6b; --gold:#c8a84b; --goldlt:#f0d86e; --bg:#0d1c35; --white:#ffffff; --offwh:#f7f8fc; --text:#1e2b3c; --muted:#6b7a8d; --border:#dde2ea; --radius:16px; --shadow:0 8px 40px rgba(0,0,0,.22); }
    body { font-family: 'Segoe UI', 'Arial Hebrew', Arial, sans-serif; background: linear-gradient(160deg, var(--bg) 0%, var(--blue) 100%); min-height: 100vh; color: var(--text); direction: rtl; }
    .site-header { position: sticky; top: 0; display: flex; align-items: center; justify-content: space-between; padding: 14px 32px; background: rgba(15,38,71,.88); border-bottom: 1px solid rgba(200,168,75,.25); z-index:200; }
    .logo { display: flex; align-items: center; gap: 12px; text-decoration: none; }
    .logo-icon { width: 46px; height: 46px; background: linear-gradient(135deg, var(--gold), var(--goldlt)); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 22px; }
    .logo-title { color: var(--white); font-size: 18px; font-weight: 700; }
    .logo-sub { color: var(--gold); font-size: 12px; }
    #backBtn { padding: 8px 22px; background: transparent; border: 1.5px solid var(--gold); color: var(--gold); border-radius: 8px; cursor: pointer; font-size: 14px; font-weight: 600; text-decoration: none; transition: .2s; }
    #backBtn:hover { background: var(--gold); color: var(--navy); }
    .page { padding: 36px 20px 60px; min-height: calc(100vh - 74px); display: block; }
    .editor-wrap { display: grid; grid-template-columns: 370px 1fr; gap: 28px; max-width: 1220px; margin: 0 auto; align-items: start; }
    @media (max-width: 880px) { .editor-wrap { grid-template-columns: 1fr; } }
    .form-panel { background: var(--white); border-radius: var(--radius); padding: 28px 24px; box-shadow: var(--shadow); position: sticky; top: 88px; }
    .form-panel > h2 { font-size: 1.25rem; color: var(--blue); border-bottom: 3px solid var(--gold); padding-bottom: 12px; margin-bottom: 4px; }
    .form-panel > .fp-sub { color: var(--muted); font-size: .83rem; margin-bottom: 22px; }
    .sec-title { font-size: .73rem; font-weight: 700; text-transform: uppercase; letter-spacing: .6px; color: var(--blue); margin: 20px 0 10px; display: flex; align-items: center; gap: 8px; }
    .sec-title::after { content:''; flex:1; height:1px; background: rgba(26,58,107,.18); }
    .frow { margin-bottom: 12px; }
    .frow label { display:block; font-size:.82rem; font-weight:600; color:#556; margin-bottom:5px; }
    input[type=text], input[type=number], select { width:100%; padding:9px 13px; border:1.5px solid var(--border); border-radius:9px; font-family:inherit; font-size:.93rem; color: var(--text); background: var(--offwh); direction:rtl; outline:none; transition: .2s; }
    input:focus, select:focus { border-color: var(--blue); box-shadow: 0 0 0 3px rgba(26,58,107,.1); background:#fff; }
    .row2 { display:grid; grid-template-columns:1fr 1fr; gap:10px; }
    .id-wrap { display:flex; gap:8px; }
    .id-wrap select { width:105px; flex-shrink:0; }
    .btn-gen { width:100%; margin-top:16px; padding:13px; background: linear-gradient(135deg, var(--blue), #2a5298); color:#fff; border:none; border-radius:12px; font-size:.97rem; font-weight:700; cursor:pointer; display:flex; align-items:center; justify-content:center; gap:9px; box-shadow: 0 5px 18px rgba(26,58,107,.32); }
    .btn-gen:hover { transform:translateY(-2px); }
    .preview-panel { background: var(--white); border-radius: var(--radius); padding: 26px 28px; box-shadow: var(--shadow); }
    .preview-top { display:flex; justify-content:space-between; align-items:center; margin-bottom:18px; padding-bottom:14px; border-bottom:2px solid #eef0f5; }
    .preview-top h3 { color: var(--blue); font-size:1rem; }
    .btn-pdf { padding:9px 22px; background: linear-gradient(135deg, var(--gold), var(--goldlt)); color: var(--navy); border:none; border-radius:9px; font-size:.9rem; font-weight:700; cursor:pointer; box-shadow:0 3px 12px rgba(200,168,75,.35); transition:.2s; }
    .btn-pdf:hover { transform:translateY(-2px); box-shadow:0 6px 20px rgba(200,168,75,.45); }
    
    .doc-scroll { max-height: 72vh; overflow-y:auto; border:1px solid #e8eaf0; border-radius:12px; padding: 20px; background: #eaedf2; display: flex; justify-content: center;}
    
    /* PDF Container strictly constrained */
    #doc-container {
        width: 190mm; /* perfectly centered for A4 size (210mm) deducting margins */
        min-height: 270mm;
        padding: 40px 30px; 
        background: #ffffff;
        box-shadow: 0px 5px 20px rgba(0,0,0,0.15);
        position: relative;
        direction: rtl;
        text-align: right;
        font-family: Arial, sans-serif;
        font-size: 11pt; 
        line-height: 1.5; 
        color: #111;
        box-sizing: border-box;
    }

    .doc-title { text-align:center; font-size:20px; font-weight:700; text-decoration:underline; margin-bottom:10px; }
    
    /* Bolding user data safely */
    .dynamic-val { display:inline-block; font-weight:bold; padding:0 3px; min-width:30px; border-bottom:1px solid #111; white-space:nowrap; }

    /* Fix bullet margins in PDF */
    ul.ag-list { margin: 10px 0; padding-right: 15px; list-style-position: inside; direction:rtl; text-align:right;}
    ul.ag-list li { margin-bottom: 4px; }
  </style>
</head>
<body>

  <header class="site-header">
    <a href="index.html" class="logo">
      <div class="logo-icon">📋</div>
      <div><div class="logo-title">איתי ראובני</div><div class="logo-sub">יצירת הסכמים</div></div>
    </a>
    <a id="backBtn" href="index.html">← חזרה לדף הבית</a>
  </header>

  <section class="page">
    <div class="editor-wrap">
      
      <!-- FORM -->
      <div class="form-panel">
        <h2>מילוי פרטי ההסכם</h2>
        <p class="fp-sub">הסכם בין בעל נכס למזמין</p>

        <div class="sec-title">תאריך וזמן</div>
        <div class="frow"><label>תאריך ההסכם</label><input id="a1date" type="text" placeholder="לחץ לבחירת תאריך..." readonly /></div>
        <div class="row2">
          <div class="frow"><label>שעת התחלה</label><input id="a1tstart" type="text" placeholder="HH:MM" readonly /></div>
          <div class="frow"><label>שעת סיום</label><input id="a1tend" type="text" placeholder="HH:MM" readonly /></div>
        </div>

        <div class="sec-title">בעל הנכס</div>
        <div class="frow"><label>שם בעל הנכס</label><input id="a1oname" type="text" placeholder="שם מלא..." oninput="render1()" /></div>
        <div class="frow">
          <label>מספר מזהה</label>
          <div class="id-wrap">
            <select id="a1oidtype" onchange="render1()">
              <option value="ת.ז.">ת.ז.</option>
              <option value="ח.פ.">ח.פ.</option>
              <option value="ע.מ.">ע.מ.</option>
            </select>
            <input id="a1oid" type="text" placeholder="מספר..." oninput="render1()" />
          </div>
        </div>

        <div class="sec-title">המזמין</div>
        <div class="frow"><label>שם המזמין</label><input id="a1cname" type="text" placeholder="שם מלא..." oninput="render1()" /></div>
        <div class="frow"><label>תעודת זהות</label><input id="a1cid" type="text" placeholder="מספר ת.ז. ..." oninput="render1()" /></div>

        <div class="sec-title">פרטי הנכס</div>
        <div class="frow">
          <label>סוג הנכס</label>
          <select id="a1ptype" onchange="render1()">
            <option value="">בחר...</option><option>דירה</option><option>בית פרטי</option>
            <option>פנטהאוז</option><option>דופלקס</option><option>וילה</option>
            <option>סטודיו</option><option>חדר</option><option>נכס מסחרי</option>
          </select>
        </div>
        <div class="frow"><label>כתובת הנכס</label><input id="a1addr" type="text" placeholder="רחוב, מספר, עיר..." oninput="render1()" /></div>

        <div class="sec-title">צוות ומטרה</div>
        <div class="frow"><label>מספר אנשי צוות (מקסימום)</label><input id="a1crew" type="number" placeholder="מספר אנשים..." min="1" max="50" oninput="render1()" /></div>
        <div class="frow">
          <label>מטרה</label>
          <select id="a1purp" onchange="togglePurp1()">
            <option value="">בחר...</option>
            <option>שיווק הנכס למכירה</option>
            <option>שיווק הנכס להשכרה</option>
            <option>תיעוד אדריכלי</option>
            <option>פרסום שיווקי</option>
            <option value="__other__">אחר (הכנס ידנית)</option>
          </select>
          <input id="a1purpcustom" type="text" placeholder="הכנס מטרה..." oninput="render1()" style="margin-top:8px; display:none;" />
        </div>

        <button class="btn-gen" onclick="downloadPDF()">📥 הורדת PDF</button>
      </div>

      <!-- PREVIEW -->
      <div class="preview-panel">
        <div class="preview-top">
          <h3>תצוגה מקדימה</h3>
          <button class="btn-pdf" onclick="downloadPDF()">📥 הורד PDF</button>
        </div>
        <div class="doc-scroll">
          <div id="doc-container"></div>
        </div>
      </div>
    </div>
  </section>

  <!-- SCRIPTS -->
  <script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
  <script src="https://cdn.jsdelivr.net/npm/flatpickr/dist/l10n/he.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>

  <script>
    "use strict";

    function g(id) { return document.getElementById(id); }
    function v(id) { const el = g(id); return el ? el.value.trim() : ''; }
    function fv(val, ph) {
      if (!val) return `&nbsp;<b class="dynamic-val" style="color:#bbb; border-bottom-color:#bbb;">${ph || '___________'}</b>&nbsp;`;
      return `&nbsp;<b class="dynamic-val">${val}</b>&nbsp;`;
    }
    function hebDate(str) {
      if (!str) return null;
      const [y, m, d] = str.split('-');
      const mn = ['','ינואר','פברואר','מרץ','אפריל','מאי','יוני','יולי','אוגוסט','ספטמבר','אוקטובר','נובמבר','דצמבר'];
      return `${+d} ב${mn[+m]} ${y}`;
    }

    document.addEventListener('DOMContentLoaded', () => {
      flatpickr('#a1date', { locale: 'he', dateFormat: 'Y-m-d', allowInput: false, onChange: render1 });
      flatpickr('#a1tstart', { enableTime: true, noCalendar: true, dateFormat: 'H:i', time_24hr: true, defaultHour: 9, defaultMinute: 0, onChange: render1 });
      flatpickr('#a1tend', { enableTime: true, noCalendar: true, dateFormat: 'H:i', time_24hr: true, defaultHour: 17, defaultMinute: 0, onChange: render1 });
      render1();
    });

    function togglePurp1() {
      const sel = v('a1purp');
      g('a1purpcustom').style.display = (sel === '__other__') ? 'block' : 'none';
      render1();
    }
    function getPurp1() {
      const s = v('a1purp');
      return s === '__other__' ? v('a1purpcustom') : s;
    }

    function render1() {
      const hdate = hebDate(v('a1date')), ts = v('a1tstart'), te = v('a1tend');
      const oname = v('a1oname'), oidtype = v('a1oidtype') || 'ת.ז.', oid = v('a1oid');
      const cname = v('a1cname'), cid = v('a1cid'), ptype = v('a1ptype'), addr = v('a1addr');
      const purp = getPurp1(), crew = v('a1crew');

      g('doc-container').innerHTML = `
<!-- Header -->
<div style="position:relative; margin-bottom:12px; font-size:11pt; border:none;">
  <span style="float:right; white-space:nowrap;">לכבוד ${fv(cname,'המזמין')}</span>
  <span style="float:left; white-space:nowrap;">תאריך ${fv(hdate)}</span>
  <div style="clear:both;"></div>
</div>
<div style="margin-bottom:12px; font-size:11pt; white-space:nowrap;">המזמין – סוג בית ${fv(ptype,'_____')} בכתובת ${fv(addr,'_____')}</div>

<div class="doc-title">הסכם שימוש בלוקיישן "${fv(ptype,'סוג בית')} בכתובת ${fv(addr,'_____')}"</div>

<!-- Intro -->
<div style="margin-bottom:6px;">
<strong>בין</strong> בעל הנכס ${fv(oname,'_____')} ${oidtype} ${fv(oid,'_____')} – להלן "חברת ההפקה" או "הלקוח"
</div>
<div style="margin-bottom:10px;">
<strong>לבין</strong> המזמין ${fv(cname,'_____')} ת.ז ${fv(cid,'_____')}, סוג בית ${fv(ptype,'_____')} בכתובת ${fv(addr,'_____')} - להלן "הלוקיישן".
</div>

<div style="margin-bottom:10px;">
הח"מ מצהיר/ה שהיא מטעם סוג בית ${fv(ptype,'_____')} בכתובת ${fv(addr,'_____')}, אשר מנוהל ע"י בעל הנכס, וכי חתימתה מחייבת את שותפיו וכן את הנכס.
</div>

<div style="margin-bottom:6px;">
חברת ההפקה ו/או "הלקוח" שוכרת את הנכס סוג בית ${fv(ptype,'_____')} בכתובת ${fv(addr,'_____')} בתאריך ${fv(hdate)}
</div>
<div style="margin-bottom:6px;">
בין השעות ${fv(ts,'__:__')} - ${fv(te,'__:__')}.
</div>
<div style="margin-bottom:10px;">
בגין כל שעה נוספת יתבצע תשלום כפי שסוכם עם איתי מ-<span style="letter-spacing:1px">LOCK AND ACTION</span>.
</div>

<div style="margin-bottom:10px;"><strong>מטרת הצילומים</strong> ${fv(purp,'_____')}</div>
<div style="margin-bottom:10px;">צוות ההפקה – עד ${fv(crew,'X')} אנשים. על כל איש צוות נוסף יתבצע תשלום נוסף כפי שסוכם עם איתי מ-<span style="letter-spacing:1px">LOCK AND ACTION</span>.</div>

<!-- Terms -->
<div style="margin-bottom:6px;">מוסכם בזאת שלצורך הצילומים הבית והחצר יעמוד לרשות הלקוח.</div>
<div style="margin-bottom:6px;">הנכס יימסר לידי הלקוח כאשר הינו נקי.</div>
<div style="margin-bottom:6px;">חברת ההפקה מתחייבת להחזיר את המצב לקדמותו בגמר יום הצילום.</div>
<div style="margin-bottom:6px;">וכן חברת ההפקה מתחייבת לשאת באחריות מלאה לכל נזק במידה ויגרם למקום בעקבות ובמהלך יום הצילום והחזרות.</div>

<div style="margin-bottom:6px; color:red !important;">
הלקוח יבטח סיכוניו בקשר עם יום הצילומים, ביטוח לעובדים ולציוד לרבות ביטוח צד ג. הלקוח אחראי לביטוח הנכס או תכולתו ביום הצילום בגין נזקים שיעשו למושכר ביום הצילומים, שריפה וכו. המשכיר אינו אחראי לרכוש המפיק עובדיו ואורחיו ואינו נושא באחריות על כל נזק או פגיעה שעלולים להגרם למפיק, עובדיו או אורחיו במהלך שהותם במקום.
</div>

<div style="margin-bottom:6px;">את התמורה בגין יום הצילום יקבל בעל הנכס מאיתי ראובני "<span style="letter-spacing:1px">LOCK AND ACTION</span>" אשר הינה קשורה עימו בחוזה תמורה.</div>
<div style="margin-bottom:10px;">המשכיר יספק נציג צמוד מטעם הבית שילווה את הלקוח לאורך הצילומים.</div>

<ul class="ag-list">
  <li>יתאפשר להכניס לבית ציוד צילום, תאורה, הפקה וארט.</li>
  <li>יתאפשר לפתוח ארוחת בוקר וצהרים בחצר הבית או בפינת האוכל לצוות ההפקה.</li>
  <li>יתאפשר להשתמש בחדרים למטרת איפור והלבשה.</li>
  <li>יתאפשר להזיז חפצים שונים בבית למטרת הצילום ולהחזירם למקומם.</li>
  <li>יתאפשר להשתמש בחשמל של הבית למטרת הצילומים.</li>
</ul>

<div style="margin-bottom:6px;">חומר הגלם, אופן השימוש בו ושיקולי העריכה הם של חברת ההפקה בלבד.</div>
<div style="margin-bottom:16px;">חברת ההפקה שומרת לעצמה את הזכות לביטול הצילומים.</div>

<!-- Signatures -->
<div style="margin-bottom:10px; font-weight:700;">אנו הח"מ מאשרים את פרטי ההסכם</div>

<div style="margin-top:30px; display:block; position:relative; width:100%; height:80px; page-break-inside:avoid;">
  <div style="display:inline-block; width:45%; vertical-align:top; text-align:center; float:right;">
    <div style="border-top:1px solid #333; padding-top:8px; font-size:11pt; color:#555;">
      בעל הנכס ${oidtype} <strong>${fv(oid,'_____')}</strong><br/>${fv(oname,'שם בעל הנכס')}
    </div>
  </div>
  <div style="display:inline-block; width:45%; vertical-align:top; text-align:center; float:left;">
    <div style="border-top:1px solid #333; padding-top:8px; font-size:11pt; color:#555;">
      המזמין ת.ז <strong>${fv(cid,'_____')}</strong><br/>${fv(cname,'שם המזמין')}
    </div>
  </div>
  <div style="clear:both;"></div>
</div>
`.replace(/\\n\\s*/g, ' ');
    }

    function downloadPDF() {
      const element = document.getElementById('doc-container');
      const cname = v('a1cname') || 'הסכם';
      
      // Temporarily remove shadow for clean print
      const prevShadow = element.style.boxShadow;
      element.style.boxShadow = 'none';

      // Centered Export Logic!
      // Setting precision bounds and using a clean standardized padding.
      const opt = {
          margin: [15, 10, 15, 10], // top right bottom left
          filename: \`הסכם_בעל_נכס_\${cname}.pdf\`,
          image: { type: 'jpeg', quality: 1 },
          html2canvas: { 
              scale: 3, 
              useCORS: true, 
              letterRendering: true,
              scrollY: 0,
              windowWidth: 800
          },
          jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
      };

      html2pdf().set(opt).from(element).save().then(() => {
          element.style.boxShadow = prevShadow;
      });
    }
  </script>
</body>
</html>
"""

# Write index.html OVERWRITE fully to make it purely the hub page
with open(r"c:\Users\P0039428\OneDrive - Ness Israel\Desktop\איתי הסכמים וקוד\codes\index.html", "w", encoding="utf-8") as f:
    f.write(INDEX_CODE)

# Write agreement1.html as standalone component
with open(r"c:\Users\P0039428\OneDrive - Ness Israel\Desktop\איתי הסכמים וקוד\codes\agreement1.html", "w", encoding="utf-8") as f:
    f.write(AG1_CODE)

print("SUCCESS")
