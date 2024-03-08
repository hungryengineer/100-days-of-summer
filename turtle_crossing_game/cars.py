import turtle
from turtle import Turtle, Screen
import random

color = ["blue","black", "white", "brown", "red", "purple", "yellow"]
class Cars:
    def __init__(self):
        self.cars = []

    def traffic(self):
        car = Turtle()
        car.shape("square")
        car.color(random.choice((color)))
        car.shapesize(0.3, 1.5, 0.3)
        car.setheading(180)
        car.penup()
        car.position()
        y_position = random.randint(-200,200)
        car.goto(300, y_position)
        self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.forward(5)
