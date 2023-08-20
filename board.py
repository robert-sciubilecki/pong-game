from turtle import Turtle


class BoardPainter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')

    def paint_borders(self, width, height):
        adjusted_height = height - 60
        self.goto(x=width, y=adjusted_height/2)
        self.pendown()
        self.goto(x=-width, y=adjusted_height/2)
        self.goto(x=-width, y=-adjusted_height/2)
        self.goto(x=width, y=-adjusted_height/2)
        return round(adjusted_height/2) - 10, round(-adjusted_height/2) + 10
