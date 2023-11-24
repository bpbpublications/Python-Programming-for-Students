# Key events in Turtle

import turtle

ws1 = turtle.Screen()  # Create a screen object
turtle = turtle.Turtle()  # Create a turtle object
turtle.speed(0)  # Set the turtle speed to 0
turtle.showturtle()  # Make the turtle visible on screen

def up():  # Define method to set turtle settings
    turtle.setheading(90)
    turtle.forward(100)

def left():  # Define method to set turtle orientation
    turtle.left(90)
    turtle.forward(100)

def change_blue():   # Define method to set turtle properties
    turtle.shape('circle')
    turtle.color("blue")

def inc_size():
    size = turtle.turtlesize()
    newsize = tuple(2 * elem for elem in size)
    print(newsize)
    turtle.turtlesize(*newsize)
 # Note: The turtlesize() function does not accept a tuple of three  values  as it accepts only int or float, so we need to unpack the   tuple using a * as we pass the tuple to the function to obtain three separate values.

ws1.listen()   # To set focus on turtle screen & register key events
ws1.onkey(up, 'Up')  # Bind up() method with up direction key
ws1.onkey(left, 'Left')  # Bind left() with left direction key
ws1.onkeyrelease(change_blue, 'b')  # Bind change_blue() to 'b' key
ws1.onkeypress(inc_size, '+')  # Increase size of turtle '+' key
ws1.mainloop()
