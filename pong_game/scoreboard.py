from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 200)
        self.score_1 = 0
        self.score_2 = 0
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score_2}   {self.score_1}", move=False, align="center", font=("Courier", 80, "normal"))
