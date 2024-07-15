from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.back(20)
