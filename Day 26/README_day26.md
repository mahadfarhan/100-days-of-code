# Day 26 — List Comprehensions, Dictionary Comprehensions & NATO Alphabet

Day 26 of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** focused on writing more concise Python using **list comprehensions** and **dictionary comprehensions**, then applying those concepts to existing and new projects.

This day included an improved version of the U.S. States game and a NATO phonetic alphabet converter built with Pandas and comprehensions.

## What This Day Covers

- List comprehensions
- Dictionary comprehensions
- Conditional comprehensions
- Iterating over Pandas DataFrames
- Building dictionaries from structured data
- Transforming user input into new data
- Refactoring earlier loop-based code
- Basic exception handling with `try` / `except`
- Handling invalid dictionary lookups

## Folder Structure

```text
Day 26/
├── improved us states/
├── NATO alphabet/
└── README.md
```

## Improved U.S. States Game

The U.S. States game from the previous day was revisited and simplified using list comprehensions.

The game still:

- Loads state data from a CSV file
- Accepts state guesses through Turtle
- Prevents duplicate answers
- Looks up state coordinates from a Pandas DataFrame
- Writes correct answers onto the map
- Tracks progress toward all 50 states
- Generates a CSV containing missed states when the player exits

### Refactoring

The previous loop used to build the list of missed states was replaced with a list comprehension:

```python
missing_states = [state for state in state_list if state not in correct_answers]
```

This keeps the same behavior while expressing the filtering operation more directly.

## NATO Phonetic Alphabet Converter

The NATO project converts user input into its corresponding phonetic alphabet code words.

### How It Works

1. The NATO phonetic alphabet CSV is loaded into a Pandas DataFrame.
2. A dictionary comprehension converts the table into a dictionary where each letter is a key and each phonetic code word is its value.
3. The user enters their name.
4. The input is converted to uppercase and stripped of leading/trailing spaces.
5. A list comprehension converts each character into its NATO phonetic equivalent.
6. If an invalid character is entered, a `KeyError` is caught.
7. The program identifies the invalid character and asks the user to enter their name again.

### Dictionary Creation

```python
nato_dict = {row.letter: row.code for (_, row) in df.iterrows()}
```

### Phonetic Conversion

```python
user_name_phonetics = [nato_dict[letter] for letter in user_name]
```

## Error Handling

The final version of the NATO converter uses `try` / `except` to handle invalid characters.

If a character does not exist in the NATO dictionary, the resulting `KeyError` is caught and the user is told which character caused the problem before being prompted again.

This allows the program to recover cleanly instead of crashing.

## Concepts Practiced

- List comprehensions
- Dictionary comprehensions
- Conditional filtering
- Pandas
- DataFrames
- `.iterrows()`
- Dictionary lookups
- CSV files
- User input
- String normalization
- `try` / `except`
- `KeyError`
- Refactoring
- Reusing and improving earlier projects

## Development Notes

This day focused less on building a large new application and more on learning how to express common looping and transformation patterns more concisely.

The improved U.S. States game demonstrates refactoring an existing loop into a list comprehension, while the NATO project combines Pandas, dictionary comprehensions, list comprehensions, and error handling in a small standalone program.

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**
