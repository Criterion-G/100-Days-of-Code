import turtle as t
import random as rng

# create the objects
timmy = t.Turtle()
screen = t.Screen()
screen.bgcolor('grey20')
t.colormode(255) # so pencolor accepts RGB tuples with values from 0 to 255
timmy.shape('classic')
timmy.color('MistyRose1')

# the challenge is to create the random walk for timmy

# set the thickness of the lines and the speed of timmy
timmy.pensize(7)
timmy.speed('fastest')

# variables
# a list with colorstrings
RAND_COLORS = [
    'MistyRose1', 'LightPink', 'HotPink', 'PaleVioletRed1', 'plum1',
    'orchid1', 'MediumPurple1', 'LightSteelBlue1', 'SkyBlue1', 'LightSkyBlue',
    'CadetBlue1', 'aquamarine', 'PaleTurquoise1', 'DarkSeaGreen1', 'PaleGreen1',
    'khaki1', 'LightGoldenrod1', 'NavajoWhite1', 'LightSalmon1', 'coral1',
]

# a tuple with random RGB numbers

def random_color():
    r = rng.randint(100, 255)
    g = rng.randint(100, 255)
    b = rng.randint(100, 255)
    return (r, g, b) # returns a tuple, which can never be edited once returned.

# my solution
# def rand_direction(x):
#     if x == 1:
#         return timmy.right(90)
#     elif x == 2:
#         return timmy.left(90)
#     elif x == 3:
#         return None

# for _ in range(500):
#     rand_direction(rng.randint(1,3))
#     timmy.forward(10)
#     timmy.pencolor(rng.choice(RAND_COLORS))

# timmy.home()
# timmy.clear()

# her solution
directions = [0, 90, 180, 270]

# for _ in range(500):
#     timmy.setheading(rng.choice(directions))
#     timmy.forward(10)
#     timmy.pencolor(rng.choice(RAND_COLORS)) # with a predefined list

for _ in range(1000):
    timmy.setheading(rng.choice(directions))
    timmy.forward(20)
    timmy.pencolor(random_color()) # with a function that returns a tuple of rgb numbers

screen.exitonclick()
