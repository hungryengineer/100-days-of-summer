import turtle
from turtle import Turtle, Screen
import random
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.hideturtle()
        self.shapesize(3, 2, 1.5)
        self.first_racket_score = 0
        self.second_racket_score = 0

    def update_scoreboard(self):
        self.clear()
        self.penup()
        self.goto(-280, 150)
        self.write(self.first_racket_score)
        self.goto(280, 150)
        self.write(self.second_racket_score)
    def increase_first_racket_score_count(self):
        self.first_racket_score +=1
    def increase_second_racket_score_count(self):
        self.second_racket_score +=1