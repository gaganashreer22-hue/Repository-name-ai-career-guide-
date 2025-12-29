import streamlit as st

st.set_page_config(page_title="AI Career Guide", page_icon="🎓")
st.title("🎓 AI Career Learning Path Recommendation System")

career_paths = {
    "Doctor": ["Study PCB", "Clear NEET", "Medical college", "Internship", "Specialization"],
    "Engineer": ["Study PCM", "Clear JEE", "Engineering college", "Projects", "Internships"],
    "Teacher": ["Graduation", "B.Ed", "Clear TET/CTET", "Teaching job", "Experience"],
    "Software Developer": ["Learn coding", "DSA", "Projects", "Internships", "Job"],
    "Data Scientist": ["Python", "Statistics", "ML", "Projects", "Job"],
    "AI Engineer": ["Python", "ML", "Deep Learning", "Projects", "Job"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "Projects", "Job"],
    "Full Stack Developer": ["Frontend", "Backend", "Databases", "Projects", "Job"],
    "Mobile App Developer": ["Android/iOS", "APIs", "Projects", "Testing", "Job"],
    "Game Developer": ["Game engines", "Coding", "Assets", "Projects", "Job"],
    "Cyber Security Analyst": ["Networking", "Security basics", "Tools", "Certifications", "Job"],
    "Ethical Hacker": ["Linux", "Networking", "Cybersecurity", "Certifications", "Job"],
    "Cloud Engineer": ["AWS/Azure", "Linux", "DevOps", "Projects", "Job"],
    "DevOps Engineer": ["Linux", "Docker", "CI/CD", "Cloud", "Job"],
    "Network Engineer": ["Networking", "CCNA", "Internships", "Projects", "Job"],
    "Database Administrator": ["SQL", "DB tools", "Optimization", "Projects", "Job"],
    "Blockchain Developer": ["Blockchain basics", "Solidity", "Projects", "Internships", "Job"],
    "UI/UX Designer": ["Design basics", "Figma", "UX research", "Portfolio", "Job"],
    "Graphic Designer": ["Photoshop", "Illustrator", "Portfolio", "Clients", "Job"],
    "Digital Marketer": ["SEO", "Ads", "Content", "Campaigns", "Job"],
    "Content Writer": ["Writing skills", "SEO", "Portfolio", "Freelance", "Clients"],
    "Journalist": ["News writing", "Internship", "Field work", "Portfolio", "Media job"],
    "Photographer": ["Camera basics", "Editing", "Portfolio", "Clients", "Brand"],
    "Videographer": ["Shooting", "Editing", "Portfolio", "Clients", "Projects"],
    "YouTuber": ["Choose niche", "Create content", "Consistency", "Monetization", "Branding"],
    "Blogger": ["Choose niche", "Writing", "SEO", "Traffic", "Monetization"],
    "Social Media Manager": ["Content planning", "Analytics", "Growth", "Clients", "Job"],
    "Business Analyst": ["Excel", "SQL", "Analytics", "Projects", "Job"],
    "MBA Graduate": ["Graduation", "CAT", "MBA", "Internship", "Corporate job"],
    "Chartered Accountant": ["Foundation", "Intermediate", "Articleship", "Final", "Practice"],
    "Lawyer": ["Graduation", "LLB", "Internship", "Practice", "Specialization"],
    "Civil Engineer": ["Site work", "AutoCAD", "Internships", "Projects", "Job"],
    "Mechanical Engineer": ["Design tools", "Manufacturing", "Internships", "Projects", "Job"],
    "Electrical Engineer": ["Power systems", "PLC", "Internships", "Projects", "Job"],
    "Electronics Engineer": ["Circuits", "Embedded", "Internships", "Projects", "Job"],
    "Architect": ["Design basics", "Architecture college", "Internship", "Portfolio", "Job"],
    "Interior Designer": ["Design skills", "Software tools", "Portfolio", "Clients", "Job"],
    "Financial Analyst": ["Finance basics", "Excel", "Analysis", "Internships", "Job"],
    "Stock Trader": ["Market basics", "Technical analysis", "Practice", "Risk management", "Trading"],
    "Economist": ["Statistics", "Research", "Policy study", "Analysis", "Job"],
    "Banker": ["Bank exams", "Preparation", "Clear exam", "Training", "Job"],
    "Government Officer": ["UPSC/SSC", "Preparation", "Clear exam", "Training", "Posting"],
    "Army Officer": ["Physical training", "Defense exams", "SSB", "Training", "Service"]
}

career = st.selectbox("Choose your career", sorted(career_paths.keys()))

if st.button("Show Learning Path"):
    st.subheader("🧭 Learning Path")
    for step in career_paths[career]:
        st.write("➡", step)

