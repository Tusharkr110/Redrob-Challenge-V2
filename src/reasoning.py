IMPORTANT_SKILLS = {
    "Embeddings",
    "Pinecone",
    "Weaviate",
    "Qdrant",
    "FAISS",
    "Vector Search",
    "Learning to Rank",
    "Python",
    "NLP",
    "Sentence Transformers",
    "OpenSearch",
    "pgvector",
    "Milvus",
    "BM25",
    "MLflow"
}


def generate_reasoning(candidate):

    profile = candidate.get("profile", {})

    title = profile.get(
        "current_title",
        "Unknown"
    )

    years = profile.get(
        "years_of_experience",
        0
    )

    company = profile.get(
        "current_company",
        ""
    )

    skills = []

    for skill in candidate.get(
            "skills", []):

        skill_name = skill.get(
            "name", ""
        )

        if skill_name in IMPORTANT_SKILLS:
            skills.append(skill_name)

    skills = skills[:3]

    skill_text = (
        ", ".join(skills)
        if skills
        else "relevant ML skills"
    )

    reasoning = (
        f"{title} with {years} years of experience"
    )

    if company:
        reasoning += (
            f" currently at {company}"
        )

    reasoning += (
        f". Strong match for Redrob's AI ranking and retrieval focus through "
        f"{skill_text}."
    )

    return reasoning