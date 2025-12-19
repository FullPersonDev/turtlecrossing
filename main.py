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
scoreboard = Scoreboard()

# Listen for key presses
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
turn = 0
while game_is_on:
    # Refresh screen animation
    screen.update()
    time.sleep(0.1)

    # Create new car every 6th iteration of this while loop
    if turn % 6 == 0:
        car_manager.create_car()

    # Constantly move cars
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.print_game_over()
            game_is_on = False

    # Detect if made it to the top
    if player.at_finish_line():
        car_manager.level_up()
        scoreboard.level_up()

    # Increment turn variable
    turn += 1

screen.exitonclick()
