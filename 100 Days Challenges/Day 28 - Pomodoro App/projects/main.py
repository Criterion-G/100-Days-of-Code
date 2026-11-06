from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = '✓'

# ---------------------------- VARIABLES ------------------------------- #
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_button():
    global reps
    reps = 0

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    if reps > 0:
        count_min = math.floor(count / 60)
        count_sec = count % 60
        # we can do the following because Python is a strongl dynamically typed language. Read for further info: https://stackoverflow.com/questions/11328920/is-python-strongly-typed
        if count_sec < 10:
            count_sec = f'0{count_sec}'
        else:
            count_sec

        canvas.itemconfig(timer_text, text= f'{count_min}:{count_sec}')

        if count > 0:
            window.after(1000, countdown, count -1) # the counter
        else:
            start_timer()
            marks = ''
            work_sessions = math.floor(reps/2)
            for _ in range(work_sessions):
                marks += '✓'
            check.config(text= marks)
    else:
        canvas.itemconfig(timer_text, text='25:00')
        pom_title.config(text='Timer', fg= GREEN)
        check.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        pom_title.config(text= 'Long Break', bg= YELLOW, fg= RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        pom_title.config(text= 'Short Break', bg= YELLOW, fg= PINK)
    else:
        countdown(work_sec)
        pom_title.config(text= 'Work', bg= YELLOW, fg= GREEN)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=80, pady=50, bg= YELLOW)
window.minsize(width= 500, height= 500)

pom_title = Label(text='Timer', font=(FONT_NAME,'36','bold'), bg= YELLOW, fg= GREEN)
pom_title.grid(column= 3, row= 0)

canvas = Canvas(width= 250, height= 274, bg= YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file= r'100 Days Challenges\Day 28 - Pomodoro App\projects\tomato.png')
canvas.create_image(120, 130, image= tomato_img)
timer_text = canvas.create_text(120, 150, text='25:00', fill='white', font= (FONT_NAME, '24', 'bold'))
canvas.grid(column= 3, row= 2)
check = Label(font= ('Arial','14', 'bold'), bg= YELLOW, fg= GREEN, highlightthickness=0)
check.grid(column=3, row= 3)
start = Button(text= 'start' ,command= start_timer)
start.grid(column=0, row= 3)
reset = Button(text= 'reset' ,command= reset_button)
reset.grid(column=4, row= 3)

window.mainloop()
