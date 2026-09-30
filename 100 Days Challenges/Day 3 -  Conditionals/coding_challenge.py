# Create a simple Pizza Delivery app

# print('welcome to binary pizza deliveries:\n')

# size = input('what size pizza do you want? small, medium or large? ')
# pepperoni = input('do you want some pepperoni with that? yes or no ')
# extra_cheese = input('do you want to add extra cheese? yes or no ')

# s_answer = size.strip()[0].lower() # this technique is called input normalization.
# p_answer = pepperoni.strip()[0].lower()
# ec_answer = extra_cheese.strip()[0].lower()
# bill = 0

# if s_answer == 's':
#     bill = 15
#     print('small pizza is 15$')
#     if p_answer == 'y':
#         bill += 2
#         print('pepperoni is 2$ extra for small size.')
#     print(f'total {bill}$')
# elif s_answer == 'm':
#     bill = 20
#     print('medium pizza is 20$')
#     if p_answer == 'y':
#         bill += 3
#         print('pepperoni is 3$ extra for medium pizza')
#     print(f'total {bill}$')
# elif s_answer == 'l':
#     bill = 25
#     print('large pizza is 25$')
#     if p_answer == 'y':
#         bill += 3
#         print('pepperoni is 3$ extra for large pizza')
#     print(f'total {bill}$')

# else:
#     print('invalid input. try again.')

# if ec_answer == 'y':                                # This is optional, so we don't need an else statment. Otherwise, the code will bel messy.
#     bill += 1
#     print('extra cheese is 1$')

# print(f'your total bill is {bill}$')

# The Solution

print('welcome to binary pizza deliveries:\n')

size = input('what size pizza do you want? small, medium or large? ').strip()[0].lower()   # Input Normalization
pepperoni = input('do you want some pepperoni with that? yes or no ').strip()[0].lower()
extra_cheese = input('do you want to add extra cheese? yes or no ').strip()[0].lower()

bill = 0

if size == 's':
    bill = 15
elif size == 'm':
    bill = 20
elif size == 'l':
    bill == 25
else:
    print('invalid input. try again.')

if pepperoni == 'y':
    if size == 's':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'y':
    bill += 1

print(f'your total bill is {bill}$')
