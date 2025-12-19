from turtle import Turtle
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.player_level = 1
        self.write(f"Level: {self.player_level}", False, "left", font=FONT)

    def level_up(self):
        self.player_level += 1
        self.clear()
        self.write(f"Level: {self.player_level}", False, "left", font=FONT)

    def print_game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, "center", font=FONT)
