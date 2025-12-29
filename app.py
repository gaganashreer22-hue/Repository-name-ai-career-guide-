import streamlit as st
import google.generativeai as genai

# CONFIGURE API KEY
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.set_page_config(page_title="AI Career Guide", page_icon="🎓")
import google.generativeai as genai

st.title("🎓 AI Career Guidance System")

st.write("Type any career and get a real answer in sentences.")

career = st.text_input("Enter your career (example: Doctor, Pilot, Fashion Designer)")

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

if st.button("Get Career Guidance") and career:
    prompt = f"""
    You are a career counselor in India.

    A student wants to become a {career}.

    Explain in simple English and FULL SENTENCES:
    - What stream to choose
    - What exams are required
    - What courses to take
    - Which colleges in India are best

    Give a real and practical answer.
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    st.subheader("Career Guidance")
    st.write(response.text)


career = st.text_input("Enter your career goal (example: Pilot, Astronaut, Fashion Designer)")

if st.button("Get Career Guidance") and career:
    prompt = f"""
    You are a career guidance expert in India.

    The user wants to become a {career}.

    Give a clear, real, and practical answer in FULL SENTENCES covering:
    1. Which stream to choose after 10th/12th
    2. Entrance exams required
    3. Courses to study
    4. Best colleges in India
    5. Skills required

    Write the answer in simple English, student-friendly language.
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    st.subheader(f"📘 Career Guidance for {career}")
    st.write(response.text)

