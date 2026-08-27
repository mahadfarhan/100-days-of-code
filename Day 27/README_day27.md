# Day 27 — Tkinter, *args/**kwargs & Miles to Km Converter

Day 27 of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** focused on building graphical user interfaces with **Tkinter**, while also introducing flexible function arguments with `*args` and `**kwargs`.

This day included Tkinter widget exercises, experimentation with variable-length arguments, and a final GUI project that converts miles into kilometers.

## What This Day Covers

- Creating windows with Tkinter
- Labels
- Buttons
- Entry fields
- Text widgets
- Spinboxes
- Scales
- Checkbuttons
- Radiobuttons
- Listboxes
- Event-driven programming
- Callback functions
- Grid-based layouts
- Widget configuration
- `*args`
- `**kwargs`
- Flexible class initialization
- Basic GUI input validation

## Folder Structure

```text
Day 27/
├── exercises/
│   ├── main.py
│   ├── Other_Tkinter_Widgets.py
│   └── playground.py
├── miles to km converter/
│   └── main.py
└── README.md
```

## Tkinter Exercises

The Tkinter exercises introduce the fundamentals of building interactive desktop interfaces.

Topics practiced include:

- Creating a `Tk()` window
- Setting window titles and dimensions
- Creating labels and buttons
- Reading user input from an `Entry`
- Updating widget text dynamically
- Using `.grid()` for layout
- Registering callback functions with buttons
- Exploring additional Tkinter widgets

The widget reference file demonstrates a wider range of Tkinter controls, including text boxes, spinboxes, scales, checkbuttons, radiobuttons, and listboxes.

## `*args` and `**kwargs`

The playground exercises demonstrate how Python can accept a flexible number of positional and keyword arguments.

### `*args`

Used to collect an arbitrary number of positional arguments.

### `**kwargs`

Used to collect keyword arguments into a dictionary.

The exercises also demonstrate using `.get()` inside a class constructor so optional values can safely default to `None`.

## Miles to Km Converter

The final project is a small desktop GUI that converts a distance in miles into kilometers.

### Features

- User input through a Tkinter `Entry`
- Button-triggered conversion
- Conversion result displayed inside the GUI
- Rounded output to two decimal places
- Invalid input handling with `try` / `except`
- Grid-based widget positioning
- Reusable font and background constants

### How It Works

1. The user enters a number of miles.
2. Pressing the **Calculate** button calls the conversion function.
3. The program reads the value from the input field.
4. The value is converted from miles to kilometers.
5. The result is rounded to two decimal places.
6. The output label is updated with the converted value.
7. If the user enters invalid input, the GUI displays an error message instead of crashing.

## Concepts Practiced

- Tkinter
- GUI programming
- Event-driven programming
- Callback functions
- Widget configuration
- Grid layouts
- User input
- Input validation
- Exception handling
- `*args`
- `**kwargs`
- Flexible function parameters
- Flexible class constructors
- Constants
- Separating interface behavior into functions

## Development Notes

This day builds naturally on earlier Turtle projects by moving further into event-driven programming.

Instead of controlling graphical objects directly, the program now responds to GUI events such as button presses and text input.

The Miles to Km converter also adds basic error handling so invalid input is handled gracefully rather than terminating the program.

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**
