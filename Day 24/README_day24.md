# Day 24 — Files, Directories & Mail Merge

Day 24 of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** focused on working with files and directories in Python.

This day was a mix of smaller file I/O exercises, an update to the existing Snake game to add persistent high-score storage, and a final Mail Merge project.

## What This Day Covers

- Reading from text files
- Writing to text files
- Appending to existing files
- Creating new files
- Working with relative file paths
- Using `with open(...)`
- Converting file contents into usable Python data
- Persisting data between program runs
- Updating an existing project with file-based storage
- Generating multiple output files from a template

## Folder Structure

```text
Day 24/
├── exercises/
├── updated_snake/
├── Mail Merge Project/
└── README.md
```

## Exercises

The exercises introduce basic file input and output.

Examples include:

- Reading the contents of a text file
- Appending new text to an existing file
- Creating and writing to a new file
- Practicing relative file paths

These exercises establish the file-handling concepts used later in the Snake update and Mail Merge project.

## Updated Snake Game — Persistent High Score

The existing Snake game was updated so that the high score persists even after the program is closed.

### Changes

- The scoreboard reads the saved high score from `data.txt` when the game starts.
- When the current score exceeds the saved high score, the new value is written back to the file.
- Colliding with a wall or the snake's tail now resets the round instead of ending the program.
- The snake is rebuilt at its starting position after a reset.
- The current score returns to zero while the high score remains saved.

### Persistence

The high score is stored in:

```text
updated_snake/data.txt
```

This means the score survives between separate executions of the program rather than existing only in memory.

## Mail Merge Project

The final project generates personalized letters automatically from a template and a list of names.

### Project Structure

```text
Mail Merge Project/
├── Input/
│   ├── Letters/
│   │   └── starting_letter.txt
│   └── Names/
│       └── invited_names.txt
└── Output/
    └── ReadyToSend/
```

### How It Works

1. The program reads the invited names from `invited_names.txt`.
2. `.splitlines()` converts the file contents into a list of individual names.
3. The starting letter is read once and stored as a template.
4. The program loops through each invited person.
5. `[name]` in the template is replaced with the current person's name.
6. A separate personalized `.txt` file is created for each recipient.

This allows one template to generate multiple ready-to-send letters automatically.

## Concepts Practiced

- File I/O
- Context managers
- `read()`
- `write()`
- Append and write modes
- `.splitlines()`
- String replacement
- Relative paths
- Persistent program state
- Reading and writing numeric data
- Reusing previous projects
- Automation through file generation

## Development Notes

This day differs from some of the previous project-focused days because it combines several smaller exercises with improvements to an existing project and a separate final project.

The exercises introduce the underlying file-handling concepts, the Snake update demonstrates persistent storage in an existing application, and the Mail Merge project applies the same ideas to simple automation.

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**
