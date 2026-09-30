# create the hirst painting

import random as rng
import turtle as t
import colorgram

# create the pen object
# there's no need for pencolor as we will be using the dot method which has built-in color control.
pen = t.Turtle()
screen = t.Screen()
screen.bgcolor('bisque')
screen.tracer(0) # instantly paint, for demo purposes. uncomment if you want the long ass animation.
pen.hideturtle()
pen.speed('fastest')
t.colormode(255) # sets the color mode to accept RGB color numbers in the dot argument.
screen.setup(0.6, 0.8) # sets the screen size portion
pen.penup()

# extract the color palette
rgb_colors = []
colors = colorgram.extract(r'100 Days Challenges\Day 18\Day_18_Project\image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
# remove background matching colors
for color in [0, 1, 3, 4]:
    rgb_colors.remove(rgb_colors[color])

# variables and functions for the script
screen_w = screen.window_width()
screen_h = screen.window_height()
x_axis = screen_w / 2
y_axis = screen_h / 2
STARTING_POS = ((x_axis * -1) + 50, (y_axis * -1) + 50)
ENDING_POS = (x_axis - 50,  - 50)
MAX_X_AXIS = STARTING_POS[0] * - 1 - 50
MAX_Y_AXIS = STARTING_POS[1] * - 1

def max_distance(max_x_pos):
    if pen.pos()[0] > max_x_pos:
        return True
    else:
        return False

def draw_column(rgb_colors):
    while not max_distance(MAX_X_AXIS):
        pen.forward(50)
        pen.dot(10, rng.choice(rgb_colors))
    screen.update()

def out_of_bounds():
    if pen.pos()[1] > MAX_Y_AXIS:
        return True
    else:
        return False

# the painting script
axis_incremenet = 50
pen.teleport(STARTING_POS[0], STARTING_POS[1])
while not out_of_bounds():
    draw_column(rgb_colors)
    pen.teleport(STARTING_POS[0], STARTING_POS[1] + axis_incremenet)
    axis_incremenet += 50

screen.exitonclick()
