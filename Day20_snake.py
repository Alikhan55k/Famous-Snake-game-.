POSITION=[(0,0),(-20,0),(-40,0)]
DISTANCE=20

from turtle import Turtle
class Snake:
    def __init__(self):
        self.turtle = []
        self.creat_snake(3)
    def creat_snake(self,blocks):
        for i in range(blocks):
            a = Turtle()
            a.penup()
            a.shape("square")
            a.color("white")
            self.turtle.append(a)
            a.goto(POSITION[i])
    def snake_growth(self):
        self.creat_snake(1)
    def move_snake(self):
        for tur in range(len(self.turtle) - 1, 0, -1):
            x = self.turtle[tur - 1].xcor()
            y = self.turtle[tur - 1].ycor()
            self.turtle[tur].goto(x, y)
        self.turtle[0].forward(DISTANCE)

    def go_right(self):
        self.turtle[0].setheading(0)

    def go_up(self):
        self.turtle[0].setheading(90)

    def go_left(self):
        self.turtle[0].setheading(180)

    def go_down(self):
        self.turtle[0].setheading(270)
