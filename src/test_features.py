from load_data import candidate_generator
from feature_engineering import extract_features

candidate = next(
    candidate_generator("data/candidates.jsonl")
)

features = extract_features(candidate)

for key, value in features.items():
    print(key, ":", value)