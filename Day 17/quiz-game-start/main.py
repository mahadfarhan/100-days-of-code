from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    temp_text = item["question"]
    temp_answer = item["correct_answer"]
    temp_q = Question(temp_text, temp_answer)
    question_bank.append(temp_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
