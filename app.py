import re
import nltk
import pdfplumber
import streamlit as st
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("stopwords", quiet=True)
stop_words = set(stopwords.words("english"))

skills_list = [
    "python", "java", "sql", "html", "css", "javascript",
    "flask", "git", "github", "mysql", "rdbms", "data structures",
    "web technology", "ms office", "power bi", "excel", "salesforce"
]


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    words = [w for w in text.split() if w not in stop_words]
    return " ".join(words)


def find_skills(text):
    return [s for s in skills_list if re.search(r"\b" + s + r"\b", text)]


st.title("Resume Matcher")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
job_description = st.text_area("Paste the job description here", height=200)

if st.button("Check Match"):
    if uploaded_file is None or job_description.strip() == "":
        st.warning("Please upload a resume and paste a job description.")
    else:
        with pdfplumber.open(uploaded_file) as pdf:
            resume_text = ""
            for page in pdf.pages:
                resume_text += page.extract_text() or ""

        resume_clean = clean_text(resume_text)
        job_clean = clean_text(job_description)

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([resume_clean, job_clean])
        score = cosine_similarity(vectors[0], vectors[1])[0][0]
        match_percentage = round(score * 100, 2)

        resume_skills = find_skills(resume_clean)
        job_skills = find_skills(job_clean)
        matched = [s for s in job_skills if s in resume_skills]
        missing = [s for s in job_skills if s not in resume_skills]

        st.subheader("Result")
        st.metric("Match Score", str(match_percentage) + " %")
        st.write("**Matched skills:**", ", ".join(matched) if matched else "None")
        st.write("**Missing skills:**", ", ".join(missing) if missing else "None")