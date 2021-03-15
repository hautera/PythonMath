import math 
import numpy as np
import matplotlib.pyplot as plt 

class LinearMap(IterMap):
	def __init__(self, s0, a):
		self.a = a 
		super.__init__(s0, fn=lambda x: a * x)

	def derivative(self):
		return self.a

class IterMap():
	"""
	Creates a iterative map
	"""
	def __init__(self, s0, fn=lambda x: x):
		self.prev_state = None
		self.state = s0 
		self.fn = fn

	"""
	Returns the next state of the map 
	"""
	def current_state(self):
		return self.state

	"""
	returns the next state in the iterative map 
	"""
	def __call__(self):
		self.prev_state, self.state = self.state, self.fn(self.state)
		return self.fn(self.state)

	"""
	Calculates the (approximate) derivative the map at current state 
	"""
	def derivative(self):
		if self.prev_state is not None:
			return (self.fn(self.state) - self.fn(self.prev_state)) / (self.state - self.prev_state)
		else:
			return 0

	def plot_against_time(self, N):
		X = np.array(range(N))
		Y = list()
		for i in range(N):
			Y.append(self.__call__())

		plt.plot(X,Y)
		plt.show()

	def plot_against_state(self, N):
		X = list()
		Y = list()
		X.append(self.state)
		for i in range(N):
			next_state = self.__call__()
			Y.append(self.state)
			X.append(self.state)
		del X[-1]

		plt.plot(X,Y)
		plt.show()

if __name__ == '__main__':
	test = IterMap(1, fn=lambda X: 2*X)
	test()
	print(test.derivative())



