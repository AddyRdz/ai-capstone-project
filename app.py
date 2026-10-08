import streamlit as st
from ai_capstone_project.validation import validate_inputs
from ai_capstone_project.prompts import build_prompt
from ai_capstone_project.llm_client import ask_model

st.title("AI Marketing Campaign Content Generator")