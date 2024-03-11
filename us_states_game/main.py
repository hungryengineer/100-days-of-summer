import pandas
import turtle
from turtle import Turtle, Screen

score = 0
data = pandas.read_csv("50_states.csv")
# print(data.state)

myturtle = Turtle()
scoreboard = Turtle()

screen = Screen()
screen.title("U.S states game")

screen.bgcolor("white")
img = "blank_states_img.gif"
screen.addshape(img)
myturtle.shape(img)

scoreboard.color("brown")
scoreboard.hideturtle()
scoreboard.shapesize(1.3, 1.3)
scoreboard.penup()
scoreboard.goto(220, 220)
scoreboard.write(score, align="left", font="courier")


# def get_mouse_click_coor(x, y):
#     print(x, y)
#     answer_state = screen.textinput(title="guess the state", prompt="what is the name of this state?")
#     print(answer_state)
# screen.onscreenclick(get_mouse_click_coor)
game_on = True
while game_on:

    answer_state = screen.textinput(title="guess the state", prompt="what is the name of this state?")
    state_list = data.state.to_list()
    if answer_state == "Exit":
        missing_states = []
        if answer_state not in state_list:
            missing_states.append(state_list)
            print(missing_states)
            break
    elif answer_state in state_list:
        pointer = Turtle()
        pointer.color("blue")
        pointer.hideturtle()
        pointer.penup()
        state_data = data[data.state == answer_state]
        pointer.goto(int(state_data.x), int(state_data.y))
        pointer.write(answer_state)
    else:
        game_on = False

screen.mainloop()
