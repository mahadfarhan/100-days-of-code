from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 15, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()
        self.ht()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font= FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()