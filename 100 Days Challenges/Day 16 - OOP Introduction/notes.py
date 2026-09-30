# All the previous days were what's called 'Procedual Programming' where it follows a procedure from top to bottom and calling functions that produce outputs.
# Python is an Object Oriented Programming language. Meaning it orgnizes the code around 'objects' rather than just functinos and logic 'procedual'.
# OOP is an essential part of many modern design patterns such as factory patterns and others.
# OOP bundles data and behaviour into objects; class = blueprint, object = an instance of the blueprint, each have attributes and methods.
# The benifits of OOP include organization, reusability, abstraction, encapsulation, inheritance, polymorphism and eaiser maintance and teamwork.
# You can you different modules which are essentially a group of objects that add funcationlities to your programs. Facilitating teamwork and orgainzing the work across multiple people in an easier way.
# Also, most of the libraries of Python are premade objects that serve a certian purpose and are reusable across many different projects.

# Classes:
# A class is the blueprint that multiple objects can be created from. The objects created from a class are instances of that class
# Objects have:
# Attribues = what the object has (variables for the object). 
# Methods = what the object does (functions for the object).

# let's look at some examples:

# this is the class that define the blueprint from the object. and we can create as many objects from this blueprint as we want
# the naming convention for classes is Pascal Case
class CarBlueprint():
    wheels = 4
    max_speed = 200 #km/h
    doors = 4
    colors = ['black', 'white', 'blue', 'red', 'brown']
    engine = 'petrol'

# now let's create an object from that class. this is called instantiating.

tuarus = CarBlueprint() # now an object has been create from that blueprint or class

print(type(tuarus)) # printing this will return the wrpping identifying it as a class
print(isinstance(tuarus, CarBlueprint)) # shows if the object is an instance of the class by retruning a boolean
