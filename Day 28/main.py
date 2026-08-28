from tkinter import *
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

checkmarks_list = []
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    global timer
    global checkmarks_list

    if timer is not None:
        window.after_cancel(timer)
    checkmarks_list = []
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    reps = 1
    start_btn.config(state=NORMAL)
    timer = None


# ---------------------------- TIMER MECHANISM ------------------------------- #

reps = 1


def breaks():
    checkmarks_list.append("✔")
    check_marks.config(text="".join(checkmarks_list))


def start_timer():
    global timer

    start_btn.config(state=DISABLED)

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1 and reps <= 7:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
    elif reps == 8:
        count_down(long_break_sec)
        title_label.config(text="Long break", fg=RED)
        breaks()

    elif reps == 9:
        timer = None
        reset_timer()
    else:
        count_down(short_break_sec)
        title_label.config(text="Short break", fg=PINK)
        breaks()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"

    if count_min == 0:
        count_min = "00"

    if type(count_sec) == int and count_sec < 10:
        count_sec = f"0{count_sec}"

    if type(count_min) == int and count_min > 0 and count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        reps += 1
        timer = window.after(1000, start_timer)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=1, column=1)

start_btn = Button(text="Start", bg="white", command=start_timer)
start_btn.grid(row=2, column=0)
end_btn = Button(text="Reset", bg="white", command=reset_timer)
end_btn.grid(row=2, column=2)

check_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 14))
check_marks.grid(row=3, column=1)

window.mainloop()
