from turtle import Turtle, Screen

t = Turtle()
s = Screen()

for _ in range(10):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown() 

s.exitonclick()