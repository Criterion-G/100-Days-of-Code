# functions created in the chapter:

import random as rng

# this is the first function I will create to test my knowledge before starting the chapter
def rng_password(input_letters: int, input_numbers: int, input_symbols: int):
    ''' a function that returns a psuedorandom passworad that takes the arguments of how many letters, numbers and symbols does the user want. '''
    list_password = []
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']         # these are local variables.

    for i in range(0, input_letters):
        list_password += rng.choice(letters)
    for i in range(0, input_numbers):
        list_password += rng.choice(numbers)
    for i in range(0, input_symbols):
        list_password += rng.choice(symbols)

    rng.shuffle(list_password)
    password = ''
    return f'your password is {password.join(list_password)}'  # by default, a function returns none, you have to specificy what to return if you want your function to output something.

# the following are my notes on the lessons

def greet(user_id: str):         # a simple functions that highlights the logic behind creating functions. def is the defining of the function, followed by the name of the function and in the paranthesis is the parameters
    print(f'hello {user_id}')    # here is the logic that the function will execute when called.
#                                  then the function is called to execute the logic. 'called in "notes"'