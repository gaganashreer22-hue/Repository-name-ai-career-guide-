import streamlit as st
import google.generativeai as genai

# CONFIGURE API KEY
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.set_page_config(page_title="AI Career Guide", page_icon="🎓")
st.title("🎓 AI Career Learning Path Recommendation System")

st.write("Type **ANY career** and get real guidance with courses and best colleges.")

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

