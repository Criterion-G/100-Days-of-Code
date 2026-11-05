# Create a unit conversion tool with a GUI
from tkinter import *

PADDING = 30

def unit_convert():
    convert_answer.config(text= f'{round(float(user_input.get()) * 1.609344, 2)}')

# The Window Object
window = Tk()
window.title('Miles to Kilometers Converter')
window.config(padx= PADDING, pady= PADDING)
window.minsize(width= 500, height= 300)

# The Labels
input_title = Label(text='Type in the Miles:')
input_title.config(padx=PADDING , pady=PADDING ,font=('Arial', 18, 'bold'))
input_title.grid(column=0, row=0)

convert_title = Label(text='Kilometers are:')
convert_title.config(padx=PADDING , pady=PADDING ,font=('Arial', 18, 'bold'))
convert_title.grid(column=0, row=2)

convert_answer = Label(text='')
convert_answer.config(padx=PADDING , pady=PADDING ,font=('Arial', 18, 'bold'))
convert_answer.grid(column=1, row=2)


# Input Box
user_input = Entry()
user_input.grid(column=1, row=0)
user_input.config(font=('Arial', 18, 'normal'))

# The Convert Button
convert_button = Button()
convert_button.config(text='calculate', command= unit_convert)
convert_button.grid(column=1, row= 1)

window.mainloop()

# Challenge completed in less than 30 mins.
# I can come back to this later and add more features like different options for different units.. etc.
