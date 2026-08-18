# Day 17 — Quiz Game

A command-line quiz game built as part of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**.

This project uses object-oriented programming to represent quiz questions as objects and manage quiz state, scoring, and question progression through a dedicated quiz controller.

## Features

- Loads quiz data from a separate data module
- Converts raw question data into `Question` objects
- Presents questions one at a time
- Accepts `True` or `False` answers
- Checks each answer against the correct answer
- Tracks the current question number
- Tracks the user's score
- Displays feedback after every question
- Displays the final score when the quiz is complete

## Project Structure

```text
Day 17/
├── main.py
├── data.py
├── question_model.py
├── quiz_brain.py
└── README.md
```

### `main.py`

Builds the question bank from the quiz data, creates the `QuizBrain` object, runs the quiz loop, and displays the final result.

### `data.py`

Stores the quiz questions and answers as structured dictionary data.

### `question_model.py`

Contains the `Question` class, which represents an individual question with its text and correct answer.

### `quiz_brain.py`

Contains the `QuizBrain` class, which manages:

- The current question number
- The score
- The question list
- Question progression
- User input
- Answer checking
- Quiz completion

## Concepts Practiced

- Object-oriented programming
- Classes and objects
- Constructors
- Attributes and methods
- Passing objects between classes
- Lists of objects
- Dictionaries
- Multiple Python modules
- Loops and conditionals
- User input
- Score tracking
- Separating data, models, and program logic

## Program Flow

1. Quiz data is loaded from `data.py`.
2. Each dictionary entry is converted into a `Question` object.
3. The resulting objects are stored in a question bank.
4. A `QuizBrain` object receives the question bank.
5. The quiz continues while unanswered questions remain.
6. Each answer is checked immediately.
7. The current score is displayed after every question.
8. Once all questions have been answered, the final score is shown.

## Course Attribution

The project concept and exercise originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this project was written independently by me.**
