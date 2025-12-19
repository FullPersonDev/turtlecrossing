from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.player_score = 0
        self.write(f"Level: {self.player_score}", False, font=FONT)

    def level_up(self):
        self.player_score += 1
        self.clear()
        self.write(f"Level: {self.player_score}", False, font=FONT)

    def print_game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, font=("arial", 14, "normal"))
