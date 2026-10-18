# create a version of etch a scketch
# requirements:
# - a way to take the user's input and turn it into a drawing, whether a line, circle.. etc

import turtle as t

tim = t.Turtle()
screen = t.Screen()

# movement functions
def move_forward():
    tim.forward(10)
def move_left():
    tim.left(20)
    tim.forward(10)
def move_right():
    tim.right(20)
    tim.forward(10)
def move_back():
    tim.back(10)

screen.listen()

screen.onkeypress(fun= move_forward, key= 'w')
screen.onkeypress(fun= move_left, key= 'a')
screen.onkeypress(fun= move_right, key= 'd')
screen.onkeypress(fun= move_back, key= 's')

screen.exitonclick()

# with a little more effort, I can make moving based on the turtle's heading, but that is not what was requested.
