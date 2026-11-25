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
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');

:root {
  --cream:#fffaf1; --ink:#29251f; --muted:#766f64;
  --orange:#e87936; --green:#314d3b; --green-soft:#eef5ee; --line:#e9e1d3;
  --ease:cubic-bezier(.22,1,.36,1);
}

/* ---------- Smooth scroll (Streamlit scroll di dalam container, bukan <html>) ---------- */
html, body, .stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
section.main, .main { scroll-behavior:smooth !important; }

.stApp { background:var(--cream); color:var(--ink); font-family:'DM Sans',sans-serif; }
.block-container { max-width:1180px; padding-top:6.2rem; padding-bottom:3rem; }
header, footer { visibility:hidden; }
[data-testid="stToolbar"] { display:none; }
.stApp a { transition:all .35s var(--ease); }

/* ---------- Animasi ---------- */
@keyframes fadeUp   { from {opacity:0; transform:translateY(28px);} to {opacity:1; transform:none;} }
@keyframes fadeDown { from {opacity:0; transform:translate(-50%,-24px);} to {opacity:1; transform:translate(-50%,0);} }
@keyframes floaty   { 0%,100% {transform:translateY(0) rotate(var(--r,0deg));} 50% {transform:translateY(-16px) rotate(calc(var(--r,0deg) + 6deg));} }
@keyframes bob      { 0%,100% {transform:translateY(0) rotate(-8deg);} 50% {transform:translateY(-10px) rotate(-3deg);} }
@keyframes reveal   { from {opacity:0; transform:translateY(34px);} to {opacity:1; transform:none;} }

/* Muncul halus saat di-scroll (browser yang belum mendukung tetap tampil normal) */
@supports (animation-timeline: view()) {
  .reveal { animation:reveal linear both; animation-timeline:view(); animation-range:entry 0% entry 40%; }
}

