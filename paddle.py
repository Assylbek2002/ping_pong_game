from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x_pos = x
        self.y_pos = y
        self.shape('square')
        self.penup()
        self.goto(self.x_pos, self.y_pos)
        self.shapesize(stretch_len=0.7, stretch_wid=4)
        self.color("white")

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.x_pos, new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.x_pos, new_y)
