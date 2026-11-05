from tkinter import *

# pack()
# the pack layout manager 'packs' every element as you spceifiy it on top of each other or next to each other. not very flexable
pack_win = Tk()
pack_win.title('the pack manager')
pack_win.minsize(width= 800, height= 500)

pk_label_1 = Label(pack_win,text= 'Text 1')
pk_label_2 = Label(pack_win,text= 'Text 2')
pk_label_3 = Label(pack_win,text= 'Text 3')
pk_label_4 = Label(pack_win,text= 'Text 4')
pk_label_1.pack()
pk_label_2.pack()
pk_label_3.pack(side= 'left')
pk_label_4.pack(side= 'left')

# grid()
# the middle ground between the others, and probably the best because of it
# it divides the screen into rows and columns where we specifiy where each element lives with column and row numbers 
grid_win = Tk()
grid_win.title('the grid manager')
grid_win.minsize(width= 800, height= 500)

grd_label_1 = Label(grid_win, text= 'Text 1')
grd_label_2 = Label(grid_win, text= 'Text 2')
grd_label_3 = Label(grid_win, text= 'Text 3')
grd_label_4 = Label(grid_win, text= 'Text 4')
grd_label_1.grid(column= 5, row= 0)
grd_label_2.grid(column= 2, row= 0)
grd_label_3.grid(column= 0, row= 5)
grd_label_4.grid(column= 0, row= 2)

# place()
# using x and y coordinates. more persice but more that's it's downside if you have a lot of widgets.
place_win = Tk()
place_win.title('the place manager')
place_win.minsize(width= 800, height= 500)

plc_label_1 = Label(place_win, text= 'Text 1')
plc_label_2 = Label(place_win, text= 'Text 2')
plc_label_3 = Label(place_win, text= 'Text 3')
plc_label_4 = Label(place_win, text= 'Text 4')
plc_label_1.place(x= 0, y= 0)
plc_label_2.place(x= 100, y= 0)
plc_label_3.place(x= 0, y= 100)
plc_label_4.place(x= 0, y= 100)

pack_win.mainloop()
grid_win.mainloop()
place_win.mainloop()
