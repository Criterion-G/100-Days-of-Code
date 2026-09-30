# the goal is to create a simple calculator that can perform basic arithmetic operations such as addition, subtraction, multiplication, and division. 
# the calculator should take two numbers and an operator as input from the user and return the result of the operation.
# we can utilize the return features that are available in functions to structure the whole project around.

def first_op(num_1, operation, num_2):
    '''
    this is exclusively for the first operation only which will return the result\n
    this is how you create a docsting
    '''
    if operation == '+':
        return num_1 + num_2
    elif operation == '-':
        return num_1 - num_2
    elif operation == '*':
        return num_1 * num_2
    elif operation == '/':
        return num_1 / num_2

def subsequent_ops(result, operation, num_2):
    if operation == '+':
        return result + num_2
    elif operation == '-':
        return result - num_2
    elif operation == '*':
        return result * num_2
    elif operation == '/':
        return result / num_2

# now the calculator

status = True
cumulative_result = 0
cumulative_result += first_op(float(input('please type the first number\n')), input('please select your desired operator ( + , - , * , / )\n'), float(input('please type the second number\n')))
# cumulative_result += first_op(511, '+', 511)
print(f'the result of the operation = {cumulative_result}')

while status is True:

    if input('do you want to continue? y or n\n') == 'n':
        status = False
    else:
        cumulative_result = subsequent_ops(float(cumulative_result), input('please select your desired operator ( + , - , * , / )\n'), float(input('please type the number\n'))) # this was a gotcha

    print(f'the result of the operation = {cumulative_result}')

first_op()
