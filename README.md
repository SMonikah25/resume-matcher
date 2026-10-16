# Resume Matcher

A Python project that compares a resume with a job description and shows a match score, matched skills and missing skills.

## Features
- Reads text from a PDF resume
- Cleans the text (lowercase, removes symbols and stopwords)
- Finds skills present in the resume
- Calculates a match score using TF-IDF and cosine similarity
- Shows matched skills and missing skills

## Tech Used
Python, pdfplumber, NLTK, scikit-learn

## How to Run
1. Install the libraries: `pip install pdfplumber nltk scikit-learn`
2. Put a resume file named `resume.pdf` in the project folder
3. Run: `python main.py`

## Author
Monika
