import time
from turtle import Screen
from player import Player
from car import CarManager
from scoreboard import Scoreboard

# Set up screen
screen = Screen()
screen.setup(600, 600)
screen.title("Welcome to Turtle Crossing")
screen.tracer(0)

# Create player, car manager, and scoreboard
player = Player()
car_manager = CarManager()

# Listen for key presses
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
turn = 0
while game_is_on:
    # Refresh screen animation
    screen.update()
    time.sleep(0.1)

    if turn % 6 == 0:
        car_manager.create_car()

    car_manager.move_cars()
    player.refresh_turtle()

    turn += 1

screen.exitonclick()