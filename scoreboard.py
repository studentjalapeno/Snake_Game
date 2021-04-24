from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 225)
        self.refresh_score()

    def increase_score(self):
        self.score += 1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align="center",
                   font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.refresh_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", False, align="center", font=("Arial", 24, "normal"))
