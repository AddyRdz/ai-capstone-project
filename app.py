import streamlit as st
from ai_capstone_project.validation import validate_inputs
from ai_capstone_project.prompts import build_prompt
from ai_capstone_project.llm_client import ask_model

st.title("AI Marketing Campaign Content Generator")

with st.form("marketing_form"):
    product = st.text_input ("Product or service")
    audience = st.text_input ("Audience")
    goal = st.text_input ("Goal")
    tone = st.text_input ("Tone")
    st.form_submit_button ("Submit")