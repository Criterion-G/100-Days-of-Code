import random as rng
from ascii import stages

# Tasks
# Task 1: random word gen and answer evaluation
# Task 2: Fill in the Blanks
# Task 3: While loop to keep the user guessing and saving the user's progress until all the guesses are made

# word gen
word_list = ['aardvark', 'baboon', 'camel']
selected_word = rng.choice(word_list)


print(selected_word)  # show the word for testing.

# create the placeholder blanks for the user
placeholder = ''
word_len = len(selected_word)
for letter in range(word_len):
    placeholder += '_'
print(placeholder)

# global game variables
game_state = False
correct_letters = []
life = 6 * word_len
art = life / 6
# game logic and local variables
while game_state is False:

    user_guess = input('type here: ').lower()
    display = ''

    for letter in selected_word:
        # if lg.evaluation(letter, user_guess, correct_letters, display) is True:
        #     pass
        if letter == user_guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:                  # This is how you save the progress of the player. Basically checking if the current iteration is within the global variable list, thus adding to the disply with the current guess.
            display += letter
        else:
            display += '_'
            life -= 1

    if '_' not in display:
        game_state = True
        print('you won!')
    elif life <= 0:
        game_state = True
        print('you lose')

    print(display)
