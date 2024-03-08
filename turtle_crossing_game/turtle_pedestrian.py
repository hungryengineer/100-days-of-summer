import turtle
from turtle import Turtle, Screen
import random

class TurtlePedestrian(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.shapesize(1)
        self.setheading(90)
        self.penup()
        self.goto(0,-180)

    def move(self):
        self.forward(10)