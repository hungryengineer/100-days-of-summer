import random
import turtle
from turtle import Turtle

race_on = True
myscreen = turtle.Screen()
myscreen.setup(width=400, height=300)
myscreen.bgcolor("beige")
user_bet = myscreen.textinput(title='Place your bet', prompt='who will win the race?')
print(user_bet)
timmys = []
rand_dist = random.randint(0,15)
timmy = Turtle()  #timmy is an object instantiated from the Turtle class
timmy.shape("turtle")
timmy.color("green")
timmy.speed('fast')
colors =['red','pink','blue','green','brown','gold']
y_positions = [0, -5, -10, -15, -20]

for i in range(0,5):
    timmy = Turtle(shape='turtle') # we are creating multiple objects from Turtle class
    timmy.penup()
    timmys.append(timmy)
    timmy.color(random.choice(colors))
    timmy.goto(x=-180, y=y_positions[i])
print(timmy)

while race_on: #putting a condition of race finish
    for i in timmys:
        i.forward(rand_dist)
    if timmy.xcor() > 175:
        race_on = False
        winner_turtle = timmy.pencolor()
        if winner_turtle == user_bet:
            print("You won!")
        else:
            print("tough luck!")
print("race over")

myscreen.exitonclick()
print(myscreen)
