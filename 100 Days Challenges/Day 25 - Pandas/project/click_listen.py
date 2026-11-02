# this is how Anglea got the image coordinates for each state

import turtle as t

# Our Screen Object
image = r'100 Days Challenges\Day 25 - Pandas\project\blank_states_img.gif'
screen = t.Screen()
screen.title('US States Game')
screen.addshape(image)
t.shape(image)

def get_mouse_click_cor(x, y):
    ''' prints the coordiante when clicking on the screen object 
    has to call the onscreenclick method '''
    print(x, y)

t.onscreenclick(get_mouse_click_cor)

screen.mainloop() # the opposite of exit on click, keeps the screen open
