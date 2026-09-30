# create the max function using for loops and conditionals.

scores = [72, 18, 95, 41, 67, 9, 88, 54, 30, 100, 46, 83,
                 12, 77, 63, 25, 90, 35, 58, 14, 98, 21, 69, 43,
                 81, 7, 56, 94, 39, 11, 74, 29, 87, 50, 66, 16,
                 92, 45, 62, 27, 99, 34, 59, 8, 76, 22, 84, 37, 71, 51]

# create a the max() function with a for loop.

highest_score = 0

for score in scores:
    if highest_score < score:  # or score > highest score <-- maybe this is more intutive.
        highest_score = score

print(highest_score)

## I did it! that was fun!

# The FizzBuzz Quiz:

for i in range(1,101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
