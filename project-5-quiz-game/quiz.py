import random

# Quiz questions: each is a dictionary with question, options, and answer
questions = [
    {
        "question": "What is the output of print(2**3)?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 5"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. def", "C. function", "D. define"],
        "answer": "B"
    },
    {
        "question": "What data type is the result of: type(3.14)?",
        "options": ["A. int", "B. float", "C. str", "D. bool"],
        "answer": "B"
    },
    {
        "question": "Which of these is a mutable data type?",
        "options": ["A. tuple", "B. list", "C. str", "D. int"],
        "answer": "B"
    },
    {
        "question": "What is the correct way to start a comment in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. /* */"],
        "answer": "C"
    },
    {
        "question": "Which operator is used for floor division?",
        "options": ["A. /", "B. //", "C. %", "D. **"],
        "answer": "B"
    },
    {
        "question": "What is the output of len('Python')?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "B"
    },
    {
        "question": "Which of these is used to handle exceptions?",
        "options": ["A. try/except", "B. if/else", "C. for/while", "D. switch/case"],
        "answer": "A"
    },
    {
        "question": "What is the default value of a function parameter if not provided?",
        "options": ["A. None", "B. 0", "C. ''", "D. False"],
        "answer": "A"
    },
    {
        "question": "Which module is used to generate random numbers?",
        "options": ["A. math", "B. random", "C. os", "D. sys"],
        "answer": "B"
    }
]

# Shuffle questions for randomness
random.shuffle(questions)

score = 0

print("Welcome to the Python Quiz!\n")

for i, q in enumerate(questions, 1):
    print(f"Q{i}: {q['question']}")
    for option in q["options"]:
        print(option)
    answer = input("Your answer (A/B/C/D): ").upper()

    if answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {q['answer']}.\n")

print(f"Quiz finished! Your final score is {score}/10.")
