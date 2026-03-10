import streamlit as st

# 1. Grundinställningar
st.set_page_config(page_title="Vem är bäst?", layout="centered")

# 2. Session State
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'w' not in st.session_state:
    st.session_state.w = 100   
if 'h' not in st.session_state:
    st.session_state.h = 40   
if 'f' not in st.session_state:
    st.session_state.f = 14   

# --- STANDARD-CSS ---
st.markdown(f"""
    <style>
        div.stButton > button {{
            width: 100px !important;
            height: 40px !important;
            font-size: 14px !important;
            background-color: rgb(240, 242, 246) !important;
            color: rgb(49, 51, 63) !important;
            border: 1px solid rgba(49, 51, 63, 0.2) !important;
        }}
    </style>
""", unsafe_allow_html=True)

# --- DYNAMISK CSS ---
grow_css = ""
if st.session_state.page == 1:
    grow_css = f"div.stColumn:nth-child(1) button {{ width: {st.session_state.w}px !important; height: {st.session_state.h}px !important; font-size: {st.session_state.f}px !important; }}"
elif st.session_state.page == 2:
    grow_css = f"div.stColumn:nth-child(2) button {{ width: {st.session_state.w}px !important; height: {st.session_state.h}px !important; font-size: {st.session_state.f}px !important; }}"
elif st.session_state.page == 3:
    grow_css = f"div.stColumn:nth-child(1) button {{ width: {st.session_state.w}px !important; height: {st.session_state.h}px !important; font-size: {st.session_state.f}px !important; }}"

st.markdown(f"<style>{grow_css}</style>", unsafe_allow_html=True)

# --- SIDA 1 ---
if st.session_state.page == 1:
    st.markdown("<h1 style='text-align: center;'>Vem av oss är smartast?</h1>", unsafe_allow_html=True)
    # Här tvingar vi den att försöka visa bilden direkt
    st.image("Pinguin1.jfif", use_container_width=True)

    col1, col2 = st.columns(2)
    if col1.button("Jaro"):
        st.session_state.page = 2
        st.session_state.w, st.session_state.h, st.session_state.f = 100, 40, 14
        st.rerun()
    if col2.button("Alice"):
        st.session_state.w += 80; st.session_state.h += 50; st.session_state.f += 10
        st.rerun()

# --- SIDA 2 ---
elif st.session_state.page == 2:
    st.markdown("<h1 style='text-align: center;'>Vem av oss är bäst?</h1>", unsafe_allow_html=True)
    st.image("pinguin2.jfif", use_container_width=True)

    col1, col2 = st.columns(2)
    if col1.button("Jaro"):
        st.session_state.w += 80; st.session_state.h += 50; st.session_state.f += 10
        st.rerun()
    if col2.button("Alice"):
        st.session_state.page = 3
        st.session_state.w, st.session_state.h, st.session_state.f = 100, 40, 1
