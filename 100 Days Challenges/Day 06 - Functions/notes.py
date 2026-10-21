# this lesson covers functions and while loops.
# to ease the use of functions and understanding, I will create a module called 'functions' and add all the functions I create in this lessons there and simply call them in the tasks file for tasks.

import functions as func

print(func.rng_password(7,7,10))

func.greet('faisal')

# while loops:
# the key thing about while loops is that the run until the condition of the loop becomes false, then it stops. There are techniques of using the 'True' boolean value to keep the loop running until you break it.

a = 0               # the variable has to be outside the loop in this example

while True:
    print('hi')
    a += 1
    if a > 5:
        break

# other uses for boolean data types

while True:           # keep running until we break out of the loop.
    try:
        age = int(input('type age:\n'))
        break
    except ValueError:
        print('please input a number')

print(age)
