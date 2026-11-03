import pandas as pd

#TODO 1. Create a dictionary in this format:
with open('100 Days Challenges\\Day 26 - List Comprehension\\project\\nato_phonetic_alphabet.csv') as alphabet_file:
    print(alphabet_file)

ph_alphabet = pd.read_csv('100 Days Challenges\\Day 26 - List Comprehension\\project\\nato_phonetic_alphabet.csv')
ph_alphabet_df = pd.DataFrame(ph_alphabet)
ph_alphabet_dict = {row.letter: row.code for row in ph_alphabet_df.itertuples()} # new method .itertuples() is useful for our scenario. Check notes for how it outputs data

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input('please type in your name: ').upper()
phonetic_list = [ph_alphabet_dict[letter] for letter in user_input]
print(phonetic_list)
