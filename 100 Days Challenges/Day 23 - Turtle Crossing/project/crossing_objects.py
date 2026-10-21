# Our Turtle Crossing Game Classes
import turtle as t
import random as rng

# Car Constants
# Chosen for legibility on the 'grey20' (#333333) background:
# every one clears a 4.2:1 contrast ratio against it.
COLORS = [
    "tomato",          # #ff6347  4.3:1   red
    "orange",          # #ffa500  6.4:1   orange
    "gold",            # #ffd700  9.0:1   yellow
    "yellowgreen",     # #9acd32  6.7:1   lime
    "mediumseagreen",  # #3cb371  4.7:1   green
    "turquoise",       # #40e0d0  7.7:1   cyan
    "cornflowerblue",  # #6495ed  4.3:1   blue
    "orchid",          # #da70d6  4.4:1   purple
    "hotpink",         # #ff69b4  4.8:1   pink
    "wheat",           # #f5deb3  9.6:1   cream
]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Screen Constants
X_AXIS = 280
Y_AXIS = 260
LANES = []
for _ in range(-Y_AXIS + 40, Y_AXIS, 80):
    LANES.append(_)
COLUMNS = []
for _ in range(-X_AXIS + 40, X_AXIS, 80):
    COLUMNS.append(_)

# Player Constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
DEFAULT_LIFE = 5
FINISH_LINE_Y = 280
FINISH_LINE_X = 280

# Scoreboard Constants
FONT = ("Courier", 14, "normal")
SCORE_POSITION = (-X_AXIS + 20, Y_AXIS - 20)

# Our Classes
class CarManager(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color(rng.choice(COLORS))
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid= 1, stretch_len= 2.5)
        self.move_speed = STARTING_MOVE_DISTANCE
        self.starting_pos()

    def move(self):
        self.forward(self.move_speed)
        if self.pos()[0] > X_AXIS + 40:
            self.set_pos()

    def speed_increase(self):
        self.move_speed += MOVE_INCREMENT

    def starting_pos(self):
        self.goto(rng.choice(COLUMNS), rng.choice(LANES))

    def set_pos(self):
        self.goto(-320, rng.choice(LANES))

class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('white')
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.speed('fastest')

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
    def go_left(self):
        self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())
    def go_right(self):
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    def reset_pos(self):
        self.goto(STARTING_POSITION)

class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.finsish_line = FINISH_LINE_Y
        self.lives = DEFAULT_LIFE
        self.score = 0
        self.refresh()

    def draw_finish(self):
        self.goto(-FINISH_LINE_X - 20, FINISH_LINE_Y)
        self.pendown()
        self.goto(FINISH_LINE_X + 20, FINISH_LINE_Y)
        self.penup()

    def refresh(self):
        self.clear()
        self.draw_finish()
        self.update_score()

    def decrease_life(self):
        self.lives -= 1
        self.refresh()

    def increase_score(self):
        self.score += 1
        self.refresh()

    def update_score(self):
        self.goto(SCORE_POSITION)
        self.write(f'current score: {self.score} - current lives: {self.lives}', align= 'left', font= FONT)
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f'GAME OVER! YOUR SCORE: {self.score}. ggs!', align= 'center', font= FONT)




def main():
    pass
# this guardrail works only if we put anything that excutes into the main function.
# for now we don't have anything to execute in this module so this guardrail isn't needed. Good practice to do it anyway.
if __name__ == '__main__':
    main()
