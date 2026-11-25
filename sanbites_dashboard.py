import streamlit as st

st.set_page_config(
    page_title="Sanbites | Sandwich",
    page_icon="🥪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');

:root { --cream:#fffaf1; --ink:#29251f; --muted:#766f64; --orange:#e87936; --green:#314d3b; }
html { scroll-behavior:smooth; }
.stApp { background:var(--cream); color:var(--ink); font-family:'DM Sans',sans-serif; }
.block-container { max-width:1180px; padding-top:1rem; padding-bottom:4rem; }
header, footer {visibility:hidden;}
[data-testid="stToolbar"] {display:none;}
.navbar {
  position:sticky; top:0; z-index:999; display:flex; align-items:center;
  justify-content:space-between; gap:20px; padding:16px 24px; margin:0 0 28px;
  background:rgba(255,250,241,.94); backdrop-filter:blur(12px);
  border:1px solid #eee5d8; border-radius:18px; box-shadow:0 8px 28px #392b1710;
}
.brand {font-size:23px; font-weight:800; letter-spacing:-1px; color:var(--green);}
.brand span {color:var(--orange);}
.navlinks {display:flex; gap:10px; flex-wrap:wrap;}
.navlinks a {text-decoration:none; color:#514b42; font-weight:700; font-size:14px;
  padding:10px 16px; border-radius:999px; transition:.2s;}
.navlinks a:hover {background:#f5e6d4; color:#b95720;}
.hero {background:var(--green); border-radius:28px; padding:58px 52px; color:white;
  position:relative; overflow:hidden; min-height:330px;}
.hero:after {content:'🥪'; position:absolute; right:7%; top:12%; font-size:170px;
  transform:rotate(-13deg); filter:drop-shadow(0 18px 14px #17251c55);}
.eyebrow {color:#f6bd87; font-size:12px; font-weight:800; letter-spacing:2px; text-transform:uppercase;}
.hero h1 {font-family:'Playfair Display',serif; font-size:clamp(38px,5vw,62px);
  line-height:1.06; max-width:570px; margin:15px 0;}
.hero p {color:#e4e9df; font-size:16px; max-width:470px; line-height:1.7;}
.hero .tag {display:inline-block; margin-top:12px; background:#ffffff1c; border:1px solid #ffffff35;
  padding:10px 16px; border-radius:999px; font-weight:700; font-size:13px;}
.section-kicker {color:var(--orange); text-transform:uppercase; letter-spacing:2px;
  font-size:11px; font-weight:800; margin-bottom:7px;}
.section-title {font-family:'Playfair Display',serif; font-size:36px; margin:0 0 8px; color:var(--ink);}
.section-desc {color:var(--muted); margin:0 0 24px;}
.product-card {background:#fff; border:1px solid #eee5d8; border-radius:22px;
  overflow:hidden; box-shadow:0 10px 30px #392b170b; height:100%;}
.product-art {height:185px; display:flex; align-items:center; justify-content:center;
  background:linear-gradient(135deg,#f8e7d2,#f3d4b5); font-size:105px;}
.product-info {padding:22px;}
.product-info h3 {margin:0 0 7px; font-size:20px; color:var(--ink);}
.product-info p {color:var(--muted); font-size:14px; min-height:42px; line-height:1.55;}
.price {font-size:25px; font-weight:800; color:var(--green); margin-top:12px;}
.price small {font-size:12px; font-weight:600; color:var(--muted);}
.pill {display:inline-block; background:#fff0e3; color:#b95720; border-radius:999px;
  padding:6px 10px; font-size:11px; font-weight:800;}
.info-panel {background:#fff; border:1px solid #eee5d8; border-radius:22px; padding:26px;}
.social-link {display:inline-block; margin:7px 8px 0 0; padding:11px 17px; border-radius:999px;
  text-decoration:none; color:white !important; background:var(--green); font-weight:700;}
.footer {text-align:center; color:#8b8378; font-size:12px; padding:28px 0 4px;}
@media(max-width:700px) {
 .hero {padding:38px 25px; min-height:390px;}
 .hero:after {right:5%; top:auto; bottom:0; font-size:110px; opacity:.85;}
 .navbar {align-items:flex-start; flex-direction:column; padding:14px;}
 .navlinks {gap:2px;} .navlinks a {padding:8px 11px;}
}
</style>

<div class="navbar">
  <div class="brand">san<span>bites.</span> 🥪</div>
  <div class="navlinks">
    <a href="#beranda">Beranda</a>
    <a href="#produk">Produk</a>
    <a href="#media-sosial">Media Sosial</a>
  </div>
</div>

<div id="beranda"></div>
<section class="hero">
  <div class="eyebrow">Fresh • Simple • Delicious</div>
  <h1>Sandwich enak,<br>teman setiap hari.</h1>
  <p>Temukan sandwich lezat dengan isian pilihan. Dibuat untuk menemani aktivitasmu, kapan pun kamu lapar.</p>
  <span class="tag">Mulai dari Rp10.000</span>
</section>
""", unsafe_allow_html=True)

st.markdown("""
<div style="height:54px"></div>
<div id="produk"></div>
<div class="section-kicker">Pilihan favoritmu</div>
<div class="section-title">Menu Sanbites</div>
<div class="section-desc">Pilih sandwich favoritmu, rasakan nikmatnya di setiap gigitan.</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")
with col1:
    st.markdown("""
    <div class="product-card">
      <div class="product-art">🥪</div>
      <div class="product-info">
        <span class="pill">SIMPLE & DELICIOUS</span>
        <h3>Sandwich Telur</h3>
        <p>Roti lembut dengan isian telur yang gurih dan nikmat. Pilihan pas untuk camilan praktis.</p>
        <div class="price">Rp10.000 <small>/ porsi</small></div>
      </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="product-card">
      <div class="product-art" style="background:linear-gradient(135deg,#f5dfc5,#e8c49e)">🥪</div>
      <div class="product-info">
        <span class="pill">LEBIH MENGENYANGKAN</span>
        <h3>Sandwich Telur + Daging</h3>
        <p>Kombinasi telur dan daging yang gurih dalam roti lembut. Cocok untuk mengisi energimu.</p>
        <div class="price">Rp17.000 <small>/ porsi</small></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="height:58px"></div>
<div id="media-sosial"></div>
<div class="section-kicker">Tetap terhubung</div>
<div class="section-title">Ikuti Media Sosial Kami</div>
<div class="section-desc">Dapatkan informasi menu, promo, dan kabar terbaru dari Sanbites.</div>
<div class="info-panel">
  <h3 style="margin:0 0 8px;color:#314d3b">Yuk, jadi bagian dari Sanbites!</h3>
  <p style="margin:0;color:#766f64;line-height:1.7">Ikuti akun media sosial kami agar tidak ketinggalan update terbaru.</p>
  <a class="social-link" href="https://www.instagram.com/" target="_blank">Instagram ↗</a>
  <a class="social-link" href="https://www.tiktok.com/" target="_blank">TikTok ↗</a>
</div>
<div class="footer">© 2026 Sanbites. Made with love and good taste. 🥪</div>
""", unsafe_allow_html=True)
