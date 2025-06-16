from turtle import Turtle, Screen

t = Turtle()
print(t)

t.shape("turtle")
t.color("red")
t.forward(100)

s = Screen()
print(s.canvwidth)
print(s.canvheight)
s.exitonclick()