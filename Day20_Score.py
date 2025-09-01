from turtle import Turtle,Screen
screen = Screen()
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        f = open("highscore.txt", "r")
        self.high_score = int(f.read())
        f.close()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.write(f"Score: {self.score}    High Score={self.high_score}", align="center", font=("Arial", 10, "bold"))
    def score_up(self):
        self.score+=1
        self.clear()
        self.update_score()
        if self.score > self.high_score:
            self.high_score = self.score
            f=open("highscore.txt", "w")
            f.write(str(self.high_score))
            f.close()
