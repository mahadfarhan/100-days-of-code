from turtle import Turtle, Screen
import os
import random

is_race_on = False
screen = Screen()

turtle_list = []
color_list = ["indigo", "blue", "green", "yellow", "orange", "red"]

screen.setup(width=500, height=400)
y = 100
for i in range(6):
    turtle = Turtle(shape="turtle")
    turtle.pu()
    turtle.color(color_list[i])
    turtle.goto(x=-230, y=y)
    y -= 40
    turtle_list.append(turtle)

user_bet = screen.textinput(
    title="Make your bet",
    prompt=f"Which turtle will win the race? Enter a color ({', '.join(color_list)}): ",
).lower()

while user_bet not in color_list:
    user_bet = screen.textinput(
        title="Make your bet",
        prompt=f"Which turtle will win the race? Enter a color ({', '.join(color_list)}): ",
    ).lower()

is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 230:
            is_race_on = False
            screen.bye()
            print(f"{turtle.color()[0]} won!")
            if turtle.color()[0] == user_bet:
                print("Your turtle won! :D")
            else:
                print("Your turtle lost D:")
            break
