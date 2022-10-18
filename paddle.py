from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle():
    def __init__(self):
        self.paddle = Turtle(shape='square')
        self.create_paddle()

    def create_paddle(self):
        self.paddle.penup()
        self.paddle.color('white')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.goto(350, 0)

    def up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)
