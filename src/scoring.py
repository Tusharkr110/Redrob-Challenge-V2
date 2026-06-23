def score_candidate(features):

    score = 0

    years = features["years_exp"]

    ideal = 7

    score += max(
        0,
        25 - abs(years - ideal) * 3
    )
    

    score += features["skill_match_count"] * 3

    score += features["retrieval_count"] * 8

    score += features["embedding_count"] * 8

    score += features["vector_db_count"] * 8

    score += features["eval_count"] * 10

    score += features["python_count"] * 5

    score += features["llm_count"] * 3

    score += features["response_rate"] * 15

    score += features["interview_completion"] * 10

    score += features["open_to_work"] * 5

    score += features["title_match"] * 25

    score -= features["bad_title"] * 30

    score += features["production_count"] * 8

    score += features["ai_job_count"] * 8

    score -= features["suspicious_profile"] * 25

    score += features["retrieval_skill_count"] * 3

    score -= features["vision_count"] * 2

    score -= features["non_ai_title"] * 40

    github = features["github_score"]

    if github > 0:
        score += min(github / 10, 10)

    notice = features["notice_period"]

    if notice > 120:
        score -= 10

    return round(min(score, 100),3)