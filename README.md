# 🤖 Follow-up Question Generator (AI Interview System)

## 📌 Overview

This project generates intelligent **follow-up questions** based on a candidate’s answer during an interview.
It helps simulate **adaptive interviewing**, where the next question depends on how well the candidate performed.

---

## 🎯 Objective

* Generate **context-aware follow-up questions**
* Improve **depth of evaluation**
* Stay within the **same topic**
* Adapt based on answer quality

---

## 🧠 How It Works

### 🔹 Input

```json
{
  "previous_question": "...",
  "candidate_answer": "...",
  "evaluation": {
    "correctness": "weak | partial | incorrect | empty | irrelevant",
    "missing_concepts": [],
    "mistakes": []
  }
}
```

---

### 🔹 Output

```json
{
  "follow_up_question": "...",
  "intent": "clarification | deep_dive | correction"
}
```

---

## ⚙️ Intent Mapping Logic

| Answer Quality | Intent                           |
| -------------- | -------------------------------- |
| empty / weak   | clarification                    |
| partial        | deep_dive                        |
| incorrect      | correction                       |
| irrelevant     | clarification (with redirection) |

---

## 🛠️ Features

* ✅ Adaptive questioning logic
* ✅ Context-aware (same topic)
* ✅ Handles edge cases (empty, irrelevant answers)
* ✅ Rule-based fallback (no API required)
* ✅ Clean modular code structure
* ✅ Easy to integrate into larger interview systems

---

## 📁 Project Structure

```
followup-question-generator/
│
├── src/
│   ├── main.py        # Main execution file
│   ├── logic.py       # Intent decision logic
│   ├── prompt.py      # Prompt builder (for future AI use)
│   └── utils.py       # Helper functions
│
├── tests/
│   └── test_cases.json
│
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/followup-question-generator.git
cd followup-question-generator
```

### 2. Run the project

```bash
cd src
python main.py
```

---

## 🧪 Sample Output

```json
{
  "follow_up_question": "Can you explain what parent class means in this context?",
  "intent": "clarification"
}
```

---

## 🚨 Constraints

* ❌ No repetition of previous question
* ❌ No topic switching
* ❌ Must remain context-aware

---

## 🔥 Future Improvements

* 🔗 Integrate OpenAI API for dynamic question generation
* 📊 Add scoring & evaluation system
* 🧠 Multi-step follow-up conversations
* 📝 Generate full interview reports

---

## 👩‍💻 Author

Nandini Pulapa

---

## ⭐ Contribution

Feel free to fork this repo and improve the system!

---
