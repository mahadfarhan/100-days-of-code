from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0, 9)


@app.route("/")
def hello_world():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGhidGh5bWFtZmtqdzhtZ2I0M3RuYThtMXRjMmR2OTl5Y2g1dDVwZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o7aCSPqXE5C6T8tBC/giphy.gif'>"
    )


@app.route("/<int:number>")
def check(number):
    if number < random_number:
        return (
            "<h1 style='color: red;'>Too low, try again!</h1>"
            "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExamFxZmZmd2Fza2o4NHB0czZ2cnV0dnlkN2FwNzVxendrbWd5bGZrMSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/tK0GGOtRGBBFryIBWy/giphy.gif'>"
        )
    elif number > random_number:
        return (
            "<h1 style='color: blue;'> Too high, try again!</h1>"
            "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2E3Y3RvcHR4ZHdjbHk5eXRsbmxrNTJvYW95bGJ1emYzcGh0NWFvaCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/26tPmgvOZmiDXBsyI/giphy.gif'>"
        )
    else:
        return (
            "<h1 style='color: green;'> You found me!</h1>"
            "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZm8zZXF0N25qMXBpMnZwN245MXBoYWlzbHplNmNubzlvYXltaG1qdiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3ndAvMC5LFPNMCzq7m/giphy.gif'>"
        )


if __name__ == "__main__":
    app.run(debug=True)
