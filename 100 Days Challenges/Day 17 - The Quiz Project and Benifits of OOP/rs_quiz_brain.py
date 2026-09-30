# the class for the logic of the game

class QuizBrain:
    def __init__(self, question_list):
        self.question_num = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_num < len(self.question_list) # we don't need an if statement here as this expression evaluates itself and returns True or False by itself

    def check_answer(self, user_answer, correct_answer):
        return user_answer.lower() == correct_answer.lower() # same as the above, will return either True or Flase, no if needed

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f'Q{self.question_num}: {current_question.question} (True/False) ')
        if self.check_answer(user_answer, current_question.answer):
            self.score += 1
            print(f'your answer is correct, your current score is {self.score}')
        else:
            print(f'wrong answer, better luck in the next question. your current score is {self.score}')
