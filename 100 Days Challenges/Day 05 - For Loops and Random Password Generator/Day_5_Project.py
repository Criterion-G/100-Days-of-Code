# Create a random password generator:

# Solution attempted before lesson:

import random as rng 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

input_letters = int(input('how many letters do you want in your password?\n'))
input_numbers = int(input('how many numbers do you want in your password?\n'))
input_symbols = int(input('how many symbols do you want in your password?\n'))

user_letters = 0
user_numbers = 0
user_symbols = 0

password = []

# while user_letters < input_letters:
#     password.append(letters[ rng.randint( 0, index_letters ) ])         <<< This was how my first attempt worked, but it was not very effcient due to creating more variables than necessary.
#     user_letters += 1

while user_letters < input_letters:
    password.append(rng.choice(letters))
    user_letters += 1

while user_numbers < input_numbers:
    password.append(rng.choice(numbers))
    user_numbers += 1

while user_symbols < input_symbols:
    password.append(rng.choice(symbols))
    user_symbols += 1

rng.shuffle(password)    # Randomizes the order of the generated sequence.
generated_password = ''.join(password)

print(f'your password is: {generated_password})')

# Thoughts:
# A better way to do this is by creating a function for the while loop.
