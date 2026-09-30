# in this day we will learn how to create classes and finish by creating a quiz game using OOP

class User:         # the naming convention of classes is the PascalCase. Everything else follows a snake_case naming convention
    def __init__(self, user_id, user_name): # this is the constructor that initialize the class. this special function will always be called when you create an object from the class.
        print('new user created!')
        self.id = user_id
        self.user_name = user_name
        self.followers = 0 # in this case we have created a default attribute that starts at zero, and since we didn't declare in the constructor param it always starts at zero and is not required when creating the object
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    # in addition to creating attributes for the class, the second thing we can create are methods, which are functions associated with the class

# the self paramater is refers to any object being created from the class. so user_1 will be user_1.paramaters
# after the self parameter, we can add as many other paramaters as we want which all will be passed to the object being created

class Car:
    def __init__(self, seats, engine):
        print('car being created')
        self.seats = seats # in the car_1 object below, it will essential be this line of code (car_1.seats = 2)
        self.engine = engine # when we create an object from this class, these attributes will be assigned with any parameter passed during the class call
        self.mode = 'normal'
        print(f'created car with {seats} seats and a {engine} engine')

    def enter_race_mode(self):
        self.mode = 'race mode'

car_1 = Car(2, 'V8')
car_1.enter_race_mode()
print(car_1.mode)

user_1 = User('001', 'faisal') # to initialize the instance of the object we have to call the class with the paranthsies
user_2 = User('002', 'nada')
# user_1.id = '001'
# user_1.username = 'faisal' # these are the attributes, variables associated with the object

# in the above the attributes are declared and assigned from the variable itself, which is something we can do, but it's better if we want to create multiple instances
# of that class is to create the attributes by initializing the class and adding the attributes there.
# this is made by something called the Constructor, or as it is known in programming 'initializing'

print(user_1.user_name)
print(user_1.id)
user_1.follow(user_2) # you have to call the class itself for the method to work
print(f'following: {user_1.following}')
print(user_2.user_name)
print(f'followers: {user_2.followers}')

# any paramater declared in the constructor function is required when creating an instance of the class (creating an object)
