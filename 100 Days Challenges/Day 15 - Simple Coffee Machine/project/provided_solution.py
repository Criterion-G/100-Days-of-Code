# this is the provided solution by the instructor

# machine variables
COFFEE = {
    'espresso':
    {
        'ingredients': {
            'water': 50, # ml
            'coffee': 18, #g
            'milk': 0,
        },
        'price': 1.5
    },
    'latte':
    {
        'ingredients': {
            'water': 200,
            'coffee': 24,
            'milk': 150, #ml
        },
        'price': 2.5
    },
    'cappuccino':
    {
        'ingredients': {
            'water': 250,
            'coffee': 24,
            'milk': 100,
        },
        'price': 3
    }
}

resources = {
    'water': 300,
    'coffee': 100,
    'milk': 200
}

revenue = 0

# function
def is_resource_sufficient(order_ingredient):
    ''' checks if the resources are available and returns False if not and Ture if yes '''

    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f'sorry, there is not enough {item}')
            return False
    return True

def process_coins():
    ''' returns the total monetary value of all the inserted coins '''
    total = 0
    print('please insert coins.')
    total += int(input('how many quarters? ')) * 0.25
    total += int(input('how many dimes? ')) * 0.1
    total += int(input('how many nickles? ')) * 0.05
    total += int(input('how many pennies? ')) * 0.01
    return total

def transactoin_check(money_recieved, drink_price):
    ''' returns True if the payment is successful and False if not '''

    global revenue
    change = round(money_recieved - drink_price, 2)

    if money_recieved >= drink_price:
        revenue += drink_price
        print(f'here is your change: {change}')
        return True
    else:
        print('sorry, that is not enough money. money refunded')
        return False

def make_coffee(drink_name, order_ingredients):
    ''' manages resources and 'makes' coffee'''

    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'thank you, here is your {drink_name}')

# the running machine    
is_on = True

while is_on:

    choice = input('What would you like? (espresso - latte - cappuccino)\n')

    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f'{resources['water']} ml') 
        print(f'{resources['coffee']} mg') 
        print(f'{resources['milk']} ml')
        print(f'{revenue}$')
    else:
        drink = COFFEE[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if transactoin_check(payment, drink['price']):
                make_coffee(choice, drink['ingredients'])
