import turtle
from turtle import Turtle, Screen
import random
from turtle_pedestrian import TurtlePedestrian
from cars import Cars

#step 1. create a screen

screen = Screen()
screen.bgcolor("beige")
screen.setup(height=400, width=600)
screen.tracer(0)

#step 2. create a turtle object

turtle_pedestrian = TurtlePedestrian()

cars = Cars()

screen.listen()
screen.onkeypress(turtle_pedestrian.move, "Up")

game_on = True
while game_on:
    screen.update()
    cars.traffic()
    cars.move_car()
    for car in cars.cars:
        if turtle_pedestrian.distance(car) < 20:
            print("squish!!")
            game_on = False
            turtle_pedestrian.write("GAME OVER", align="center")


screen.exitonclick()

