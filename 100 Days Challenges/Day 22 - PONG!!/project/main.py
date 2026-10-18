import turtle as t
import pong as p
import random as rng

# The Screen
screen = t.Screen()
screen.bgcolor('black')
screen.setup(width= 800, height= 600)
screen.title('PONG!!')
screen.tracer(0)

# Our constants
RIGHT_X_AXIS = 350
LEFT_Y_AXIS = -350

# Our Game objects
paddle_1 = p.Paddle()
paddle_2 = p.Paddle()
ball = p.Ball()
scoreboard = p.ScorBoard()

# Selecting the starting position
pos_select = input('please select your starting position, right or left? ')[0].lower()
if pos_select == 'r':
    paddle_1.goto(RIGHT_X_AXIS, 0)
    paddle_2.goto(LEFT_Y_AXIS, 0)
else:
    paddle_1.goto(LEFT_Y_AXIS, 0)
    paddle_2.goto(RIGHT_X_AXIS, 0)

# the game loop
game_is_on = True
while game_is_on:
    screen.update()
    screen.listen()
    screen.onkeypress(fun= paddle_1.up, key= 'Up')
    screen.onkeypress(fun= paddle_1.down, key= 'Down')

screen.exitonclick()
