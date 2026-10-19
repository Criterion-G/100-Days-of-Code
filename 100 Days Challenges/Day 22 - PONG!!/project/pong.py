# classes
import turtle as t
import random as rng

# Our constants
PADDLE_SPEED = 50
BALL_SPEED = 10
WALL = 280

# Our classes
class Paddle(t.Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len= 1, stretch_wid= 5)
        self.color('white')
        self.speed('fastest')
        self.goto(position, 0)
        self.x_move = PADDLE_SPEED
        self.y_move = PADDLE_SPEED

    def up(self):
        new_y = self.ycor()
        self.goto(self.xcor(), new_y + PADDLE_SPEED)

    def down(self):
        new_y = self.ycor()
        self.goto(self.xcor(), new_y + - PADDLE_SPEED)
    
    def computer_move(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)
        if self.ycor() >= WALL - 30:
            self.change_direction()
        if self.ycor() <= -WALL + 30:
            self.change_direction()

    def change_direction(self):
        self.y_move *= -1

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len= 1, stretch_wid= 1)
        self.color('white')
        self.speed('fastest')
        self.x_move = BALL_SPEED
        self.y_move = BALL_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

class ScoreBoard(t.Turtle):
    def __init__(self, p1_side):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 275)
        # label each side of the screen with the player standing there
        if p1_side == 'left':
            self.left_label, self.right_label = 'P1', 'P2'
        else:
            self.left_label, self.right_label = 'P2', 'P1'
        self.left_score = 0
        self.right_score = 0
        self.update_scorboard()


    def update_scorboard(self):
        self.write(f'{self.left_label} Score: {self.left_score} - {self.right_label} Score: {self.right_score}', move= False, align= 'center', font= ('Arial', '14', 'bold'))

    def increase_score(self, side):
        if side == 'left':
            self.left_score += 1
        else:
            self.right_score += 1
        self.clear()
        self.update_scorboard()

    def game_over():
        pass
