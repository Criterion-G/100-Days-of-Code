import turtle

# this file is a demonstration of how OOP and Classes work using the turtel module
# for more information on the turtle module, see the docs at: https://docs.python.org/3/library/turtle.html#introduction

# creating a turtule object from the Turtle class
# here we instansiate the instance of the turtle class, and changing its attributes based on what the class blueprint has.
timmy = turtle.Turtle()
print(timmy)
timmy.shape('turtle') # attributes
timmy.color('IndianRed3')

# object methods
my_screen = turtle.Screen() # this is a function for a hidden class called screen that allow us to control the GUI of the module
print(my_screen)
my_screen.bgcolor('black')

# we will use the methods here to control the turtle using the predefined fucntions of the class
timmy.forward(100)
timmy.right(25)
timmy.forward(100)

my_screen.exitonclick() # this needs to be at the end of the script for anything above to execute
