import random
import turtle
from turtle import Turtle

timmy = Turtle() #timmy is an object instantiated from the Turtle class
timmy.shape("turtle")
timmy.color("brown","black")
timmy.speed('fast')

#generating a random walk
colors =['red','pink','blue','green','brown','gold']
direction = [0, 90, 180, 270]
for i in range(50):
    timmy.pensize(5)
    timmy.color(random.choice(colors))
    timmy.fillcolor('aqua')
    timmy.setheading(random.choice(direction))
    timmy.forward(30)
    timmy.screen.bgcolor("beige")
print(timmy)

myscreen = turtle.Screen()
print(myscreen)
myscreen.exitonclick()