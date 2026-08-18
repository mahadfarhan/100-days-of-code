from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.movement_amount = 10
        self.generate_y()
        self.shape("square")
        self.turtlesize(1)
        self.color("white")
        self.pu()

    def generate_y(self):
        self.y_movement = random.randint(-5, 5)
        while self.y_movement == 0:
            self.y_movement = random.randint(-5, 5)

    def move(self):
        self.setx(self.xcor() + self.movement_amount)
        self.sety(self.ycor() + self.y_movement)

    def bounce(self):
        self.movement_amount *= -1

    def move_y_down(self):
        self.y_movement = -random.randint(1, 3)

    def move_y_up(self):
        self.y_movement = random.randint(1, 3)

    def swap_y(self):
        self.y_movement *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.generate_y()
        self.bounce()
