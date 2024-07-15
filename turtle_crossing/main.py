import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()

scoreboard = Scoreboard()
scoreboard.update_level()

cars = []


def new_car():
    my_car = CarManager()
    cars.append(my_car)


dist = 5

screen.onkey(player.move, "Up")
start_time = time.time()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    i = random.randint(1, 6)
    for _ in range(scoreboard.level + 1):
        if i == _:
            new_car()
    for car in cars:
        car.cars_run(dist)
        if car.xcor() < -320:
            cars.remove(car)

    if player.ycor() > 275:
        scoreboard.level += 1
        scoreboard.update_level()
        player.reset()
        dist += 10

    for car in cars:
        if car.xcor() - player.xcor() < 20 and player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
