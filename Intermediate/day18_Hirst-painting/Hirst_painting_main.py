# import colorgram
import turtle
from turtle import Turtle, Screen
import random

# colors = colorgram.extract('img.jpg', 25)
#
# color_palette = []
#
# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#
#     random_color = (r, g, b)
#     color_palette.append(random_color)
#
# print(color_palette)

turtle.colormode(255)
timmy = Turtle()
color_list = [(190, 150, 89), (112, 40, 33), (231, 213, 120), (106, 44, 48), (217, 225, 231), (108, 115, 25),
              (50, 81, 109), (105, 76, 91), (104, 152, 199), (113, 176, 159), (57, 54, 53), (179, 150, 68),
              (43, 74, 51), (41, 63, 95), (168, 201, 212), (167, 98, 95), (60, 86, 66), (38, 67, 45),
              (80, 37, 40), (174, 150, 155), (35, 55, 83), (163, 101, 103)]

# Makes a different starting point for the turtle:
timmy.hideturtle()
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.pendown()


def turning():
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)


row = 1

while row < 11:
    for dot in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
    turning()
    row += 1


my_screen = Screen()
my_screen.exitonclick()
