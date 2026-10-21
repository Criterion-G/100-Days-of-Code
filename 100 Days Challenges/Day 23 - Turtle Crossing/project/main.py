import time
import random as rng
from turtle import Screen
import crossing_objects as co

# Our Screen Object
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('grey20')

# Our Constants
X_AXIS = 280
Y_AXIS = 280

# Our Objects
cars = []
for car in range(0, 16):
    car = co.CarManager()
    cars.append(car)

tim = co.Player()
score = co.ScoreBoard()

# Events
screen.listen()
screen.onkeypress(fun= tim.up, key= 'Up')
screen.onkeypress(fun= tim.down, key= 'Down')
screen.onkeypress(fun= tim.go_left, key= 'Left')
screen.onkeypress(fun= tim.go_right, key= 'Right')

# The Game Loop
game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.move()

    # Collisions
    for car in cars:
        if car.xcor() - 10 <= tim.xcor() and car.distance(tim) < 30:
            score.decrease_life()
            tim.reset_pos()

    # Crossing the Finish Line
    if tim.pos()[1] >= score.finsish_line:
        score.increase_score()
        tim.reset_pos()
        for car in cars:
            car.speed_increase()

    # Game Condition
    if score.lives <= 0:
        score.game_over()
        game_is_on = False

screen.exitonclick()
