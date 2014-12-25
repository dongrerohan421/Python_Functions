import turtle 

def draw_square() : # define function
	window = turtle.Screen() # add screen to draw shape
	window.bgcolor("red") # add background color for window
	
	brad = turtle.Turtle()
	brad.shape("turtle") # set shape of turtle
	brad.color("yellow")  # set turtle color
	brad.speed(2)	     # set turtle speed

	'''
	brad.forward(100) # draw line forward in one direction
	brad.right(90)    # turn right at 90 degree
	brad.forward(100)
        brad.right(90) 
	brad.forward(100) 
        brad.right(90)
	brad.forward(100) 
        brad.right(90)
	'''
	for i in range(4):
		brad.forward(100)
        	brad.right(90)
	
	draw_circle()	
	draw_triangle()
	window.exitonclick() # Window will exit on click

def draw_circle() :
        angie = turtle.Turtle()
        angie.shape("circle") # set shape of turtle
        angie.color("green")  # set turtle color
        angie.speed(4)        # set turtle speed
	angie.circle(100)
	
def draw_triangle() :
	tr = turtle.Turtle()
	tr. shape("triangle")
	tr.color("blue")
	
	for i in range(2):
		tr.right(60)	
		tr.forward(100)
	tr.right(150)
	tr.forward(165)
draw_square() # call function
#draw_circle()
