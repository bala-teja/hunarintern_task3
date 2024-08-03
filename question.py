questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"}
]
def run_quiz():
    score = 0
    for idx, q in enumerate(questions):
        print(f"Question {idx + 1}: {q['question']}")
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == q['answer'].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {q['answer']}.\n")

    print(f"Your final score is {score} out of {len(questions)}.")
run_quiz()
