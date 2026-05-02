def decide_intent(evaluation):
    correctness = evaluation.get("correctness", "").lower()

    if correctness in ["empty", "weak"]:
        return "clarification"
    elif correctness == "partial":
        return "deep_dive"
    elif correctness == "incorrect":
        return "correction"
    elif correctness == "irrelevant":
        return "clarification"
    else:
        return "deep_dive"
