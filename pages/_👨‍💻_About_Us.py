#version 1.3
from utils import local_css
local_css("assets/style.css")

import streamlit as st
st.title("👨‍💻 About Us")
st.markdown("""
Built by a passionate team of ML developers and designers.

- 🤖 AI by: Sarvesh & Team  
- 🎨 UI/UX by: You!  
- 📬 Contact: sarvesh@email.com
""")
