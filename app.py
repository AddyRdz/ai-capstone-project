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
    channel = st.selectbox("Channel", ["email", "social_post", "ad _copy"])
    submitted = st.form_submit_button("Generate")
    if submitted:
        data = {
            "product" : product,
            "audience" : audience,
            "goal" : goal,
            "channel" : channel,
            "tone" : tone,
        }
        problems = validate_inputs(data)
        if problems:
            for p in problems:
                st.error(p)
        else:
            prompt = build_prompt(data)
            draft = ask_model(prompt)
            st.write(draft)