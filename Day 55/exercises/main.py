from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        function_string = function()
        bolded_string = f"<b>{function_string}</b>"
        return bolded_string

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        function_string = function()
        emphasised_string = f"<em>{function_string}</em>"
        return emphasised_string

    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        function_string = function()
        underlined_string = f"<u>{function_string}</u>"
        return underlined_string

    return wrapper_function


@app.route("/")
def hello_world():
    return (
        "<h1 style='text-align: center'>Hello, World!</h1>"
        "<p> This is a paragraph </p>"
        "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWhlaXMwb3EwcmxqNjdhaHNyenMyMmcxZnp2cnNoZ3NlaXl2aXE3aiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/XQebwq1LPmTWU/giphy.gif'>"
    )


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


@app.route("/<name>")
def greet(name):
    return f"Hello {name}!"


@app.route("/<name>/<int:number>")
def greet_1(name, number):
    return f"Hello {name}! You are {number} years old"


if __name__ == "__main__":
    app.run(debug=True)
