#Koch curve
import turtle
def Recursive_Koch(length, depth):
	if depth == 0:	
		turtle.forward(length)
	else:
		Recursive_Koch(length, depth-1)
		turtle.right(60)
		Recursive_Koch(length, depth-1)
		turtle.left(120)
		Recursive_Koch(length, depth-1)
		turtle.right(60)
		Recursive_Koch(length, depth-1)
# ----------
#turtle.left(90)
turtle.speed(0)
turtle.backward(300)
Recursive_Koch(1, 6)

turtle.exitonclick()