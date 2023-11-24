# Pentagon, Hexagon and Octagon in Turtle

import turtle
# Create a new canvas window with white background color
window1 = turtle.Screen()
window1.bgcolor("white")
# Create a star shape
star_turtle = turtle.Turtle()
star_turtle.color("green")
star_turtle.shape("turtle")
# executing loop 5 times for a star
for i in range(5):
    # moving turtle 100 units forward
    star_turtle.forward(100)
    # rotating turtle 144 degree right
    star_turtle.right(144)
# Create a Hexagon
hex_turtle = turtle.Turtle()
hex_turtle.shape("square")
hex_turtle.color("purple")
hex_turtle.penup()
hex_turtle.goto(150,200)
hex_turtle.pendown()
for i in range(6):     # Draw six sides of Hexagon
    hex_turtle.forward(100)
    hex_turtle.right(60)

oct_turtle = turtle.Turtle()    # Create an Octagon
oct_turtle.shape("arrow")
oct_turtle.color("orange")
oct_turtle.penup()
oct_turtle.goto(-250, 100)
oct_turtle.pendown()
for i in range(8):     # Draw 8 sides of Octagon
    oct_turtle.forward(100)
    oct_turtle.right(45)

window1.exitonclick()
