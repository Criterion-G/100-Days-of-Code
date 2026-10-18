# the provided solution

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

pen.setheading(225)
pen.forward(300)
pen.setheading(0)
num_dots = 100

for dot_count in range(1, num_dots):
    pen.dot(20, rng.choice(rgb_colors))
    pen.forward(50)
    if dot_count % 10 == 0:
        pen.setheading(90)
        pen.forward(50)
        pen.setheading(180)
        pen.forward(500)
        pen.setheading(0)

screen.exitonclick()
