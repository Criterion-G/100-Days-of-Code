# I didn't face significant issues while attempting the project, however, I did the project using my previous knowldge of while loops, which at this point of the bootcamp is not yet covered.
# So, I'll attempt it again using what is covered up till now.

import random as rng

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

input_letters = int(input('how many letters do you want in your password?\n'))
input_numbers = int(input('how many numbers do you want in your password?\n'))
input_symbols = int(input('how many symbols do you want in your password?\n'))

list_password = []

for char in range(0, input_letters):
    list_password += rng.choice(letters)   # I didn't know that the compound assignment works on strings AND LISTS TOO!!! HOW FUN!!!

for num in range(0, input_numbers):
    list_password += rng.choice(numbers)

for symbol in range(0, input_symbols):
    list_password += rng.choice(symbols)

rng.shuffle(list_password)
password = ''

print(f'your password is: {password.join(list_password)}')

# the result is less lines and easier to read code, but I wasn't off by much in my first attempt.
