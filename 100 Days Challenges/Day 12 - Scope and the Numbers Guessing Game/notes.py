# local and global scope

# the key difference between a global and a local scope is where you define you variable
# if you define it within an object, like a function, then its scope will be local. Meaning,
# it can only be called within the function itself and not outside.

# global variables as they're not a part of any object
player_health = 100
player_strenght = 5

def strengh():
    player_strenght = 10
    print(f'{player_strenght}')

strengh()   # this will print the local variable's value
print(f'{player_strenght}')  # this will print the global variable's value

# the key takeaway from this is that the local varaible is treated as sperate from a global variable.
# meaning that it will not change the value of the global variable itself

# the global and local scope doesn’t apply to variables only, it also applies to anything within the namespace

def dexterity():
    def increase_dex():     # a local variable with a local namespace. it will not be recognized in the global scope
        dex = 20            # a local varaible within a local function
        return dex

    print(increase_dex())

# increase_dex()              # both will throw an error as they are a part of a local scope
# print(dex)

print(dexterity())

# you define the scope of a namespace based on where you have defined it. so it pays to pay attention to this.

# unlike other languages, python doesn't have a block scope.
# having no block scope basically means that a variable you define within a block of regular code,
# like loops and if statements, will be considered with the scope of the block itself. Meaning,
# if the loop or if statement are not encased in a function for example, then the variable will be
# global

game_level = 5
enemies = ['skele boi', 'decomposing boi', 'tentical boi']

if game_level < 6:
    new_enemy = enemies[0]

print(new_enemy)  # this is perfectly valid because the variable defined is a global one

game_level = 15
if game_level < 10:
    weak_enemy = enemies[0:2]  # the key thing here is that if the condition is not met, then the variable will never be created anyway
print(new_enemy)
# print(weak_enemy)               # this will throw an error because you are calling a variable that isn't defined.

# we can use the 'global' statement to allow a function to modify a global scope
def vitality():
    global player_health # if we comment out this line and call the function it will return a scope error
    player_health += 50

vitality()
print(player_health)
# this is generally considered bad practice and it's advised to avoid it if possible.

# if we want to do this however, we can utilize the return statements within a function and it's the best practice in this case
def vitality_2(health):
    return health + 50

player_health = vitality_2(player_health)
print(player_health)

# now there is a global variable and there is a global constant
# the difference is that for global constants, you define the variable and never want to change it.
# there is no specific command for it, but there is a naming convention,
# when you want to create a global constant you define the variable name in all caps

PI = 3.14
GOOGLE = 'https://www.google.com/'
AUTHOR_NAME = 'faisal'
author_age = 29

# in this, we maybe would want to change the age within the code
author_age += 1


