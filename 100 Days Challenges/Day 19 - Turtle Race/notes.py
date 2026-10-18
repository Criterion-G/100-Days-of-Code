# In this section, we will be learning more Turtle Graphics, Event Listeners and States and Instances

import turtle as t

# Event Listeners

tim = t.Turtle()
screen = t.Screen()

def move_forward():
    tim.forward(10)

screen.listen() # this method sets the screen to listen and record and input from the user.
screen.onkeypress(key= 'space', fun= move_forward) # this is the Higher-Order Function concept. To undertand what's going on here, refer to: appendix_1.
# review keyword and positional arguments

screen.exitonclick()
