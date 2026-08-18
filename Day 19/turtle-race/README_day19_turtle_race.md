# Day 19 — Turtle Race

A Turtle graphics racing game built as part of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**.

The player chooses a turtle color, then six turtles race across the screen using randomized movement until one reaches the finish line.

## Features

- Six racing turtles with different colors
- User betting through a Turtle graphics input dialog
- Input validation for valid turtle colors
- Randomized movement for each racer
- Finish-line detection
- Winner announcement
- Win/loss feedback based on the user's bet

## Controls

The user selects one of the available turtle colors:

- Indigo
- Blue
- Green
- Yellow
- Orange
- Red

The race then runs automatically.

## Project Structure

```text
turtle-race/
├── main.py
└── README.md
```

## How It Works

1. A Turtle graphics window is created.
2. Six Turtle objects are generated and placed at different vertical positions.
3. Each Turtle is assigned a unique color.
4. The user is prompted to choose which turtle they think will win.
5. Invalid guesses are rejected until a valid color is entered.
6. During the race, each turtle moves forward by a random distance.
7. The first turtle to reach the finish line wins.
8. The program compares the winner's color with the user's bet and displays the result.

## Concepts Practiced

- Turtle graphics
- Multiple objects
- Lists
- Loops
- Randomization
- User input
- Input validation
- Object attributes and methods
- Coordinate checking
- Game state
- Event-driven graphical programs

## Implementation Notes

All six Turtle objects are stored in a list and updated repeatedly during the race. Each racer receives a random movement distance on every pass through the loop, creating a different result each time the program runs.

The winner is detected by checking when a turtle's x-coordinate reaches the finish line.

## Course Attribution

The project concept and exercise originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this project was written independently by me.**
