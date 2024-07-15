from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.move_dist = STARTING_MOVE_DISTANCE
        k = random.randint(0, 16)
        self.goto(320, (-240 + (30*k)))

    def cars_run(self, dist):
        new_x = self.xcor() - dist
        self.speed("fastest")
        self.goto(new_x, self.ycor())
