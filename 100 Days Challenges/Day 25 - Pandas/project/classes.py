# Our Classes for the game
import turtle as t

NUMBER_STATES = 50

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.hideturtle()
        self.goto(210.0, 265.0)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f'the score is: {self.score} out of {NUMBER_STATES}', align= 'center', font=('Arial', '18', 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

class State_Writeer(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.hideturtle()

    def write_state(self, state, x_cor, y_cor):
        self.goto(x_cor, y_cor)
        self.write(f'{state}',  align= 'center', font=('Arial', '12', 'normal'))
