from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, x):
        super().__init__()
        self.ht()
        self.color("white")
        self.pu()
        self.goto(x, 200)
        self.score = 0
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"{self.score}", move=False, align="center", font=("OCR A Extended", 80, "bold"))

    def increment_score(self):
        self.score += 1
        self.display_score()