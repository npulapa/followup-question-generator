from logic import decide_intent
from prompt import build_prompt
import json

def generate_followup(data):
    previous_question = data["previous_question"]
    candidate_answer = data["candidate_answer"]
    evaluation = data["evaluation"]

    intent = decide_intent(evaluation)
    prompt = build_prompt(previous_question, candidate_answer, evaluation, intent)

    # TEMP (without API)
    response = {
        "follow_up_question": "Sample generated question based on logic",
        "intent": intent
    }

    return response


if __name__ == "__main__":
    sample_input = {
        "previous_question": "What is inheritance in OOP?",
        "candidate_answer": "It is something in programming.",
        "evaluation": {
            "correctness": "weak",
            "missing_concepts": ["parent class", "child class"]
        }
    }

    result = generate_followup(sample_input)
    print(json.dumps(result, indent=2))
