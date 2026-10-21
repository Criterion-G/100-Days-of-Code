# Create a rock paper scissors game.
# The goal is to create this using lists, but I decided to do it with dicts because they look cleaner and better.

import random as rng

# ASCII ART

rock_pc = '''
computer choose: rock

    _______
---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
'''

paper_pc = '''
computer choose: paper

    ________
 ---    ____)____
            ______)
            _______)
           _______)
  ---.__________)
'''

scissor_pc = '''

computer choose: scissors
     _______
 ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
'''

rock_player = '''
you choose: rock

    _______
---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
'''

paper_player = '''
you choose: paper

    ________
 ---    ____)____
            ______)
            _______)
           _______)
  ---.__________)
'''

scissor_player = '''

you choose: scissors
     _______
 ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
'''

# Computer Choice

choices_pc = {
    0: rock_pc,
    1: paper_pc,
    2: scissor_pc
}
# computer_choice = rng.choice(choices_pc)
computer_choice = rng.choice(choices_pc)


# Player Chocie

choices_player = {
    0: rock_player,
    1: paper_player,
    2: scissor_player
}

# Exception handeling for invalid user input.
while True:
    try:
        player_input = int(input('choose 0 for rock, 1 for paper and 2 for scissors\n'))
        break
    except ValueError:
        print('invalid input!')


player_choice = choices_player[player_input]

# Outcome


print(player_choice)
print(computer_choice)

# Rules

# Rock situations
if player_choice == rock_player and computer_choice == rock_pc:
    print('draw')
elif player_choice == rock_player and computer_choice == paper_pc:
    print('you lose :(')
elif player_choice == rock_player and computer_choice == scissor_pc:
    print('you win')
# Paper situations
elif player_choice == paper_player and computer_choice == rock_pc:
    print('you win!')
elif player_choice == paper_player and computer_choice == paper_pc:
    print('draw.')
elif player_choice == paper_player and computer_choice == scissor_pc:
    print('you lose :(')
# Scissor Situations
elif player_choice == scissor_player and computer_choice == rock_pc:
    print('you lose :(')
elif player_choice == scissor_player and computer_choice == paper_pc:
    print('you win!')
elif player_choice == scissor_player and computer_choice == scissor_pc:
    print('draw.')
else:
    print('invalid input')