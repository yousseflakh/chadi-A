import streamlit as st
from PIL import Image

# الحالة (state)
if "step" not in st.session_state:
    st.session_state.step = 1
if "finished" not in st.session_state:
    st.session_state.finished = False
if "message" not in st.session_state:
    st.session_state.message = ""

# العنوان
st.set_page_config(page_title="Wach Katbghini?", page_icon="💖")

st.markdown("<h1 style='text-align:center; color:#AD1457;'>jawbi bsara7a 💖👀</h1>", unsafe_allow_html=True)

# الصورة
try:
    img = Image.open("images.png")  # حط الصورة فـ نفس dossier
    st.image(img, width=150)
except:
    st.warning("حط الصورة فـ نفس الملف وسميها images.png")

# السؤال أو النتيجة
if not st.session_state.finished:
    question = "Wach Katbghinii?"

    if st.session_state.step == 2:
        question = "Wach mat2akdaaa? 🤔"
    elif st.session_state.step == 3:
        question = "Takdi? 😱"
    elif st.session_state.step == 4:
        question = "chofi wkan? 😱"
    elif st.session_state.step == 5:
        question = "rah anskhaaff takdi? 😱"

    st.markdown(f"<h2 style='text-align:center; color:#D81B60;'>{question}</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # زر AH
    with col1:
        if st.button("AH 💖"):
            st.session_state.message = "knt 3arfha! Hta ana kanbghik! ❤️✨"
            st.session_state.finished = True

    # زر LA
    with col2:
        if st.button("LA 💔"):
            if st.session_state.step < 5:
                st.session_state.step += 1
            else:
                st.session_state.message = "Hchoma 3lik \n Sf 9l9tini 😢💔"
                st.session_state.finished = True

else:
    st.markdown(f"<h2 style='text-align:center; color:#880E4F;'>{st.session_state.message}</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>The End! ✨</h3>", unsafe_allow_html=True)

    if st.button("Restart 🔄"):
        st.session_state.step = 1
        st.session_state.finished = False