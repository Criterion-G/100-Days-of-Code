import pandas as pd
import random as rng

# Generates Random Words Based on Difficulty

# file reading and filtering
words_df = pd.DataFrame(pd.read_csv(r'100 Days Challenges\Day 7\Hangman_Project\words_tiers.csv')) # read csv and create dataframe.
selected_pos = ['verb','adjective']                                               # filter the df to only include certain parts of speech.
words_df = words_df[words_df['pos'].isin(selected_pos)]                                            # apply the fileter to the df.

# difficulty levels
very_easy_words = words_df[words_df['CEFR'] == 'A1']
easy_words = words_df[words_df['CEFR'] == 'A2']
medium_words = words_df[words_df['CEFR'] == 'B1']
hard_words = words_df[words_df['CEFR'] == 'B2']

# main function to select a random word and create a guess string based on the word length.
def select_word():
    words = []

    difficulty = input('choose your difficulty\n ee for very easy - e for easy - m for medium - h for hard\n')

    if difficulty == 'ee':
        words = very_easy_words['headword'].to_list()
    elif difficulty == 'e':
        words = easy_words['headword'].to_list()
    elif difficulty == 'm':
        words = medium_words['headword'].to_list()
    elif difficulty == 'h':
        words = hard_words['headword'].to_list()
    else:
        print('invalid input')

    word = rng.choice(words).lower()                # strings are immutable, so we cannot change the underscore if the guess is correct. We need to convert the string to a mutable object first.

    return word

def main():
    pass

if __name__ == '__main__':
    main()
