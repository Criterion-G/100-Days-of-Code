import word_gen as wg
import random as rng
from ascii import stages, logo

# select difficulty and generate word
selected_word = wg.select_word()

# print(selected_word)  # show the word for testing.

# create the placeholder blanks for the user
placeholder = ''
word_len = len(selected_word)
for letter in range(word_len):
    placeholder += '_'

print('welcome to the hangman game\n')
print(logo)

print('guess the word: \n')
print(placeholder)

# global game variables
game_state = False
correct_letters = []
life = 6


# game logic and local variables
while game_state is False:

    print(stages[life])
    user_guess = input('type here: ').lower()
    print('\n')
    display = ''

    for letter in selected_word:
        if letter == user_guess:
            display += letter
            correct_letters.append(letter)
            print(f'you guessed {user_guess}, which is correct!')
            print(f'you have {life} lives left')
        elif letter in correct_letters:                  # This is how you save the progress of the player. Basically checking if the current iteration is within the global variable list, thus adding to the disply with the current guess.
            display += letter
        else:
            display += '_'

    # for visual display.
    print('\n')
    print(display)
    print('\n')
    # check game state
    if '_' not in display:
        game_state = True
        print('************ YOU WON! ************')
    elif user_guess not in selected_word:
        life -= 1
        print(f'you guessed {user_guess}, your guess is wrong!')
        print(f'you have {life} lives left')
        if life == 0:
            game_state = True
            print('************ YOU LOSE! ************')
            print(f'************ the word was {selected_word} ************')


def main():
    pass
if __name__ == '__main__':
    main()
