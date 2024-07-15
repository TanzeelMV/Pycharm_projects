# ---------------------------- CONSTANTS ------------------------------- #
import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    label.config(text="Timer", font=("Courier", 35, "bold"), bg=YELLOW, fg=GREEN)
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)
    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Long Break", font=("Courier", 35, "bold"), bg=YELLOW, fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Short Break", font=("Courier", 35, "bold"), bg=YELLOW, fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", font=("Courier", 35, "bold"), bg=YELLOW, fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + f"{count_sec}"
    if count_min < 10:
        count_min = "0" + f"{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check = ""
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            check += "✔"
        check_label.config(text=check)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW)
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(108, 138, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="Timer", font=("Courier", 35, "bold"), bg=YELLOW, fg=GREEN)
label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(text="", font=("Courier", 15, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

window.mainloop()
