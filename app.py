import streamlit as st
import random
import time

st.set_page_config(page_title="Happy Birthday Hamza 🎂", page_icon="🎂", layout="centered")

st.markdown("""
<style>
.card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 18px;
    padding: 22px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}
.big { font-size: 40px; font-weight: 800; line-height: 1.1; }
.sub { font-size: 18px; opacity: 0.95; }
.badge {
    display: inline-block;
    padding: 6px 10px;
    border-radius: 999px;
    background: rgba(0,255,140,0.15);
    border: 1px solid rgba(0,255,140,0.35);
    font-weight: 600;
}
.small { font-size: 14px; opacity: 0.85; }
</style>
""", unsafe_allow_html=True)

friend_name = "Hamza"

msg_lines = [
    "Hamza, one of the most precious gifts Allah gave me in 2025 was you and your friendship.",
    "Meri pyaari bro, happy birthday! I wish you a life full of happiness and joy ahead.",
    "May Allah fulfill all your wishes and bless you with success in everything you do.",
    "And yes… I’m still waiting to hear your engagement news soon 😂",
]

if "revealed" not in st.session_state:
    st.session_state.revealed = False
if "score" not in st.session_state:
    st.session_state.score = 0
if "target" not in st.session_state:
    st.session_state.target = random.randint(1, 9)

st.markdown(f"""
<div class="card">
  <div class="big">Happy Birthday, {friend_name} 🎉</div>
  <div class="sub">A tiny website made in Python—because you're a programmer 😄</div>
  <div style="margin-top:12px" class="badge">Status: Build ✅ | Bugs: Maybe 😈</div>
</div>
""", unsafe_allow_html=True)

st.write("")
col1, col2 = st.columns(2)

with col1:
    if st.button("🎁 Reveal birthday message", use_container_width=True):
        st.session_state.revealed = True
        st.balloons()

with col2:
    if st.button("🔄 Reset game", use_container_width=True):
        st.session_state.score = 0
        st.session_state.target = random.randint(1, 9)
        st.toast("Game reset. Go hunt bugs 🐛")

st.write("")

if st.session_state.revealed:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📨 Message")
    for line in msg_lines:
        st.write(line)
    st.markdown('<div class="small">May Allah bless you always. آمين 🤍</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.write("")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🐛 Mini Game: Bug Hunt")
st.write("Click the bug with the **same number** as the target. Get **5 points** to unlock the final surprise.")

target = st.session_state.target
st.markdown(f"**Target bug number:** `{target}`")

bugs = list(range(1, 10))
random.shuffle(bugs)

grid = st.columns(3)
clicked = None
for i, n in enumerate(bugs):
    with grid[i % 3]:
        if st.button(f"🐛 Bug {n}", key=f"bug_{n}", use_container_width=True):
            clicked = n

if clicked is not None:
    if clicked == target:
        st.session_state.score += 1
        st.toast("Nice! Bug squashed ✅")
    else:
        st.toast("Wrong bug 😈 Try again.")
    st.session_state.target = random.randint(1, 9)

st.write(f"**Score:** {st.session_state.score} / 5")

if st.session_state.score >= 5:
    st.success("Unlocked 🎉")
    st.markdown("### Final Surprise 😄")
    st.markdown("""
- Clean builds ✅  
- Big wins ✅  
- Engagement news… loading… **any day now** 😂
""")
    st.snow()

st.markdown("</div>", unsafe_allow_html=True)
st.caption("Made with Python + Streamlit.")