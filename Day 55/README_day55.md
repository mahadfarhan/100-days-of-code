# Day 55 — Flask URL Routing & Higher or Lower Game

Day 55 of **100 Days of Code: The Complete Python Pro Bootcamp** builds on the introduction to Flask by exploring dynamic URL routes, HTML responses, and decorators that modify the output of view functions.

The exercises include a Flask application demonstrating different routes and custom HTML-formatting decorators, followed by a **Higher or Lower** number-guessing game that responds to guesses entered directly in the URL.

## Features

- Creates web applications using Flask
- Defines multiple endpoints with `@app.route()`
- Returns HTML headings, paragraphs, and images from Flask view functions
- Uses URL variables to pass values into Python functions
- Uses Flask's `<int:...>` converter to receive integers from URLs
- Creates decorators that wrap and format a function's return value
- Stacks multiple decorators on a single route
- Generates a random target number between 0 and 9
- Compares a URL-based guess against the target number
- Displays different text colors and GIFs for low, high, and correct guesses
- Runs Flask's development server with debug mode enabled

## Technologies Used

- Python
- Flask
- `random`
- Python decorators and nested functions
- HTML
- Inline CSS
- Dynamic URL routing

## Exercises

### Flask Routes & HTML Decorators (`exercises/main.py`)

The first exercise defines several routes, each returning a different response.

The home route returns HTML rather than plain text:

```python
@app.route("/")
def hello_world():
    return (
        "<h1 style='text-align: center'>Hello, World!</h1>"
        "<p> This is a paragraph </p>"
        "<img src='...'>"
    )
```

This demonstrates how a Flask route can send HTML markup that the browser renders as a formatted page.

#### Custom HTML Decorators

Three decorators modify the string returned by a function:

- `make_bold()` wraps the response in `<b>` tags.
- `make_emphasis()` wraps the response in `<em>` tags.
- `make_underlined()` wraps the response in `<u>` tags.

For example, the bold decorator retrieves the wrapped function's return value and adds HTML tags:

```python
def make_bold(function):
    def wrapper_function():
        function_string = function()
        bolded_string = f"<b>{function_string}</b>"
        return bolded_string

    return wrapper_function
```

The decorators are then stacked on the `/bye` route:

```python
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"
```

The resulting response applies all three styles to `Bye!`.

#### Dynamic URL Paths

Flask can capture part of a URL and pass it to the associated view function:

```python
@app.route("/<name>")
def greet(name):
    return f"Hello {name}!"
```

For example, visiting `/Alex` returns `Hello Alex!`.

The next route uses two URL variables, including a typed integer:

```python
@app.route("/<name>/<int:number>")
def greet_1(name, number):
    return f"Hello {name}! You are {number} years old"
```

For example, `/Alex/22` returns `Hello Alex! You are 22 years old`.

### Higher or Lower Game (`higher-lower/server.py`)

The main challenge is a number-guessing web app. When the Flask process starts, the program chooses a number from 0 to 9:

```python
app = Flask(__name__)
random_number = random.randint(0, 9)
```

The root route instructs the user to guess a number and displays a GIF:

```python
@app.route("/")
def hello_world():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        "<img src='...'>"
    )
```

Rather than using an input field, the user submits a guess by appending an integer to the URL, such as `/5`.

Flask captures the integer and passes it into `check()`:

```python
@app.route("/<int:number>")
def check(number):
    if number < random_number:
        return (
            "<h1 style='color: red;'>Too low, try again!</h1>"
            "<img src='...'>"
        )
    elif number > random_number:
        return (
            "<h1 style='color: blue;'> Too high, try again!</h1>"
            "<img src='...'>"
        )
    else:
        return (
            "<h1 style='color: green;'> You found me!</h1>"
            "<img src='...'>"
        )
```

The response depends on how the guess compares to the chosen number:

| Guess | Result | Heading color |
| --- | --- | --- |
| Below the target | `Too low, try again!` | Red |
| Above the target | `Too high, try again!` | Blue |
| Equal to the target | `You found me!` | Green |

Each outcome also displays a different GIF.

**Note:** The random number is chosen when the Python module loads, not after every guess. It remains the same across requests until the module is reloaded or the application restarts.

## Game Flow

```text
Start Flask application
        ↓
Generate random integer (0–9)
        ↓
Visit the home route (/)
        ↓
Display guessing instructions
        ↓
Enter a number in the URL
        ↓
Flask passes number to check()
        ↓
Compare guess with target
        ↓
┌────────────────────────────┐
│ Guess too low?             │── Yes → Red message + GIF
│         ↓ No               │
│ Guess too high?            │── Yes → Blue message + GIF
│         ↓ No               │
│ Correct guess              │──────→ Green message + GIF
└────────────────────────────┘
        ↓
Try another URL if needed
```

## Project Structure

```text
Day 55/
├── exercises/
│   └── main.py
└── higher-lower/
    └── server.py
```

### `exercises/main.py`

Demonstrates Flask routing, HTML responses, custom decorators, decorator stacking, and dynamic URL parameters.

### `higher-lower/server.py`

Contains the Higher or Lower guessing game, including random number generation, URL-based guesses, comparisons, and conditional HTML responses.

## Running the Projects

Install Flask if it is not already installed:

```bash
pip install flask
```

Run either script from its folder:

```bash
python main.py
```

or:

```bash
python server.py
```

Then open the local URL printed by Flask (normally `http://127.0.0.1:5000/`). For the game, add a number from 0 to 9 to the URL, such as `http://127.0.0.1:5000/5`.

Only one project should use the default Flask port at a time unless the applications are configured to use different ports.

## What I Learned

Day 55 extends the Flask fundamentals from Day 54 into routing and basic web application behavior.

Key concepts included:

- Flask routes connect URL paths to Python functions
- View functions can return HTML strings, not just plain text
- Browsers interpret HTML tags and inline CSS in the returned response
- Dynamic route segments allow URLs to provide function arguments
- Flask converters such as `<int:number>` validate and convert route parameters
- Decorators can transform a function's return value
- Stacking decorators combines multiple transformations
- `random.randint()` generates a target value for the game
- Conditional logic can determine which page response to return
- Separate requests can share application-level state such as the chosen number
- `debug=True` enables Flask's development debugging features

## Development Notes

Day 55 connects Python functions and decorators with an interactive, URL-driven web application.

The progression is:

**Flask routes → HTML responses → dynamic URLs → stacked decorators → conditional responses → number-guessing web app**

The decorator exercises show how a function's output can be modified without changing the original function body. The Higher or Lower project uses dynamic routing to turn a URL into user input and select the appropriate response based on that input.

This is a small introduction to request-driven web applications: **receive a request → extract URL data → apply Python logic → return an HTML response**.

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**

Course-provided instructional material, starter code, project structures, assets, and example implementations are not claimed as my original work.
