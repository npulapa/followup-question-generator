import re


def clean_text(text):
    if not text:
        return ""
    return re.sub(r"\s+", " ", text.strip())


def is_empty_answer(answer):
    if not answer:
        return True

    answer = answer.strip().lower()
    return answer in ["", "i don't know", "dont know", "no idea", "idk"]


def is_irrelevant_answer(previous_question, answer):
    if not answer:
        return False

    q_words = set(previous_question.lower().split())
    a_words = set(answer.lower().split())

    overlap = q_words.intersection(a_words)
    return len(overlap) < 2


def validate_input(data):
    required_fields = ["previous_question", "candidate_answer", "evaluation"]

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    return True


def extract_keywords(evaluation):
    keywords = []

    if evaluation.get("missing_concepts"):
        keywords.extend(evaluation["missing_concepts"])

    if evaluation.get("mistakes"):
        keywords.extend(evaluation["mistakes"])

    return keywords


def enrich_prompt_with_keywords(prompt, keywords):
    if not keywords:
        return prompt

    keyword_str = ", ".join(keywords)
    return prompt + f"\nFocus on: {keyword_str}\n"
