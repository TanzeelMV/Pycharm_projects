from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.goto(random.randint(-270, 270), random.randint(-270, 270))

    def refresh(self):
        self.goto(random.randint(-270, 270), random.randint(-270, 270))
