# a demo of how classes work with the Turtle Module
import turtle as t
import random as rng

# create the objects and set their attributes to what we want
timmy = t.Turtle()
screen = t.Screen()
screen.bgcolor('grey20')
timmy.shape('turtle')
timmy.color('MistyRose1')

# challenges for timmy the turtle

# challenge one, draw a sqaure. (alt + shift + up to repeat the first two lines)
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

timmy.home()
timmy.clear()
# challenge two, draw a dashed line
timmy.penup()
timmy.goto(-500,0)
timmy.pendown()
for _ in range(50):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
    timmy.forward(10)

timmy.home()
timmy.clear()
# challenge three, drawing different shapes.

def draw_shape(num_angles, space):
    for _ in range(num_angles):
        timmy.forward(space)
        timmy.right(360 / num_angles)
        timmy.forward(space)

angles = 3 # default
space = 30 # default
rand_colors = [
    'MistyRose1', 'LightPink', 'HotPink', 'PaleVioletRed1', 'plum1',
    'orchid1', 'MediumPurple1', 'LightSteelBlue1', 'SkyBlue1', 'LightSkyBlue',
    'CadetBlue1', 'aquamarine', 'PaleTurquoise1', 'DarkSeaGreen1', 'PaleGreen1',
    'khaki1', 'LightGoldenrod1', 'NavajoWhite1', 'LightSalmon1', 'coral1',
]
timmy.penup()
timmy.goto(0,300) # set the starting location up top
timmy.pendown()
timmy.speed('fastest')

for _ in range(10):
    draw_shape(angles, space)
    angles += 1
    space += 5
    timmy.pencolor(rng.choice(rand_colors))
    

screen.exitonclick() # at the end to exit after evrything has been done
