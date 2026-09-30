# consider the following code:
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 or number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        else:
            print([number])

# i've found a couple of issues documented below, the fix:
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0: # here we should use and instead of or
            print("FizzBuzz")
        elif number % 3 == 0:                   # use elif instead of if, using if we cause the last else statement to be considered for the last if statment only
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)                       # the number vairable was wrapped in square brackets making it output a list instead of an integer



