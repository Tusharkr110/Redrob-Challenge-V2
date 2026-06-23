from load_data import candidate_generator

target_id = input("Candidate ID: ")

for candidate in candidate_generator(
        "data/candidates.jsonl"):

    if candidate["candidate_id"] == target_id:

        print("\nID:")
        print(candidate["candidate_id"])

        print("\nHeadline:")
        print(candidate["profile"]["headline"])

        print("\nCurrent Title:")
        print(candidate["profile"]["current_title"])

        print("\nExperience:")
        print(candidate["profile"]["years_of_experience"])

        print("\nSummary:")
        print(candidate["profile"]["summary"])

        print("\nSkills:")

        for skill in candidate["skills"]:
            print("-", skill["name"])

        print("\nCareer History:")

        for job in candidate["career_history"]:
            print(
                job["title"],
                "|",
                job["company"]
            )

        break