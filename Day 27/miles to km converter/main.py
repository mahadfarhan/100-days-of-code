from tkinter import *

FONT = ("Arial", 12)
BG_COLOR = "white"


def calculate_km():
    try:
        num = round(float(user_input.get()) / 0.621371, 2)
    except ValueError:
        num = "Sorry, that isn't acceptable."

    label_3.config(text=num)


window = Tk()
window.config(bg=BG_COLOR)
window.title("Miles to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

user_input = Entry(width=10)
user_input.grid(column=1, row=0, pady=10, padx=20)

label_1 = Label(text="Miles", font=FONT, bg=BG_COLOR)
label_1.grid(column=2, row=0)

label_2 = Label(text="is equal to", font=FONT, bg=BG_COLOR)
label_2.grid(column=0, row=1)

label_3 = Label(text=0, font=FONT, bg=BG_COLOR)
label_3.grid(column=1, row=1)

label_4 = Label(text="Km", font=FONT, bg=BG_COLOR)
label_4.grid(column=2, row=1)

button = Button(text="Calculate", bg=BG_COLOR, command=calculate_km)
button.grid(column=1, row=2, pady=10)

window.mainloop()
