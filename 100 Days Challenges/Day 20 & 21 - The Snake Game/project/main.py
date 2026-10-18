import turtle as t
import random as rng
import time
import snake as s

# create the screen object
screen = t.Screen()
screen.setup(width= 600, height= 600) # keyword arguments are better than poistional for readability
screen.bgcolor('grey20')
screen.title('Snake Eeater')
screen.tracer(0)

# create the snake object
snake = s.Snake()
food = s.Food()
scoreboard = s.ScoreBoard()

screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()
    screen.onkeypress(fun= snake.up, key= 'Up')
    screen.onkeypress(fun= snake.down, key= 'Down')
    screen.onkeypress(fun= snake.left, key= 'Left')
    screen.onkeypress(fun= snake.right, key= 'Right')
    # colision with food
    if snake.seg_1.distance(food) < 10:
        food.location()
        scoreboard.increase_score()
        snake.grow()
    if snake.seg_1.xcor() > 290 or snake.seg_1.xcor() < -290 or snake.seg_1.ycor() > 290 or snake.seg_1.ycor() < -290: # wall collision.
        game_is_on = False
        scoreboard.game_over()
    if snake.head_in_tail():
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
