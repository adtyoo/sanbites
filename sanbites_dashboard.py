import streamlit as st

st.set_page_config(
    page_title="Sanbites | Sandwich",
    page_icon="🥪",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def html(s: str) -> str:
    """Hapus indentasi & baris kosong agar Markdown tidak merusak HTML."""
    return "\n".join(line.strip() for line in s.strip().splitlines() if line.strip())


# =====================================================================
# CSS
# =====================================================================
st.markdown(html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,800;1,9..144,700&display=swap');

:root {
  --cream:#fff8ec; --paper:#fffdf8; --ink:#231f1a; --muted:#756d60;
  --tomato:#e8612c; --tomato-d:#c94b1b; --mustard:#f4b942;
  --green:#254233; --green-m:#35604a; --green-soft:#edf4ec;
  --line:#ebe0cc; --ease:cubic-bezier(.22,1,.36,1);
  --shadow:0 18px 44px #3a2a1514;
}

/* ---------- Dasar ---------- */
html, body, .stApp,
[data-testid="stAppViewContainer"], [data-testid="stMain"], section.main, .main { scroll-behavior:smooth !important; }
.stApp {
  color:var(--ink); font-family:'DM Sans',sans-serif;
  background:
    radial-gradient(900px 500px at 8% -5%, #ffe9c7 0, transparent 60%),
    radial-gradient(800px 500px at 100% 35%, #e6f1e3 0, transparent 60%),
    var(--cream);
}
.block-container { max-width:1180px; padding-top:6.2rem; padding-bottom:3rem; }
header, footer { visibility:hidden; }
[data-testid="stToolbar"] { display:none; }
.stApp a { transition:all .35s var(--ease); }
.serif { font-family:'Fraunces',serif; }

/* ---------- Animasi ---------- */
@keyframes fadeUp   { from {opacity:0; transform:translateY(30px);} to {opacity:1; transform:none;} }
@keyframes fadeDown { from {opacity:0; transform:translate(-50%,-24px);} to {opacity:1; transform:translate(-50%,0);} }
@keyframes floaty   { 0%,100% {transform:translateY(0) rotate(var(--r,0deg));} 50% {transform:translateY(-16px) rotate(calc(var(--r,0deg) + 8deg));} }
@keyframes bob      { 0%,100% {transform:translateY(0) rotate(-6deg);} 50% {transform:translateY(-12px) rotate(-1deg);} }
@keyframes spin     { to {transform:rotate(360deg);} }
@keyframes marquee  { from {transform:translateX(0);} to {transform:translateX(-50%);} }
@keyframes pulse    { 0%,100% {box-shadow:0 0 0 0 #e8612c55;} 50% {box-shadow:0 0 0 12px #e8612c00;} }
@keyframes reveal   { from {opacity:0; transform:translateY(36px) scale(.98);} to {opacity:1; transform:none;} }
@supports (animation-timeline: view()) {
  .reveal { animation:reveal linear both; animation-timeline:view(); animation-range:entry 0% entry 42%; }
}

/* ---------- Navbar ---------- */
.navbar {
  position:fixed; top:14px; left:50%; transform:translateX(-50%);
  width:min(1180px, calc(100% - 32px)); z-index:9999;
  display:flex; align-items:center; justify-content:space-between; gap:20px;
  padding:11px 12px 11px 26px;
  background:rgba(255,253,248,.8); backdrop-filter:blur(18px) saturate(1.4); -webkit-backdrop-filter:blur(18px) saturate(1.4);
  border:1px solid var(--line); border-radius:999px; box-shadow:0 12px 34px #392b1714;
  animation:fadeDown .8s var(--ease) both;
}
.brand { font-family:'Fraunces',serif; font-size:24px; font-weight:800; letter-spacing:-1px; color:var(--green); }
.brand span { color:var(--tomato); }
.navlinks { display:flex; align-items:center; gap:2px; }
.navlinks a.link { text-decoration:none; color:#4f483e; font-weight:700; font-size:14px; padding:10px 15px; border-radius:999px; }
.navlinks a.link:hover { background:#fbe9d3; color:var(--tomato-d); transform:translateY(-1px); }
.nav-cta {
  text-decoration:none; background:var(--tomato); color:#fff !important; font-weight:800; font-size:14px;
  padding:12px 24px; border-radius:999px; margin-left:8px; box-shadow:0 10px 22px #e8612c40;
}
.nav-cta:hover { background:var(--tomato-d); transform:translateY(-2px); }

/* ---------- Section ---------- */
.section { scroll-margin-top:110px; padding:84px 0 6px; }
.section-head { text-align:center; margin-bottom:42px; }
.section-kicker {
  display:inline-block; color:var(--tomato-d); background:#fdeadb; padding:6px 14px; border-radius:999px;
  text-transform:uppercase; letter-spacing:2px; font-size:11px; font-weight:800; margin-bottom:14px;
}
.section-title { font-family:'Fraunces',serif; font-weight:800; font-size:clamp(30px,4.4vw,46px); line-height:1.1; margin:0 0 12px; color:var(--ink); letter-spacing:-1px; }
.section-title em { color:var(--tomato); font-style:italic; }
.section-desc { color:var(--muted); margin:0 auto; max-width:520px; line-height:1.75; }

/* ---------- Hero ---------- */
.hero-wrap { scroll-margin-top:110px; position:relative; margin-bottom:34px; }
.hero {
  position:relative; overflow:hidden; border-radius:40px; min-height:580px;
  padding:70px 60px 80px; display:grid; grid-template-columns:1.05fr .95fr; align-items:center; gap:20px;
  background:
    radial-gradient(circle at 88% 15%, #ffdfae 0, transparent 42%),
    radial-gradient(circle at 5% 100%, #d9ecd5 0, transparent 40%),
    linear-gradient(135deg,#fffdf8 0%,#fff6e6 100%);
  border:1px solid var(--line); box-shadow:var(--shadow);
}
.hero::before {
  content:""; position:absolute; width:520px; height:520px; right:-140px; top:-160px; border-radius:50%;
  border:2px dashed #f0cda0; animation:spin 60s linear infinite; opacity:.7;
}
.hero-text { position:relative; z-index:2; }
.hero-text > * { animation:fadeUp .9s var(--ease) both; }
.eyebrow {
  display:inline-flex; align-items:center; gap:8px; color:var(--green); font-size:12px; font-weight:800;
  letter-spacing:2px; text-transform:uppercase; background:#fff; border:1px solid var(--line);
  padding:8px 16px; border-radius:999px; animation-delay:.1s !important;
}
.eyebrow i { width:8px; height:8px; border-radius:50%; background:#3cb06a; display:inline-block; animation:pulse 2s infinite; }
.hero h1 {
  font-family:'Fraunces',serif; font-weight:800; font-size:clamp(42px,5.8vw,76px); line-height:1.02; letter-spacing:-2px;
  margin:22px 0 20px; color:var(--ink); animation-delay:.22s !important;
}
.hero h1 em { color:var(--tomato); font-style:italic; position:relative; white-space:nowrap; }
.hero h1 em::after {
  content:""; position:absolute; left:0; right:0; bottom:4px; height:12px; z-index:-1;
  background:var(--mustard); opacity:.55; border-radius:6px; transform:rotate(-1deg);
}
.hero p { color:var(--muted); font-size:17px; max-width:480px; line-height:1.8; margin:0 0 30px; animation-delay:.34s !important; }
.btn-row { display:flex; flex-wrap:wrap; gap:12px; animation-delay:.46s !important; }
.btn {
  display:inline-block; text-decoration:none; font-weight:800; font-size:15px;
  padding:16px 30px; border-radius:999px; border:2px solid var(--green);
}
.btn.primary { background:var(--green); color:#fff !important; box-shadow:0 14px 26px #25423344; }
.btn.primary:hover { background:var(--green-m); transform:translateY(-3px); box-shadow:0 20px 34px #25423355; }
.btn.ghost { background:rgba(255,255,255,.75); color:var(--green) !important; }
.btn.ghost:hover { background:var(--green); color:#fff !important; transform:translateY(-3px); }
.btn.hot { background:var(--tomato); border-color:var(--tomato); color:#fff !important; box-shadow:0 14px 26px #e8612c44; }
.btn.hot:hover { background:var(--tomato-d); border-color:var(--tomato-d); transform:translateY(-3px); }
.hero-stats { display:flex; gap:30px; margin-top:34px; animation-delay:.6s !important; }
.hero-stats div b { display:block; font-family:'Fraunces',serif; font-size:28px; color:var(--green); line-height:1; }
.hero-stats div span { font-size:12px; color:var(--muted); font-weight:600; }

.plate-wrap { position:relative; z-index:2; display:flex; justify-content:center; align-items:center; animation:fadeUp 1.1s var(--ease) .3s both; }
.plate {
  width:min(410px,78vw); aspect-ratio:1; border-radius:50%; display:flex; align-items:center; justify-content:center;
  background:radial-gradient(circle at 35% 28%, #ffffff 0%, #f3ecdf 100%);
  box-shadow:0 36px 70px #392b1730, inset 0 0 0 14px #fff, inset 0 0 0 16px #eadfcb;
  transition:transform .6s var(--ease);
}
.plate:hover { transform:scale(1.04) rotate(3deg); }
.plate-emoji { font-size:clamp(125px,17vw,200px); filter:drop-shadow(0 22px 16px #17251c45); animation:bob 6s ease-in-out infinite; }
.float { position:absolute; font-size:clamp(34px,5vw,56px); filter:drop-shadow(0 8px 8px #17251c30); animation:floaty 5s ease-in-out infinite; }
.f1 { top:0;  left:6%;  --r:-12deg; }
.f2 { top:8%; right:2%; --r:10deg; animation-delay:-1.2s; }
.f3 { bottom:6%; left:2%; --r:8deg; animation-delay:-2.4s; }
.f4 { bottom:0; right:10%; --r:-6deg; animation-delay:-3.4s; }
.badge {
  position:absolute; top:-6px; right:-6px; z-index:4; width:108px; height:108px; border-radius:50%;
  background:var(--tomato); color:#fff; display:flex; flex-direction:column; align-items:center; justify-content:center;
  text-align:center; font-weight:800; line-height:1.1; box-shadow:0 16px 30px #e8612c55; transform:rotate(12deg);
  border:4px solid #fff;
}
.badge small { font-size:10px; letter-spacing:1.5px; text-transform:uppercase; opacity:.9; }
.badge strong { font-family:'Fraunces',serif; font-size:24px; }
.badge::before { content:""; position:absolute; inset:-14px; border-radius:50%; border:2px dashed #e8612c80; animation:spin 14s linear infinite; }

.hero-social { position:absolute; left:50%; bottom:-24px; transform:translateX(-50%); display:flex; gap:12px; z-index:5; animation:fadeUp 1s var(--ease) .8s both; }
.hero-social a {
  width:50px; height:50px; border-radius:50%; background:var(--green); color:#fff !important;
  display:flex; align-items:center; justify-content:center; text-decoration:none; font-size:20px;
  box-shadow:0 12px 24px #25423345; border:3px solid var(--cream);
}
.hero-social a:hover { transform:translateY(-6px) scale(1.1); background:var(--tomato); }

/* ---------- Marquee ---------- */
.marquee { overflow:hidden; margin:56px -2px 0; background:var(--green); border-radius:20px; padding:16px 0; transform:rotate(-1deg); box-shadow:0 16px 32px #25423328; }
.marquee-track { display:flex; width:max-content; animation:marquee 28s linear infinite; }
.marquee-track span { color:#fff4de; font-weight:800; font-size:15px; letter-spacing:1.5px; text-transform:uppercase; padding:0 26px; white-space:nowrap; }
.marquee-track span b { color:var(--mustard); margin-left:52px; }

/* ---------- Keunggulan ---------- */
.features { display:grid; grid-template-columns:repeat(4,1fr); gap:18px; }
.feature {
  position:relative; overflow:hidden; background:var(--paper); border:1px solid var(--line); border-radius:24px; padding:28px 22px;
  transition:transform .45s var(--ease), box-shadow .45s var(--ease), background .45s var(--ease), border-color .45s;
}
.feature::after {
  content:""; position:absolute; width:120px; height:120px; border-radius:50%; right:-40px; bottom:-40px;
  background:var(--green-soft); transition:transform .6s var(--ease); z-index:0;
}
.feature:hover { transform:translateY(-8px); box-shadow:0 24px 44px #25423318; border-color:#cfe0cf; }
.feature:hover::after { transform:scale(2.6); }
.feature > * { position:relative; z-index:1; }
.feature .icon {
  width:56px; height:56px; margin:0 0 16px; border-radius:18px; background:#fff3e2; border:1px solid #f3dcc0;
  display:flex; align-items:center; justify-content:center; font-size:27px; transition:transform .45s var(--ease);
}
.feature:hover .icon { transform:rotate(-10deg) scale(1.12); }
.feature h4 { margin:0 0 6px; font-size:16px; color:var(--ink); }
.feature p { margin:0; color:var(--muted); font-size:13px; line-height:1.65; }

/* ---------- Produk ---------- */
.products { display:grid; grid-template-columns:repeat(2,1fr); gap:30px; }
.product-card {
  position:relative; background:#fff; border:1px solid var(--line); border-radius:30px; overflow:hidden; box-shadow:0 12px 32px #392b170d;
  transition:transform .5s var(--ease), box-shadow .5s var(--ease);
}
.product-card:hover { transform:translateY(-10px); box-shadow:0 30px 56px #392b1722; }
.product-art {
  position:relative; height:230px; display:flex; align-items:center; justify-content:center; font-size:120px; overflow:hidden;
  background:radial-gradient(circle at 70% 20%, #fff2dc 0, transparent 50%), linear-gradient(135deg,#f9e3c6,#f0c79c);
}
.product-art::before { content:""; position:absolute; width:260px; height:260px; border-radius:50%; background:#ffffff55; }
.product-art span { position:relative; transition:transform .6s var(--ease); display:inline-block; filter:drop-shadow(0 16px 12px #3a2a1535); }
.product-card:hover .product-art span { transform:scale(1.18) rotate(-8deg); }
.tag-corner {
  position:absolute; top:18px; left:18px; z-index:2; background:var(--green); color:#fff; font-size:11px; font-weight:800;
  letter-spacing:1px; padding:7px 14px; border-radius:999px; text-transform:uppercase;
}
.tag-corner.hot { background:var(--tomato); }
.product-info { padding:26px 28px 30px; }
.product-info h3 { font-family:'Fraunces',serif; margin:12px 0 8px; font-size:25px; color:var(--ink); letter-spacing:-.5px; }
.product-info p { color:var(--muted); font-size:14px; min-height:46px; line-height:1.7; margin:0; }
.product-bottom { display:flex; align-items:flex-end; justify-content:space-between; gap:12px; margin-top:20px; padding-top:18px; border-top:1px dashed var(--line); }
.price { font-family:'Fraunces',serif; font-size:30px; font-weight:800; color:var(--green); line-height:1; }
.price small { font-family:'DM Sans',sans-serif; font-size:12px; font-weight:600; color:var(--muted); }
.order-link {
  text-decoration:none; background:var(--tomato); color:#fff !important; font-weight:800; font-size:13px;
  padding:12px 20px; border-radius:999px; box-shadow:0 10px 20px #e8612c3a;
}
.order-link:hover { background:var(--tomato-d); transform:translateY(-2px); }
.pill { display:inline-block; background:#fff0e3; color:var(--tomato-d); border-radius:999px; padding:6px 12px; font-size:11px; font-weight:800; letter-spacing:.5px; }

/* ---------- Cara Pesan ---------- */
.steps { display:grid; grid-template-columns:repeat(3,1fr); gap:24px; position:relative; }
.step {
  position:relative; background:var(--green); color:#fff; border-radius:28px; padding:34px 28px; overflow:hidden;
  transition:transform .5s var(--ease);
}
.step:nth-child(2) { background:var(--green-m); }
.step:nth-child(3) { background:var(--tomato); }
.step:hover { transform:translateY(-8px) rotate(-.6deg); }
.step .num { font-family:'Fraunces',serif; font-weight:800; font-size:92px; line-height:.8; position:absolute; right:18px; top:18px; opacity:.16; }
.step .emoji { font-size:40px; display:block; margin-bottom:18px; }
.step h4 { margin:0 0 8px; font-size:20px; font-family:'Fraunces',serif; }
.step p { margin:0; font-size:14px; line-height:1.7; opacity:.9; }

/* ---------- Momen ---------- */
.moments { display:grid; grid-template-columns:repeat(3,1fr); gap:26px; }
.moment { transition:transform .5s var(--ease); }
.moment:hover { transform:translateY(-8px); }
.moment-art {
  height:200px; border-radius:28px; display:flex; align-items:center; justify-content:center; font-size:88px;
  box-shadow:0 16px 34px #392b1716; overflow:hidden;
}
.moment-art span { transition:transform .6s var(--ease); display:inline-block; }
.moment:hover .moment-art span { transform:scale(1.18) rotate(6deg); }
.moment h4 { font-family:'Fraunces',serif; margin:20px 0 6px; font-size:21px; color:var(--ink); }
.moment p { margin:0 0 12px; color:var(--muted); font-size:14px; line-height:1.7; }

/* ---------- FAQ ---------- */
.faq { max-width:760px; margin:0 auto; display:grid; gap:12px; }
.faq details { background:var(--paper); border:1px solid var(--line); border-radius:20px; padding:4px 24px; transition:box-shadow .4s var(--ease), border-color .4s; }
.faq details[open] { box-shadow:var(--shadow); border-color:#f0cda0; }
.faq summary { cursor:pointer; list-style:none; font-weight:700; font-size:15px; padding:18px 0; display:flex; justify-content:space-between; align-items:center; color:var(--ink); }
.faq summary::-webkit-details-marker { display:none; }
.faq summary::after { content:"+"; font-size:24px; color:var(--tomato); transition:transform .4s var(--ease); }
.faq details[open] summary::after { transform:rotate(45deg); }
.faq details p { margin:0 0 18px; color:var(--muted); font-size:14px; line-height:1.75; }

/* ---------- CTA ---------- */
.cta {
  position:relative; overflow:hidden; display:grid; grid-template-columns:1.05fr .95fr; align-items:center; gap:40px;
  background:linear-gradient(135deg,#254233 0%,#35604a 100%); color:#fff; border-radius:40px; padding:60px;
  box-shadow:0 30px 60px #25423340;
}
.cta::before { content:""; position:absolute; width:420px; height:420px; border-radius:50%; background:#ffffff0d; left:-120px; bottom:-200px; }
.cta > * { position:relative; }
.cta .section-kicker { background:#ffffff1f; color:#ffe2b8; }
.cta h2 { font-family:'Fraunces',serif; font-weight:800; font-size:clamp(30px,4.2vw,46px); line-height:1.1; letter-spacing:-1px; margin:0 0 14px; color:#fff; }
.cta h2 em { color:var(--mustard); font-style:italic; }
.cta p { color:#d6e4d6; line-height:1.8; margin:0 0 26px; }
.cta .btn.ghost { background:transparent; color:#fff !important; border-color:#ffffff80; }
.cta .btn.ghost:hover { background:#fff; color:var(--green) !important; }
.cta-art {
  height:320px; border-radius:32px; display:flex; align-items:center; justify-content:center; font-size:150px;
  background:linear-gradient(135deg,#ffe3bd,#f0a96e); box-shadow:0 28px 54px #00000035; overflow:hidden;
  transition:transform .6s var(--ease);
}
.cta-art:hover { transform:scale(1.03) rotate(-1.5deg); }
.cta-art span { animation:bob 6s ease-in-out infinite; display:inline-block; filter:drop-shadow(0 20px 14px #3a2a1550); }

/* ---------- Footer ---------- */
.footer { margin-top:70px; text-align:center; padding:38px 20px 10px; color:var(--muted); font-size:13px; line-height:1.9; border-top:1px solid var(--line); }
.footer b { font-family:'Fraunces',serif; color:var(--green); font-size:24px; letter-spacing:-1px; }
.footer b span { color:var(--tomato); }

/* ---------- Responsif ---------- */
@media (max-width:900px) {
  .features { grid-template-columns:repeat(2,1fr); }
  .moments, .steps { grid-template-columns:1fr; }
  .cta { grid-template-columns:1fr; padding:40px 28px; }
  .hero { padding:50px 34px 70px; }
}
@media (max-width:760px) {
  .block-container { padding-top:5.6rem; }
  .navbar { padding:10px 10px 10px 18px; }
  .navlinks a.link { padding:8px 9px; font-size:13px; }
  .nav-cta { display:none; }
  .hero { grid-template-columns:1fr; padding:40px 24px 64px; }
  .plate-wrap { order:-1; }
  .badge { width:88px; height:88px; right:0; }
  .badge strong { font-size:19px; }
  .products { grid-template-columns:1fr; }
  .hero-stats { gap:20px; }
}
@media (max-width:520px) {
  .brand { font-size:20px; }
  .navlinks a.link:nth-child(2) { display:none; }
  .features { grid-template-columns:1fr; }
}

@media (prefers-reduced-motion: reduce) {
  * { animation:none !important; transition:none !important; scroll-behavior:auto !important; }
}
</style>
"""), unsafe_allow_html=True)


# =====================================================================
# KONTEN
# =====================================================================
st.markdown(html("""
<div class="navbar">
  <div class="brand">SAN<span>BITES</span> 🥪</div>
  <div class="navlinks">
    <a class="link" href="#beranda" target="_self">Beranda</a>
    <a class="link" href="#keunggulan" target="_self">Keunggulan</a>
    <a class="link" href="#produk" target="_self">Menu</a>
    <a class="link" href="#cara-pesan" target="_self">Cara Pesan</a>
    <a class="nav-cta" href="#media-sosial" target="_self">Pesan Sekarang</a>
  </div>
</div>

<div id="beranda" class="hero-wrap">
  <section class="hero">
    <div class="hero-text">
      <div class="eyebrow"><i></i> Fresh • Simple • Delicious</div>
      <h1>Sandwich enak,<br><em>teman</em> setiap hari.</h1>
      <p>Roti lembut dengan isian pilihan yang gurih. Dibuat untuk menemani aktivitasmu, kapan pun perut mulai keroncongan.</p>
      <div class="btn-row">
        <a class="btn hot" href="#produk" target="_self">Lihat Menu</a>
        <a class="btn ghost" href="#media-sosial" target="_self">Ikuti Kami</a>
      </div>
      <div class="hero-stats">
        <div><b>Rp10rb</b><span>Harga mulai</span></div>
        <div><b>2 Menu</b><span>Pilihan isian</span></div>
        <div><b>Fresh</b><span>Disiapkan segar</span></div>
      </div>
    </div>
    <div class="plate-wrap">
      <div class="badge"><small>mulai</small><strong>10K</strong><small>per porsi</small></div>
      <div class="plate"><span class="plate-emoji">🥪</span></div>
      <span class="float f1">🍅</span>
      <span class="float f2">🥬</span>
      <span class="float f3">🥚</span>
      <span class="float f4">🍋</span>
    </div>
  </section>
  <div class="hero-social">
    <a href="https://www.instagram.com/" target="_blank" title="Instagram">📸</a>
    <a href="https://www.tiktok.com/" target="_blank" title="TikTok">🎵</a>
  </div>
</div>

<div class="marquee">
  <div class="marquee-track">
    <span>Roti Lembut <b>✦</b></span><span>Isian Gurih <b>✦</b></span><span>Harga Terjangkau <b>✦</b></span><span>Praktis Dibawa <b>✦</b></span><span>Segar &amp; Higienis <b>✦</b></span><span>Cepat Disiapkan <b>✦</b></span>
    <span>Roti Lembut <b>✦</b></span><span>Isian Gurih <b>✦</b></span><span>Harga Terjangkau <b>✦</b></span><span>Praktis Dibawa <b>✦</b></span><span>Segar &amp; Higienis <b>✦</b></span><span>Cepat Disiapkan <b>✦</b></span>
  </div>
</div>

<section id="keunggulan" class="section">
  <div class="section-head reveal">
    <div class="section-kicker">Kenapa Sanbites?</div>
    <div class="section-title">Dibuat dengan <em>sepenuh hati</em></div>
    <div class="section-desc">Setiap sandwich disiapkan agar nikmat, praktis, dan ramah di kantong.</div>
  </div>
  <div class="features">
    <div class="feature reveal"><div class="icon">🍞</div><h4>Roti Lembut</h4><p>Tekstur empuk di setiap gigitan.</p></div>
    <div class="feature reveal"><div class="icon">🥚</div><h4>Isian Gurih</h4><p>Telur dan daging dengan rasa yang pas.</p></div>
    <div class="feature reveal"><div class="icon">💸</div><h4>Harga Terjangkau</h4><p>Mulai dari Rp10.000 per porsi.</p></div>
    <div class="feature reveal"><div class="icon">🎒</div><h4>Praktis Dibawa</h4><p>Mudah dimakan di mana saja.</p></div>
    <div class="feature reveal"><div class="icon">🌿</div><h4>Segar &amp; Higienis</h4><p>Disiapkan dengan bahan pilihan.</p></div>
    <div class="feature reveal"><div class="icon">⚡</div><h4>Cepat Disiapkan</h4><p>Lapar datang, sandwich siap.</p></div>
    <div class="feature reveal"><div class="icon">😋</div><h4>Cocok Semua Usia</h4><p>Disukai anak-anak sampai dewasa.</p></div>
    <div class="feature reveal"><div class="icon">💬</div><h4>Pesan Mudah</h4><p>Hubungi kami lewat media sosial.</p></div>
  </div>
</section>

<section id="produk" class="section">
  <div class="section-head reveal">
    <div class="section-kicker">Pilihan favoritmu</div>
    <div class="section-title">Menu <em>Sanbites</em></div>
    <div class="section-desc">Pilih sandwich favoritmu, rasakan nikmatnya di setiap gigitan.</div>
  </div>
  <div class="products">
    <div class="product-card reveal">
      <span class="tag-corner">Favorit</span>
      <div class="product-art"><span>🥪</span></div>
      <div class="product-info">
        <span class="pill">SIMPLE &amp; DELICIOUS</span>
        <h3>Sandwich Telur</h3>
        <p>Roti lembut dengan isian telur yang gurih dan nikmat. Pilihan pas untuk camilan praktis.</p>
        <div class="product-bottom">
          <div class="price">Rp10.000 <small>/ porsi</small></div>
          <a class="order-link" href="https://www.instagram.com/" target="_blank">Pesan ↗</a>
        </div>
      </div>
    </div>
    <div class="product-card reveal">
      <span class="tag-corner hot">Paling Kenyang</span>
      <div class="product-art" style="background:radial-gradient(circle at 70% 20%, #ffeccf 0, transparent 50%), linear-gradient(135deg,#f6d9b8,#e5ae7c)"><span>🥪</span></div>
      <div class="product-info">
        <span class="pill">LEBIH MENGENYANGKAN</span>
        <h3>Sandwich Telur + Daging</h3>
        <p>Kombinasi telur dan daging yang gurih dalam roti lembut. Cocok untuk mengisi energimu.</p>
        <div class="product-bottom">
          <div class="price">Rp17.000 <small>/ porsi</small></div>
          <a class="order-link" href="https://www.instagram.com/" target="_blank">Pesan ↗</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="cara-pesan" class="section">
  <div class="section-head reveal">
    <div class="section-kicker">Gampang banget</div>
    <div class="section-title">Pesan dalam <em>3 langkah</em></div>
    <div class="section-desc">Tanpa ribet, sandwich favoritmu langsung meluncur.</div>
  </div>
  <div class="steps">
    <div class="step reveal"><span class="num">1</span><span class="emoji">👀</span><h4>Pilih menu</h4><p>Tentukan sandwich telur atau telur + daging sesuai seleramu.</p></div>
    <div class="step reveal"><span class="num">2</span><span class="emoji">💬</span><h4>Hubungi kami</h4><p>Kirim pesan lewat Instagram atau TikTok Sanbites.</p></div>
    <div class="step reveal"><span class="num">3</span><span class="emoji">😋</span><h4>Nikmati</h4><p>Sandwich disiapkan segar, tinggal santap kapan saja.</p></div>
  </div>
</section>

<section id="momen" class="section">
  <div class="section-head reveal">
    <div class="section-kicker">Kapan saja</div>
    <div class="section-title">Cocok untuk <em>setiap momen</em></div>
    <div class="section-desc">Dari pagi hingga sore, Sanbites siap menemani harimu.</div>
  </div>
  <div class="moments">
    <div class="moment reveal">
      <div class="moment-art" style="background:linear-gradient(135deg,#fde9c9,#f7cf9b)"><span>🌅</span></div>
      <h4>Teman Sarapan</h4>
      <p>Mulai hari dengan sandwich yang mengenyangkan dan praktis.</p>
      <span class="pill">PAGI HARI</span>
    </div>
    <div class="moment reveal">
      <div class="moment-art" style="background:linear-gradient(135deg,#dcebd9,#bcd8bb)"><span>🎒</span></div>
      <h4>Bekal Sekolah &amp; Kerja</h4>
      <p>Mudah dibawa dan dimakan kapan saja tanpa ribet.</p>
      <span class="pill">AKTIVITAS</span>
    </div>
    <div class="moment reveal">
      <div class="moment-art" style="background:linear-gradient(135deg,#f9dccb,#eeb593)"><span>☕</span></div>
      <h4>Camilan Santai</h4>
      <p>Pas dinikmati sambil bersantai bersama teman atau keluarga.</p>
      <span class="pill">SORE HARI</span>
    </div>
  </div>
</section>

<section id="faq" class="section">
  <div class="section-head reveal">
    <div class="section-kicker">Ada pertanyaan?</div>
    <div class="section-title">Pertanyaan <em>umum</em></div>
  </div>
  <div class="faq reveal">
    <details open><summary>Berapa harga sandwich Sanbites?</summary><p>Sandwich Telur Rp10.000 dan Sandwich Telur + Daging Rp17.000 per porsi.</p></details>
    <details><summary>Bagaimana cara memesan?</summary><p>Hubungi kami lewat Instagram atau TikTok Sanbites, sebutkan menu dan jumlah yang kamu inginkan.</p></details>
    <details><summary>Apakah cocok untuk bekal?</summary><p>Tentu. Sandwich kami praktis dibawa dan mudah dimakan di sekolah, kantor, atau di perjalanan.</p></details>
  </div>
</section>

<section id="media-sosial" class="section">
  <div class="cta reveal">
    <div>
      <div class="section-kicker">Tetap terhubung</div>
      <h2>Yuk, jadi bagian dari <em>Sanbites!</em></h2>
      <p>Ikuti akun media sosial kami untuk info menu, promo, dan kabar terbaru dari Sanbites.</p>
      <div class="btn-row" style="animation:none">
        <a class="btn hot" href="https://www.instagram.com/" target="_blank">Instagram ↗</a>
        <a class="btn ghost" href="https://www.tiktok.com/" target="_blank">TikTok ↗</a>
      </div>
    </div>
    <div class="cta-art"><span>🥪</span></div>
  </div>
</section>

<div class="footer">
  <b>SAN<span>BITES</span> 🥪</b><br>
  Fresh • Simple • Delicious<br>
  © 2026 Sanbites. Made with love and good taste.
</div>
"""), unsafe_allow_html=True)