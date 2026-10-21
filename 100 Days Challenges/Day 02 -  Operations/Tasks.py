# import pandas as pd
# import numpy as nm

# obj_sample = pd.DataFrame([33, 33])

# print(len(str(324_343_432))) # << Underscore is not counted as an element for int data types. It's simply there for readability

# underscore_demo = str(324_343_432)
# print(underscore_demo[5]) # << The fith element will not return an underscore. It will return 3. Underscores are invisible to py.

# # Something of note here is that ints are not subscriptable because they are not a sequence like a string or a list
# # To know what a dtype is for data is to use the function tpye()
# print(type(underscore_demo))

# # Task 3
# #Primitve Data Types:
# print('The basic data types are:')
# print(type(123))
# print(type("32"))
# print(type(True))
# print(type(32.4))
# #More Data Types:
# print('Other data types are:')
# print(type([32, 43, 343]))
# print(type((43,423,423)))
# print(type({"y": 4, "x": 5}))
# # And:
# print('And all data types are objects')
# print(type(obj_sample))

# # Changing the dtype is called type casting.
# int(underscore_demo)
# str(underscore_demo)
# float(underscore_demo)

# # Practice
# name = input('type your name:\n')
# lenght = len(name)
# print('number of letters in your name= ' + str(lenght))

# Math operations
# Division is an implicit type caster, meaning it will always return a float even if the divison is even.
print(type( 6 / 3 ))
# We can eaither type cast it to int, or use double slashes to return an int
print(type( 6 // 3))
# The tricky thing with this is that it drops the decimals if the division is not even and not round anything.
print( 7 / 3 )
print( 7 // 3 )
print( 8 ** 2 ) # << This is exponentiation, or raising a number to a power. In this case, 8 squared.

# Python's order of operations is PEMDAS
# Take this example
print(3 * 3 + 3 / 3 - 3) # < The answer is 7 becasue 3 / 3 happens first and not 3 - 3. So you won't get a div 0 error.

# You can change the outcome to 3 if you want by doing the following:
print(3 * (3 + 3) / 3 - 3)

# BMI Calc
height = 1.65 
weight = 84

# BMI is weight divided by the height squared.
# Brackets are optional since exponants happen first anyway.
bmi = weight/height**2

print(bmi)

# Number manipulation
# Flooring: Drops all digits.
print(int(bmi))

# Rounding
print(round(bmi)) # Round to the nearst whole number.
print(round(bmi, 2)) # Specifiy the number of digits to round.

# Assigning to variables:
score = 0
# Player scores:
score += 1
# Player loses two points:
score -= 2
# Player scores 4:
score += 4
# Player got a buff that doubles the score:
score *= 2
print('the socre is = ', score)
# Overwrite the socre
score = 0
print('reset = ', score)

# f-Strings
# to put all data types into one string without contiously type casting everything, you can use f-strings as such:

score = 6
status = 'you\'re the goat!'
buffs = True

print(f'your scoure is {score} and {status}.\n Active buffs: {buffs}')
