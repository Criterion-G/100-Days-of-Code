# create a numbers gussing game..

import random as rng
# TODO1: random number function and attempt setting function and user guess eval
def rand_num():
    nums = list(range(1,100))
    return rng.choice(nums)

def attempts(user_input):
    if user_input == 'h':
        return 5
    elif user_input == 'e':
        return 10
    else:
        print('invalid input')
        return ValueError

def eval(user_guess, choosen_num):
    ''' this function chooses the random number and evaluates '''
    if user_guess == choosen_num:
        print(f'your guess is correct! the number was {choosen_num}')
        return 10000
    elif user_guess < choosen_num:
        print(f'your guess is lower than the number')
        return -1
    elif user_guess > choosen_num:
        print(f'your guess is higher than the number')
        return -1


# TODO2: create a while loop that utilizes the attempts function

num_attempts = attempts(input('type \'hard\' or \'easy\' to select your difficulty\n')[0].lower().strip())
choosen_num = rand_num()
progress = 0

while num_attempts > 0:
    print(f'pssst.. this is for your testing, the number is {choosen_num}')

    progress += eval(int(input('please type your guess\n')), choosen_num)

    if progress > 2000:
        print('congrat on your win!\n')
        num_attempts = 0
    else:
        num_attempts -= 1
        print(f'you have {num_attempts} attempts left!\n')


# status: did it first try in almost 30-40 minutes. structuring then breaking down the problem into smaller chunks is really the way to go.
