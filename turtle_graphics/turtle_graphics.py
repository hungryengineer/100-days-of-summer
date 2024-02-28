import turtle
from prettytable import PrettyTable
import pokemon
import random

timmy = turtle.Turtle() #this is a class
timmy.shape("turtle")
timmy.color("green","black")

def draw_shape(num_sides):
    angle = 360/num_sides
    for i in range(num_sides):
      timmy.forward(50), timmy.left(angle)
draw_shape(10)

colors =['red','pink','blue','green','peach','gold']
for num_sides in range(3,11):
    timmy.color(random.choice(colors))
    draw_shape(num_sides)
print(timmy)

#dashed line
# for i in range(1,10):
#     timmy.pendown(),timmy.forward(10), timmy.penup(),timmy.forward(10)
# for i in range(5):
#     timmy.forward(2), timmy.color('black'),timmy.forward(2), timmy.color('white')

myscreen = turtle.Screen()
print(myscreen)
myscreen.exitonclick()


#table = PrettyTable()
#print(table)
# table.field_names = ["Pokemon Name","Type"]
#
# table.add_row(["Pikachu","Electric"])
# table.add_row(["Squirtle","Water"])
# table.add_row(["Charmander","Fire"])
# table.align = 'l'
# print(table)