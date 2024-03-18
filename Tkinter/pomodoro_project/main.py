import tkinter
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5#25
SHORT_BREAK_MIN = 1#5
LONG_BREAK_MIN = 2#20
reps = 0 #times run
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps +=1
    if reps%8 == 0:
        counter(WORK_MIN*60)
        timer_label.config(text="WORK", bg=GREEN, font=FONT_NAME)

    elif reps%2 == 0:
        counter(SHORT_BREAK_MIN*60)
        timer_label.config(text="BREATHER", bg=PINK, font=FONT_NAME)

    else:
        counter(LONG_BREAK_MIN*60)
        timer_label.config(text="BREAK", bg=RED, font=FONT_NAME)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def counter(time):
    min = time//60
    sec = time%60
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if time > 0:
        global timer
        timer = window.after(1000, counter, time-1)
    else:
        start_timer() #recursion
        mark = ""
        checks = float(reps/2)
        for i in range(checks):
            mark+=1
        check_label.config(text="mark")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title(string="pomodoro app")
window.config(bg=YELLOW)

canvas = Canvas(height=200, width=225, bg=YELLOW)
img = PhotoImage(file="tomato.png")
canvas.create_image(100,115, image=img)
canvas.place(x=450, y=220)
timer_text = canvas.create_text(100,115, text="00:00", font='bold')

timer_label = Label(text="TIMER", bg=YELLOW, font=FONT_NAME)
timer_label.place(x=500, y=200)

check_label = Label(text="TIMER", bg=YELLOW, font=FONT_NAME)
check_label.place(x=1000, y=800)


start_button = Button(text="start", bg=GREEN, font=FONT_NAME, command=start_timer)
start_button.place(x=300, y=200)

reset_button = Button(text="stop", bg=RED, font=FONT_NAME, command=reset_timer)
reset_button.place(x=800, y=200)



window.mainloop()