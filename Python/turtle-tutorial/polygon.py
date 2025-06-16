from turtle import Turtle, Screen

t = Turtle()
s = Screen()

def draw_shapes(num_sides):
    for _ in range(num_sides):
        angle = 360/num_sides
        t.forward(100)
        t.right(angle)

for i in range(3, 21):
    draw_shapes(i)