# For Loops
# Standard example for a for loop:

fruits = ['apple', 'peach', 'pear']
for fruit in fruits:
    print(fruit)

# # the 'fruit' is the itrable variable, and you can name it whatever you want, but it's better to have a clear name for your variable. It basically assigns that to you iterable for each iteration.

# for i in fruits:
#     print(i)
#     print(fruits)  # Will print the list over how many iterables we have.

# Creating a sum function

student_score = [72, 18, 95, 41, 67, 9, 88, 54, 30, 100, 46, 83,
                 12, 77, 63, 25, 90, 35, 58, 14, 98, 21, 69, 43,
                 81, 7, 56, 94, 39, 11, 74, 29, 87, 50, 66, 16,
                 92, 45, 62, 27, 99, 34, 59, 8, 76, 22, 84, 37, 71, 51]

score_func = sum(student_score) # the built-in Python function.

total_score = 0
for score in student_score:     # this is more or less how the sum function is created.
    total_score += score

print(score_func)  # both should return the same value.
print(total_score)

# The range function and loops:
# the range function by itself doesn't output anything even if you print it.
print(range(1, 10))
# because it by itself is a class.
# but, we can utilize its functionality to do something we it. In this case assigning it to a list for example using for loops:

range_100 = []
for i in range(1 , 101):                                  # the range function is exclusive of the highest number.
    range_100.append(i)

print(sum(range_100))
# we can then sum it up to simulate the gauss challenge.
# or just do it from the loop immediately as such

range_100 = 0
for i in range(1, 101):
    range_100 += i

print(range_100)

# you can also specifiy how many times do you want to step in the range as such

for i in range (1,11, 3): # the last argument is how many times you want to 'step'
    print(i)
