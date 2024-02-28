import random
import turtle
from turtle import Turtle

timmy = Turtle() #timmy is an object instantiated from the Turtle class
timmy.shape("turtle")
timmy.color("black")
timmy.speed('fast')
timmy.screen.bgcolor("beige")
colors =['red','pink','blue','green','brown','gold']

def spirograph():
    for i in range(15):
        timmy.color(random.choice(colors))
        timmy.circle(30)
        timmy.penup()
        timmy.right(90)
        timmy.pendown()
        timmy.right(60)
        timmy.circle(30)
print(timmy)
spirograph()
myscreen = turtle.Screen()
print(myscreen)
myscreen.exitonclick()