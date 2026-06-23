from load_data import candidate_generator
from reasoning import generate_reasoning

candidate = next(
    candidate_generator(
        "data/candidates.jsonl"
    )
)

print(
    generate_reasoning(candidate)
)