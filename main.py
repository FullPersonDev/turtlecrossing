from turtle import Screen
import time
from player import Player
from car import CarManager
from scoreboard import Scoreboard

# Set up screen
screen = Screen()
screen.setup(600, 600)
screen.title("Welcome to Turtle Crossing")
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()