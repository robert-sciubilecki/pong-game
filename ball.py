from turtle import Turtle
from random import choice

BOUNCE_DIRECTION_WALL = {
    45: 315,
    315: 45,
    225: 135,
    135: 225
}

BOUNCE_DIRECTION_PADDLE = {
    45: 135,
    135: 45,
    225: 315,
    315: 225
}


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.reset_ball()

    def fly(self):
        self.forward(1)

    def bounce(self, element):
        heading = round(self.heading())
        if element == 'paddle':
            self.setheading(BOUNCE_DIRECTION_PADDLE[heading])
        elif element == 'wall':
            self.setheading(BOUNCE_DIRECTION_WALL[heading])

    def coordinates(self):
        x, y = round(self.xcor()), round(self.ycor())
        return x, y

    def contact(self, paddle):
        paddle_x, paddle_ys = paddle.coordinates()
        ball_x, ball_y = self.coordinates()
        contact = any(ball_y == paddle_y for paddle_y in paddle_ys) and ball_x == paddle_x
        if contact:
            return True

    def reset_ball(self):
        self.setheading(choice([value for value in BOUNCE_DIRECTION_WALL.values()]))
        self.goto(0, 0)
