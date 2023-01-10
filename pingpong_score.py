from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_cyan = 0
        self.score_green = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 25)
        self.color('white')
        self.my_score = 0

    def update_my_score(self):
        self.goto(0,-40)
        self.write(f'Score = {self.my_score}', align='center', font=('Arial',30, 'normal'))

    def my_score_up(self):
        self.my_score += 1
        self.clear()
        self.update_my_score()



    # def update_score(self):
    #     self.write(f'cyan score = {self.score_cyan} green score = {self.score_green}',align='center', font=('Roboto', 20, 'normal'))

    # def cyan_score(self):
    #     self.score_cyan += 1
    #     self.clear()
    #     self.update_score()
    #
    # def green_score(self):
    #     self.score_green += 1
    #     self.clear()
    #     self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('Wall hit! Game Over!', align='center', font=('ComicSans', 20, 'normal'))

    # def final_score(self):
    #     self.goto(0, 50)
    #     # self.write(f'{self.score_cyan}', align='center', font=('Arial', 35, 'normal'))
    #     # print(type(self.score_cyan))
    #     if self.score_cyan > self.score_green:
    #         print('Cyan Wins')
    #         self.write('Cyan Wins', align='center', font=('Arial', 35, 'normal'))
    #     elif self.score_green > self.score_cyan:
    #         self.write('Green Wins', align='center', font=('Arial', 35, 'normal'))
    #     else:
    #         self.write('Draw', align='center', font=('Arial', 35, 'normal'))