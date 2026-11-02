# Main file for the States gussing game.
# We'll use Turtle for the bg screen of the US
import pandas as pd
import turtle as t
import classes as c

# Create the data frame
states_df = pd.DataFrame(pd.read_csv(r'100 Days Challenges\Day 25 - Pandas\project\50_states.csv'))
print(states_df)

# A good habit is to get a quick glance at your data
print(states_df.head())
print(states_df.info())

# Our Screen Objects
image = r'100 Days Challenges\Day 25 - Pandas\project\blank_states_img.gif'
screen = t.Screen()
screen.title('US States Game')
screen.addshape(image)
t.shape(image)
scoreboard = c.Scoreboard()
state_writer = c.State_Writeer()

# The Game

while True:
    answer_state = screen.textinput(title= 'Guess the State',
                                    prompt= "enter your guess (or 'Exit' to quit):")

    # Cancel / closing the dialog returns None instead of a string
    if answer_state is None:
        break

    answer_state = answer_state.title()

    if answer_state == 'Exit':
        break

    if answer_state in states_df['state'].array:
        scoreboard.increase_score()
        state_writer.write_state(answer_state,
                                 states_df[states_df['state'] == answer_state]['x'].iloc[0],
                                 states_df[states_df['state'] == answer_state]['y'].iloc[0])

screen.bye()
