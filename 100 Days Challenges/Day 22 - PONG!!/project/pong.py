# classes
import turtle as t
import random as rng

# Our constants
PADDLE_SPEED = 20

# Our classes
class Paddle(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len= 1, stretch_wid= 5)
        self.color('white')
        self.speed('fastest')

    def up(self):
        new_y = self.ycor()
        self.goto(self.xcor(), new_y + PADDLE_SPEED)

    def down(self):
        new_y = self.ycor()
        self.goto(self.xcor(), new_y + - PADDLE_SPEED)

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len= 1, stretch_wid= 1)
        self.color('white')
        self.speed('fastest')

class ScorBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 275)
        self.p1_score = 0
        self.p2_score = 0
        self.write(f'P1 Score: {self.p1_score} - P2 Score: {self.p2_score}', move= False, align= 'center', font= ('Arial', '14', 'bold'))

    def update_score():
        pass
