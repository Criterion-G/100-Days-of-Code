# this is the solution Dr. Yu has created.
# her workflow is a follows:

# TODO1: write 4 functions, add, subtract, divide, and multiply

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

# TODO2: Add the functions to a dictionary as the values, with the keys being the operators

operations = {

    # since we are assigning the fucntions to the keys as values, we don't need to add the parentheses as we are not calling the functions yet

    '+': add,
    '-': subtract,
    '*': mult,
    '/': div
}

# TODO3: Functionality test, multiply 4 by 8 using the dictionary

operations['+'](4, 8)  # prints 32

# TODO4: The Operations

while True:

    num_1 = float(input('please type your first number\n'))
    accumlate = True

    while accumlate:
        operator = input('please choose your operator ( + , - , * , / )\n')
        num_2 = float(input('please type your next number\n'))

        answer = operations[operator](num_1 , num_2)

        print(f'{num_1} {operator} {num_2} = {answer}')

        choice = input('y to continue n to reset')

        if choice == 'y':
            num_1 = answer
        else:
            accumlate = False
            print('\n' * 100)
