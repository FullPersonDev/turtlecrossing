from turtle import Turtle
import random
COLORS = ["red", "yellow", "blue", "orange", "green", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.resizemode("user")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        ran_y = random.randint(-250, 250)
        new_car.goto(280, ran_y)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
