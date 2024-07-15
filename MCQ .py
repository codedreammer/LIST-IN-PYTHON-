# List of questions
questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "What is the largest mammal?",
    "Who wrote 'To Kill a Mockingbird'?"
]

# List of options for each question
options = [
    ["a) Berlin", "b) Madrid", "c) Paris", "d) Rome"],
    ["a) Earth", "b) Mars", "c) Jupiter", "d) Saturn"],
    ["a) Elephant", "b) Blue Whale", "c) Giraffe", "d) Great White Shark"],
    ["a) Harper Lee", "b) J.K. Rowling", "c) Ernest Hemingway", "d) Mark Twain"]
]

# List of correct answers
correct_answers = ["c", "b", "b", "a"]


# Function to run the quiz
def run_quiz(questions, options, correct_answers):
    score = 0
    for i in range(len(questions)):
        print(f"Q{i+1}: {questions[i]}")
        for option in options[i]:
            print(option)
        answer = input("Your answer: ").lower()
        if answer == correct_answers[i]:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is {correct_answers[i]}\n")
    print(f"Your final score is {score}/{len(questions)}/'Well Done!'")
    if score == 4:
        print("Well Done!")

    if score == 0:
        print("please try AGAIN!")

# Run the quiz
run_quiz(questions, options, correct_answers)