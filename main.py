import turtle
from prettytable import PrettyTable
import pokemon
# timmy = turtle.Turtle() #this is a class
# timmy.shape("turtle")
# timmy.color("green","red")
# timmy.forward(30)
#
# print(timmy)
#
# myscreen = turtle.Screen()
# print(myscreen)
# myscreen.exitonclick()
table = PrettyTable()
#print(table)

table.field_names = ["Pokemon Name","Type"]

table.add_row(["Pikachu","Electric"])
table.add_row(["Squirtle","Water"])
table.add_row(["Charmander","Fire"])
table.align = 'l'
print(table)