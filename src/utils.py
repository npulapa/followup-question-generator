import re


def clean_text(text):
    """
    Normalize text input (remove extra spaces, lowercase)
    """
    if not text:
        return ""
    return re.sub(r"\s+", " ", text.strip())


def is_empty_answer(answer):
    """
    Check if candidate answer is empty or meaningless
    """
    if not answer:
        return True

    answer = answer.strip().lower()

    return answer in ["", "i don't know", "dont know", "no idea", "idk"]


def is_irrelevant_answer(previous_question, answer):
    """
    Basic keyword overlap check (simple heuristic)
    """
    if not answer:
        return False

    q_words = set(previous_question.lower().split())
    a_words = set(answer.lower().split())

    overlap = q_words.intersection(a_words)

    return len(overlap) < 2  # threshold can be tuned


def validate_input(data):
    """
    Ensure required fields exist
    """
    required_fields = ["previous_question", "candidate_answer", "evaluation"]

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    return True


def avoid_repetition(previous_question, follow_up_question):
    """
    Prevent repeating same question
    """
    prev = clean_text(previous_question)
    follow = clean_text(follow_up_question)

    return prev != follow


def extract_keywords(evaluation):
    """
    Extract important concepts for better prompting
    """
    keywords = []

    if "missing_concepts" in evaluation and evaluation["missing_concepts"]:
        keywords.extend(evaluation["missing_concepts"])

    if "mistakes" in evaluation and evaluation["mistakes"]:
        keywords.extend(evaluation["mistakes"])

    return keywords


def enrich_prompt_with_keywords(prompt, keywords):
    """
    Add keywords into prompt for better LLM response
    """
    if not keywords:
        return prompt

    keyword_str = ", ".join(keywords)

    return prompt + f"\nFocus on these concepts: {keyword_str}\n"
