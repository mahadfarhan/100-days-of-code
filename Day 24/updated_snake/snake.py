from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        x = 0
        y = 0
        starting_positions = []
        for _ in range(3):
            starting_positions.append((x, y))
            x -= MOVE_DISTANCE

        for position in starting_positions:
            self.add_square(position)

    def add_square(self, position):
        square = Turtle(shape="square")
        square.pu()
        square.color("white")
        square.setpos(position)
        self.squares.append(square)

    def extend(self):
        self.add_square(self.squares[-1].position())

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def move(self):
        for square_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for square in self.squares:
            square.ht()
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]
