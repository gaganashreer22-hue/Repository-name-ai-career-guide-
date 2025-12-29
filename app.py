import streamlit as st

st.set_page_config(page_title="AI Career Guide", page_icon="🎓")
st.title("🎓 AI Career Learning Path Recommendation System")

career_paths = {
    "Doctor": {
        "stream": "Science (PCB)",
        "exams": ["NEET"],
        "courses": ["MBBS", "MD / MS"],
        "colleges": [
            "AIIMS Delhi",
            "Christian Medical College, Vellore",
            "AFMC Pune",
            "JIPMER Puducherry"
        ],
        "skills": ["Clinical skills", "Communication", "Research"]
    },

    "Software Developer": {
        "stream": "Science (PCM) / Any stream",
        "exams": ["JEE (optional)", "University Entrance"],
        "courses": ["B.Tech (CSE)", "BCA", "MCA"],
        "colleges": [
            "IIT Bombay",
            "IIT Madras",
            "NIT Trichy",
            "IIIT Hyderabad"
        ],
        "skills": ["Python", "DSA", "Web Development", "Git"]
    },

    "Teacher": {
        "stream": "Any stream",
        "exams": ["TET", "CTET"],
        "courses": ["B.Ed", "M.Ed"],
        "colleges": [
            "Delhi University",
            "BHU",
            "Jamia Millia Islamia",
            "TISS Mumbai"
        ],
        "skills": ["Teaching", "Communication", "Subject knowledge"]
    }
}

career = st.selectbox("Choose your career", career_paths.keys())

if st.button("Show Career Details"):
    data = career_paths[career]

    st.subheader("📘 Required Stream")
    st.write(data["stream"])

    st.subheader("📝 Entrance Exams")
    for exam in data["exams"]:
        st.write("•", exam)

    st.subheader("🎓 Courses to Take")
    for course in data["courses"]:
        st.write("•", course)

    st.subheader("🏫 Top Colleges in India")
    for college in data["colleges"]:
        st.write("•", college)

    st.subheader("🛠 Skills to Learn")
    for skill in data["skills"]:
        st.write("•", skill)
