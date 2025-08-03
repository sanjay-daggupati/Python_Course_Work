quiz_data = [
    {
        "question": "Which keyword is used to create a generator in Python?",
        "options": ["A. yield", "B. return", "C. def", "D. gen"],
        "answer": "A"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D"
    },
    {
        "question": "Which data type does not allow duplicate values?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to handle exceptions?",
        "options": ["A. raise", "B. try", "C. except", "D. catch"],
        "answer": "C"
    },
    {
        "question": "Which of the following is a mutable data type?",
        "options": ["A. string", "B. int", "C. list", "D. float"],
        "answer": "C"
    }
]

def question_generator(questions):
    for i, q in enumerate(questions):
        yield i, q

def play_quiz(questions):
    print("\n🎮 Welcome to the Python Quiz!")
    print("Type 'STOP' at any time to quit.\n")

    score = 0
    gen = question_generator(questions)

    for i, q in gen:
        print(f"Q{i + 1}: {q['question']}")
        for opt in q['options']:
            print(opt)

        answer = input("Your answer (A/B/C/D or STOP to quit): ").strip().upper()

        if answer == "STOP":
            print(f"\n🛑 Quiz stopped. Your score: {score}/{i}")
            return

        if answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {q['answer']}.\n")

    print(f"🎉 Quiz completed! Final score: {score}/{len(questions)}")
