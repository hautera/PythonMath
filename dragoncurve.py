import turtle 

SPIRAL = True 

def curve(t, length, depth, sign):
	#print(t)
	if depth == 0:
		#print(depth)
		for turtle in t: 
			#print(type(turtle))
			turtle.forward(length)
	else:
		#print(depth)
		curve(t,length, depth-1, 1)
		for turtle in t:
			turtle.right(90*sign)
		curve(t,length, depth-1, -1)


if __name__ == '__main__':
	heading = 0
	colors = ['purple', 'red', 'green', 'blue']
	if SPIRAL: 
		turtles = []
		for i in range(4):
			t = turtle.Turtle()
			t.setheading(heading)
			t.color(colors[i])
			t.speed(0)
			heading += 90
			turtles.append(t)
	else:
		turtles = [turtle.Turtle()]
	
	
	curve(turtles, 1, 15, 1)
	turtle.exitonclick()