questions = [
    {
        "question": "What is the capital city of france?",
        "choices":  ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "correct_answer":  "C"
    },
    {
        "question": "Which planet is known as the red planet?",
        "choices": ["A) Earth", "B) Venus", "C) Jupiter", "D) Mars"],
        "correct_answer": "D"
    },
    {
        "question": "What is the largest ocean on earth?",
        "choices": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
        "correct_answer": "D"
    }, 
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "choices": ["A) Mark Twain", "B) Harper Lee", "C) J.K. Rowling", "D) Jane Austen"],
        "correct_answer": "B"
    }
]

score = 0

def ask_question(question_data):
    global score
    print(question_data["question"])
    for choice in question_data["choices"]:
        print(choice)
    
    answer = input("Enter your answer (A, B, C, or D): ").upper()
   
    if answer == question_data["correct_answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {question_data['correct_answer']}\n")

for question in questions:
    ask_question(question)

print(f"Your final score is {score}/{len(questions)}.")