/* ---------- Navbar ---------- */
.navbar {
  position:fixed; top:14px; left:50%; transform:translateX(-50%);
  width:min(1180px, calc(100% - 32px)); z-index:9999;
  display:flex; align-items:center; justify-content:space-between; gap:20px;
  padding:12px 14px 12px 26px;
  background:rgba(255,250,241,.82); backdrop-filter:blur(16px); -webkit-backdrop-filter:blur(16px);
  border:1px solid var(--line); border-radius:999px; box-shadow:0 10px 30px #392b1712;
  animation:fadeDown .8s var(--ease) both;
}
.brand { font-size:23px; font-weight:800; letter-spacing:-1px; color:var(--green); }
.brand span { color:var(--orange); }
.navlinks { display:flex; align-items:center; gap:4px; }
.navlinks a.link {
  text-decoration:none; color:#514b42; font-weight:700; font-size:14px;
  padding:10px 16px; border-radius:999px;
}
.navlinks a.link:hover { background:#f5e6d4; color:#b95720; transform:translateY(-1px); }
.nav-cta {
  text-decoration:none; background:var(--green); color:#fff !important; font-weight:700; font-size:14px;
  padding:11px 22px; border-radius:999px; margin-left:8px; box-shadow:0 8px 18px #314d3b35;
}
.nav-cta:hover { background:#3d5f49; transform:translateY(-2px); box-shadow:0 12px 24px #314d3b45; }

/* ---------- Section umum ---------- */
.section { scroll-margin-top:110px; padding:78px 0 6px; }
.section-head { text-align:center; margin-bottom:38px; }
.section-kicker { color:var(--orange); text-transform:uppercase; letter-spacing:2px; font-size:11px; font-weight:800; margin-bottom:8px; }
.section-title { font-family:'Playfair Display',serif; font-size:clamp(28px,4vw,38px); margin:0 0 10px; color:var(--ink); }
.section-desc { color:var(--muted); margin:0 auto; max-width:520px; line-height:1.7; }

/* ---------- Hero ---------- */
.hero-wrap { scroll-margin-top:110px; position:relative; margin-bottom:34px; }
.hero {
  position:relative; overflow:hidden; border-radius:34px; min-height:540px;
  padding:64px 56px 70px; display:grid; grid-template-columns:1.05fr .95fr; align-items:center; gap:20px;
  background:
    radial-gradient(circle at 85% 20%, #f9e6cf 0, transparent 45%),
    linear-gradient(135deg,#f2f7f0 0%,#ffffff 55%,#f8efe2 100%);
  border:1px solid var(--line); box-shadow:0 24px 60px #392b1710;
}
.hero-text > * { animation:fadeUp .9s var(--ease) both; }
.eyebrow { color:var(--green); font-size:12px; font-weight:800; letter-spacing:2.5px; text-transform:uppercase; animation-delay:.10s !important; }
.hero h1 {
  font-family:'Playfair Display',serif; font-size:clamp(40px,5.4vw,68px); line-height:1.05;
  margin:16px 0 18px; color:var(--ink); animation-delay:.22s !important;
}
.hero h1 em { color:var(--orange); font-style:normal; }
.hero p { color:var(--muted); font-size:16px; max-width:470px; line-height:1.75; margin:0 0 28px; animation-delay:.34s !important; }
.btn-row { display:flex; flex-wrap:wrap; gap:12px; animation-delay:.46s !important; }
.btn {
  display:inline-block; text-decoration:none; font-weight:700; font-size:14px;
  padding:14px 28px; border-radius:999px; border:1.5px solid var(--green);
}
.btn.primary { background:var(--green); color:#fff !important; box-shadow:0 10px 22px #314d3b30; }
.btn.primary:hover { background:#3d5f49; transform:translateY(-3px); box-shadow:0 16px 30px #314d3b45; }
.btn.ghost { background:rgba(255,255,255,.7); color:var(--green) !important; }
.btn.ghost:hover { background:var(--green); color:#fff !important; transform:translateY(-3px); }
.price-tag {
  display:inline-block; margin-top:22px; background:#fff; border:1px solid var(--line);
  padding:9px 16px; border-radius:999px; font-weight:700; font-size:13px; color:var(--green);
  animation-delay:.58s !important;
}

.plate-wrap { position:relative; display:flex; justify-content:center; align-items:center; animation:fadeUp 1.1s var(--ease) .3s both; }
.plate {
  width:min(400px,78vw); aspect-ratio:1; border-radius:50%; display:flex; align-items:center; justify-content:center;
  background:radial-gradient(circle at 35% 30%, #ffffff 0%, #f1ece2 100%);
  box-shadow:0 30px 60px #392b1725, inset 0 0 0 14px #fff, inset 0 0 0 16px #ece4d6;
  transition:transform .6s var(--ease);
}
.plate:hover { transform:scale(1.04) rotate(3deg); }
.plate-emoji { font-size:clamp(120px,17vw,190px); filter:drop-shadow(0 18px 14px #17251c40); animation:bob 6s ease-in-out infinite; }
.float { position:absolute; font-size:clamp(34px,5vw,54px); filter:drop-shadow(0 8px 8px #17251c30); animation:floaty 5s ease-in-out infinite; }
.f1 { top:2%;  left:8%;  --r:-12deg; }
.f2 { top:8%;  right:4%; --r:10deg;  animation-delay:-1.2s; }
.f3 { bottom:6%; left:4%; --r:8deg;  animation-delay:-2.4s; }
.f4 { bottom:2%; right:10%; --r:-6deg; animation-delay:-3.4s; }

.hero-social {
  position:absolute; left:50%; bottom:-24px; transform:translateX(-50%);
  display:flex; gap:12px; z-index:5; animation:fadeUp 1s var(--ease) .8s both;
}
.hero-social a {
  width:48px; height:48px; border-radius:50%; background:var(--green); color:#fff !important;
  display:flex; align-items:center; justify-content:center; text-decoration:none; font-size:20px;
  box-shadow:0 10px 22px #314d3b40; border:3px solid var(--cream);
}
.hero-social a:hover { transform:translateY(-6px) scale(1.08); background:var(--orange); }

/* ---------- Kartu keunggulan ---------- */
.features { display:grid; grid-template-columns:repeat(4,1fr); gap:20px; }
.feature {
  background:var(--green-soft); border:1px solid #dfeadf; border-radius:22px; padding:28px 20px; text-align:center;
  transition:transform .45s var(--ease), box-shadow .45s var(--ease), background .45s var(--ease);
}
.feature:hover { transform:translateY(-8px); background:#fff; box-shadow:0 20px 40px #314d3b18; }
.feature .icon {
  width:58px; height:58px; margin:0 auto 14px; border-radius:50%; background:#fff; border:1.5px solid #cfe0d0;
  display:flex; align-items:center; justify-content:center; font-size:26px; transition:transform .45s var(--ease);
}
.feature:hover .icon { transform:rotate(-8deg) scale(1.12); }
.feature h4 { margin:0 0 6px; font-size:16px; color:var(--ink); }
.feature p { margin:0; color:var(--muted); font-size:13px; line-height:1.6; }

/* ---------- Produk ---------- */
.products { display:grid; grid-template-columns:repeat(2,1fr); gap:28px; }
.product-card {
  background:#fff; border:1px solid var(--line); border-radius:26px; overflow:hidden; box-shadow:0 10px 30px #392b170b;
  transition:transform .5s var(--ease), box-shadow .5s var(--ease);
}
.product-card:hover { transform:translateY(-10px); box-shadow:0 28px 50px #392b1720; }
.product-art {
  height:200px; display:flex; align-items:center; justify-content:center; font-size:110px; overflow:hidden;
  background:linear-gradient(135deg,#f8e7d2,#f3d4b5);
}
.product-art span { transition:transform .6s var(--ease); display:inline-block; }
.product-card:hover .product-art span { transform:scale(1.18) rotate(-8deg); }
.product-info { padding:24px 26px 28px; }
.product-info h3 { margin:12px 0 8px; font-size:21px; color:var(--ink); }
.product-info p { color:var(--muted); font-size:14px; min-height:44px; line-height:1.6; margin:0; }
.price { font-size:26px; font-weight:800; color:var(--green); margin-top:14px; }
.price small { font-size:12px; font-weight:600; color:var(--muted); }
.pill { display:inline-block; background:#fff0e3; color:#b95720; border-radius:999px; padding:6px 11px; font-size:11px; font-weight:800; }

/* ---------- Momen ---------- */
.moments { display:grid; grid-template-columns:repeat(3,1fr); gap:24px; }
.moment { transition:transform .5s var(--ease); }
.moment:hover { transform:translateY(-8px); }
.moment-art {
  height:190px; border-radius:24px; display:flex; align-items:center; justify-content:center; font-size:84px;
  box-shadow:0 14px 30px #392b1714; overflow:hidden;
}
.moment-art span { transition:transform .6s var(--ease); display:inline-block; }
.moment:hover .moment-art span { transform:scale(1.15) rotate(6deg); }
.moment h4 { margin:18px 0 6px; font-size:18px; color:var(--ink); }
.moment p { margin:0 0 12px; color:var(--muted); font-size:14px; line-height:1.65; }

/* ---------- Media sosial / CTA ---------- */
.cta {
  display:grid; grid-template-columns:1.05fr .95fr; align-items:center; gap:40px;
  background:var(--green-soft); border-radius:34px; padding:56px; border:1px solid #dfeadf;
}
.cta h2 { font-family:'Playfair Display',serif; font-size:clamp(28px,4vw,40px); line-height:1.15; margin:0 0 14px; color:var(--ink); }
.cta p { color:var(--muted); line-height:1.75; margin:0 0 24px; }
.cta-art {
  height:300px; border-radius:28px; display:flex; align-items:center; justify-content:center; font-size:140px;
  background:linear-gradient(135deg,#f8e2c8,#eab98a); box-shadow:0 24px 50px #392b1725; overflow:hidden;
  transition:transform .6s var(--ease);
}
.cta-art:hover { transform:scale(1.03) rotate(-1.5deg); }
.cta-art span { animation:bob 6s ease-in-out infinite; display:inline-block; }

/* ---------- Footer ---------- */
.footer {
  margin-top:70px; background:var(--green); color:#dfe8dc; text-align:center; border-radius:26px;
  padding:34px 20px; font-size:13px; line-height:1.8;
}
.footer b { color:#fff; font-size:18px; letter-spacing:-.5px; }
.footer b span { color:#f6bd87; }

/* ---------- Responsif ---------- */
@media (max-width:900px) {
  .features { grid-template-columns:repeat(2,1fr); }
  .moments { grid-template-columns:1fr; }
  .cta { grid-template-columns:1fr; padding:36px 26px; }
}
@media (max-width:760px) {
  .block-container { padding-top:5.6rem; }
  .navbar { padding:10px 12px 10px 18px; }
  .navlinks a.link { padding:8px 9px; font-size:13px; }
  .nav-cta { display:none; }
  .hero { grid-template-columns:1fr; padding:40px 26px 60px; text-align:left; }
  .plate-wrap { order:-1; }
  .products { grid-template-columns:1fr; }
}
@media (max-width:520px) {
  .brand { font-size:19px; }
  .navlinks a.link:nth-child(2) { display:none; }
}

/* Hormati pengguna yang mematikan animasi di perangkatnya */
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
    <a class="link" href="#produk" target="_self">Produk</a>
    <a class="link" href="#media-sosial" target="_self">Media Sosial</a>
    <a class="nav-cta" href="#produk" target="_self">Lihat Menu</a>
  </div>
</div>

<div id="beranda" class="hero-wrap">
  <section class="hero">
    <div class="hero-text">
      <div class="eyebrow">Fresh • Simple • Delicious</div>
      <h1>Sandwich enak,<br><em>teman</em> setiap hari.</h1>
      <p>Temukan sandwich lezat dengan isian pilihan. Dibuat untuk menemani aktivitasmu, kapan pun kamu lapar.</p>
      <div class="btn-row">
        <a class="btn primary" href="#produk" target="_self">Lihat Menu</a>
        <a class="btn ghost" href="#media-sosial" target="_self">Ikuti Kami</a>
      </div>
      <span class="price-tag">Mulai dari Rp10.000</span>
    </div>
    <div class="plate-wrap">
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

<section id="keunggulan" class="section">
  <div class="section-head reveal">
    <div class="section-kicker">Kenapa Sanbites?</div>
    <div class="section-title">Dibuat dengan sepenuh hati</div>
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
    <div class="section-title">Menu Sanbites</div>
    <div class="section-desc">Pilih sandwich favoritmu, rasakan nikmatnya di setiap gigitan.</div>
  </div>
  <div class="products">
    <div class="product-card reveal">
      <div class="product-art"><span>🥪</span></div>
      <div class="product-info">
        <span class="pill">SIMPLE &amp; DELICIOUS</span>
        <h3>Sandwich Telur</h3>
        <p>Roti lembut dengan isian telur yang gurih dan nikmat. Pilihan pas untuk camilan praktis.</p>
        <div class="price">Rp10.000 <small>/ porsi</small></div>
      </div>
    </div>
    <div class="product-card reveal">
      <div class="product-art" style="background:linear-gradient(135deg,#f5dfc5,#e8c49e)"><span>🥪</span></div>
      <div class="product-info">
        <span class="pill">LEBIH MENGENYANGKAN</span>
        <h3>Sandwich Telur + Daging</h3>
        <p>Kombinasi telur dan daging yang gurih dalam roti lembut. Cocok untuk mengisi energimu.</p>
        <div class="price">Rp17.000 <small>/ porsi</small></div>
      </div>
    </div>
  </div>
</section>

<section id="momen" class="section">
  <div class="section-head reveal">
    <div class="section-kicker">Kapan saja</div>
    <div class="section-title">Cocok untuk setiap momen</div>
    <div class="section-desc">Dari pagi hingga sore, Sanbites siap menemani harimu.</div>
  </div>
  <div class="moments">
    <div class="moment reveal">
      <div class="moment-art" style="background:linear-gradient(135deg,#fde9c9,#f7cf9b)"><span>🌅</span></div>
      <h4>Teman Sarapan</h4>
      <p>Mulai hari dengan sandwich hangat yang mengenyangkan dan praktis.</p>
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

<section id="media-sosial" class="section">
  <div class="cta reveal">
    <div>
      <div class="section-kicker">Tetap terhubung</div>
      <h2>Yuk, jadi bagian dari Sanbites!</h2>
      <p>Ikuti akun media sosial kami untuk info menu, promo, dan kabar terbaru dari Sanbites.</p>
      <div class="btn-row" style="animation:none">
        <a class="btn primary" href="https://www.instagram.com/" target="_blank">Instagram ↗</a>
        <a class="btn ghost" href="https://www.tiktok.com/" target="_blank">TikTok ↗</a>
      </div>
    </div>
    <div class="cta-art"><span>🥪</span></div>
  </div>
</section>

<div class="footer">
  <b>SAN<span>BITES</span> 🥪</b><br>
  © 2026 Sanbites. Made with love and good taste.
</div>
"""), unsafe_allow_html=True)