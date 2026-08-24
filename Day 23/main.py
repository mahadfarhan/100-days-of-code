import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    car_manager.create_car()
    car_manager.move_forward()
    if player.check_win():
        scoreboard.level_up()
        car_manager.increment_speed()
        car_manager.delete_all_cars()
    time.sleep(0.1)
    screen.update()
    for car in car_manager.list_of_cars:
        if (
            player.ycor() + 12.5 >= car.ycor() - 12.5
            and player.ycor() - 12.5 <= car.ycor() + 12.5
        ):
            if (
                player.xcor() + 20 >= car.xcor() - 20
                and player.xcor() - 20 <= car.xcor() + 20
            ):
                scoreboard.game_over()
                game_is_on = False
                break
    car_manager.del_car()

screen.exitonclick()
