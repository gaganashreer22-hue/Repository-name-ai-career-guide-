import streamlit as st

st.set_page_config(page_title="AI Career Guide", page_icon="🎓")

st.title("🎓 AI Career Learning Path Recommendation System")

career_paths = {
    "Doctor": ["Study PCB", "Clear NEET", "Medical College", "Internship"],
    "Engineer": ["Study PCM", "Clear JEE", "Engineering College", "Projects"],
    "Teacher": ["Graduation", "B.Ed", "Clear TET/CTET", "Teaching Job"],
    "Software Developer": ["Learn Coding", "Build Projects", "Internships", "Job"],
    "Data Scientist": ["Python", "Statistics", "ML", "Projects"]
}

career = st.selectbox("Choose your career", career_paths.keys())

if st.button("Show Learning Path"):
    st.subheader("🧭 Learning Path")
    for step in career_paths[career]:
        st.write("➡", step)

