import streamlit as st
import streamlit.components.v1 as components

# Configure the page to use the full width and set title
st.set_page_config(
    page_title="Your Companion – Mental Wellness Chat",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to remove Streamlit's default margins and padding
# This makes the iframe take up the entire screen space
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        header {visibility: hidden !important;}
        #MainMenu {visibility: hidden !important;}
        footer {visibility: hidden !important;}
        
        /* Make the iframe fill the viewport */
        iframe {
            width: 100vw !important;
            height: 100vh !important;
            border: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# Read the HTML content
with open("companion.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render the application
# We provide a height to fallback, but the CSS above will force it to 100vh
components.html(html_content, height=1000, scrolling=True)
