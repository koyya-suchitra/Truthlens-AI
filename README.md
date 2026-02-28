# TruthLens AI

**AI-Powered Resume Credibility Analyzer**

TruthLens AI is a full-stack system that evaluates resume credibility by analyzing skill–project consistency and optionally verifying GitHub activity. It is designed to help recruiters quickly identify potential exaggerations and assist candidates in assessing their profiles.

---

## 🚧 Status

Environment setup completed. Core functionality is under active development.

---

## ✨ Planned Features

* Resume upload and text extraction
* Skill and project detection
* Truth Score generation
* Risk flag identification
* GitHub verification (planned)
* Recruiter-friendly dashboard (planned)

---

## 🏗️ Architecture

```text
User → React Frontend → FastAPI Backend → AI Engine → (MongoDB - planned) → GitHub API
```

---

## 🧩 Tech Stack

**Frontend:** React.js, HTML, CSS
**Backend:** FastAPI, Python
**AI/NLP:** Python-based processing
**Database (planned):** MongoDB
**External API:** GitHub REST API

---

## ⚙️ Local Setup

```bash
git clone https://github.com/your-username/truthlens-ai.git
cd truthlens-ai
```

**Backend**

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 👤 Author

Suchitra Koyya
B.Tech CSE (Data Science) — 2027

---

*Project in active development.*
