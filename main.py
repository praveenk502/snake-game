from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

s1 = Screen()
s1.setup(width=600, height=600)
s1.bgcolor("black")
s1.title("Snake Game")
s1.tracer(0)

snake = Snake()
food = Food()
score = Score()

s1.listen()
s1.onkey(snake.up,"Up")
s1.onkey(snake.down,"Down")
s1.onkey(snake.right,"Right")
s1.onkey(snake.left,"Left")

game_on = True

while game_on:
    s1.update()
    time.sleep(0.1)
    snake.move()
#detection of food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()
#detection of wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.over()
        game_on = False
#detection of tail
    for segment in snake.all_segment[1:]:
        if snake.head.distance(segment) < 10:
            score.over()
            game_on = False



s1.exitonclick()
