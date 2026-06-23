import json

count = 0

with open("data/candidates.jsonl", "r", encoding="utf8") as f:
    for line in f:
        if line.strip():
            count += 1

print("Candidates:", count)