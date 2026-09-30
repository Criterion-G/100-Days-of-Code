import turtle as t
import random as rng

# create the objects
timmy = t.Turtle()
screen = t.Screen()
screen.bgcolor('grey20')
t.colormode(255) # so pencolor accepts RGB tuples with values from 0 to 255
timmy.shape('classic')
timmy.color('MistyRose1')
timmy.speed('fastest')

def random_color():
    r = rng.randint(100, 255)
    g = rng.randint(100, 255)
    b = rng.randint(100, 255)
    return (r, g, b) # returns a tuple, which can never be edited once returned.

# the challenge is to create a Spirograph
def draw_spiro(size_of_gap):
    for _ in range (int(360 / size_of_gap)):
        timmy.pencolor(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spiro(10)

screen.exitonclick()

# this probably the easiest. the main goal of this is to teach us that documentations can be really useful.
