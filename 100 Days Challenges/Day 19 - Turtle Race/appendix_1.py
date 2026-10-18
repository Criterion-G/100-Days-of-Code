# Passing functions as an argument for another function doesn’t require the parenthesis. 
# The parenthesis immediately call the function even if it’s passed as an argument.
# To pass it as an argument you name the function without the parenthesis,
# this will essentially just pass in the name of the function into the other function to call it when it executes.
# Think of the following example:

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calc(n1, n2, func):
    return func(n1, n2)

calc(5, 5, multiply)

# calling the multiply function will cause an error if you called it without its required args.
# debug for clearer understanding.

# This is what's called a 'Higher-Order Function' and it essentially means a function that can work with other functions.
