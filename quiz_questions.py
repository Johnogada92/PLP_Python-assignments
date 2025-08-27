import random

# Quiz questions and answers
quiz_questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "Which of these is NOT a Python data type?",
        "options": ["A. list", "B. tuple", "C. dictionary", "D. array"],
        "answer": "D"
    },
    {
        "question": "What is the output of: print(2 ** 3)?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 23"],
        "answer": "B"
    },
    {
        "question": "Which method is used to add an item to a list?",
        "options": ["A. append()", "B. add()", "C. insert()", "D. push()"],
        "answer": "A"
    },
    {
        "question": "How do you start a for loop in Python?",
        "options": ["A. for i in range:", "B. for i in range()", "C. for (i=0; i<10; i++)", "D. loop i from 1 to 10:"],
        "answer": "B"
    }
]

def run_quiz():
    print("🎮 Welcome to the Python Quiz Game!")
    print("-----------------------------------")
    print("Answer the questions by typing A, B, C, or D\n")
    
    score = 0
    random.shuffle(quiz_questions)  # Shuffle questions for variety
    
    for i, q in enumerate(quiz_questions, 1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(f"   {option}")
        
        # Get user answer with validation
        while True:
            user_answer = input("Your answer: ").upper().strip()
            if user_answer in ['A', 'B', 'C', 'D']:
                break
            print("Please enter A, B, C, or D")
        
        # Check if answer is correct
        if user_answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer is {q['answer']}\n")
    
    # Display final score
    print("📊 Quiz Complete!")
    print(f"Your final score: {score}/{len(quiz_questions)}")
    
    # Calculate percentage and give feedback
    percentage = (score / len(quiz_questions)) * 100
    if percentage == 100:
        print("🎉 Perfect! You're a Python expert!")
    elif percentage >= 70:
        print("👍 Great job! You know Python well!")
    elif percentage >= 50:
        print("😊 Good effort! Keep learning!")
    else:
        print("👏 Keep practicing! You'll improve!")

# Main game loop
while True:
    run_quiz()
    
    # Ask if user wants to play again
    play_again = input("\nWould you like to play again? (yes/no): ").lower().strip()
    if play_again not in ['yes', 'y']:
        print("Thanks for playing! 👋")
        break
    print("\n" + "="*50 + "\n")