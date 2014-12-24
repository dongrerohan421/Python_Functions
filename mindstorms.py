import turtle 

def draw_square() : # define function
	window = turtle.Screen() # add screen to draw shape
	window.bgcolor("red") # add background color for window
	
	brad = turtle.Turtle()
	brad.shape("turtle") # set shape of turtle
	brad.color("yellow")  # set turtle color
	brad.speed(2)	     # set turtle speed

	brad.forward(100) # draw line forward in one direction
	brad.right(90)    # turn right at 90 degree
	brad.forward(100)
        brad.right(90) 
	brad.forward(100) 
        brad.right(90)
	brad.forward(100) 
        brad.right(90)

	window.exitonclick() # Window will exit on click

draw_square() # call function
