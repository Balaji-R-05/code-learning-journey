import turtle as tr
import random

tr.colormode(255)

t = tr.Turtle()
s = tr.Screen()

directions = [0, 90, 180, 270]
t.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rc = (r, g, b)
    return rc

def draw_spirograph(gap):
    for _ in range(360//gap):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + gap)

draw_spirograph(5)

s.exitonclick()