import turtle

t = turtle.Pen()

# draw a 120 polygon
def draw_120():
	for y in range(0, 120):
		t.forward(5)
		t.left(3)

draw_120() 	