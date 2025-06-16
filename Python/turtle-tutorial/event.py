import turtle as tr
import random

t = tr.Turtle()
s = tr.Screen()

tr.colormode(255)
s.listen()

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def move_left():
    t.left(90)

def move_right():
    t.right(90)

def change_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    t.color(r, g, b)


s.onkey(move_forward, 'w')
s.onkey(move_backward, 's')
s.onkey(move_left, 'a')
s.onkey(move_right, 'd')
s.onkey(change_color, "space")


s.exitonclick()
