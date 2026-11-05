# Main Concpets to Learn for Today's Lesson are:
# Tinkter GUI, Default Arguments, *args and **kwargs

# Tikter
# The default built-in GUI library for python that allows us to create GUI for our programs
import tkinter as tk

window = tk.Tk()
label = tk.Label(text= 'the screen label, used with pack', font= ('Arial', 24, 'bold'))
window.title('My First GUI.. YAY') # title attribute
window.minsize(width= 800, height= 500) # size attribute
label.pack(side= 'left', expand= True) # required attribute to pack labels. It's a geometry management system that helps with padding the layout. Read docs: https://www.tcl-lang.org/man/tcl8.6/TkCmd/pack.htm
window.mainloop() # this method will keep the window always open and should always be at the end of the program

# Default Arguments, Args and Kwargs
# They are arguments set with a default value to start off with.

def greet_na(name, age= None):
    '''setting this as a default value will pass in whatever we give as the default. Which then we can change if we want when calling the function by passing in the value we want by the keyword.
    one of the main reasons it is used is to make the argument optional by setting a default value that can be changed.'''
    print(name)

greet_na('faisal')

# Args and Kwargs are variable argumnets that allows functions to have flexibility in terms of how it works and what passes in them.
# Args are positional arguments while kwargs are keyword arguments.

# *args
# args just basically create a tuple with all the elements you pass in the posiontion of args
def add(*args):
    n = 0
    for x in args:
        n += x
    print(n)

add(1,3,3,4,5,6,3,6)

def greet(*args):
    '''returns the args and its type'''
    for name in args:
        print(f'hello, {name}!')
        print(type(args))
        print(args)
        print(args[1])

greet('faisal', 'nada')

# **kwargs
# **kwargs create a dictionary with your arguments
def calculate(n, **kwargs):
    n *= kwargs['multiply'] # the method get will return none if the key doesn't exist in the dictionar, making the arguments optional and don't need to be passed in.
    n += kwargs['add']
    n /= kwargs['divide']
    print(n)

calculate(5, multiply= 5, add= 0, divide= 1) # if we just want to use on operation

def info(**kwargs):
    '''defining a keyword at that time of calling the function will throw out a type error. Keywords are a requirment in a kwargs function'''
    for key, value in kwargs.items():
        print(f'{key}: {value}')
        print(type(kwargs))
        print(kwargs)

info(name= 'Faisal', age= 29, city= 'Riyadh')

def complete_info(name, *args, age= None, **kwargs):
    '''all of the together in action'''
    print(f'name: {name}')
    print(f'age: {age}')
    print('Other Info:')
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f'{key}: {value}')

complete_info('faisal', 'loves gaming', 'enjoys coding', 'passionate about learning', age= 29, city= 'Riyadh',)

# We can create classes with args and kwargs such as the ones used in the tkinter module
class Car:
    def __init__(self, **kwargs):
        # the get method returns none if the key doesn't exist in the dictionary, making it an optional argument.
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.color = kwargs.get('color')
        self.seats = kwargs.get('seats')

my_car = Car(make= 'BMW')
print(my_car.make)
print(my_car.model)
