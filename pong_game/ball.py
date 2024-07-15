from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed(1)
        self.penup()
        self.setheading(45)
        self.timer = 0.1

    def move(self):
        self.forward(20)

    def reset(self):
        self.timer = 0.1
        self.goto(0, 0)

    def speed_up(self):
        self.timer *= 0.9
