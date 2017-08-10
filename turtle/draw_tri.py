import turtle

t = turtle.Pen()

# draw a triangle
def draw_triangle():
	for x in range(0,3):
		t.forward(150)
		t.left(120)

draw_triangle() 	