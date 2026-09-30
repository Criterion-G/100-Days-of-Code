# create a coffee dispencere program that tracks rescourcs and revenue, for our purposes there will only be 3 types of coffee
# and we will only take from a quarter to a penny.

# set up a global constant list that contains a dictionary of each coffee and its attributes

COFFEE = {
    'espresso':
    {
        'water': 50, # ml
        'coffee': 18, #g
        'milk': 0,
        'price': 1.5
    },
    'latte':
    {
        'water': 200,
        'coffee': 24,
        'milk': 150, #ml
        'price': 2.5
    },
    'cappuccino':
    {
        'water': 250,
        'coffee': 24,
        'milk': 100,
        'price': 3
    }
}

# accepted change
QUARTAR = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01

# global vars

resources = {
    'water': 300,
    'coffee': 100,
    'milk': 200,
    'revenue': 0
}

# create functions for, 'resource managmenet' and 'checking transaction'

def resource_mgm(order):
    '''changes the resources variable based on the order'''

    resources['coffee'] -= COFFEE[order]['coffee']
    resources['milk'] -= COFFEE[order]['milk']
    resources['water'] -= COFFEE[order]['water']

def coins():
    '''processes the user's coins'''

    total_quarters = int(input('how many quarters?\n'))
    total_dimes = int(input('how many dimes?\n'))
    total_nickles = int(input('how many nickles?\n'))
    total_pennies = int(input('how many pennsies?\n'))

    return (total_quarters * QUARTAR) + (total_dimes * DIME) + (total_nickles * NICKLE) + (total_pennies * PENNY)
    

def transaction(order, payment):
    '''checks payment, returns True if payment is successful with no change, returns False if the payment is less than the price
    and returns the delta if the payment is more than the price. manages the rescources'''

    delta = round( payment - COFFEE[order]['price'] , 3)

    if delta < 0:
        return delta
    elif delta >= 0:
        return delta

def report():
    '''prints a report summary of the current machine resources'''

    print('\n' * 20)
    print(f'the current water level: {resources['water']} ml')
    print(f'the current milk level: {resources['milk']} ml')
    print(f'the current coffee level: {resources['coffee']} grams')
    print(f'the current revenue: {resources['revenue']}$')

def coffee_machine(order):
    '''the logic of the machine'''
    user_pay = coins()
    print('\nprocessing your order\n')
    change = transaction(order, user_pay)

    if change < 0:
        print('the amount you\'ve deposited is less than the price')
        print('your payment has been refunded')
        print('please try again')
    elif change >= 0:
        print('order completed')
        print(f'your change is {change}$')
        print('thank you for your order, enjoy your delicious coffee ☕')
        # only manage resources if the transaction is correct
        resources['revenue'] += COFFEE[user_input]['price']
        resource_mgm(user_input)
    else:
        print('invalid input, please try again')

def rescource_check():

    return any(value < 0 for value in resources.values()) # any evaluates all values, if any of them meets the condition it will return true

# the working coffee machine

status = True

while status:

    if rescource_check() is True:
        print('sorry, the machine is out of resources. Please come back again once they have been refilled.')
        print('thank you and sorry for the inconvience.')
        break
    else:
        print('welcome to your caffeine addiction corner ☕')
        user_input = input('please select your order: espresso 1.5$ - latte 2.5$ - cappuccino 3$\n')
        # admin utility
        if user_input == 'report':
            report()
        elif user_input == 'stop':
            break
        else:
            coffee_machine(user_input)

# completed
# self review:
# I think the best part of my approach is that the resources check happens before taking the input from the user,
# simulating how an actual coffee machine works probably.
# all in all, I believe this attempt is good. 8/10
