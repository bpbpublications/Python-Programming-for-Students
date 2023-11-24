# Spiral in Turtle

import turtle
a = turtle.Turtle()
colors = ["green", "red", "yellow", "blue", "orange", "cyan"]
for i in range(100):
    a.pensize(5)
    a.color(colors[i % 6])
    a.forward(7+i)
    a.right(21)
turtle.done()
