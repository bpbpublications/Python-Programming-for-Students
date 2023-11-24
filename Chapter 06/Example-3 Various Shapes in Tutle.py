# Various shapes in Turtle

import turtle
# Create a new canvas window with white background color
window1 = turtle.Screen()
window1.bgcolor("white")
# Create a new turtle object to draw square
square_turtle = turtle.Turtle()
square_turtle.shape("turtle")
square_turtle.color("red")
# To draw the first edge of the square
# Originally the turtle is moved forward by 100 pixel units
square_turtle.forward(100)
# Move right by 90 degrees to turn in downwards direction.
square_turtle.right(90)
# Move forward by 100 units to draw the second edge of square
square_turtle.forward(100)
# Again turn to right by 90 degrees and move forward by 100 pixels
square_turtle.right(90)  # Third edge of square
square_turtle.forward(100)
square_turtle.right(90)  # Fourth edge of square
square_turtle.forward(100)
square_turtle.penup()  # Stop cursor from drawing
# Create Rectangle with length and breadth as 100 and 200 pixels
rec_turtle = turtle.Turtle()
rec_turtle.shape("arrow")
rec_turtle.color("blue")
rec_turtle.penup()  # Stop turtle from drawing while moving
rec_turtle.goto(-200, 100)   # Set turtle location (-200, 100)
rec_turtle.pendown()  # Start drawing by turtle
rec_turtle.forward(100)
rec_turtle.right(90)
rec_turtle.forward(200)
rec_turtle.right(90)
rec_turtle.forward(100)
rec_turtle.right(90)
rec_turtle.forward(200)
# Create a Triangle
tri_turtle = turtle.Turtle()
tri_turtle.shape("circle")
tri_turtle.color("green")
tri_turtle.penup()
tri_turtle.goto(200, -100)
tri_turtle.pendown()
# Draw 3 sides of triangle
for i in range(3):
    tri_turtle.forward(100)
    tri_turtle.left(120)
# Wait for user mouse click to exit canvas window
window1.exitonclick()
