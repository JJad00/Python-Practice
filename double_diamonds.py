"""this program is to generate two diamonds using turtle graphics"""

import turtle

# predefine the diamond side lenght 
SIDE_LENGTH = 100
# predefine the fill color - 
COLOR = "blue"

# setup the turtle window
turtle.setup(500,600)

#setup the turtle
turtle.hideturtle()
turtle.fillcolor(COLOR)

# draw the left-side diamond first using the predefined SIDE_LENGTH - fill the code
turtle.begin_fill()
turtle.left(45)
turtle.forward(SIDE_LENGTH)
turtle.right(90)
turtle.forward(SIDE_LENGTH)
turtle.right(90)
turtle.forward(SIDE_LENGTH)
turtle.right(90)
turtle.forward(SIDE_LENGTH)
turtle.right(90)
turtle.end_fill()

# draw the right-side diamond next -
turtle.right(45)
turtle.penup()
turtle.forward(SIDE_LENGTH * 1.414)
turtle.pendown()
turtle.left(45)
turtle.begin_fill()
turtle.forward(SIDE_LENGTH)
turtle.right(90)
turtle.forward(SIDE_LENGTH)
turtle.right(90)
turtle.forward(SIDE_LENGTH)
turtle.right(90)
turtle.forward(SIDE_LENGTH)
turtle.right(90)
turtle.end_fill()

turtle.done()