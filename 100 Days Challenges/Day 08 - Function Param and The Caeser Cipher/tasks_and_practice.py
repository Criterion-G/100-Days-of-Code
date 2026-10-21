# create a greet function that prints three statements
from datetime import datetime

def greet(user, location):                   # user = parameter
    today = datetime.today()
    print(f'hello {user}!')
    print(f'today is {today}')
    print(f'have a magnificant day in {location}!')

greet('faisal', 'riyadh')                    # 'faisal' the arguement for the parameter.. and the agrumentsin Python are positional arguments by default.

def life_in_weeks(current_age, life_expactancy):
    years_remaining = life_expactancy - current_age
    weeks_remaining = years_remaining * 52 #weeks

    print(f'you have {int(round(weeks_remaining,0))} weeks remaining.')

life_in_weeks(29, 150)

# since Python by default has postional arguments, you can override that with the use of Keyword Arguments.
# you simply specifiy the paratmeter of the function with an equal sign and just type your argument.

greet('riyadh', 'faisal')                  # positional arguments
greet(location= 'riyadh', user= 'faisal')  # if you use one keyword argument and the other is just positional argument then you'll get a syntax error.

# love calculator challenge

def love_calculator(name_1, name_2):

    t_score = 0
    l_score = 0

    check_var = (name_1 + name_2).lower()

    for letter in check_var:
        if letter in 'true':
            t_score += 1
    for letter in check_var:
        if letter in 'love':
            l_score +=1

    print(str(t_score) + str(l_score))


love_calculator('kanye west', 'kim kardashian')
