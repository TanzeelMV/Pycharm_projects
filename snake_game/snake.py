from turtle import Turtle, Screen

screen = Screen()

MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.len_snake = 3
        self.turtle_seg = []
        for turtle in range(0, self.len_snake):
            self.add_seg(x=(20 * turtle), y=0)
        self.head = self.turtle_seg[0]

    def add_seg(self, x, y):
        timmy = Turtle()
        timmy.color("white")
        timmy.shape("square")
        timmy.speed('fastest')
        timmy.penup()
        timmy.goto(x, y)
        self.turtle_seg.append(timmy)

    def extend(self):
        new_x = self.turtle_seg[-1].xcor()
        new_y = self.turtle_seg[-1].ycor()
        self.add_seg(new_x, new_y)
        pass

    def move(self):
        for i in range(len(self.turtle_seg) - 1, 0, -1):
            new_x = self.turtle_seg[i - 1].xcor()
            new_y = self.turtle_seg[i - 1].ycor()
            self.turtle_seg[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.turtle_seg:
            seg.hideturtle()
        self.turtle_seg = []
        for turtle in range(0, self.len_snake):
            self.add_seg(x=(20 * turtle), y=0)
        self.head = self.turtle_seg[0]

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
