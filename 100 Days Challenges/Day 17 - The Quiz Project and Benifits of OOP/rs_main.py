# the main file for the quiz game
from rs_data import question_data
from rs_question_model import Question
from rs_quiz_brain import QuizBrain

questions_bank = []

# creat a question object for each question and its answer from question_data and append it to the list
for question in question_data:
    questions_bank.append(Question(question['text'], question['answer']))

quiz = QuizBrain(questions_bank)

while quiz.still_has_questions():

    quiz.next_question()

print(f'the quiz game has ended and your score is ( {quiz.score} / {len(quiz.question_list)} )')

# day 17 complete!
