import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

s = Screen()
s.setup(width=600, height=600)
s.tracer(0)
s.bgcolor("#f8f9fa")

p = Player()
car = CarManager()
p.starting_position()

s.listen()
s.onkeypress(p.move, "Up")

score = Scoreboard()

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    score.update_scoreboard()

    car.create_car()
    car.move_car()

    if p.ycor() == 290:
        p.reset_game()
        score.increase_score()
        car.STARTING_MOVE_DISTANCE += 10

    for i in car.all_cars:
        if i.distance(p) < 20:
            score.game_over()
            game_is_on = False

s.exitonclick()
