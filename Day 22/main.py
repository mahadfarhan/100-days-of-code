from turtle import Screen
import time

from paddle import Paddle
from divider import Divider
from ball import Ball
from scoreboard import Scoreboard

POS_1 = -350
POS_2 = 350

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

paddle1 = Paddle(POS_1)
paddle2 = Paddle(POS_2)
divider = Divider()
ball = Ball()
scoreboard1 = Scoreboard(-100)
scoreboard2 = Scoreboard(100)
screen.update()

screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")

screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")


def handle_paddle_collision(ball, paddle):
    if (
        ball.xcor() == paddle.xcor()
        and ball.ycor() <= (paddle.ycor() + 40)
        and ball.ycor() >= (paddle.ycor() - 40)
    ):
        if ball.ycor() < paddle.ycor():
            ball.move_y_down()
        elif ball.ycor() > paddle.ycor():
            ball.move_y_up()
        ball.bounce()


def handle_boundary_collision(ball):
    if ball.ycor() >= 285:
        ball.swap_y()
    elif ball.ycor() <= -285:
        ball.swap_y()


def handle_scoring(scoreboard):
    scoreboard.increment_score()
    ball.reset_ball()
    paddle1.reset_paddle(POS_1)
    paddle2.reset_paddle(POS_2)
    screen.update()
    time.sleep(1)


def main():
    while True:
        time.sleep(0.025)
        ball.move()
        if ball.xcor() >= 400:
            handle_scoring(scoreboard1)
        elif ball.xcor() <= -400:
            handle_scoring(scoreboard2)

        handle_paddle_collision(ball, paddle1)
        handle_paddle_collision(ball, paddle2)
        handle_boundary_collision(ball)

        screen.update()


main()
