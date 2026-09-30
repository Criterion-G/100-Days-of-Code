# through out your programming endaviours, you will inevitably create bugs.
# they key thing is developing the skills to understand them, why they happen and how to fix them

# the process can be broken down into a few simple steps as demonstrated below:

# STEP1: Descirbe the Problem
# if the problem is not well understood, then it will be almost impossible to debug
# in this step, we try to untangle the problem and make sense of what's goning on

def my_func():
    for i in range(1,20):
        if i == 20:
            print('you got it')

my_func()

# in the language's understanding this code is correct, there are no syntax or indentaion errors.
# the problem is that the language doesn't understand your intentions.
# in this function we want to print when the iteration reaches 20. The problem is that the range function used, the upper bound is exclusive and it will return and stop at the number you provided
# the solution:

def my_func():
    for i in range(1, 21):
        if i == 20:
            print('you got it')

my_func()

# STEP2: Reproduce the bug
# if you can't reproduce it, you can't understand it, or look for an answer to said bug

from random import randint
dice_nums = [1, 2, 3, 4, 5, 6]
selected = randint(1,6)
# print(dice_nums[selected])

# let's first describe the problem. The code works ocassianlly, but sometimes, it throughs an error.
# the error is an IndexError
# now the problem is that the list has 5 indcies, while the selected variable chooses from 1 to 6 including both
# so index 1 will gives us the element '2' from the list and index 6 will through an error because there is no sixth element
# for this step we will reproduce the bug
# print(dice_nums[6]) # this is our bug
# to fix it we simply change the randint function arguments

selected = randint(0,5)
print(dice_nums[selected])

# STEP3: Play the computer
# if you can't think or take on the role of a computer, you'll most likely produce more bugs, and be unable to fix any bug you come across
# playing the role of a computer that is executing the code, gives you the depth needed not only for debugging, but for designing good code as well

year = int(input('what\'s your year of birth?\n'))

if year > 1980 and year < 1994:
    print('you are a millennial')
elif year > 1994:
    print('you are a gen Z')

# running this code gives no error.
# but let's say someone's birth year is 1994. think like a computer. what will happen? nothing
# because in our statement nothing handles this fact. so the computer just doesn't return anything
# the fix is just adding >= or <= to one of the statments to account for this possiblity

# General Tips for Handling Bugs:

# Exception Handling
# in the code below, without exception handling, if the user types a different type from the expected integer value, the program will through out and exception.
# we can handle this exception to tell the user to provide a valid input

try:
    age = int(input('please type in your age\n'))
except ValueError:                                                                  # you have to specify which error type to handle
    print('your input is invalid, please type a numerical response such as 20')
    age = int(input('please type in your age\n'))

if age > 18:
    print(f'yay, you can drive.. my condolences!')

# Use the Print function to search for bugs
# consider the following code:

word_per_page = 0
pages = int(input('Type the number of pages: '))
word_per_page == int(input('Type the average number of words per page: ')) # the issue is here, as the double equal sign is a comparison operator and not an assignment one 
total_words = pages * word_per_page
print(total_words)
# trouble shooting print statements
print(f'the pages variable = {pages}')
print(f'the word_per_page variable = {word_per_page}')

# Use a Debugger for bigger and more complex problems. I can use the debugger from VS Code
# Examples for a debugger use is in another file

# Final Tips for Debugging

# 1) When struggling for a while. Take a break and come back with a fresh set of eyes
# 2) Ask a Friend: this would require building a network of capable software devs within your field
# 3) Run Your Code: Keep running your code and trouble shoot bits and pieces of it to get a clear understanding for what is going on
# 4) When all else fails: Look for the answer at stackoverflow or then it becomes acceptable to ask AI. Making it guide you through and not just give you the answer if your goal is to learn and imporve
