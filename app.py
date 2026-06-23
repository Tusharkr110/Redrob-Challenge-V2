import sys 
import json
sys.path.append("src")

import pandas as pd
import streamlit as st


from feature_engineering import extract_features
from scoring import score_candidate

st.title("Redrob Candidate Ranking Demo")
st.markdown("""
Upload a candidate dataset in JSONL format.

The system will:
1. Parse candidate profiles
2. Extract features
3. Score candidates
4. Display the Top 100 candidates
""")

uploaded_file = st.file_uploader(
    "Upload candidates.jsonl",
    type=["jsonl"]
)

if uploaded_file is None:
    st.info("Please upload a JSONL file to continue.")
    st.stop()

candidates = []

for line in uploaded_file:

    line = line.decode("utf-8").strip()

    if not line:
        continue

    candidates.append(
        json.loads(line)
    )
@st.cache_data
def rank_candidates(candidates):

    results = []

    for candidate in candidates:

        features = extract_features(candidate)

        score = score_candidate(features)

        profile = candidate.get("profile", {})

        results.append({
            "candidate_id": candidate["candidate_id"],
            "score": score,
            "title": profile.get(
                "current_title",
                ""
            ),
            "experience": profile.get(
                "years_of_experience",
                0
            ),
            "candidate": candidate
        })

    results.sort(
        key=lambda x: (
            -x["score"],
            x["candidate_id"]
        )
    )

    return results[:100]


st.set_page_config(
    page_title="Redrob Candidate Ranker",
    layout="wide"
)

st.title("Redrob Candidate Ranking Demo")

top_candidates = rank_candidates(candidates)

df = pd.DataFrame([
    {
        "Rank": idx + 1,
        "Candidate ID": row["candidate_id"],
        "Score": row["score"],
        "Title": row["title"],
        "Experience": row["experience"]
    }
    for idx, row in enumerate(top_candidates)
])

st.dataframe(
    df,
    use_container_width=True
)

selected_id = st.selectbox(
    "Select Candidate",
    df["Candidate ID"]
)

candidate = next(
    x for x in top_candidates
    if x["candidate_id"] == selected_id
)

profile = candidate["candidate"]["profile"]

st.subheader("Profile")

st.write(
    profile.get("headline", "")
)

st.write(
    profile.get("summary", "")
)