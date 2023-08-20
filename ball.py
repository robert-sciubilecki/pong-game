from turtle import Turtle
from random import choice

BOUNCE_DIRECTION = {
    45: 315,
    315: 225,
    225: 135,
    135: 45
}


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.reset_ball()

    def fly(self):
        self.forward(0.7)

    def bounce(self):
        heading = round(self.heading())
        self.setheading(BOUNCE_DIRECTION[heading])

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
        self.setheading(choice([value for value in BOUNCE_DIRECTION.values()]))
        self.goto(0, 0)
