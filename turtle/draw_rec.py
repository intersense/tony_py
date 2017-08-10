import turtle

t = turtle.Pen()

# draw a rectangle
def draw_rec():
	for x in range(0, 4):
		t.forward(150)
		t.left(90)

draw_rec()