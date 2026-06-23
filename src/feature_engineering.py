from constants import *
TARGET_SKILLS = {
    "python",
    "machine learning",
    "deep learning",
    "nlp",
    "llm",
    "rag",
    "retrieval",
    "ranking",
    "embeddings",
    "sentence-transformers",
    "vector database",
    "pinecone",
    "weaviate",
    "qdrant",
    "milvus",
    "faiss",
    "elasticsearch",
    "opensearch",
    "evaluation",
    "ndcg",
    "mrr",
    "map"
}


def normalize(text):
    if not text:
        return ""

    return str(text).lower().strip()


def extract_features(candidate):

    profile = candidate.get("profile", {})
    skills = candidate.get("skills", [])
    signals = candidate.get("redrob_signals", {})

    summary = profile.get("summary", "")

    headline = profile.get("headline", "")

    career_text = ""

    for job in candidate.get("career_history", []):
        career_text += " "
        career_text += job.get("description", "")
        career_text += " "
        career_text += job.get("title", "")

    full_text = (
        headline + " " +
        summary + " " +
        career_text
    ).lower()

    

   
    years = profile.get("years_of_experience", 0)

    feature = {}

    # Experience
    feature["years_exp"] = years

    # Skill Match
    skill_names = {
        normalize(skill.get("name"))
        for skill in skills
    }

    matched = skill_names.intersection(TARGET_SKILLS)

    feature["skill_match_count"] = len(matched)

    # Engagement Signals
    feature["response_rate"] = signals.get(
        "recruiter_response_rate", 0
    )

    feature["interview_completion"] = signals.get(
        "interview_completion_rate", 0
    )

    feature["github_score"] = signals.get(
        "github_activity_score", -1
    )

    feature["open_to_work"] = int(
        signals.get("open_to_work_flag", False)
    )

    feature["notice_period"] = signals.get(
        "notice_period_days", 180
    )

    feature["retrieval_count"] = count_matches(
        full_text,
        RETRIEVAL_TERMS
    )

    feature["embedding_count"] = count_matches(
        full_text,
        EMBEDDING_TERMS
    )

    feature["vector_db_count"] = count_matches(
        full_text,
        VECTOR_DB_TERMS
    )

    feature["llm_count"] = count_matches(
        full_text,
        LLM_TERMS
    )

    feature["eval_count"] = count_matches(
        full_text,
        EVAL_TERMS
    )

    feature["python_count"] = count_matches(
        full_text,
        PYTHON_TERMS
    )

    current_title = normalize(
        profile.get("current_title", "")
    )

    feature["title_match"] = int(
        current_title in AI_TITLES
    )

    feature["bad_title"] = int(
        current_title in BAD_TITLES
    )

    feature["production_count"] = count_matches(
        full_text,
        PRODUCTION_TERMS
    )

    retrieval_skill_count = 0

    for skill in skills:

        name = skill.get("name", "")

        if name in RETRIEVAL_SKILLS:
            retrieval_skill_count += 1

    feature["retrieval_skill_count"] = retrieval_skill_count

    # Count AI jobs

    ai_job_count = 0

    for job in candidate.get("career_history", []):

        title = normalize(
            job.get("title", "")
        )

        if title in GOOD_AI_TITLES:
            ai_job_count += 1

    feature["ai_job_count"] = ai_job_count


    # Detect suspicious profiles

    feature["suspicious_profile"] = int(
        feature["skill_match_count"] >= 8
        and ai_job_count == 0
    )

    vision_count = 0

    for skill in skills:

        if skill.get("name", "") in VISION_SKILLS:
            vision_count += 1

    feature["vision_count"] = vision_count

    feature["non_ai_title"] = int(
        current_title in NON_AI_TITLES
    )


    return feature
def count_matches(text, keywords):

    text = text.lower()

    count = 0

    for keyword in keywords:
        if keyword in text:
            count += 1

    return count