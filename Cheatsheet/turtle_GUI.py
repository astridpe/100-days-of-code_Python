import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
timmy.speed("fastest")

# timmy.shape("turtle")
# timmy.color("DarkOliveGreen")

# Timmy makes a sircle:
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# Timmy makes a dashed line:
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# CHALLANGE 3:
# # Make a loop that draw shapes from 3 to 10 corners and changes color for each round:
# corner = 3
#
# # color-list:
# colors = ["coral", "dark green", "teal", "dark red", "chocolate", "olive", "navy", "gold"]
#
# while corner < 11:
#     angle = 360 / corner
#
#     for _ in range(corner):
#         timmy.forward(100)
#         timmy.right(angle)
#
#     timmy.color(random.choice(colors))
#     corner += 1


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_tuple = (r, g, b)
    return random_tuple


# # CHALLANGE 4
# # Random Walk:
#
# directions = [0, 90, 180, 270]
# timmy.pensize(10)
#
# for _ in range(200):
#     timmy.setheading(random.choice(directions))
#     timmy.forward(50)
#     timmy.color(random_color())

# CHALLANGE 5
# Draw a spirograph

def draw_spirograph(size_of_gap):
    for circle in range(int(360 / size_of_gap)):
        timmy.circle(100)
        timmy.color(random_color())
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)


my_screen = Screen()
my_screen.exitonclick()


