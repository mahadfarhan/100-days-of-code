from turtle import Turtle, Screen
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

screen = Screen()
image_file = "car.gif"
screen.register_shape(image_file)


class CarManager:
    def __init__(self):
        self.list_of_cars = []
        self.current_moving_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        tick = random.randint(0, 100)
        if tick > 75:
            turtle = Turtle()
            turtle.pu()
            turtle.goto(300, random.randint(-300, 280))
            turtle.seth(180)
            turtle.shape(image_file)
            self.list_of_cars.append(turtle)

    def move_forward(self):
        for car in self.list_of_cars:
            car.forward(self.current_moving_distance)

    def increment_speed(self):
        self.current_moving_distance += MOVE_INCREMENT

    def del_car(self):
        cars_snapshot = self.list_of_cars.copy()
        for car in cars_snapshot:
            if car.xcor() <= -300:
                self.list_of_cars.remove(car)
                car.ht()

    def delete_all_cars(self):
        for car in self.list_of_cars:
            car.ht()
        self.list_of_cars.clear()
