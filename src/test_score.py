from load_data import candidate_generator
from feature_engineering import extract_features
from scoring import score_candidate

candidate = next(
    candidate_generator("data/candidates.jsonl")
)

features = extract_features(candidate)

print(score_candidate(features))