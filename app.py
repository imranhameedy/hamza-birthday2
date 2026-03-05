import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="Happy Birthday Hamza 🎂", page_icon="🎂", layout="centered")

def read_bytes(rel_path: str) -> bytes:
    p = Path(__file__).parent / rel_path
    if not p.exists():
        st.error(f"Missing file: {rel_path} (check filename exactly in GitHub)")
        st.stop()
    return p.read_bytes()

friend_name = "Hamza"
sender_name = "Imran Khan"

# ---------- CSS: notebook + fixed page size ----------
st.markdown("""
<style>
.stApp{
  background: radial-gradient(circle at top, #fff7ea 0%, #fff 35%, #f7fbff 100%);
}
.block-container{
  max-width: 950px;
  position: relative;
  z-index: 2;
}

/* balloons */
.balloon{ position:fixed; bottom:-120px; width:55px; height:70px; border-radius:50% 50% 45% 45%;
  opacity:.30; animation: floatUp linear infinite; z-index:0; }
.balloon:after{ content:""; position:absolute; left:50%; top:66px; width:2px; height:90px; background:rgba(0,0,0,.10); }
@keyframes floatUp{ from{transform:translateY(0)} to{transform:translateY(-120vh)} }

/* header */
.bigtitle{ text-align:center; font-size:52px; font-weight:900; margin: 8px 0 4px 0; }
.sub{ text-align:center; font-size:18px; opacity:.85; margin:0 0 10px 0; }
.smallnote{ font-size: 13px; opacity:0.72; text-align:center; margin-top:6px; }

/* notebook shell */
.notebook{
  position: relative;
  background: rgba(255,255,255,0.92);
  border: 1px solid rgba(0,0,0,0.08);
  border-radius: 22px;
  box-shadow: 0 18px 40px rgba(0,0,0,0.08);
  overflow: hidden;
}

/* notebook header strip */
.nb-head{
  padding: 14px 18px;
  background: linear-gradient(90deg, rgba(255,205,178,.55), rgba(189,224,254,.55));
  display:flex; justify-content:space-between; align-items:center;
}
.nb-title{ font-size: 20px; font-weight: 850; margin:0; }
.nb-page{ font-size: 14px; opacity:0.75; }

/* page area */
.page{
  padding: 18px 20px;
  background: #fffdf7;
}
.page-inner{
  border-radius: 18px;
  border: 1px solid rgba(0,0,0,0.06);
  background: rgba(255,255,255,0.75);
  padding: 14px;
}

/* fixed media frame */
.media-frame{
  height: 520px;             /* change to 600 if you want taller */
  border-radius: 16px;
  border: 1px solid rgba(0,0,0,0.08);
  background: white;
  box-shadow: 0 12px 26px rgba(0,0,0,0.10);
  overflow:hidden;
  display:flex;
  align-items:center;
  justify-content:center;
}
.media-frame img{
  width: 100%;
  height: 100%;
  object-fit: contain;        /* shows full image without cropping */
}

.caption{ font-size: 14px; opacity:0.72; margin-top: 10px; }

div.stButton > button{
  border-radius: 14px !important;
  padding: 0.55rem 0.9rem !important;
}
</style>
""", unsafe_allow_html=True)

