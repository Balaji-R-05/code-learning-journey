from turtle import Turtle, Screen


t = Turtle()
x = Turtle()
s = Screen()

t.color("red")
x.color("blue")

t.forward(200)
x.left(180)
x.forward(200)


for i in range(180):
    t.forward(i)
    t.left(i)
    x.forward(i)
    x.right(i)

x.left(90)
t.right(90)
t.forward(200)
x.forward(200)


s.exitonclick()