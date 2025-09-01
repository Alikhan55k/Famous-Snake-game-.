import turtle
from turtle import Screen
import time
from Day20_snake import Snake
from Day20_Food import Food
from Day20_Score import scoreboard
scoreboard = scoreboard()
scoreboard.score=0
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
Snake = Snake()
Food = Food()
end=False
while not end:
    Snake.move_snake()
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(Snake.go_left, "Left")
    screen.onkey(Snake.go_right, "Right")
    screen.onkey(Snake.go_up, "Up")
    screen.onkey(Snake.go_down, "Down")

    if Snake.turtle[0].distance(Food) < 15:
        Food.refresh()
        Snake.snake_growth()
        scoreboard.score_up()
        


screen.exitonclick()