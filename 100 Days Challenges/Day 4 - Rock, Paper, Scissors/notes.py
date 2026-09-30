# We will rely heavily in this chapter on the random module
# This chpater also slightly explains modules, their functionalities and how to create one.
# The random module provided by Python is determinstic, it is basically used for simulations of random numbers and is not truly random.
# For security uses use the secrets module, and for truly random numbers we can use other modules and methods as well.

import random as rng

random_int = rng.randint(1, 100)

print(random_int)

rng.random() # this will return a random float between 0 and 1 and is the basic function that the random module relies on.
rng.uniform(1, 10) # this returns a random float between the range provided, inclusive of both numbers.

# Data Structures:
# Basic ones are:
#   Lists << Mutable
#   tuples << Immutable
#   dictionaries << Key Value pairs

# In this section we will cover lists.

fruits = ['cherry', 'orange', 'apple']
fruits[0] # indexing >> Returns the first data in the list.
fruits[0][3] # Indexing + Subscripting >> Returns the fourth element from thne first data in the lists.

fruits[0] = 'peach' # changes the first data in the list
fruits.append('cherry') # adds the appended data to the end of the list.
fruits.remove('orange') # removes any data that contains the specified object. Returns an error if there is no such object.
# there are many more methods. Read the documentation to know what is possible.
print(fruits)

# Dirty Dozen: nested lists.

fruits = ['strawberries', 'nectarines', 'apples', 'grapes', 'peaches', 'cherries', 'pears']
vegetables = ['spinach', 'kale', 'tomatoes', 'celery', 'potatoes']

dirty_dozen = [fruits, vegetables]

# to get nectarines using indexing from a nested list, we can first select the order of the list it is in then call it using it's index within said list as follow:

dirty_dozen[0][1] # this will return 'nectarines'
dirty_dozen[1][4] # this will return 'potatoes'

# we can also subscript them to get one of their letters or a data element:

dirty_dozen[0][1][3] # this will return 't'
dirty_dozen[1][4][-4] # this will return 't'
