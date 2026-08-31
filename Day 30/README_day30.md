# Day 30 — Errors, Exceptions & Improved Password Manager

Day 30 of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** focused on Python error handling, exceptions, JSON data storage, and improving the Password Manager project from Day 29.

This day included exception-handling exercises, an upgrade from plain-text storage to JSON, and a new search feature for retrieving saved credentials.

## What This Day Covers

- Python exceptions
- `try`
- `except`
- `else`
- `finally`
- `raise`
- `FileNotFoundError`
- `KeyError`
- `IndexError`
- `TypeError`
- JSON data storage
- `json.load()`
- `json.dump()`
- Updating structured data
- Recovering from missing files
- Searching stored credentials
- Improving an existing Tkinter project

## Folder Structure

```text
Day 30/
├── exercises/
│   └── main.py
├── improved password generator/
│   ├── main.py
│   ├── data.json
│   ├── data.txt
│   ├── logo.png
│   └── README.md
└── README.md
```

> A local `.venv` may also exist in the Day 30 folder, but it should not be committed to GitHub.

## Exception Handling Exercises

The exercises introduced common Python errors and how to handle them.

Examples included:

- Handling missing files with `FileNotFoundError`
- Handling missing dictionary keys with `KeyError`
- Demonstrating `IndexError`
- Demonstrating `TypeError`
- Using `else` after a successful `try`
- Using `finally`
- Raising custom exceptions with `raise`

These exercises established the concepts used later in the improved Password Manager.

## NATO Alphabet Note

The course also revisited the NATO phonetic alphabet project to add exception handling.

I skipped that section because I had already independently added `KeyError` handling to my Day 26 NATO project before the course formally introduced that improvement.

## Improved Password Manager

The Day 29 Password Manager was upgraded to use **JSON** instead of appending credentials to a plain-text file.

The application now stores data in a structured format and can search for previously saved website credentials.

## Features

- Website input
- Email/username input
- Password input
- Random password generation
- Clipboard copy for generated passwords
- Empty-field validation
- JSON-based credential storage
- Existing-data preservation
- Automatic creation of a new data structure when no JSON file exists
- Search button for retrieving saved credentials
- Missing-website handling
- Missing-data-file handling
- Case-normalized website storage and search
- Leading/trailing whitespace removal
- Automatic clearing of fields after saving

## JSON Storage

New entries are stored using the website as the dictionary key.

Example structure:

```json
{
    "example.com": {
        "email": "user@example.com",
        "password": "generated-password"
    }
}
```

When a new credential is saved:

1. The program attempts to open `data.json`.
2. Existing JSON data is loaded.
3. The new website entry is added with `.update()`.
4. If the file does not exist, a new dictionary is created.
5. The final dictionary is written back to `data.json` with indentation.

## Search Feature

The Search button allows the user to retrieve stored credentials by website name.

### How It Works

1. The website field is read.
2. The value is converted to lowercase and stripped of leading/trailing whitespace.
3. Blank input is rejected.
4. The program attempts to load `data.json`.
5. If the website exists, its saved email and password are displayed.
6. If the website has not been stored, the user is informed.
7. If the data file does not exist, an error message is shown.

Normalizing website names during both saving and searching prevents differences such as `Google`, `google`, and ` GOOGLE ` from being treated as separate entries.

## Concepts Practiced

- Exception handling
- Defensive programming
- `try` / `except`
- JSON
- Dictionaries
- Persistent structured data
- Data lookup
- File I/O
- Tkinter
- Message boxes
- User input validation
- String normalization
- Refactoring and extending an existing application

## Development Notes

This day builds directly on the Day 29 Password Manager.

The main improvement is the move from simple text-based storage to structured JSON data, which makes it possible to retrieve credentials by website rather than only appending entries to a file.

The final version also includes some small implementation choices beyond the base exercise, including normalizing website input with `.lower().strip()` so saved and searched website names behave consistently.

## Course Attribution

The Day 30 lesson structure, exception-handling exercises, Password Manager upgrade, and project concepts originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

The course also includes adding exception handling to the earlier NATO alphabet project; that portion was skipped because equivalent handling had already been implemented independently in my Day 26 version.

## Disclosure

This README was written with AI assistance.

**This project builds on guided course code and project structure from Dr. Angela Yu's course. Some challenge solutions, modifications, error handling, and implementation details were completed independently by me.**
