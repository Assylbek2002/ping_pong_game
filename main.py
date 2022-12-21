from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.listen()
screen.tracer(0)
right_paddle = Paddle(350, 0)
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")

left_paddle = Paddle(-350, 0)
screen.onkey(fun=left_paddle.up, key='w')
screen.onkey(fun=left_paddle.down, key='s')

ball = Ball()
score = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 45 and ball.xcor() > 320 or ball.distance(left_paddle) < 45 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reverse_position()
        score.l_point()
        score.update_scoreboard()

    if ball.xcor() < -380:
        ball.reverse_position()
        score.r_point()
        score.update_scoreboard()
    ball.move()

screen.exitonclick()