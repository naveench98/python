import turtle as t
import random

circle=t.Turtle()

circle.pensize(1)
circle.speed("normal")

t.colormode(255)
circle.pensize(1)


def random_color():
    r=random.randint(0,255)
    y=random.randint(0,255)
    g=random.randint(0,255)
    random_color=(r,y,g)
    return random_color

for i in range(30):
    Current_heading=circle.heading()
    circle.setheading(Current_heading + 10)
    circle.circle(50)
    circle.color(random_color())