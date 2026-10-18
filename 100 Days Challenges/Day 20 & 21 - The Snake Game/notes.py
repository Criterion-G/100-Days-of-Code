# In Day 20 we'll start the first part of creating the Snake Game. Part 2 will be in Day 21.
# Requirements:
# - Snake Body
# - Movement (WASD or Arrow Key)
# - Randomly generated dot for the snake to eat (detect collision with the food)
# - Keep track of the score
# - Game end (hitting the wall or its own body)
# - Growing functionalitty
# - Goal: Eat as much as you can
# Optional:
# - Balance
# - Win Condition

# For this, I'll try to follow along with the lessons instead of going overboard.
# later I can enhance it by making the screen dynamic or any other enhancements.
# I the idea is that the snake itself should be a class, and the food, and the scoreboard.

# We will also learn about inheretance for classes and slicing.

# class inheratince: taking attributes or methods from a class into a newer class

class Animal:
    def __init__(self):
        self.eyes = 2
        self.skin = True

    def breath(self):
        print('inhale, exhale')

class Fish(Animal):
    def __init__(self):
        super().__init__() # inherent the constructor

    def underwater_breath(self):
        super().breath() # inheret a method
        print('but underwater')

fish = Fish()
print(fish.underwater_breath())

# slicing
# a concpet that I don't really remember about slicing is that you can increment as in the following:
rand_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(rand_list[7::2])
# or
print(rand_list[2:5:2])
