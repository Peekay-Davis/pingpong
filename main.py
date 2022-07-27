from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("PONG")
screen.bgcolor("black")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

time_speed = 0.1
is_game_on = True
while is_game_on:
    time.sleep(time_speed)
    screen.update()
    ball.move()

    # DETECT COLLISION WITH WALL
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # DETECT COLLISION WITH THE PADDLE
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        print("made contact")
        ball.bounce_x()
        time_speed *= 0.9

    # ESCAPING r_Paddle
    if ball.xcor() > 380:
        print("stop")
        ball.reset_position()
        scoreboard.increase_l_score()

    # ESCAPING l_Paddle
    if ball.xcor() < -380:
        time_speed = 0.1
        ball.reset_position()
        scoreboard.increase_r_score()

screen.exitonclick()
