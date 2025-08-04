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
    },
    {
        "question": "Which function is used to get the length of a list in Python?",
        "options": ["A. length()", "B. size()", "C. len()", "D. count()"],
        "answer": "C"
    },
    {
        "question": "What is the output of: bool(0)?",
        "options": ["A. True", "B. False", "C. None", "D. Error"],
        "answer": "B"
    },
    {
        "question": "Which of these is not a valid Python loop?",
        "options": ["A. for", "B. while", "C. loop", "D. none of the above"],
        "answer": "C"
    },
    {
        "question": "What data structure does {} create?",
        "options": ["A. List", "B. Set", "C. Dictionary", "D. Tuple"],
        "answer": "C"
    },
    {
        "question": "Which of the following methods adds an item to a list?",
        "options": ["A. append()", "B. add()", "C. insert()", "D. extend()"],
        "answer": "A"
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
            print(f"\n🛑 Quiz stopped. Your score: {score}/{len(quiz_data)}")
            return

        if answer == q['answer']:
            score += 1
            print("✅ Correct!")
        else:
            print(f"❌ Wrong! The correct answer is {q['answer']}. Your score: {score}/{len(quiz_data)}\n")

    print(f"🎉 Quiz completed! Final score: {score}/{len(questions)}")
play_quiz(quiz_data)