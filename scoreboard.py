
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level_count = 1
        self.hideturtle()
        self.penup()
        self.goto(-270,270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level is: {self.level_count}", font=("courier", 20, "normal"))

    def score(self):
        self.level_count += 1
        self.update_score()



    def game_over(self):
        self.penup()
        self.goto(-70, 20)
        self.color("red")
        self.write("Game Over", font=("courier", 30, "normal"))
