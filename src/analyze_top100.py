from collections import Counter

from load_data import candidate_generator
from feature_engineering import extract_features
from scoring import score_candidate

results = []

print("Loading candidates...")

for candidate in candidate_generator(
        "data/candidates.jsonl"):

    features = extract_features(candidate)

    score = score_candidate(features)

    results.append({
        "candidate": candidate,
        "score": score
    })

results.sort(
    key=lambda x: (
        -x["score"],
        x["candidate"]["candidate_id"]
    )
)

top100 = results[:100]

title_counter = Counter()
skill_counter = Counter()

experience_sum = 0

for row in top100:

    candidate = row["candidate"]

    profile = candidate["profile"]

    title = profile.get(
        "current_title",
        "Unknown"
    )

    title_counter[title] += 1

    experience_sum += profile.get(
        "years_of_experience",
        0
    )

    for skill in candidate.get(
            "skills", []):

        skill_counter[
            skill["name"]
        ] += 1

avg_exp = experience_sum / 100

print("\n=== TOP TITLES ===")

for title, count in title_counter.most_common(15):
    print(f"{title}: {count}")

print(
    f"\nAverage Experience: {avg_exp:.2f}"
)

print("\n=== TOP SKILLS ===")

for skill, count in skill_counter.most_common(20):
    print(f"{skill}: {count}")