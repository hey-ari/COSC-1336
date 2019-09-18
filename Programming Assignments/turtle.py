### Program 3 -- written by Ariadna Ayala.


## creating a pink diamond with red outline which has each side = 100.

import turtle
turtle.penup()
turtle.goto(-200,275)
turtle.pendown()
turtle.fillcolor('pink')
turtle.begin_fill()
turtle.pencolor('red')
turtle.setheading(-45)
turtle.forward(100)
turtle.setheading(-135)
turtle.forward(100)
turtle.setheading(-225)
turtle.forward(100)
turtle.setheading(-315)
turtle.forward(100)
turtle.end_fill()

## Here I'm moving to an empty space to create a new figure and resetting heading.

turtle.setheading(0)
turtle.penup()
turtle.goto(-200,50)

## Creating a black circle with blue outline and r=50.

turtle.pendown()
turtle.fillcolor('black')
turtle.pencolor('blue')
turtle.begin_fill()
turtle.setheading(-90)  ## I realized that if I keep heading at 0 the figures will overlap,
turtle.circle(50)       ## so I changed the direction of the "turtle"
turtle.end_fill()

## Moving to an empty space to write the text away from the figures.

turtle.setheading(0)
turtle.penup()
turtle.goto(50,100)

## Creating text using black pen.

turtle.pencolor('black')
turtle.write('This program is written by Ariadna Ayala')
turtle.forward(25)  ## just to move the "turtle" away from the text.


##   THE END   ##
