import turtle as t
import pong as p
import random as rng
import time

# The Screen
screen = t.Screen()
screen.bgcolor('black')
screen.setup(width= 800, height= 600)
screen.title('PONG!!')
screen.tracer(0)

# Our Constants
PADDLE_POSITION = 350
WALL = 280
GOAL = 370

# Our Variables
p1_pos = input('please select your position, left or right? ')[0].lower()

if p1_pos == 'r':
    p1_side = 'right'
    p1_pos = PADDLE_POSITION
    p2_pos = -PADDLE_POSITION
else:
    p1_side = 'left'
    p1_pos = -PADDLE_POSITION
    p2_pos = PADDLE_POSITION

# Our Game Objects
paddle_1 = p.Paddle(p1_pos)
paddle_2 = p.Paddle(p2_pos)
ball = p.Ball()
scoreboard = p.ScoreBoard(p1_side)

# Our Listening and Input
screen.listen()
screen.onkeypress(fun= paddle_1.up, key= 'Up')
screen.onkeypress(fun= paddle_1.down, key= 'Down')
screen.onkeypress(fun= paddle_2.up, key= 'w')
screen.onkeypress(fun= paddle_2.down, key= 's')

# The Game Loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # collisions detection:
    # collision with wall
    if ball.ycor() >= WALL or ball.ycor() <= -WALL:
        ball.wall_bounce()
    # collision with either paddle, whichever side it's on
    for paddle in (paddle_1, paddle_2):
        if abs(ball.xcor()) >= PADDLE_POSITION - 10 and ball.distance(paddle) <= 50:
            ball.paddle_bounce()

    # scoring: a ball past one goal is a point for the player on the other side
    if ball.xcor() > GOAL:
        scoreboard.increase_score('left')
        ball.goto(0,0)
        time.sleep(0.5)
    if ball.xcor() < -GOAL:
        scoreboard.increase_score('right')
        ball.goto(0,0)
        time.sleep(0.5)

screen.exitonclick()
