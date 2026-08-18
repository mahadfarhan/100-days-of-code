from turtle import Turtle

class Divider():
    def __init__(self):
        self.create_divider()
        
    def create_divider(self):
        x = 0
        y = 280
        for _ in range(20):
            divider_segment = Turtle(shape="square")
            divider_segment.color("white")
            divider_segment.turtlesize(0.8, 0.25)
            divider_segment.pu()
            divider_segment.goto(x, y)
            y -= 30