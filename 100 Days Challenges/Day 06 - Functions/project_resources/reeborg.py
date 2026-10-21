# list of commands I created for reeborg that passed the tasks and this file is not meant to run.

# reeborg's pre defined functions
def turn_left():
    return None
def move():
    return None
def at_goal():
    return None  # returns 'True' when reeborg is at the goal of the hurdle.
def wall_in_front():
    return None
def front_is_clear():
    return None
def wall_on_right():
    return None
def right_is_clear():
    return None

# Functions created for hurdles.
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_around()
    turn_left()
    
# def jump():         <<< Deprecated
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# changed the jump function to be able to solve this hurdle as well as the previous ones
def jump():
    '''makes the jump function more dynamic'''
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

# Hurdle 1

def hurdle(movements):
    for i in range(1,movements+1):
        move()
        jump()
        
hurdle(6)

# Hurdle 2
while not at_goal():  # at_goal returns 'True' when reeborg reaches the goal. So by using not, it will evaluate to 'True' when he's not at the goal and 'False' when he is thus breaking the loop when he reaches the goal.
    move()
    jump()

# Hurdle 2 if the at_goal() function is not available

num_hurdles = 6 # for example
while num_hurdles > 0:
    move()
    jump()
    num_hurdles -= 1

# Hurdle 3

while not at_goal():
    if wall_in_front():
        jump()
    elif front_is_clear():
        move()

# Hurdle 4
# the solution is the same as hurdle 3, the change happened in the jump function

while not at_goal():
    if wall_in_front():
        jump()
    elif front_is_clear():
        move()

# THE MAZE

# this is my first attempt, but it's not complete:

def move_forward():
    if front_is_clear() and right_is_clear():
        turn_right()
    else:
        while front_is_clear():
            move()
            
while not at_goal():
    move_forward()
    if right_is_clear():
        turn_right()
    elif wall_in_front() and not right_is_clear():
        turn_left()

