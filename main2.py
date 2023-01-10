from turtle import Screen
from paddle import Paddle, Hor_Paddle
# from ball import Ball
from ball2 import Ball
import time
from pingpong_score import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Solo Player Virtual PingPong')
# The screen.tracer(0) serves to omit the animation when the objects are being created
screen.tracer(0)

right_paddle = Paddle((380,0))
right_paddle.color('cyan')
left_paddle = Paddle((-385,0))
left_paddle.color('green')
top_paddle = Hor_Paddle((0,290))
top_paddle.color('cyan')
bottom_paddle = Hor_Paddle((0, -280))
bottom_paddle.color('green')
ball = Ball()
scores = Scoreboard()

screen.listen()
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')

screen.onkey(top_paddle.right, 'd')
screen.onkey(bottom_paddle.right, 'Right')
screen.onkey(top_paddle.left, 'a')
screen.onkey(bottom_paddle.left, 'Left')

pong_on = True
t = 0.1
# interval = 0.001
interval = 0.005
while pong_on:
    time.sleep(t)
    screen.update()
    ball.move()

    if ball.ycor() >= 300 or ball.xcor() >= 400:
        print(ball.xcor(), ball.ycor())
        ball.game_over()
        # ball.green_wins()
        pong_on = False

    if ball.ycor() <= -300 or ball.xcor() <= -400:
        print(ball.xcor(), ball.ycor())
        ball.game_over()
        # ball.cyan_wins()
        pong_on = False

    if ball.distance(right_paddle) <= 80 and ball.xcor() > 370:
        ball.bounce_x()
        scores.my_score_up()
        if t == 0.01000000000000001:
            interval = 0
            t -= interval
        else:
            t -= interval

    if ball.distance(top_paddle) <= 80 and ball.ycor() >= 280:
        ball.bounce_y()
        scores.my_score_up()

    if ball.distance(bottom_paddle) <= 80 and ball.ycor() <= -280:
        scores.my_score_up()
        ball.bounce_y()

    if ball.distance(left_paddle) <= 80 and ball.xcor() < -370:
        scores.my_score_up()
        ball.bounce_x()
        if t == 0.01000000000000001:
            interval = 0
            t -= interval
        else:
            t -= interval

    # if top_paddle.xcor() >= 340:
    #     top_paddle.stop_right()
    #
    # if top_paddle.xcor() <= -321:
    #     top_paddle.stop_left()
    #
    # if bottom_paddle.xcor() >= 340:
    #     bottom_paddle.stop_right()
    #
    # if bottom_paddle.xcor() <= -321:
    #     bottom_paddle.stop_left()
    #
    # if right_paddle.ycor() >= 208:
    #     right_paddle.stop_up()
    #
    # if right_paddle.ycor() <= -202:
    #     right_paddle.stop_down()
    #
    # if left_paddle.ycor() >= 208:
    #     left_paddle.stop_up()
    #
    # if left_paddle.ycor() <= -202:
    #     left_paddle.stop_down()

screen.exitonclick()