from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
SLEEP_TIME = 3000

# Pulling data from csv

try:
    df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("./data/french_words.csv")
cards = df.to_dict(orient="records")

# functions


def choose_random_word():
    random_selection = random.choice(cards)
    return random_selection


def correct_choice():
    cards.remove(current_card)
    new_df = pd.DataFrame(cards)
    new_df.to_csv("./data/words_to_learn.csv", index=False)
    start_new_card()


def incorrect_choice():
    start_new_card()


def show_side(image, text, fill):
    canvas.itemconfig(canvas_image, image=image)
    canvas.itemconfig(language_text, text=text, fill=fill)
    canvas.itemconfig(word_text, text=current_card[text], fill=fill)


def set_button_state(state):
    correct_btn.config(state=state)
    wrong_btn.config(state=state)


def flip_card():
    show_side(card_back_img, "English", "white")
    set_button_state(NORMAL)


def start_new_card():
    global current_card
    current_card = choose_random_word()
    show_side(card_front_img, "French", "black")
    window.after(SLEEP_TIME, flip_card)
    set_button_state(DISABLED)


# window

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50, width=900, height=626)

# images

correct_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

# canvas

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263)
canvas.grid(row=0, column=0, columnspan=2)

# text

language_text = canvas.create_text(400, 150, fill="black", font=("Arial", 40, "italic"))

word_text = canvas.create_text(
    400,
    263,
    fill="black",
    font=("Arial", 60, "bold"),
)

# buttons

correct_btn = Button(
    image=correct_img,
    highlightthickness=0,
    bg=BACKGROUND_COLOR,
    bd=0,
    command=correct_choice,
)
correct_btn.grid(row=1, column=0)
wrong_btn = Button(
    image=wrong_img,
    highlightthickness=0,
    bg=BACKGROUND_COLOR,
    bd=0,
    command=incorrect_choice,
)
wrong_btn.grid(row=1, column=1)

start_new_card()

window.mainloop()
