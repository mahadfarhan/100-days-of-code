# Day 29 — Password Manager

Day 29 of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** focused on building a desktop **Password Manager** with Tkinter.

This project combines GUI development, file handling, input validation, confirmation dialogs, randomized password generation, and clipboard integration.

## What This Day Covers

- Tkinter GUI development
- Entry fields and labels
- Buttons and callback functions
- Canvas and images
- Input validation
- Message boxes
- File writing
- Random password generation
- List comprehensions
- String joining
- Clipboard integration with `pyperclip`
- Focus management
- Basic desktop app workflow

## Project Structure

```text
Day 29/
├── main.py
├── logo.png
├── data.txt
└── README.md
```

> A local `.venv` may also exist in the project folder, but it should not be committed to GitHub.

## Password Manager

The application allows the user to enter a website, email/username, and password, then save those credentials to a text file.

It also includes a built-in password generator.

## Features

- Website input field
- Email/username input field
- Password input field
- Default email value
- Automatic focus on the website field
- Random password generation
- Generated passwords automatically copied to the clipboard
- Empty-field validation
- Confirmation dialog before saving
- Credential storage in `data.txt`
- Automatic clearing of the website and password fields after a successful save
- Custom logo displayed in the interface

## Password Generation

The password generator is based on a project originally introduced earlier in the course on Day 5.

For this Day 29 project, the generator code was provided as part of the course materials because the earlier version had been completed separately. The generator was then used inside the Tkinter application and adapted with concepts covered later in the course, including list comprehensions.

Generated passwords contain a random mixture of:

- Uppercase letters
- Lowercase letters
- Numbers
- Symbols

The generated characters are shuffled before being combined into the final password.

Once generated, the password is:

1. Inserted into the password field.
2. Copied automatically to the clipboard using `pyperclip`.

## Saving Credentials

When the user presses **Add**:

1. The website, email, and password fields are read.
2. The program checks that no field is empty.
3. If a field is missing, an information dialog is displayed.
4. If all fields contain data, a confirmation dialog shows the entered credentials.
5. If the user confirms, the credentials are appended to `data.txt`.
6. The website and password fields are cleared for the next entry.

Stored entries follow this format:

```text
Website | Email | Password
```

## Concepts Practiced

- Tkinter
- GUI event handling
- Callback functions
- Entry widgets
- Canvas
- `PhotoImage`
- Grid layouts
- Message boxes
- Input validation
- File I/O
- Append mode
- Randomization
- List comprehensions
- `shuffle()`
- `join()`
- Clipboard access
- Application state
- Basic UX improvements

## Development Notes

This project was completed as a guided course project rather than as an entirely independent build.

The overall project skeleton and structure for Day 29 were provided by Dr. Angela Yu as part of the course. The password generator itself originated from an earlier Day 5 project and was supplied again for use in this project.

Some portions of the final implementation differ from the instructor's version because challenge sections were solved independently or implemented differently. The password-generation logic was also adapted using list comprehensions.

## Course Attribution

The Day 29 project concept, project skeleton, instructional structure, and supplied password-generator code originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance.

**This project is not entirely original code. The project skeleton and some code, including the supplied password-generator base, were provided by Dr. Angela Yu as part of the course. Some challenge solutions, modifications, refactoring choices, and implementation details were completed independently by me.**
