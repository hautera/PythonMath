# Heat Equation simulation:
# d^2u/dx^2 = du/dt
# Default init conditions:
# du/dx @(0,t) and (1,t) = 0
# u(x,0) = f(x)
# t > 0 and x in [0,1]

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


PI = 3.14159
#integrates a series of y values assuming evenly spaced y's
def integrate(a, b, y):
	n = len(y)
	s = np.sum(y) - (y[0]/2 + y[-1]/2) # Trapezoid approximation o
	return ( b - a ) * s / n

def calc_fourier_series(x, y, num=1000):
	a0 = integrate(-1,1,y)
	A = [a0]
	B = []
	n = 1
	PI = 3.14159
	while len(A) < num:
		an = integrate(-1,1, np.multiply(np.cos(n*PI*x),y))
		an = an / integrate(-1,1, np.multiply(np.cos(n*PI*x),np.cos(n*PI*x)))
		bn = integrate(-1,1, np.multiply(np.sin(n*PI*x),y))
		plt.plot(np.cos(n*PI*x))
		A.append(an)
		B.append(bn)
		n += 1

	return A#, B

def animate(i, An, X, line):
	Y = heat(An, i/10000, X)
	line.set_data(X, Y)

	return line, 

def exp(x):
	return 2.71828 ** x

def heat(A, t, X):
	s = np.zeros(len(X))
	n = 0
	for an in A: 
		s = np.add(s, an*exp(-1*((n*PI)**2)*t) * np.cos(n*PI*X))
		n += 1 
	#print(s)
	return s

def main():
	X = np.linspace(0,1,1000)
	Y = np.zeros(1000)
	Y[500] = 10000
	An = calc_fourier_series(X,Y)
	#print(An)
	fourier = heat(An, 0, X)
	#plt.plot(X,Y)
	#plt.show()
	fig, ax = plt.subplots()
	ax.set_ylim([min(fourier),max(fourier)])
	line, = ax.plot(X, fourier)
	#ax.plot(X,Y)
	anim = animation.FuncAnimation(fig, animate, fargs=(An, X, line), frames=100000, interval=100, blit=True)

	plt.show()

if __name__ == '__main__':
	main()


