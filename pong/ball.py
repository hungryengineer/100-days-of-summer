import turtle
from turtle import Turtle, Screen
import random
class Ball(Turtle):
    def __init__(self,):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.6, 0.6, 0.6)
        self.penup()
        self.x_move = 0.07
        self.y_move = 0.07
        self.speed(5)
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)