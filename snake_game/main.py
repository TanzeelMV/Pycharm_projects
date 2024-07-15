import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

food = Food()
my_snake = Snake()
my_scoreboard = Scoreboard()
my_scoreboard.pencolor("white")

screen.listen()
screen.onkey(fun=my_snake.left, key="Left")
screen.onkey(fun=my_snake.right, key="Right")
screen.onkey(fun=my_snake.up, key="Up")
screen.onkey(fun=my_snake.down, key="Down")

game_on = True

while game_on:
    my_scoreboard.show_score()
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    if my_snake.head.distance(food) < 15:
        my_snake.extend()
        food.refresh()
        my_scoreboard.increase_score()
        my_scoreboard.update_score()

    if (my_snake.head.xcor() > 285 or my_snake.head.xcor() < -285 or my_snake.head.ycor() > 285 or my_snake.head.ycor()
            < -285):
        my_scoreboard.reset_score()
        my_snake.reset()

    for segment in my_snake.turtle_seg[1:len(my_snake.turtle_seg) - 1]:
        if my_snake.head.distance(segment) < 10:
            my_scoreboard.reset_score()
            my_snake.reset()

screen.exitonclick()
