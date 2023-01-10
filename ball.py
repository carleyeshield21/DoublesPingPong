from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.xpos = 10
        self.ypos = 10

    def move(self):
        new_x = self.xcor() + self.xpos
        new_y = self.ycor() + self.ypos
        self.penup()
        self.goto(new_x, new_y)
        print(new_x, new_y)
        # Another way of slowing down the movement of the ball
        # new_x = self.xcor() + 0.70
        # new_y = self.ycor() + 0.50

    def bounce(self):
        self.ypos *= -1