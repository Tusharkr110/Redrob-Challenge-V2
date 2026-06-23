import csv

from load_data import candidate_generator
from feature_engineering import extract_features
from scoring import score_candidate
from reasoning import generate_reasoning


results = []

print("Scoring candidates...")

for candidate in candidate_generator(
        "data/candidates.jsonl"):

    features = extract_features(candidate)

    score = score_candidate(features)

    results.append({
        "candidate_id": candidate["candidate_id"],
        "score": score,
        "candidate": candidate
    })

print("Sorting...")

results.sort(
    key=lambda x: (
        -x["score"],
        x["candidate_id"]
    )
)


top100 = results[:100]

output_file = "outputs/team_Purusharth.csv"

with open(
        output_file,
        "w",
        newline="",
        encoding="utf-8") as f:

    writer = csv.writer(f)

    writer.writerow(
        [
            "candidate_id",
            "rank",
            "score",
            "reasoning"
        ]
    )

    for rank, row in enumerate(
            top100,
            start=1):

        reasoning = generate_reasoning(
            row["candidate"]
        )

        writer.writerow([
            row["candidate_id"],
            rank,
            row["score"],
            reasoning
        ])

print(
    f"Submission written to {output_file}"
)