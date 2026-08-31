from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(4, 6))]
    password_list += [choice(numbers) for _ in range(randint(3, 5))]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():

    website = website_entry.get().lower().strip()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showinfo(
            title="oops", message="Please don't leave any empty fields!"
        )
    else:
        try:
            with open("./improved password generator/data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data

        with open("./improved password generator/data.json", "w") as file:
            json.dump(data, file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_website():
    website = website_entry.get().lower().strip()
    if website == "":
        messagebox.showinfo(
            title="error",
            message="Please enter the website you wish to search for.",
        )
    else:
        try:
            with open("./improved password generator/data.json", "r") as file:
                website_dict = json.load(file)

                if website in website_dict:
                    messagebox.showinfo(
                        title=website,
                        message=f"Email: {website_dict[website]["email"]}\nPassword: {website_dict[website]["password"]}",
                    )
                else:
                    messagebox.showinfo(
                        title="error",
                        message=f"The website {website} has not been stored yet.",
                    )
        except FileNotFoundError:
            messagebox.showerror(title="error", message="No Data File Found.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Main image

lock_img = PhotoImage(file="./improved password generator/logo.png")
canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Entry fields

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="we")
email_entry.insert(0, "mahad@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="we")

# Labels

website_label = Label(
    text="Website: ", font=("Arial", 10, "normal"), bg="white", highlightthickness=0
)
website_label.grid(row=1, column=0)

email_label = Label(
    text="Email/Username: ",
    font=("Arial", 10, "normal"),
    bg="white",
    highlightthickness=0,
)
email_label.grid(row=2, column=0)

password_label = Label(
    text="Password: ", font=("Arial", 10, "normal"), bg="white", highlightthickness=0
)
password_label.grid(row=3, column=0)

# Buttons

password_button = Button(
    text="Generate Password",
    bg="white",
    highlightthickness=0,
    command=generate_password,
)
password_button.grid(row=3, column=2, sticky="we")

add_button = Button(
    text="Add", bg="white", highlightthickness=0, width=36, command=save_data
)
add_button.grid(row=4, column=1, columnspan=2, sticky="we")

search_button = Button(
    text="Search", highlightthickness=0, bg="white", command=search_website
)
search_button.grid(row=1, column=2, sticky="we")

window.mainloop()
