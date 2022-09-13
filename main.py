import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
scoreboard.hideturtle()
player = Player()
car = CarManager()
car.hideturtle()
screen.listen()
screen.onkey(player.player_move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.car_move()

# Detect collition with car
    for cars in car.car_list:
        if cars.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

# level increment if turtle reach to the final point
    if player.ycor() > 280:
        player.reset_position()
        car.level_up()
        scoreboard.score()

screen.exitonclick()
