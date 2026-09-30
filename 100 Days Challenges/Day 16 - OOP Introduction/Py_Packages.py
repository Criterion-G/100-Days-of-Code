# this will demonstrate different packages that other dev have created with their own objects.
# PyPi: a package index that is a repo of software for Python. URL: https://pypi.org/

# we will use the Pretty Table Package to organize data into an ASCII formatted table
from prettytable import PrettyTable # we can late look at the source code by using the definition command of VS Code if we want. here we'll just improt the prettytable class from the package.

table_instance = PrettyTable()  # here we create an object instance of the pretty table class

# methods:
# we can do it column by column:
table_instance.add_column('pokemon name', ['pikachu', 'squirtle', 'charmander'])
table_instance.add_column('type', ['electric', 'water', 'fire'])
print(table_instance)

# delete to show the other method
table_instance.clear()

# or we can do it in one go:
table_instance.field_names = ['pokemon name', 'type']
table_instance.add_rows(
    [
        ['pikachu', 'electric'],
        ['squirtle', 'water'],
        ['charmander', 'fire']
    ]
)

print(table_instance)
print(type(table_instance))

# it is important to note that this package is only to visualize how data looks in a terminal, it is not used for data structuring.

# attributes:
# changing the attributes of the instance of the class
table_instance.align = 'l'
table_instance.title = 'popular pokemon'

print(table_instance)
