# Redrob AI Candidate Ranking System

## Overview

This project was developed as part of the Redrob AI Candidate Ranking Challenge.

The objective is to rank candidate profiles from a large dataset and identify the top 100 candidates that best match a Senior AI Engineer role focused on:

* Machine Learning
* Retrieval Systems
* Search & Ranking
* Embeddings
* Vector Databases
* LLM Applications
* Production AI Systems

The solution processes candidate profiles, extracts meaningful hiring signals, scores candidates using a rule-based ranking engine, and generates a submission file containing ranked candidates along with human-readable reasoning.

---

## Problem Statement

Recruiters often receive thousands of candidate profiles for specialized AI roles. Manually reviewing every profile is expensive and time-consuming.

This project automates the process by:

1. Parsing candidate data.
2. Extracting relevant technical and behavioral signals.
3. Evaluating candidate-job alignment.
4. Producing a ranked shortlist of the best candidates.

---

## Solution Architecture

```text
Candidate Dataset
        │
        ▼
Data Loader
        │
        ▼
Feature Engineering
        │
        ▼
Scoring Engine
        │
        ▼
Candidate Ranking
        │
        ▼
Reasoning Generation
        │
        ▼
Submission CSV
```

---

## Feature Engineering

The ranking engine evaluates multiple dimensions of a candidate profile.

### Experience Signals

* Years of professional experience
* Alignment with target experience range
* Seniority indicators

### Career Signals

* Current job title
* Historical job titles
* AI/ML career consistency
* Relevant engineering progression

### Technical Skills

The system detects skills related to:

* Python
* Machine Learning
* Deep Learning
* NLP
* LLMs
* RAG
* Retrieval Systems
* Search Ranking
* Embeddings
* Vector Databases

Supported technologies include:

* Pinecone
* Weaviate
* Qdrant
* FAISS
* OpenSearch
* Elasticsearch
* pgvector
* Sentence Transformers

### Production Readiness

The system rewards candidates who demonstrate:

* Production deployments
* Real-world ML systems
* Evaluation frameworks
* Model monitoring
* A/B testing

### Behavioral Signals

Candidate engagement metrics are incorporated through:

* Recruiter response rate
* Interview completion rate
* Open-to-work status
* Notice period

---

## Scoring Methodology

Each candidate receives a composite score derived from:

| Component              | Purpose                          |
| ---------------------- | -------------------------------- |
| Experience             | Match desired seniority          |
| Title Alignment        | AI/ML role relevance             |
| Career Consistency     | Long-term AI focus               |
| Retrieval Skills       | Search and ranking expertise     |
| Vector Database Skills | Modern retrieval stack           |
| Production Experience  | Real-world deployment experience |
| Behavioral Signals     | Recruiter responsiveness         |

Additional penalties are applied to:

* Suspicious profiles
* Non-AI career paths
* Excessive notice periods

---

## Repository Structure

```text
.
├── src
│   ├── load_data.py
│   ├── constants.py
│   ├── feature_engineering.py
│   ├── scoring.py
│   ├── reasoning.py
│   ├── rank.py
│   ├── export_submission.py
│   ├── analyze_top100.py
│   ├── debug_top_candidate.py
│   ├── test_features.py
│   ├── test_score.py
│   └── test_reasoning.py
│
├── outputs
│   └── team_Purusharth.csv
│
├── submission_metadata.yaml
├── validate_submission.py
├── requirements.txt
├── app.py
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Redrob-Challenge-V2
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Ranking Pipeline

Generate ranked candidates:

```bash
python src/export_submission.py
```

Output:

```text
outputs/team_Purusharth.csv
```

---

## Validate Submission

```bash
python validate_submission.py outputs/team_Purusharth.csv
```

Expected result:

```text
Submission is valid.
```

---

## Candidate Analysis

Analyze ranking distribution:

```bash
python src/analyze_top100.py
```

This provides:

* Top job titles
* Average experience
* Most common skills
* Ranking quality insights

---

## Streamlit Demo

Launch local demo:

```bash
streamlit run app.py
```

The application allows reviewers to:

* View top-ranked candidates
* Inspect candidate scores
* Explore profile summaries

---

## Performance

Dataset Size:

* ~100,000 candidate profiles

Execution Characteristics:

* CPU only
* No external APIs
* Deterministic ranking
* Local execution

---

## Future Improvements

Potential enhancements include:

* Learning-to-rank models
* Embedding-based semantic matching
* LLM-generated candidate reasoning
* Skill graph analysis
* Candidate similarity clustering

---

## Author

**Ayushman Parashar**
**Tushar Kumar**
**Ravi Shankar Gupta**
**Mantu Kumar Yadav**


B.Tech Computer Science & Engineering

Chaibasa Engineering College

---

## License

This project was developed for educational and hackathon purposes.
