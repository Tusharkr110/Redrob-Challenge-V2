import json


def candidate_generator(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line:
                yield json.loads(line)


if __name__ == "__main__":
    count = 0

    for candidate in candidate_generator("data/candidates.jsonl"):
        count += 1

        if count <= 3:
            print(candidate["candidate_id"])

    print(f"\nTotal Candidates: {count}")