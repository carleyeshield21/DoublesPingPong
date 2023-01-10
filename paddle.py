from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        # self.color('cyan')
        self.shapesize(stretch_wid=5, stretch_len=0.5)
        self.penup()
        self.goto(pos)
        self.move_up = 20
        self.move_down = -20

    def up(self):
        new_ycor = self.ycor() + self.move_up
        self.goto(self.xcor(), new_ycor)

    def down(self):
        new_ycor = self.ycor() + self.move_down
        self.goto(self.xcor(), new_ycor)

    def stop_up(self):
        self.move_up = 0

    def stop_down(self):
        self.move_down = 0
        
class Hor_Paddle(Turtle):
    def __init__(self, pos1):
        super().__init__()
        self.shape('square')
        # self.color('green')
        self.shapesize(stretch_wid=0.5, stretch_len=5)
        self.penup()
        self.goto(pos1)
        self.move_right = 20
        self.move_left = -20

    def right(self):
         new_xcor = self.xcor() + self.move_right
         self.goto(new_xcor, self.ycor())

    def left(self):
         new_xcor = self.xcor() + self.move_left
         self.goto(new_xcor, self.ycor())

    def stop_right(self):
        self.move_right = 0

    def  stop_left(self):
        self.move_left = 0