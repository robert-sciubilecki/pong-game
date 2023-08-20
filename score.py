from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, x):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.score = 0
        self.goto(x, 0)

    def increase_score(self):
        self.score += 1

    def display_score(self):
        self.clear()
        self.write(arg=self.score, align='center', font=('Verdana', 50, 'normal'))


class Info(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(-width/2 + 20, height/2 - 25)
        self.write(arg="Press 'r' to reset or 'q' to quit", align='left', font=('Verdana', 13, 'normal'))
        self.goto(width/2 - 20, round(self.ycor()))
        self.write(arg="Left paddle controls: A/Z, Right paddle: Up/Down", align='right',
                   font=('Verdana', 13, 'normal'))
