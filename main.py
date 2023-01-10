# from turtle import Screen, Turtle
# from paddle import Paddle, Hor_Paddle
# # from ball import Ball
# from ball2 import Ball
# import time
# from pingpong_score import Scoreboard
#
# screen = Screen()
# screen.bgcolor('black')
# screen.setup(width=800, height=600)
# screen.title('Virtual PingPong')
# # The screen.tracer(0) serves to omit the animation when the objects are being created
# screen.tracer(0)
#
# right_paddle = Paddle((380,0))
# right_paddle.color('cyan')
# left_paddle = Paddle((-385,0))
# left_paddle.color('green')
# # top_paddle = Hor_Paddle((0,290))
# # top_paddle.color('cyan')
# # bottom_paddle = Hor_Paddle((0, -280))
# # bottom_paddle.color('green')
# ball = Ball()
# scores = Scoreboard()
#
# screen.listen()
# screen.onkey(left_paddle.up, 'w')
# screen.onkey(left_paddle.down, 's')
# screen.onkey(right_paddle.up, 'Up')
# screen.onkey(right_paddle.down, 'Down')
#
# # screen.onkey(top_paddle.right, 'd')
# # screen.onkey(bottom_paddle.right, 'Right')
# # screen.onkey(top_paddle.left, 'a')
# # screen.onkey(bottom_paddle.left, 'Left')
#
# pong_on = True
# t = 0.1
# interval = 0.001
# while pong_on:
#     time.sleep(t)
#     screen.update()
#     ball.move()
#
#     if ball.ycor() >= 300 or ball.ycor() <= -300 or ball.xcor() >= 395 or ball.xcor() <= -395:
#         ball.bounce_y()
#         # print(ball.xcor(), ball.ycor())
#         # ball.game_over()
#         # pong_on = False
#         # scores.final_score()
#
#     if ball.xcor() >= 400 or ball.xcor() <= -400:
#         print(ball.xcor(), ball.ycor())
#         ball.game_over()
#         pong_on = False
#         scores.final_score()
#
#     if ball.distance(right_paddle) <= 80 and ball.xcor() > 370:
#         print('hit')
#         print(f'xcor = {ball.xcor()}, ycor = {ball.ycor()}')
#         print(f'ball distance from right paddle = {ball.distance(right_paddle)}')
#         scores.update_score()
#         scores.cyan_score()
#         ball.bounce_x()
#         if t == 0.01000000000000001:
#             interval = 0
#             t -= interval
#         else:
#             t -= interval
#         print(t)
#
#     # if ball.distance(top_paddle) < 30 and ball.ycor() >= 280:
#     #     print(f'hit paddle_distance={ball.distance(top_paddle)} xcor={ball.xcor()}, ycor={ball.ycor()}')
#     #     ball.bounce_y()
#     # elif ball.distance(top_paddle) == 30 and ball.ycor() >= 280:
#     #     ball.game_over()
#     #     pong_on = False
#
#     # if ball.distance(bottom_paddle) < 30 and ball.xcor() > -340:
#     #     print('hit')
#     #     ball.bounce_y()
#
#     if ball.distance(left_paddle) <= 80 and ball.xcor() < -370:
#         print('hit')
#         print(f'xcor = {ball.xcor()}, ycor = {ball.ycor()}')
#         print(f'ball distance from left paddle = {ball.distance(left_paddle)}')
#         scores.update_score()
#         scores.green_score()
#         ball.bounce_x()
#         # t -= 0.0025
#         if t == 0.01000000000000001:
#             interval = 0
#             t -= interval
#         else:
#             t -= interval
#         print(t)
#
#     # if right_paddle.ycor() >= 208:
#     #     right_paddle.stop_up()
#     #     print('right paddle')
#     #
#     # if right_paddle.ycor() <= -202:
#     #     right_paddle.stop_down()
#     #
#     # if left_paddle.ycor() >= 208:
#     #     left_paddle.stop_up()
#     #
#     # if left_paddle.ycor() <= -202:
#     #     left_paddle.stop_down()
#     #
#     # if top_paddle.xcor() >= 340:
#     #     top_paddle.stop_right()
#     #
#     # if top_paddle.xcor() <= -321:
#     #     top_paddle.stop_left()
#     #
#     # if bottom_paddle.xcor() >= 340:
#     #     bottom_paddle.stop_right()
#     #
#     # if bottom_paddle.xcor() <= -321:
#     #     bottom_paddle.stop_left()
#
#
#
#
# screen.exitonclick()