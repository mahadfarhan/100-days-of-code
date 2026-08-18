# Day 19 — Etch-a-Sketch

A keyboard-controlled Turtle graphics project built as part of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**.

This project uses event listeners to control a Turtle with the keyboard, allowing the user to move, turn, and reset the drawing screen interactively.

## Features

- Move forward with `W`
- Move backward with `S`
- Turn left with `A`
- Turn right with `D`
- Reset the screen with `C`
- Uses keyboard event listeners
- Keeps the Turtle window active until the user clicks to close it

## Controls

| Key | Action |
|---|---|
| `W` | Move forward |
| `S` | Move backward |
| `A` | Turn left |
| `D` | Turn right |
| `C` | Reset the screen |

## Project Structure

```text
Day 19/
├── main.py
└── README.md
```

## How It Works

1. A `Turtle` and `Screen` object are created.
2. Separate functions are defined for movement and rotation.
3. Keyboard keys are bound to those functions using `screen.onkeypress()`.
4. `screen.listen()` enables keyboard input.
5. The Turtle responds to user input in real time.
6. Pressing `C` resets the Turtle graphics screen.
7. The program remains open until the user clicks the window.

## Concepts Practiced

- Event-driven programming
- Keyboard event listeners
- Functions as arguments
- Turtle movement
- Turtle rotation
- User interaction
- GUI event handling

## Course Attribution

The project concept and exercise originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this project was written independently by me.**
