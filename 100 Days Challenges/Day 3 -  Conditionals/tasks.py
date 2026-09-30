# Conditionals
# In this first section we will tackel conditionals.

# lvl = int(input('type your lvl: '))

# if lvl >= 5:
#     print('you can start quest!')
# else:
#     print('go do some side quests :)')

# Condtional operators are >, <, >=. <= and ==, !=
# The double equal sign is a comparison operator, while one equal sign is an asaignment operator.

# The Modulo

# The Modulo is an operation that counts how many times the denominator goes into the numerator and gives us the remaining after division. 
# If the division is for even numbers it will always return 0 because there is no remaining. If it's for odd numbers then there will be some remaining.

print(10 / 3)
print(10 % 3)

# # This next challenge is to check if the user input is an odd or even number.

# numerator = float(input('Enter a number: '))

# if numerator % 2 == 0:
#     print('even')
# else:
#     print('odd')


# Nested if/else statements

# lvl = int(input('type your lvl: '))
# difficulty = str(input('select your diffiulty (type \'hard\' or \'easy\'): '))


# if lvl >= 5:
#     if difficulty == 'hard':
#         xp = 'double XP!'
#     else:
#         xp = 'no bonus XP :('
#     print(f'you can start the quest! you gain: {xp}')
# else:
#     print('go do some side quests first :)')

# Multiple conditions
# Mulitple if statemnents

# height = int(input('type your height in cm: '))
# age = int(input('type your age: '))
# bill = 0

# if height >= 120:
    
#     print('you can enter')
#     if age <= 12:
#         bill = 5
#         print('your bill is 5$')
#     elif age <= 18:
#         bill = 12
#         print('your bill is 12$')
#     else:
#         bill = 20
#         print('your bill is 20$')

#     photo_op = input('do you want a photo for 3$? y or n ').lower()

#     if photo_op == 'y':
#         bill += 3

#     print(f'your total bill is {bill}$')
    
# else:
#     print('grow up first')


weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi < 18.5:
    print('underweight')
elif bmi >= 18.5 and bmi <25:
    print('normal weight')
else:
    print('overweight')

# Logical Operators
# and, or, not

# let's give seniors free rides

height = int(input('type your height in cm: '))
age = int(input('type your age: '))
bill = 0

if height >= 120:
    
    print('you can enter')
    if age <= 12:
        bill = 5
        print('your bill is 5$')
    elif age <= 18:
        bill = 12
        print('your bill is 12$')
    elif age >= 45 and age <= 55:
    # elif 45 <= age <= 55:  # a simpler way to do this.
        bill = 0
        print('your bill is 0')
    else:
        bill = 20
        print('your bill is 20$')

    photo_op = input('do you want a photo for 3$? y or n ').lower()

    if photo_op == 'y':
        bill += 3

    print(f'your total bill is {bill}$')
    
else:
    print('grow taller first')

# the and checks if both conditions are true then it returns true, otherwise it's false.
# the or checks if one condition is true then it returns true, if both are false it returns false.
# the not just reverses the boolean value, if the boolean value is true it will reverse it to false.

a = 5
b = 7
 
if a >= b and a != b:
    print("A")
elif not a >= b and a != b:  # The not will reverse the first condition to true making both statements true and the logic then checks out.
    print("B")
else:
    print("C")
