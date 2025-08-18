import turtle as t
import random

shape= t.Turtle()

t.colormode(255)

def random_color():
    r=random.randint(0,255)
    y=random.randint(0,255)
    g=random.randint(0,255)
    random_color=(r,y,g)
    return random_color

numbers=[4,6,3,5,7,8,9,2,3,4]
deg=[0,90,180,270]
 # number of sides
  # angle for each turn


shape.pensize(14)
shape.speed("fastest")

for j in range(50):
    shape.color(random_color())
    shape.setheading(random.choice(deg))
    shape.forward(30) 

   