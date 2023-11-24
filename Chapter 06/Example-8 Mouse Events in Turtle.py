# Mouse Events in Turtle

import turtle
ws1 = turtle.Screen()  # Define a turtle screen object
tut1 = turtle.Turtle()  # Define a turtle object
tut2 = turtle.Turtle()  # Define a turtle object

def draw_line(i, j):   # Method to draw a line using turtle
    tut1.showturtle()   # Make turtle visible on screen
    tut1.fillcolor('white')  # Fill white color in turtle
    tut1.left(90)       # Turn turtle left by 90 degrees
    tut1.forward(150)   # Move turtle forward by 150 units

def write_screen(i, j):   # Method to write coordinates of click
    tut2.penup()      # Stop turtle from drawing
    tut2.pencolor('black')   # Change turtle pen color to black
    tut2.goto(i, j)   # Relocate turtle cursor to location clicked
    tut2.write(str(i) + "," + str(j))   # Write location coordinates

def color_turtle(i, j):  # To modify turtle properties on click
    tut1.shape('turtle')  # Change turtle shape to 'turtle'
    tut1.turtlesize(2)   # Change turtle size to 2
    tut1.fillcolor('blue')  # Fill blue color in turtle
    tut1.onclick(draw_line)  # Call onclick() to draw new line

def draw_drag(i, j):   # Method to draw while dragging the mouse
    tut2.ondrag(None)   # Call ondrag() with None object
    tut2.pendown()     # Set turtle to begin drawing
    tut2.pencolor('red')     # Set turtle pencolor to red
    tut2.setheading(90)  # Set the turtle orientation to 90 degrees
    tut2.goto(i, j)   # Turtle will relocate to (i, j) location
    tut2.ondrag(draw_drag)   # Call ondrag() to continue dragging 

def reset_screen(i, j):  # Method to reset screen on mouse click
    ws1.resetscreen()    # Call resetscreen() with screen object

def change_color(i, j):  # To change background color of screen 
    ws1.bgcolor('cyan')    # Set back ground color to 'cyan'

tut1.speed(5)   # Initially set turtle speed to 5
tut1.forward(150)    # Initially move turtle forward by 150 units
tut1.onclick(draw_line, btn=1)    # Bind onclick() with draw_line()
tut1.onclick(reset_screen, btn=3)  # Set right click to reset_screen
tut1.onclick(change_color, btn=2)  # middle button change_color()
tut1.onrelease(color_turtle)  # onrelease() event with color_turtle
turtle.onscreenclick(write_screen)  # onscreenclick() write_screen()
tut2.ondrag(draw_drag)  # Bind ondrag() mouse event with draw_drag()
ws1.mainloop()    # Wait until user closes the window
