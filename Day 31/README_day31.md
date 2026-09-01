# Day 31 — Flash Card Learning App

Day 31 of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** was the capstone project for the Tkinter section.

This project combines GUI programming, data handling, file persistence, Pandas, and timed events to create a French vocabulary flashcard application.

Unlike some earlier guided projects, this capstone was implemented independently from a provided project specification. The course supplied the required assets and learning objectives, while the application logic and implementation were developed independently.

## What This Day Covers

- Tkinter GUI development
- Canvas widgets
- Image handling
- Event-driven programming
- Timed callbacks with `after()`
- Pandas DataFrames
- CSV file handling
- Converting DataFrames into dictionaries
- Random selection
- Persistent learning progress
- Dynamic UI updates
- Button state management

## Project Structure

```text
Day 31/
├── data/
│   ├── french_words.csv
│   └── words_to_learn.csv
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
└── main.py
```

## Flash Card Learning App

The application helps users learn French vocabulary by displaying French words, allowing time to think, and then revealing the English translation.

When a word is marked as correctly learned, it is removed from the remaining learning list so the user can focus on words they still need to practice.

## Features

- Random French word selection
- Automatic card flipping after a delay
- French card front
- English card back
- Correct and incorrect answer buttons
- Removal of learned words
- Progress saving through CSV files
- Loading previous progress if available
- Button state control
- Custom card graphics and UI assets

## How It Works

The application first attempts to load `words_to_learn.csv`. If it does not exist, it loads the original `french_words.csv` dataset.

The vocabulary data is converted into a list of dictionaries:

```python
cards = df.to_dict(orient="records")
```

A random card is selected and displayed. After a delay using Tkinter's `after()` method, the card flips to reveal the English translation.

When the user marks a card as correct:

1. The card is removed from the remaining vocabulary list.
2. The updated list is saved.
3. A new card is displayed.

## Concepts Practiced

- Tkinter
- Canvas
- `PhotoImage`
- GUI event handling
- Callback functions
- `after()`
- Pandas
- CSV files
- DataFrames
- Dictionary conversion
- Random selection
- File persistence
- State management
- Dynamic UI updates

## Development Notes

This project was a major step beyond simple GUI exercises because it required managing application state:

- tracking the current card
- controlling timed transitions
- updating the learning pool
- saving progress between sessions
- managing button availability

The project was completed by implementing the provided requirements independently rather than copying a complete solution.

## Course Attribution

The project specification, learning objectives, vocabulary dataset, image assets, and design resources originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance.

**The assets and data files used in this project were provided by the course. The application logic, GUI implementation, data handling, and functionality were independently implemented by me based on the provided project requirements.**
