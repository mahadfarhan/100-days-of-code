from turtle import Turtle

TOP_LIMIT = 250
BOTTOM_LIMIT = -240


class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.pu()
        self.turtlesize(3, 1)
        self.goto(x, 0)

    def up(self):
        if self.ycor() < TOP_LIMIT:
            self.sety(self.ycor() + 20)

    def down(self):
        if self.ycor() > BOTTOM_LIMIT:
            self.sety(self.ycor() - 20)

    def reset_paddle(self, x):
        self.goto(x, 0)
