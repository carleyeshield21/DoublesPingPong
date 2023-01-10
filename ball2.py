from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.x = 10
        self.y = 10
        self.my_score = 0

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.penup()
        self.goto(new_x, new_y)
        print(new_x, new_y)
        # Another way of slowing down the movement of the ball
        # new_x = self.xcor() + 0.70
        # new_y = self.ycor() + 0.50

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1

    def game_over(self):
        self.goto(0, 0)
        self.write('Wall hit! Game Over!', align='center', font=('ComicSans', 20, 'normal'))

    # def green_wins(self):
    #     self.goto(0,20)
    #     self.write('Green Wins!', align='center', font=('Arial', 35, 'normal'))
    #
    # def cyan_wins(self):
    #     self.goto(0,20)
    #     self.write('Cyan Wins!', align='center', font=('Arial', 35, 'normal'))