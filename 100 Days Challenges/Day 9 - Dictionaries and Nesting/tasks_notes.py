# create a silent auction program utiliziing dictionaries.

dict_sample = {
    'key1': 'nothing',
    'key2': 'something'
}
print(dict_sample['key2']) # dictionaries index the keys and not numbers.

# same as lists, we can assign a new key to a new value, or an existing key to a new value.

dict_sample['key3'] = 'more things'
dict_sample['key1'] = 'now it\'s something'

print(dict_sample)

# a useful techinque that comes often in a lot of python code is creating an empty dictionary that can be filled later.

empty_dict = {}
print(empty_dict)

list_range = [1,3,4,5,4]

# looping through a dictionary will assign the iteration variable to the key and not the value
for i, r in enumerate(list_range):
    empty_dict[i] = r

print(empty_dict)

for key in empty_dict:
    print(empty_dict[key])

# we can wipe an existing dictionary like variables

dict_sample = {}
print(dict_sample)

# Quiz

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

grade_ranges = {
    'Outstanding': range(91, 101),
    'Exceeds Expectation': range(81-91),
    'Acceptable': range(71-81),
    'Fail': range(-100,71)
}

student_grades = {}

for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = 'Outstanding'
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
        student_grades[key] = 'Exceeds Expectation'
    elif student_scores[key] >= 71 and student_scores[key] <= 80:
        student_grades[key] = 'Acceptable'
    else:
        student_grades[key] = 'Fail'

print(student_grades)
