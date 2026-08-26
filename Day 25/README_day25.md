# Day 25 — Pandas & U.S. States Game

Day 25 of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** focused on working with CSV data using **Pandas** and applying those concepts in a larger interactive project.

This day included a mix of introductory Pandas exercises, a small data-analysis task using the Central Park Squirrel Census, and a final U.S. States guessing game powered by CSV data.

## What This Day Covers

- Reading CSV files with Pandas
- Working with Series and DataFrames
- Converting columns to Python lists
- Calculating averages and maximum values
- Filtering rows based on conditions
- Accessing rows and individual values
- Creating DataFrames from dictionaries
- Exporting DataFrames to CSV
- Counting categorical values
- Handling missing values
- Using structured data to drive an interactive application

## Folder Structure

```text
Day 25/
├── exercises/
├── squirrel central analysis/
├── us states game/
└── README.md
```

## Pandas Exercises

The exercises introduce the basic workflow for reading and manipulating CSV data with Pandas.

Topics practiced include:

- Loading data with `pandas.read_csv()`
- Accessing DataFrame columns
- Converting a Series to a Python list
- Using methods such as `.mean()` and `.max()`
- Filtering a DataFrame based on column values
- Converting temperature values
- Creating a DataFrame from a Python dictionary
- Exporting a DataFrame with `.to_csv()`

These exercises build the foundation used in the larger projects later in the day.

## Central Park Squirrel Analysis

This project uses data from the **2018 Central Park Squirrel Census** to count squirrels by primary fur color.

### How It Works

1. The squirrel census CSV is loaded into a Pandas DataFrame.
2. Missing fur-color values are ignored.
3. Unique fur-color categories are identified.
4. The number of squirrels in each category is calculated.
5. The results are stored in a new DataFrame.
6. The final counts are exported to `squirrel_count.csv`.

The project also includes an alternative implementation using Pandas' `value_counts()` method.

## U.S. States Game

The final project combines **Pandas** with Python's **Turtle** graphics module to create an interactive geography game.

The player tries to name all 50 U.S. states, and each correct answer is written directly onto the map.

### Features

- Interactive state guessing
- Case-normalized and trimmed user input
- Duplicate-answer prevention
- CSV-backed state lookup
- Coordinate-based placement of state names
- Live score displayed in the input prompt
- Win message after all states are guessed
- Graceful exit when the input window is closed
- Automatic generation of a CSV containing missed states

### How It Works

1. The state data is loaded from `50_states.csv`.
2. The `state` column is converted into a list of valid answers.
3. The player enters a state name through a Turtle input dialog.
4. Valid answers are matched against the DataFrame.
5. The matching row is used to retrieve the state's `x` and `y` coordinates.
6. The state name is written onto the map at the correct position.
7. Correct answers are tracked to prevent duplicates.
8. If all states are guessed, a win message is displayed.
9. If the player exits early, the program identifies every state that was not guessed.
10. Those states are exported to `missing_states.csv` for later review.

## Concepts Practiced

- Pandas
- DataFrames
- Series
- CSV files
- Data filtering
- `.iloc`
- `.loc`
- `.unique()`
- `.dropna()`
- `.value_counts()`
- Boolean comparisons
- Data aggregation
- Data export
- Turtle graphics
- User input
- Input validation
- Lists and loops
- Combining data processing with application logic

## Development Notes

This day marks a shift from basic file handling into working with structured tabular data.

The Pandas exercises focus on learning the library itself, the squirrel analysis applies those tools to a real dataset, and the U.S. States game demonstrates how CSV data can become part of an interactive program rather than simply being analyzed or printed.

The U.S. States game also generates `missing_states.csv`, turning the game into a simple study tool by producing a list of the states the player did not remember.

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**
