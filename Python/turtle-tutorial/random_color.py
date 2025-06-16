import turtle as tr
import random

tr.colormode(255)

t = tr.Turtle()
s = tr.Screen()

colors = ['red', 'blue', 'orange', 'green', 'black']
directions = [0, 90, 180, 270]
t.pensize(10)
t.shape('circle')
t.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rc = (r, g, b)
    return rc


for i in range(400):
    t.pencolor(random_color())
    t.forward(20)
    t.setheading(random.choice(directions))
    
s.exitonclick()