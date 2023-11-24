# Circle and Oval in Turtle

import turtle
window1 = turtle.Screen()   # Create a new Window Canvas
window1.bgcolor("white")
circle_turtle = turtle.Turtle()    # Draw a circle
circle_turtle.penup()
circle_turtle.goto(-100, -50)
circle_turtle.shape("triangle")
circle_turtle.color("blue")
circle_turtle.pendown()
circle_turtle.circle(100)
circle_turtle.penup()
oval_turtle = turtle.Turtle()   # Draw an oval
oval_turtle.penup()
oval_turtle.goto(200, -50)
oval_turtle.pendown()
for i in range(2):
    oval_turtle.circle(120, 90)
    oval_turtle.circle(250, 90)
window1.exitonclick()
