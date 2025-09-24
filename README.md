# AIML3403 Capstone Project – AI-Powered Fake Job Posting Detector
Capstone project for AIML-3403: AI-Powered Fake Job Posting Detector (Fall 2025)

## 📖 Project Overview
This project is part of **AIML-3403 (Capstone Project)** at Lambton College, Fall 2025.  
Our goal is to develop an **AI-powered system to detect fraudulent job postings** using **machine learning and natural language processing (NLP)** techniques.  

Fraudulent job ads are a growing concern in Canada, especially for **international students, newcomers, and young professionals**.  
Our system analyzes **job descriptions and metadata** (email domains, URLs, salary ranges, etc.) to classify postings as **real or fake**, and provides **explainability outputs** highlighting red-flag features.

---

## 🎯 Objectives
- Detect fraudulent job postings using ML and NLP models.
- Compare **baseline models** (Logistic Regression, Random Forest) with **advanced models** (BERT/RoBERTa).
- Engineer **metadata-based features** and combine with NLP through a **fusion model**.
- Apply **explainable AI (SHAP/LIME)** to highlight fraud indicators.
- Build a **prototype app (Streamlit/Flask)** to demonstrate real-time fraud detection.
  
---

## 🛠️ Tech Stack
- **Languages:** Python  
- **Libraries:** scikit-learn, pandas, numpy, matplotlib, seaborn, XGBoost, PyTorch, Hugging Face Transformers  
- **Explainability:** SHAP, LIME  
- **Deployment:** Streamlit / Flask  
- **Version Control:** GitHub  
- **Collaboration:** GitHub Projects (Kanban board), Issues  

---

## 📅 Timeline
The project will be completed over **12 weeks** with the following key phases:
- Week 1: Planning & Proposal  
- Weeks 2–3: Data Exploration & Preprocessing  
- Week 4: Baseline Models  
- Weeks 5–6: Advanced NLP Models  
- Week 7: Metadata + Fusion Model  
- Week 8: Explainability Implementation  
- Week 9: Prototype App  
- Week 10: Testing & Robustness  
- Week 11: Documentation & Draft Report  
- Week 12: Final Presentation & Submission  

---
## 📂 Repository Structure
```bash
AIML3403-FakeJobPostingDetector/
│
├── .github/workflows/ # CI/CD workflows (pre-commit, linting, tests)
│
├── app/ # Prototype application (Streamlit/Flask)
│
├── data/
│ └── raw/ # Raw dataset (fake_job_postings.csv)
│
├── fakedetector/ # Main source package
│ ├── init.py
│ ├── config/ # Project configuration (YAML, constants)
│ ├── data/ # Data ingestion and processing scripts
│ ├── features/ # Feature engineering and preprocessing
│ ├── models/ # Baseline, transformer, and fusion models
│ └── utils/ # Helper functions (I/O, common utilities)
│
├── notebooks/ # Jupyter notebooks for experiments
│ ├── 01_eda.ipynb # Exploratory Data Analysis
│ └── 02_preprocessing_and_splits.ipynb # Preprocessing & data splits
│
├── tests/ # Unit and smoke tests
│ └── test_smoke.py
│
├── .gitignore # Ignored files and directories
├── .pre-commit-config.yaml # Pre-commit hooks (black, isort, ruff, etc.)
├── CODE_OF_CONDUCT.md # Contribution code of conduct
├── CONTRIBUTING.md # Guidelines for contributors
├── pyproject.toml # Project configuration for tools
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```
---

## 📊 Dataset
- **Source:** [Kaggle – Real/Fake Job Posting Prediction](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction)  
- **Size:** ~18,000 postings (≈800 labeled fraudulent)  
- **Format:** Text + metadata (title, location, department, salary, company profile, description, etc.)  
- **Label:** `fraudulent` (0 = real, 1 = fake)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/SandhyaSivakumar99/AIML3403-FakeJobPostingDetector.git
cd AIML3403-FakeJobPostingDetector
```

### 2️⃣ Create and activate virtual environment
```bash
python -m venv .venv
.\.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Mac/Linux
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
pre-commit install
```

### 4️⃣ Run pre-commit checks (formatting, linting)
```bash
pre-commit run --all-files
```

### 5️⃣ Run tests
```bash
pytest -q
```
---
## ⚙️ Team
- Sandhya Sivakumar - c0956298
- Hetvi Sodha - c0954042
- Manpreet Kaur - c0949651
- Amandeep Singh - c0956866