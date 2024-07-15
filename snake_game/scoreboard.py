from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.goto(0, 280)
        self.hideturtle()

    def show_score(self):
        self.write(f"Score: {self.score}    Highscore: {self.highscore}", False, align='center',
                   font=('Courier', 14, 'normal'))

    def update_score(self):
        self.clear()
        self.show_score()

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode='w') as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", False, align='center',
                   font=('Courier', 14, 'normal'))
