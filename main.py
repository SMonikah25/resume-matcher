import pdfplumber
with  pdfplumber.open("resume.pdf") as pdf:
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
import re
text = text.lower()
text = re.sub(r"[^a-z0-9\s]", "", text)
text = re.sub(r"\s+", " ", text).strip()
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

words = text.split()
clean_words = [w for w in words if w not in stop_words]
text = " ".join(clean_words)
skills_list = [
    "python", "java", "sql", "html", "css", "javascript",
    "flask", "git", "github", "mysql", "rdbms", "data structures",
    "web technology", "ms office", "power bi", "excel", "salesforce"
]

found_skills = []
for skill in skills_list:
    if re.search(r"\b" + skill + r"\b", text):
        found_skills.append(skill)

print("Skills found:", found_skills) 

job_description = """
We are looking for a Python Developer with knowledge of Python, Java, SQL,
HTML, CSS and Flask. Experience with Git, GitHub and MySQL is a plus.
Good understanding of data structures and web technology is required.
Knowledge of Power BI and Excel is an added advantage.
"""

job_description = job_description.lower()
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [text, job_description]

vectorizer = TfidfVectorizer(stop_words="english")
vectors = vectorizer.fit_transform(documents)

score = cosine_similarity(vectors[0], vectors[1])[0][0]
match_percentage = round(score * 100, 2)

job_skills = []
for skill in skills_list:
    if re.search(r"\b" + skill + r"\b", job_description):
        job_skills.append(skill)

matched_skills = [s for s in job_skills if s in found_skills]
missing_skills = [s for s in job_skills if s not in found_skills]

print()
print("=" * 40)
print("      RESUME MATCHER RESULT")
print("=" * 40)
print("Match Score    :", match_percentage, "%")
print("Matched skills :", ", ".join(matched_skills))
print("Missing skills :", ", ".join(missing_skills))
print("=" * 40)