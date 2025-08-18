from turtle import Turtle,Screen

timit=Turtle()  # Here we created object
print(timit)




timit.shape("arrow")  # object with methods
timit.color("red")

for j in range(6):

 timit.position()
 timit.forward(10)
 timit.penup()
 timit.forward(5)
 timit.pendown()

'''for i in range(3):
    timit.position()
    timit.right(90)
    timit.forward(100)'''


myscreen=Screen()
#print(myscreen)
myscreen.exitonclick()