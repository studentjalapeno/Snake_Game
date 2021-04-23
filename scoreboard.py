from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 225)
        self.refresh_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh_score()

    def refresh_score(self):
        self.write(f"Score = {self.score}", False, align="center", font=("Arial", 24,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, align="center", font=("Arial", 24, "normal"))
