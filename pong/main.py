import turtle
from turtle import Turtle, Screen
import random
from racket import Racket
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

first_racket = Racket((280, 0))
second_racket = Racket((-280, 0))

ball = Ball()

scoreboard = ScoreBoard()

screen.listen()
screen.onkey(first_racket.go_down, "Down")
screen.onkey(first_racket.go_up, "Up")
screen.onkey(second_racket.go_down, "s")
screen.onkey(second_racket.go_up, "w")


game_on = True
while game_on:
    screen.update()
    ball.move()
    if ball.ycor() > 200 or ball.ycor() < -200: #wall collision detection and bounce
        print("collision")
        ball.bounce_y()

    elif ball.distance(first_racket) < 30 and ball.xcor() > 280 or ball.distance(second_racket) < 30 and ball.xcor() > -280: #racket collision detection and bounce
        print("strike")
        ball.bounce_x()

    elif ball.xcor() > 280: #racket miss and bounce
        print("miss")
        ball.reset_position()
        scoreboard.update_scoreboard()
        scoreboard.increase_first_racket_score_count()

    elif ball.xcor() < -280: #racket miss and bounce
        print("miss")
        ball.reset_position()
        scoreboard.update_scoreboard()
        scoreboard.increase_second_racket_score_count()



screen.exitonclick()




