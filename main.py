from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

playing = True
while playing:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision w food
    if snake.head.distance(food) < 15:
        print("NOM")
        food.refresh()
        snake.extend()
        scoreboard.point()

    # Detect collision w wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        playing = False
        scoreboard.game_over()

    # Detect collision w tail
    # if head collides w any segment in tail - trigger game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            playing = False
            scoreboard.game_over()


screen.exitonclick()
