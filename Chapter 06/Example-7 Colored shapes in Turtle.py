# Colored shapes in Turtle

import turtle
# Set up the turtle screen and set the background color to white
window = turtle.Screen()
window.bgcolor("white")
# Create a new turtle turtle1
# Set speed of turtle to 5 (normal)
turtle1 = turtle.Turtle()
turtle1.speed(5)
# Set the fill color to yellow
turtle1.fillcolor("yellow")
turtle1.begin_fill()
# Draw the circle with a radius of 150 pixels
turtle1.circle(150)
# End the fill and stop drawing
turtle1.end_fill()
# Wait for user to manually close the window
turtle.done()
