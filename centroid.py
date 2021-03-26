import tkinter as tk
from math import sqrt

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()
		self.coord_list = []
		self.drawn_list = set()

	def create_widgets(self):
		self.canvas = tk.Canvas(self, height=500, width=600)
		self.canvas.bind("<B1-Motion>", self.drag)
		self.canvas.pack()

		self.calc_center = tk.Button(self, bg='black')
		self.calc_center["text"] = "Calculate centroid"
		self.calc_center["command"] = self.user_click
		self.calc_center.pack(side="top")
		
		self.clear = tk.Button(self, text="CLEAR", fg="black", bg='black', command=self.clear_screen)
		self.clear.pack(side="bottom")

		self.quit = tk.Button(self, text="QUIT", fg="red", bg='black',
		                      command=self.master.destroy)
		self.quit.pack(side="bottom")

	def clear_screen(self):
		"""
		Clears the screen and resets the shapes :)
		"""
		self.canvas.delete("all")
		self.drawn_list = set()
		self.coord_list = []

	def user_click(self):
		"""
		Finds the centroid of the first shape drawn
		Then draws lines on the screen showing centroid
		"""

		if len(self.drawn_list):
			for s in self.drawn_list:
				shape = self.coord_list[s[0]:s[1]]
				x, y = self.calc_centroid(shape)

			self.canvas.create_line(0, y, 600, y, fill="blue")
			self.canvas.create_line(x, 0, x, 500, fill="blue")
		else:
			print("There's no contained shapes")

	def drag(self, event):
		"""
		Responds to user's drawing on the canvas
		"""
		if len(self.coord_list) > 0:
			self.canvas.create_line(event.x, event.y, 
				self.coord_list[-1][0], self.coord_list[-1][1])

		self.coord_list.append([event.x, event.y])

		poly_list = check_contained(self.coord_list) - self.drawn_list
		for polygon in poly_list:			# will accidently draw this multilple times oops 
			#self.canvas.create_polygon( self.coord_list[polygon[0]:polygon[1]], fill='black')
			self.drawn_list.add(polygon)


	def calc_centroid(self, points):
		"""
		Calculates the centroid of an arbitrary enclosed shape
		points is the list of coordinates of the shape in question
		Works iff shape is simply closed and continuous
		"""
		self.canvas.create_polygon(points)
		x = [i[0] for i in points] # all the math is wrong :(
		y = [j[1] for j in points]

		area = x[0] * (y[0] - y[-1])
		x_hat = (x[0] ** 2) * (y[0] - y[-1]) / (2) 
		y_hat = -(y[0] ** 2) * (x[0] - x[-1]) / (2)

		for i in range(1, len(points) - 1):
			dt = length(x[i], y[i], x[i - 1], y[i - 1])
			dy = y[i] - y[i - 1]
			dx = x[i] - x[i - 1]
			area += 2 * x[i] * dy
			x_hat += (x[i] ** 2) * dy
			y_hat -= (y[i] ** 2) * dx

		area += x[-1] * (y[-1] - y[-2])
		x_hat += (x[-1] ** 2) * (y[-1] - y[-2]) / 2
		y_hat -= (y[-1] ** 2) * (x[-1] - x[-2]) / 2
		area /= 2
		x_hat /=2
		y_hat /= 2
		print("Area: %s\nX: %s\nY: %s" % (area, x_hat/area, y_hat/area))
		return x_hat/area, y_hat/area

def length(x1, y1, x2, y2):
	return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 )
		
def check_contained(ls, a=1):
	"""
		Checks if a list of coordinates encloses a space 
		Assumes that the there are lines connecting the points
	"""
	indices_of_shapes = set()
	min_index = a
	for i in range(3,len(ls)):
		b2, b1, a2, a1 = ls[i][1], ls[i-1][1], ls[i][0], ls[i-1][0]
		
		for j in range(min_index, i):
			y2, y1, x2, x1 = ls[j][1], ls[j-1][1], ls[j][0], ls[j-1][0]
			
			if lines_intersect(a1, b1, a2, b2, x1, y1, x2, y2) and abs(j - i) > 1 :
				indices_of_shapes.add((j,i))

	return indices_of_shapes


def lines_intersect(x1, y1, x2, y2, a1, b1, a2, b2):
	"""
		Checks if two line segments intersect 
	"""

	# Ensures that x1 < x2 
	(x1, x2, y1, y2) = (x1, x2, y1, y2) if x1 < x2 else (x2, x1, y2, y1) 
	(a1, a2, b1, b2) = (a1, a2, b1, b2) if a1 < a2 else (a2, a1, b2, b1) 
	
	# Make lines same domain
	if x1 > a1:
		if x1 > a2 or a1 == a2:
			return False 

		a = x1 
	else:
		if a1 > x2 or x1 == x2:
			return False
		
		a = a1 

	if x2 < a2:
		if x2 < a1 or a1 == a2:
			return False 

		b = x2
	else:
		if a2 < x1 or x1 == x2:
			return False 

		b = a2

	if x1 != x2:
		x1, y1, x2, y2 = trim_line(x1, y1, x2, y2, a, b)
	if a1 != a2:
		a1, b1, a2, b2 = trim_line(a1, b1, a2, b2, a, b)

	
	return (y1 >= b1 and y2 <= b2) or (y1 <= b1 and y2 >= b2)
		

def trim_line(x1, y1, x2, y2, a, b):
	"""
		Trims x1 and x2 to and b 
		gets angry if x1 == x2
		other wise... 
	"""
	m = (y2 - y1)/(x2 - x1)

	if x1 < a:
		y1 += m * (a - x1)

	if x2 > b: 
		y2 += m * (b - x2)

	return x1, y1, x2, y2 

if __name__ == '__main__':
	root = tk.Tk()
	app = Application(master=root)
	app.mainloop()






