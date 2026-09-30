# create a coffee dispenser program that tracks resources and revenue, for our purposes there will only be 3 types of coffee
# and we will only take from a quarter to a penny.
# v2: fixes from code review -> check resources BEFORE taking payment, validate the drink name,
# stop leaking globals into functions, and keep revenue out of the resources dict.

import sys
sys.stdout.reconfigure(encoding='utf-8') # so the emojis don't crash on non-utf8 terminals

# set up a global constant dict that contains a dictionary of each coffee and its attributes

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

# the ingredients a drink actually consumes (price lives in COFFEE too, but it isn't an ingredient)
INGREDIENTS = ('water', 'coffee', 'milk')

# accepted change
QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01

# global vars
# revenue is NOT a resource, so it gets its own variable instead of living inside the dict

resources = {
    'water': 300,
    'coffee': 100,
    'milk': 200
}

revenue = 0

# create functions for 'resource management', 'checking transaction' and 'checking stock'

def enough_resources(order):
    '''checks whether the machine can actually make THIS drink. returns True/False'''

    for item in INGREDIENTS:
        if resources[item] < COFFEE[order][item]:
            print(f"sorry, there is not enough {item} to make a {order}.")
            return False
    return True

def resource_mgm(order):
    '''subtracts the ingredients of the order from the resources'''

    for item in INGREDIENTS:
        resources[item] -= COFFEE[order][item]

def ask_for_coins(coin_name):
    '''asks for one coin type and keeps asking until the user types a valid whole number'''

    while True:
        try:
            amount = int(input(f"how many {coin_name}?\n"))
        except ValueError:
            print('please enter a whole number.')
            continue

        if amount < 0:
            print("you can't insert a negative number of coins.")
            continue

        return amount

def coins():
    '''processes the user's coins and returns the total inserted'''

    total_quarters = ask_for_coins('quarters')
    total_dimes = ask_for_coins('dimes')
    total_nickels = ask_for_coins('nickels')
    total_pennies = ask_for_coins('pennies')

    return (total_quarters * QUARTER) + (total_dimes * DIME) + (total_nickels * NICKEL) + (total_pennies * PENNY)

def transaction(order, payment):
    '''returns how much the payment differs from the price.
    negative means the user underpaid, zero or more is the change owed'''

    return round(payment - COFFEE[order]['price'], 2)

def report():
    '''prints a report summary of the current machine resources'''

    print('\n' * 20)
    print(f"the current water level: {resources['water']} ml")
    print(f"the current milk level: {resources['milk']} ml")
    print(f"the current coffee level: {resources['coffee']} grams")
    print(f"the current revenue: ${revenue:.2f}")

def coffee_machine(order):
    '''the logic of the machine. takes payment only after confirming the drink can be made'''

    global revenue

    # check the stock BEFORE asking for any money
    if not enough_resources(order):
        print('please pick something else.\n')
        return

    user_pay = coins()
    print('\nprocessing your order\n')
    change = transaction(order, user_pay)

    if change < 0:
        print("the amount you've deposited is less than the price")
        print('your payment has been refunded')
        print('please try again\n')
        return

    print('order completed')
    print(f"your change is ${change:.2f}")
    print('thank you for your order, enjoy your delicious coffee ☕\n')
    # only take the money and the ingredients if the transaction went through
    revenue += COFFEE[order]['price']
    resource_mgm(order)

# the working coffee machine

while True:

    print('welcome to your caffeine addiction corner ☕')
    user_input = input('please select your order: espresso $1.50 - latte $2.50 - cappuccino $3.00\n').strip().lower()

    # admin utility
    if user_input == 'report':
        report()
    elif user_input == 'stop':
        print('shutting down, see you next time.')
        break
    elif user_input in COFFEE:
        coffee_machine(user_input)
    else:
        print('invalid selection, please try again\n')

# completed
# self review v2:
# the resource check now runs against the specific drink ordered and happens before the machine
# takes any money, which is how a real machine behaves. a typo'd drink name no longer crashes
# the program, and coffee_machine() uses its own parameter instead of reaching for a global.
