import random as rng

# Task 1: create a heads or tails program based on random numbers.

# coin = rng.random()

# if coin <= 0.5:
#     print('heads')
# else:
#     print('tails')

# or:

# coin = rng.randin(0,1)

# if coin == 0:
#     print('heads')
# else:
#     print('tails')

# Task 2: Using lists, try to create a program that selects randomly from a list. Who's gonna pay the bill for example?

friends = ['faisal', 'ibrahim', 'abdullah', 'saud', 'hatim', 'fahad']

num_friends = len(friends) # Counts the number of data within a data structure. Not exclusive to ints or strings.
select_friennd = rng.randint(0, num_friends - 1) # We can just hard code the indexes of course, but this is more dynamic.

print(friends[select_friennd])

# Or: we can use random.choice()

random_choice = rng.choice(friends) # Much cleaner.
print(random_choice)
