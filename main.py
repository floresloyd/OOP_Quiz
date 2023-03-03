from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def quiz():
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    my_quiz_brain = QuizBrain(question_bank)
    while my_quiz_brain.still_has_questions():
        my_quiz_brain.next_question()
    print()
    print("You've completed the quiz!")
    print(f"Your final score was: {my_quiz_brain.score}/{my_quiz_brain.question_number}")


quiz()

# MODULARITY - Split all function in different files