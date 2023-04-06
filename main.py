import random
import turtle
from turtle import Turtle
import colorgram
turtle.colormode(255)
tim = Turtle()
tim.speed(25)
color_list = [(225, 234, 230), (173, 49, 79), (43, 98, 147), (204, 162, 94), (223, 210, 103), (138, 91, 64), (175, 164, 40)]



for i in range(10):
    for i in range(10):
        tim.setheading(0)
        tim.penup()
        tim.forward(50)
        for i in range(1):
            random_color = random.choice(color_list)
            tim.color((random_color))
            tim.dot(20)
    tim.penup()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)



turtle.exitonclick()