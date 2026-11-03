# List Comprehension
# A pythonic programming concept, a list comprehesion allows us to create a new list out of an existing list without the need for a for loop or other methods.

import random as rng
import pandas as pd

# Without List Comprehension
numbers = [1, 2, 3 ,4 , 5]
new_list = []

for number in numbers:
    new_list.append(number + 1)
print(new_list)

# With List Comprehesion
numbers = [1, 2, 3 ,4 , 5]
new_list = [ n + 1 for n in numbers ]
print(new_list)

# List Comprehensino Works with any sequence, not just lists. (strings, dicts.. etc)

name_1 = 'Faisal'
new_list = [letter for letter in name_1]
print(new_list)

# The main goal of list comprehesion is always to create a new list out of an existant sequence.

# Excersie

doubled_num = [n *2 for n in range(1, 5)] # range is a sequence
print(doubled_num)

# Conditional List Comprehension
# Only add an element to the new list if the logical condition is met.

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [item for item in names if len(item) < 5]
print(short_names)

# Challenge
big_names = [item.upper() for item in names if len(item) > 5]
print(big_names)

# Quiz: Sqaured Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
square_numbers = [n**2 for n in numbers]
print(square_numbers)

# Quiz: Even Numbers from a List of Strings
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
result = [n for n in numbers if n % 2 == 0]
print(result)

# Quiz: Commn Numbers in Two Files
with open('100 Days Challenges\\Day 26 - List Comprehension\\file1.txt') as file_1:
    list_1 = [int(n) for n in file_1]

with open('100 Days Challenges\\Day 26 - List Comprehension\\file2.txt') as file_2:
    list_2 = [int(n) for n in file_2]

result = [n for n in list_1 if n in list_2]

print(result)

# Dictionary Comprehesion
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

student_scores = {name:rng.randint(30,100) for name in names}
print(student_scores)

# Dictionary Comprehension with an existant dictionary
passed_studens = {student:score for (student, score) in student_scores.items() if score > 60}
print(passed_studens)

# Quiz: Create a dictionary that counts the lenght of each word in a string
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)

# Quiz: Convert tempertaure from a dictionary to a dictionary
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:(temp * 9/5 + 32) for (day, temp) in weather_c.items()}
print(weather_f)

# Looping throuhg a pandas data frame
# it's similar to looping through a dictionary

student_dict = {
    'student': ['Anglea', 'James', 'Lily'],
    'scores': [56, 76, 98]
}

# Looping through a dictionary
for student, score in student_dict.items():
    print(student)
    print(score)

# Looping through a data frame
student_df = pd.DataFrame(student_dict)
print(student_df)
for key, value in student_df.items():
    print(value)

# This way is not particulary useful for dealing with data, that's why pandas has an in-built method for that purpose. Obsereve:

for index, row in student_df.iterrows():
    print(row)

# This returns data in a structured format (a pandas series), returing the row or the index with the headers if you choose the rows. We can do more with this method:

# The following loop is filtering out data on a particular condition or requiremnt. Extremely powerful and useful. 
for index, row in student_df.iterrows():
    if row.student == 'Anglea':
        print(row.scores) # it is important to note here that the column names with comprehension becomes an attribute of the iterabel row.

print(student_df.itertuples()) # returns a map object
print(list(student_df.itertuples()))
