from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle():
    def __init__(self):
        self.paddle = []
        self.create_paddle()

    def create_paddle(self):
        paddle = Turtle(shape='square')
        paddle.penup()
        paddle.color('white')
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.setposition(350, 0)

    def up(self):
        pass

    def down(self):
        pass
