# Day 34 — Quizler: API Integration, OOP & Tkinter

Day 34 of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** revisited the quiz project originally built on Day 17 and significantly expanded it.

The original quiz logic was developed as the Day 17 project. For Day 34, that project was transformed into a GUI application, connected to a live API, and reorganized using classes and multiple modules.

## What This Day Covers

- Working with APIs
- HTTP requests with `requests`
- JSON data
- API query parameters
- Tkinter GUI development
- Object-oriented programming
- Classes and objects
- Multiple Python modules
- Type hints
- Event-driven programming
- Callback functions
- Dynamic GUI updates
- Button state management
- Delayed callbacks with `after()`
- Score tracking
- HTML entity decoding

## Project Structure

```text
Day 34/
├── images/
│   ├── false.png
│   └── true.png
├── data.py
├── main.py
├── question_model.py
├── quiz_brain.py
└── ui.py
```

## Quizler

The project is a True/False quiz application that retrieves questions from the **Open Trivia Database API** and presents them through a Tkinter GUI.

The application separates the quiz into several components:

- `data.py` — retrieves quiz questions from the API
- `question_model.py` — defines the `Question` object
- `quiz_brain.py` — manages quiz state and answer checking
- `ui.py` — handles the Tkinter interface
- `main.py` — connects the components together

## API Integration

The application requests ten True/False questions from the Open Trivia Database API:

```python
parameters = {"amount": 10, "type": "boolean"}

response = requests.get(
    url="https://opentdb.com/api.php",
    params=parameters
)
response.raise_for_status()
data = response.json()
```

The returned JSON data is then passed into the rest of the application.

This was one of the major additions to the original quiz.

## Object-Oriented Structure

The project uses separate classes for different responsibilities.

### `Question`

`Question` objects store the question text and correct answer.

### `QuizBrain`

`QuizBrain` manages the state of the quiz.

It tracks the current question number, question list, and current question. It also handles moving through the quiz and checking answers.

### `QuizInterface`

`QuizInterface` is responsible for the graphical interface.

It creates and manages the Tkinter window, question canvas, score display, True/False buttons, question transitions, visual feedback, and final score.

## GUI Behavior

When the quiz starts, the first question is displayed and both answer buttons are enabled.

When the user selects an answer:

1. Both buttons are disabled.
2. The selected answer is checked.
3. The score is updated if the answer is correct.
4. The canvas changes color to indicate correct or incorrect feedback.
5. After one second, the next question is displayed.

The delay is implemented using:

```python
self.window.after(1000, self.get_next_question)
```

## Score Tracking

The interface maintains a score counter that updates after each correct answer.

At the end of the quiz, the question area is replaced with the user's final score.

## HTML Entity Handling

Some questions returned by the API contain HTML entities. The quiz brain handles these with:

```python
html.unescape(self.current_question.text)
```

so encoded characters are displayed correctly.

## Development History

### Day 17 — Original Quiz

The original quiz was built as a Day 17 project. The underlying quiz solution from that project was my own implementation and is preserved in the repository's Day 17 work.

### Day 34 — Major Upgrade

Day 34 took that existing project and substantially expanded it.

The Day 34 implementation includes:

- Replacing the original question source with an API
- Fetching live quiz questions
- Converting the quiz into a Tkinter GUI
- Adding True/False image buttons
- Adding visual correct/incorrect feedback
- Adding score display
- Adding timed question transitions
- Splitting the application across multiple modules
- Introducing the `Question`, `QuizBrain`, and `QuizInterface` classes
- Handling HTML entities returned by the API

These Day 34 modifications and implementations were completed independently based on the course requirements and the existing Day 17 project.

## Concepts Practiced

- APIs
- HTTP requests
- JSON
- Query parameters
- `requests`
- Tkinter
- Classes
- Objects
- Multiple modules
- Type hints
- State management
- Event-driven programming
- Callbacks
- `after()`
- GUI feedback
- Score tracking
- HTML entity decoding

## Development Notes

This project was particularly useful because it required combining several concepts that had previously been learned separately.

The API supplies the data, the `Question` class represents individual questions, `QuizBrain` manages the quiz state, and `QuizInterface` presents everything to the user.

The result is a much more complete application than the original Day 17 command-line quiz.

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**

**The original Day 17 quiz implementation was written by me. For Day 34, the API integration, GUI conversion, button behavior, visual feedback, quiz state integration, modular structure, and other updates were independently implemented by me based on the course requirements.**
