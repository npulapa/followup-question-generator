import json
from logic import decide_intent
from prompt import build_prompt
from utils import (
    validate_input,
    extract_keywords,
    enrich_prompt_with_keywords,
    is_empty_answer,
    is_irrelevant_answer,
    clean_text
)


def generate_followup(data):
    validate_input(data)

    previous_question = clean_text(data["previous_question"])
    candidate_answer = clean_text(data["candidate_answer"])
    evaluation = data["evaluation"]

    # Handle edge cases
    if is_empty_answer(candidate_answer):
        evaluation["correctness"] = "empty"

    elif is_irrelevant_answer(previous_question, candidate_answer):
        evaluation["correctness"] = "irrelevant"

    # Decide intent
    intent = decide_intent(evaluation)

    # Build prompt (for future AI use)
    prompt = build_prompt(previous_question, candidate_answer, evaluation, intent)

    # Enrich prompt
    keywords = extract_keywords(evaluation)
    prompt = enrich_prompt_with_keywords(prompt, keywords)

    # Rule-based fallback (no API needed)
    follow_up_question = generate_rule_based_question(
        previous_question,
        evaluation,
        intent
    )

    return {
        "follow_up_question": follow_up_question,
        "intent": intent
    }


def generate_rule_based_question(previous_question, evaluation, intent):
    missing = evaluation.get("missing_concepts", [])
    mistakes = evaluation.get("mistakes", [])

    if intent == "clarification":
        if missing:
            return f"Can you explain what {missing[0]} means in this context?"
        return "Can you explain your answer more clearly?"

    elif intent == "deep_dive":
        if missing:
            return f"Can you elaborate on how {missing[0]} works?"
        return "Can you go deeper into your explanation?"

    elif intent == "correction":
        if mistakes:
            return f"It seems there is confusion about {mistakes[0]}. Can you reconsider your answer?"
        return "Are you sure about your answer? Can you re-evaluate it?"

    return "Can you clarify your response?"


if __name__ == "__main__":

    sample_input = {
        "previous_question": "What is inheritance in OOP?",
        "candidate_answer": "It is something in programming.",
        "evaluation": {
            "correctness": "weak",
            "missing_concepts": ["parent class", "child class"],
            "mistakes": []
        }
    }

    result = generate_followup(sample_input)

    print("\n=== FOLLOW-UP RESULT ===")
    print(json.dumps(result, indent=2))
