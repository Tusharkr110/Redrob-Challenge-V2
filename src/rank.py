from load_data import candidate_generator
from feature_engineering import extract_features
from scoring import score_candidate

results = []

for candidate in candidate_generator(
        "data/candidates.jsonl"):

    features = extract_features(candidate)

    score = score_candidate(features)

    results.append({
        "candidate_id": candidate["candidate_id"],
        "score": score,
        "candidate": candidate
    })

results.sort(
    key=lambda x: (
        -x["score"],
        x["candidate_id"]
    )
)

top100 = results[:100]

# for row in top100:
#     print(row)