# Background balloons
st.markdown("""
<div class="balloon" style="left:6%; background:#ff6b6b; animation-duration: 14s;"></div>
<div class="balloon" style="left:16%; background:#ffd166; animation-duration: 18s;"></div>
<div class="balloon" style="left:28%; background:#06d6a0; animation-duration: 16s;"></div>
<div class="balloon" style="left:40%; background:#4dabf7; animation-duration: 20s;"></div>
<div class="balloon" style="left:52%; background:#b197fc; animation-duration: 17s;"></div>
<div class="balloon" style="left:64%; background:#ff8fab; animation-duration: 19s;"></div>
<div class="balloon" style="left:76%; background:#8ce99a; animation-duration: 15s;"></div>
<div class="balloon" style="left:88%; background:#ffa94d; animation-duration: 21s;"></div>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown(f"<div class='bigtitle'>Happy Birthday, {friend_name} 🎉</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>Flip through the notebook pages 😄</div>", unsafe_allow_html=True)

# ---------- Music (reliable; needs one tap) ----------
music = read_bytes("birthday-music.mp3")
st.markdown("<div style='text-align:center; font-weight:800; opacity:.75;'>🎵 Background music</div>", unsafe_allow_html=True)
st.audio(music, format="audio/mp3", loop=True)
st.markdown("<div class='smallnote'>Tap ▶️ once to start — then it will loop.</div>", unsafe_allow_html=True)

# ---------- Messages ----------
main_message = [
    "Hamza, one of the most precious gifts Allah gave me in 2025 was you and your friendship.",
    "Meri pyaari bro, happy birthday! I wish you a life full of happiness and joy ahead.",
    "May Allah fulfill all your wishes and bless you with success in everything you do.",
    "And yes… I’m still waiting to hear your engagement news soon 😂",
]

cake_text = (
    "I wish I were in Afghanistan so we could celebrate together and cut the cake in person. "
    "But for now, please accept this virtual cake from me 🎂"
)

# ---------- Pages (your exact order) ----------
pages = [
    {"type": "img", "title": "Memory #1", "src": "hamza1.jpeg"},
    {"type": "img", "title": "Memory #2", "src": "hamza2.jpeg"},
    {"type": "img", "title": "Memory #3", "src": "hamza3.jpeg"},
    {"type": "img", "title": "Memory #4", "src": "hamza4.jpeg"},
    {"type": "img", "title": "Memory #5", "src": "hamza5.jpeg"},
    {"type": "text", "title": "Birthday Letter", "lines": main_message},
    {"type": "text", "title": "One More Thing", "lines": [cake_text]},
    {"type": "gif", "title": "Final Surprise", "src": "Birthday-animated.gif"},
]

if "page_index" not in st.session_state:
    st.session_state.page_index = 0

# ---------- Navigation ----------
col_prev, col_mid, col_next = st.columns([1, 2, 1])
with col_prev:
    if st.button("⬅️ Prev", use_container_width=True, disabled=(st.session_state.page_index == 0)):
        st.session_state.page_index -= 1
        st.rerun()
with col_mid:
    st.markdown("<div style='text-align:center; font-weight:850; opacity:0.75;'>Notebook</div>", unsafe_allow_html=True)
with col_next:
    if st.button("Next ➡️", use_container_width=True, disabled=(st.session_state.page_index == len(pages) - 1)):
        st.session_state.page_index += 1
        st.rerun()

p = pages[st.session_state.page_index]
page_no = st.session_state.page_index + 1
total = len(pages)

# ---------- Notebook page ----------
st.markdown("<div class='notebook'>", unsafe_allow_html=True)

st.markdown(f"""
  <div class="nb-head">
    <div class="nb-title">{p["title"]}</div>
    <div class="nb-page">Page {page_no} / {total}</div>
  </div>
""", unsafe_allow_html=True)

st.markdown("<div class='page'><div class='page-inner'>", unsafe_allow_html=True)

if p["type"] in ("img", "gif"):
    data = read_bytes(p["src"])
    mime = "image/gif" if p["type"] == "gif" else "image/jpeg"
    b64 = base64.b64encode(data).decode("utf-8")
    st.markdown(
        f"<div class='media-frame'><img src='data:{mime};base64,{b64}' /></div>",
        unsafe_allow_html=True
    )
    st.markdown("<div class='caption'>Tip: click <b>Next</b> to flip to the next page.</div>", unsafe_allow_html=True)
else:
    for line in p["lines"]:
        st.write(line)
    st.markdown(f"<br><div class='caption'>— from your brother, {sender_name} 🤍</div>", unsafe_allow_html=True)

st.markdown("</div></div></div>", unsafe_allow_html=True)

st.caption("Autoplay with sound is blocked by most browsers. One tap on ▶️ is required.")
