# create the simplified coffee machince from day 15 using OOP. there are pre made classes and functions attahced to this folder used to create the coffee machine
import money_machine
import menu
import coffee_maker

MENU = menu.Menu()
coffe_machine = coffee_maker.CoffeeMaker()
money = money_machine.MoneyMachine()

is_on = True

while is_on:

    print(f'welcome, please choose your order.')
    choice = input(f'What would you like? {MENU.get_items()}\n')

    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffe_machine.report()
        money.report()
    else:
        drink = MENU.find_drink(choice)
        if coffe_machine.is_resource_sufficient(drink):
            payment = money.make_payment(drink.cost)
            if payment:
                coffe_machine.make_coffee(drink)

# self review:
# using pre made code made entirely of classes made me create the same coffee machine in just 10 minutes, 5 of them was only me reading and understanding the packages.
# I think this the point the instructor is trying to make here, how easy it is to create things using pacakges and understanding how they work.
# it also shows the power of OOP and how the abstraction it provides makes this easier.
# abstraction is not without its disadvantages, but for now and for my current level, it's all upside.
