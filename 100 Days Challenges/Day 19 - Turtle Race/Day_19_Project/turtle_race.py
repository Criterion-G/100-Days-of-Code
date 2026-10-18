# create a turtle racing game
# requirementes:
#   - a betting feature
#   - multiple turtles
#   - race end
#   - winning condition

import turtle as t
import random as rng
# lighter shades of the main colors, picked to stand out on a light grey background

turtle_colors = {
    "red": (255, 105, 97),
    "orange": (255, 179, 71),
    "yellow": (240, 200, 60),
    "green": (119, 221, 119),
    "blue": (100, 149, 237),
    "purple": (177, 156, 217),
    "pink": (255, 145, 175),
    "cyan": (80, 200, 220),
    "teal": (64, 180, 170),
    "lime": (170, 220, 80),
    "magenta": (230, 120, 220),
    "brown": (190, 140, 100),
    "coral": (255, 127, 102),
    "gold": (230, 185, 50),
    "sky blue": (110, 190, 240),
    "lavender": (190, 170, 240),
    "mint": (110, 210, 170),
    "salmon": (250, 150, 130),
    "turquoise": (70, 210, 200),
    "indigo": (120, 120, 210),
}

turtle_names = [
    "Shell Shocked",
    "Usain Bolt-ed Down",
    "Speedy Boi (Ironic)",
    "Turbo, Legally Speaking",
    "Lightning McSlow",
    "Sir Loin of Lettuce",
    "Michael Shellumacher",
    "The Flash (Citation Needed)",
    "Grandmaster Crawl",
    "Yertle the Turtle",
    "Shelldon Cooper",
    "Leonardo (He Chose Violence)",
    "Mach 0.0001",
    "Tortoise Hayes",
    "Snapchat",
    "Reptar Jr.",
    "Hard Shell Drive",
    "Zoom Meeting",
    "Koopa Troopa Tax Evader",
    "Finish Line? Never Heard of Her",
]

screen = t.Screen()
screen.colormode(255)
screen.bgcolor('grey20')
screen.setup(0.6, 0.8)
starting_pos = (-(screen.window_width() / 2) + 50, 0)
finish_line = (screen.window_width() / 2) - 100 # dynmaic screen race area

LANE_HEIGHT = 40 # vertical room each turtle needs so the lanes never overlap

def max_racers():
    """how many turtles actually fit on screen, and how many we have names/colors for"""
    fits_on_screen = int(screen.window_height() // LANE_HEIGHT)
    return max(2, min(fits_on_screen, len(turtle_colors), len(turtle_names)))

def ask_turtle_count(limit):
    while True:
        answer = input(f'how many turtles in the race? (2-{limit}) ')
        if not answer.isdigit():
            print('please enter a whole number.')
            continue
        count = int(answer)
        if count < 2:
            print('a race needs at least 2 turtles.')
        elif count > limit:
            print(f'this screen only has room for {limit} turtles.')
        else:
            return count

def lane_positions(num_turtles):
    """y values spread evenly across the screen height, with equal gaps at the top and bottom"""
    spacing = screen.window_height() / (num_turtles + 1)
    top = screen.window_height() / 2
    return [top - spacing * (lane + 1) for lane in range(num_turtles)]

def turtle_select(num_turtles):
    in_race = {}
    while len(in_race) < num_turtles:
        color_select = rng.choice(list(turtle_colors.items()))
        name_select = rng.choice(turtle_names)
        if color_select[1] not in in_race.values() and name_select not in in_race:
            in_race[name_select] = color_select[1]
    return in_race

def create_turtles(t_select: dict):
    turtles = {}
    for turtle, color in t_select.items():
        turtles[turtle] = t.Turtle()
        turtles[turtle].color(color)
        turtles[turtle].shape('turtle')
    return turtles

def draw_finish_line():
    finish_draw_t = t.Turtle()
    finish_draw_t.shape('turtle')
    finish_draw_t.pencolor('white')
    finish_draw_t.teleport(finish_line, screen.window_height() / 2)
    finish_draw_t.setheading(270)
    finish_draw_t.speed('fastest')
    finish_draw_t.forward(10000)

racer_limit = max_racers()
number_turtles = ask_turtle_count(racer_limit)

race_turtles = create_turtles(turtle_select(number_turtles)) # create the turtles with their names and colors

# line them up, one turtle per evenly spaced lane
for turtle, lane_y in zip(race_turtles.values(), lane_positions(number_turtles)):
    turtle.teleport(starting_pos[0], lane_y)

draw_finish_line()



screen.exitonclick()
