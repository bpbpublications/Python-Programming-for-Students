# Sample project with solutions
# Create a two-player box completion game using Turtle in Python. 
# The player who completes the maximum boxes and stays on the window screen becomes the winner. 
# The player who first moves out of the window screen (that is, touches the window boundary first) is the loser.
# The project has two players: a red turtle and a blue turtle. The user must press r first to initiate the red turtle and
# then press key b to initiate the blue turtle. After this, the user must press the Enter key to begin the game. 
# As the game begins, both turtles begin to draw edges and create square boxes in different directions. 
# Each turtle can move in random directions based on the value of the variable flag. 
# Moreover, a turtle can repeatedly draw previously created boxes by itself or another turtle. 
# The turtle that first touches the window boundary is the loser, whereas the one who creates maximum boxes inside the window screen
# without touching the screen edge is the winner:


import random
import turtle

ws1 = turtle.Screen()
ws1.screensize(canvwidth=320, canvheight=320, bg="white")
pos = 0
Red = turtle.Turtle()
Blue = turtle.Turtle()

Red.fillcolor("red")   # set colors of turtles
Blue.fillcolor("blue")

# function to check whether turtle
# is in Screen or not
def isInWindow(wind, turt):
    # Set edge values as boundaries based on screen size of window
    leftedge = -320
    rightedge = 320
    topedge = 320
    bottomedge = -320
    # getting the current position of the turtle
    turtle_X = turt.xcor()
    turtle_Y = turt.ycor()
    # variable to store whether in screen or not
    inside = True
    # condition to check whether in screen or not
    if turtle_X > rightedge or turtle_X < leftedge:
        inside = False
    if turtle_Y > topedge or turtle_Y < bottomedge:
        inside = False
    # returning the result
    return inside

# function to check whether both turtle have different position 
def sameposition(Red, Blue):
    if Red.pos() == Blue.pos():
        return False
    else:
        return True

def red_up():
    global pos
   # set pencolor as red
    Red.pencolor("red")
    # set pensize as 5
    Red.pensize(5)
    # set turtleshape as turtle
    Red.shape('turtle')
    pos = Red.pos()

def blue_up():
    # Turtle Blue initialization and set pencolor as blue
    Blue.pencolor("blue")
    Blue.pensize(5)    # set pensize as 5
    Blue.shape('turtle')    # set turtleshape as turtle
    Blue.hideturtle()    # make the turtle invisible
    Blue.penup()    # don't draw when turtle moves
    # Set the turtle to a location 100 pixels away from Red turtle
    Blue.goto(pos[0] + 100, pos[1])
    Blue.showturtle()   # make the turtle visible
    Blue.pendown()        # draw when the turtle moves

def game():
    # To check whether turtles are inside screen or not
    rT = True    # To store red turtle location
    bT = True    # To store blue turtle location
    # loop for the game
    while rT and bT and sameposition(Red, Blue):
        flagRed = random.randrange(0, 2) # flag value for Red turtle        # change angle for Red turtle to 90 to complete the box
        angleRed = 90
        # condition for left or right based on flag
        if flagRed == 0:
            Red.left(angleRed)
        else:
            Red.right(angleRed)
        Red.forward(50)   # draw for Red box of edge of length 50
        flagBlue = random.randrange(0, 2)   # flag value for Blue turtle
        angleBlue = 90   # set angle for Blue to 90 to complete box
        # condition for left or right turn based on flag value
        if flagBlue == 0:
            Blue.left(angleBlue)
        else:
            Blue.right(angleBlue)
        Blue.forward(50)   # draw for Blue
        # checking whether turtles are inside window or not
        bT = isInWindow(ws1, Blue)
        rT = isInWindow(ws1, Red)
    # condition check for draw or win
    if rT == True and bT == False:
        # writing results
        Red.write("Red Won", True, align="center",
                  font=("arial", 15, "bold"))
    elif bT == True and rT == False:
        # writing results
        Blue.write("Blue Won", True, align="center",
                   font=("arial", 15, "bold"))
    else:
        # writing results
        Red.write("Draw", True, align="center",
                  font=("arial", 15, "bold"))
        Blue.write("Draw", True, align="center",
                   font=("arial", 15, "bold"))

ws1.listen()  # Helps to set foocus on turtle screen 
ws1.onkey(red_up, 'r')  # call red_up() method with 'r' key
ws1.onkey(blue_up, 'b')  # call red_left() with 'b' key
ws1.onkey(game, 'Return')   # Press Enter key to start game
ws1.mainloop()
