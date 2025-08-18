from turtle import Turtle
import random

shape = Turtle()

colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "cyan"]

 # number of sides
  # angle for each turn

def shapes(num):
    degree = 360 / num
    for i in range(num):
        shape.forward(100)   # move forward
        shape.right(degree)  # turn right


for j in range(3,11):
    shape.color(random.choice(colors))
    shapes(j)