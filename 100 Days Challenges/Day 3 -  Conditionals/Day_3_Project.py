# The Challenge is to create a treasure hunting narritve game with a series of choices that lead to either winning or losing the game.

print('welcome to treasure island!\nyour goal is to find the treasure!')
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************''') ### To add the ASCII art, make sure to incase them in triple qoutes.

choice_1 = 'you\'re at a cross road, where do you want to go?\nchoose: left or right '
choice_2 = 'you\'ve come at a lake, do you want to wait for a boat or swim across?\nchoose: wait or swim '
choice_3 = 'you arraive at the island and find a house with 3 doors, one is red, one is yellow and one is blue. which color door do you choose?\n type: red - yellow - blue '

choice_1 = input(choice_1)[0].lower()   # Input Normalization.

if choice_1 == 'l':
    choice_2 = input(choice_2)[0].lower()
elif choice_1 == 'r':
    print('you got kidnapped. gameover and goodluck escaping!')

if choice_2 == 'w':
    choice_3 = input(choice_3)[0].lower()
elif choice_2 == 's ':
    print('you don\'t know how to swim and drowned. gameover :(')

if choice_3 == 'y':
    print('congrats! you found the treasure chest!')
elif choice_3 == 'r' or choice_3 == 'b':
    print('you saw something you shouldn\'nt have seen and now you\'ve lost your mind! gameover!!')

# The hardest part about this is creating conditions that gives boundaries to the game. If anything other than those options is typed, the game breaks.
