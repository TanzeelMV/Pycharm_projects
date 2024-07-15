from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.level = 1

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", move=False, align="center", font=FONT)
