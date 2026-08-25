from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("./updated_snake/data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.pu()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()
        self.ht()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            False,
            align=ALIGNMENT,
            font=FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./updated_snake/data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increment_score(self):
        self.score += 1
        self.update_scoreboard()
