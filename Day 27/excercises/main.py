from tkinter import *


def button_clicked():
    change_text = user_input.get()
    my_label["text"] = change_text


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Buttons

button1 = Button(text="Click Me", command=button_clicked)
button1.grid(column=1, row=1)

button2 = Button(text="Click Me please")
button2.grid(column=2, row=0)
# entry

user_input = Entry(width=10)
user_input.grid(column=3, row=2)

window.mainloop()
