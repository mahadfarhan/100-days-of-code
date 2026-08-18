# Day 18 — Hirst Painting

A Turtle graphics project built as part of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**.

This project generates a 10 × 10 grid of colored dots using Python's Turtle module and a predefined list of RGB color tuples.

## Features

- Uses a 255-based RGB color mode
- Randomly selects a color for each dot
- Draws 100 dots in a 10 × 10 grid
- Uses coordinate positioning to reset the Turtle at the start of each row
- Hides the Turtle after the painting is complete
- Keeps the window open until the user clicks

## Project Structure

```text
Day 18/
├── main.py
└── README.md
```

## How It Works

1. Turtle color mode is set to `255` so RGB tuples can be used directly.
2. A list of RGB colors is stored in `color_list`.
3. The Turtle starts near the lower-left area of the canvas.
4. A nested loop creates 10 rows.
5. Each row contains 10 dots.
6. Every dot receives a randomly selected color.
7. After completing a row, the Turtle is repositioned to the beginning of the next row.
8. Once all 100 dots have been drawn, the Turtle is hidden.

## Concepts Practiced

- Turtle graphics
- Nested loops
- RGB color tuples
- Random selection
- Coordinate positioning
- Variables and state updates
- Pen control
- Working with graphical windows

## Implementation Notes

Rather than physically navigating the Turtle back to the beginning of each row using heading changes, this implementation tracks the row coordinates and uses `setpos()` to reposition the Turtle directly.

The grid itself is represented naturally using nested loops: one loop for the rows and one loop for the dots within each row.

## Course Attribution

The project concept and exercise originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this project was written independently by me.**
