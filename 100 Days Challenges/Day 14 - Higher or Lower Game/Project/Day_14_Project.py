# create the higher lower game
# the game compares two random numbers and the user has to guess which one is higher
# since, for some reason, the dataset provided is only available through the PyCharm files of the course material.
# I've decided to use a publicly available dataset of movies and their ratings.
import random as rng
import pandas as pd

# dataset prep
def data_to_dict():
    data = pd.read_csv(r'100 Days Challenges\Day 14 - Higher or Lower Game\Project\Popular_movies.csv')
    movies_df = pd.DataFrame(data)
    # data cleaning
    movies_df['vote_average'] = movies_df['vote_average'].round(1)
    movies_df.drop(['Unnamed: 0','release_date', 'adult', 'popularity', 'original_language'], axis='columns', inplace= True)
    movies_df = movies_df[movies_df['vote_count'] > 1000]
    return movies_df.to_dict('records') # convert the dataframe to a dictionary

# create a function that returns a randomly selected dict
def choice_selection():
    ''' used to intialize our choices randomly from the dictionary '''

    return rng.choice(MOIVIES_DB)

# create an evaluation function that returns the title of the highest score
def choice_result(guess, choice_1: dict, choice_2: dict):
    ''' evaluates the user\'s guess against the choices '''

    if choice_1['vote_average'] > choice_2['vote_average'] and guess == 'h':
        return choice_1
    
    elif choice_1['vote_average'] < choice_2['vote_average'] and guess == 'l':
        return choice_2
    
    elif choice_1['vote_average'] == choice_2['vote_average']:
        print('it\'s a tie: continue')
        return True
    
    else:
        return False


# global constants
MOIVIES_DB = data_to_dict()

# game global variables
choice_1 = choice_selection() # we intialize our first choice here, which will then be replaced from within the loop by the new value if the user guessed correctly
score = 0
game_state = True

# game loop logic
while game_state:

    choice_2 = choice_selection()

    print(f'the movie \'{choice_1['title']}\' vs. \'{choice_2['title']}\'')
    print(f'your score is {score}')

    user_input = input('please type: higher or lower\n')[0].lower()
    result = choice_result(user_input, choice_1, choice_2)

    if result == False:
        print(f'gg, you lose! your score is {score}\nbetter luck next time!')
        #reset everything if the user wants to try again
        if input('do you want to play again? y or n\n') == 'y':
            score =0
            game_state = True
            choice_1 = choice_selection()
        else:
            game_state = False

    elif result == True:
        pass

    else:
        choice_1 = result
        score += 1
