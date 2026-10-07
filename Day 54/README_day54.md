# Day 54 — Python Decorators & Flask

Day 54 of **100 Days of Code: The Complete Python Pro Bootcamp** introduced decorators and the basics of creating web applications with Flask.

The exercises include a custom decorator that modifies the behavior of functions and a minimal Flask application with a route that returns a response.

## Features

- Creates custom Python decorators
- Uses nested functions to wrap existing functions
- Uses the `@decorator` syntax
- Adds behavior before and after a function executes
- Demonstrates manually applying a decorator
- Creates a basic Flask application
- Defines a URL route with `@app.route()`
- Returns a response from a Flask route
- Runs the Flask development server

## Technologies Used

- Python
- Flask
- `time`
- Python decorators
- Nested functions
- Function wrappers
- Flask routing

## Exercises

### Python Decorators

The decorator exercise creates a `delay_decorator()` function that accepts another function and returns a wrapper:

```python
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after

    return wrapper_function
```

The decorator is then applied using Python's `@` syntax:

```python
@delay_decorator
def say_hello():
    print("Hello")
```

and:

```python
@delay_decorator
def say_bye():
    print("Bye")
```

The exercise also demonstrates applying the decorator manually:

```python
decorated_function = delay_decorator(say_greeting)
decorated_function()
```

## How Decorators Work

```text
Original function
       ↓
Pass function into decorator
       ↓
Create wrapper function
       ↓
Return wrapper
       ↓
@decorator replaces original reference
       ↓
Call decorated function
       ↓
Wrapper executes
       ↓
Original function executes
```

In this exercise, the wrapper waits for two seconds, calls the original function twice, and provides a place where additional behavior could be executed afterward.

## Flask

The Flask exercise introduces the basic structure of a Python web application.

The application is created with:

```python
from flask import Flask

app = Flask(__name__)
```

A route is defined using the `@app.route()` decorator:

```python
@app.route("/")
def hello_world():
    return "Hello, World!"
```

When the application receives a request for `/`, Flask executes `hello_world()` and returns the string `"Hello, World!"`.

The development server is started with:

```python
if __name__ == "__main__":
    app.run()
```

## Project Structure

```text
Day 54/
└── exercises/
    ├── decorators.py
    ├── hello.py
    └── __pycache__/
```

### `decorators.py`

Contains the custom decorator exercise, including `delay_decorator()` and the example functions it decorates.

### `hello.py`

Contains the basic Flask application and its `/` route.

## What I Learned

Day 54 introduces an important shift from simply writing functions to learning how Python can modify and extend function behavior.

Key concepts included:

- Functions can be passed as arguments
- Functions can be returned from other functions
- Nested functions can access functions from their enclosing scope
- Decorators wrap existing functions
- The `@decorator` syntax applies a decorator to a function
- Code can be executed before and after a wrapped function
- Flask can turn Python functions into web routes
- `@app.route()` is itself a decorator
- A Flask application can respond to HTTP requests
- Python can be used to build the basic structure of a web application

## Development Notes

Day 54 connects two ideas that become increasingly important in Python development:

**Function modification → decorators → web frameworks → routes**

The decorator exercise provides the foundation for understanding syntax such as:

```python
@app.route("/")
```

Decorators allow a framework to register or modify functions without requiring the function itself to contain the framework's implementation details.

Flask therefore provides a practical example of decorators being used outside a standalone Python exercise: `@app.route()` associates a Python function with a URL.

## Course Attribution

The project concepts and exercises originate from **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

## Disclosure

This README was written with AI assistance. **Any code authored by me in this repository was written independently by me.**

Course-provided instructional material, starter code, project structures, assets, and example implementations are not claimed as my original work.
