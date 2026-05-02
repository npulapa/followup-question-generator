def build_prompt(previous_question, candidate_answer, evaluation, intent):
    return f"""
You are an AI interviewer.

Previous Question: {previous_question}
Candidate Answer: {candidate_answer}

Evaluation:
- correctness: {evaluation.get("correctness")}
- missing_concepts: {evaluation.get("missing_concepts")}
- mistakes: {evaluation.get("mistakes")}

Generate ONE follow-up question.

Rules:
- Stay in same topic
- Do NOT repeat question
- Intent: {intent}

Return JSON:
{{
  "follow_up_question": "...",
  "intent": "{intent}"
}}
"""
