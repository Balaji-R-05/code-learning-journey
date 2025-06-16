from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()

colors = ['red', 'blue', 'orange', 'green', 'black']
directions = [0, 90, 180, 270]
t.pensize(10)
t.shape('circle')
t.speed("fastest")

for i in range(400):
    t.color(random.choice(colors))
    t.forward(20)
    t.setheading(random.choice(directions))
    
s.exitonclick()