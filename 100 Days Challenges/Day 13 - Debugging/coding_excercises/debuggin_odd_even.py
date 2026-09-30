# consider the following code
def odd_or_even(number):
    # if number % 2 = 0:                  # it is immediately obvious thanks to intellisense that this is an assignment and not an equals operator
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."
