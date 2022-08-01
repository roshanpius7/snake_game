from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import ScoreBoard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)


game_is_on=True
snake=Snake()
food=Food()
scoreboard=ScoreBoard()
screen.title("snake game")
screen.listen()
# here snake.up is a function inside another function so snake.up() is not used
#i.e paranthesis () is not used

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if  snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
     scoreboard.game_over()
     game_is_on = False

    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()
screen.exitonclick()
