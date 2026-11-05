from tkinter import * # helps us not type the name of the module or an alias, just call the class.

def button_clicked():
    label.config(text= user_input.get())
    print('i got clicked')

window = Tk()
label = Label(text= 'the screen label, used with pack', font= ('Arial', 24, 'bold'))
window.title('My First GUI.. YAY') # title attribute
window.minsize(width= 800, height= 500) # size attribute
window.config(padx= 20, pady= 20) # adding padding for the screen
label.pack(side= 'left', expand= True)
button = Button(text='click me', command= button_clicked) # the command kwarg is an event listener that we can pass in a function for the button to do.

label.config(text= 'new text')
label.pack()
button.pack(side= 'left', expand= True)

# challenge, change the label text when clicking the button
def label_change():
    label.config(text= 'the button was pressed')
button = Button(text= 'click to change the label', command= label_change)
button.pack(side= 'left', expand= True)

# Entry()
# class for taking an input from the GUI

user_input = Entry(width= 40)
user_input.pack(side= 'bottom', expand= True)
print(user_input)
print(type(user_input))

# Layout Managers
# pack()
# place()
# grid()
# notes on each in the layout_manager.py file.

# challenge, change the label with whatever gets typed in the Entry object and pressing the button
# changed in the first button above and the button_clicked function

window.mainloop() # this method will keep the window always open and should always be at the end of the program
