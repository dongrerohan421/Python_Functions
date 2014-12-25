import turtle

def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("yellow")
	# Create the turtle Brad - Draw a square
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("red")
	brad.speed(5)

	for i in range(1,37): # range is 0-36 to draw circle
		draw_square(brad)
		brad.right(10)

	window.exitonclick()

draw_art()
