from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.ht()
        self.pu()
        self.goto(-200, 250)
        self.display_text()

    def display_text(self):
        self.clear()
        self.write(f"Level: {self.level} ", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.display_text()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align="center", font=FONT)
