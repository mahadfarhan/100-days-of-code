from turtle import Screen, Turtle
import turtle
import random

turtle.colormode(255)

color_list = [
    (198, 13, 32),
    (248, 236, 25),
    (40, 76, 188),
    (39, 216, 69),
    (238, 227, 5),
    (227, 159, 49),
    (29, 40, 154),
    (212, 76, 15),
    (17, 153, 17),
    (241, 36, 161),
    (195, 16, 12),
    (223, 21, 120),
    (68, 10, 31),
    (61, 15, 8),
    (223, 141, 206),
    (11, 97, 62),
    (219, 159, 11),
    (54, 209, 229),
    (19, 21, 49),
    (238, 157, 216),
    (79, 74, 212),
    (10, 228, 238),
    (73, 212, 168),
    (93, 233, 198),
    (65, 231, 239),
    (217, 88, 51),
    (6, 68, 42),
    (176, 176, 233),
    (239, 168, 161),
    (249, 8, 48),
    (5, 246, 222),
    (15, 76, 110),
    (243, 15, 14),
    (38, 43, 221),
]

tim = Turtle()
tim.penup()
pos1 = -250
pos2 = -200
tim.setpos(pos1, pos2)

for _ in range(10):
    for _ in range(10):
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.forward(50)
    pos2 += 50
    tim.setpos(pos1, pos2)


tim.ht()
screen = Screen()
screen.screensize(650, 650)
screen.exitonclick()
