from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y, top_border, bottom_border):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.width(20)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(x, y)
        self.movement = 0
        self.top_border = top_border
        self.bottom_border = bottom_border

    def decrease_movement(self):
        if self.movement > 0:
            self.movement -= 1
        if self.movement < 0:
            self.movement += 1

    def up(self, animation=False):
        if self.ycor() < self.top_border - 40:
            self.goto(x=self.xcor(), y=self.ycor() + 1)
            if not animation:
                self.movement = -40

    def down(self, animation=False):
        if self.ycor() > self.bottom_border + 40:
            self.goto(x=self.xcor(), y=self.ycor() - 1)
            if not animation:
                self.movement = 40

    def coordinates(self):
        x, y = round(self.xcor()), round(self.ycor())
        y_coors = [y_cor for y_cor in range(y-50, y+50, 1)]

        if x < 0:
            x_coors = x+15
        else:
            x_coors = x-10
        return x_coors, y_coors

    def reset_paddle(self):
        self.goto(round(self.xcor()), 0)
