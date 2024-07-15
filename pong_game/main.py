import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("My Pong Game")
screen.tracer(0)
screen.listen()

paddle_1 = Paddle(350, 0)

paddle_2 = Paddle(-350, 0)

ball = Ball()

scoreboard = Scoreboard()
scoreboard.update_scoreboard()

screen.onkey(paddle_1.move_up, "Up")
screen.onkey(paddle_1.move_down, "Down")
screen.onkey(paddle_2.move_up, "w")
screen.onkey(paddle_2.move_down, "s")
game_on = True

while game_on:
    screen.update()
    time.sleep(ball.timer)
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.setheading(360 - ball.heading())

    if ball.distance(paddle_1) < 55 and ball.xcor() > 320:
        ball.speed_up()
        ball.setheading(540 - ball.heading())

    if ball.distance(paddle_2) < 55 and ball.xcor() < -320:
        ball.speed_up()
        ball.setheading(540 - ball.heading())

    if ball.xcor() > 400:
        ball.reset()
        scoreboard.score_2 += 1
        scoreboard.update_scoreboard()
        ball.setheading(135)

    if ball.xcor() < -400:
        ball.reset()
        scoreboard.score_1 += 1
        scoreboard.update_scoreboard()
        ball.setheading(45)

screen.exitonclick()
