import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


#There seems to be a bug..
#The program doesn't seem to be conserving the dirlect condition 


PI = 3.14159
#integrates a series of y values assuming evenly spaced y's
def integrate(a, b, y):
	n = len(y)
	s = np.sum(y) - (y[0]/2 + y[-1]/2) # Trapezoid approximation o
	return ( b - a ) * s / n

def calc_fourier_series(x, y, num=1000, sine=True, cosine=True):
	A = []
	B = []
	n = 1
	PI = 3.14159
	if cosine:
		a0 = integrate(0,1,y)
		A.append(a0)

	while n < num:
		if cosine:
			an  = integrate(0,1, np.multiply(np.cos(n*PI*x),y))
			an /= integrate(0,1, np.multiply(np.cos(n*PI*x),np.cos(n*PI*x)))
			A.append(an)
		if sine:
			bn  = integrate(0,1, np.multiply(np.sin(n*PI*x),y))
			bn /= integrate(0,1, np.multiply(np.sin(n*PI*x),np.sin(n*PI*x)))
			B.append(bn)

		n += 1

	return A, B

#Returns the solution to the wave equation for list of X,
#a value t and the calculated initial conditions A, B
# Assumes len(A) = len(B) + 1
def wave(A,B,X,t):
	n = 1
	s = np.zeros(len(X))
	
	while n < len(A):
		space_sol = np.sin(n*PI*X)
		s += (A[n]*np.cos(n*PI*t)+(B[n-1]*np.sin(n*PI*t)/(n*PI))) * space_sol
		n += 1

	return s

def animate(i, An, Bn, X, line):
	Y = wave(An, Bn, X, i/100)
	line.set_data(X, Y)

	return line, 

def main():
	plot = True
	X = np.linspace(0,1,1000)
	f = np.sin(PI*X)
	g = 0
	print("Calculating As")
	A, throwaway = calc_fourier_series(X, f, sine=False)
	print("Calculating Bs")
	throwaway, B = calc_fourier_series(X, g, cosine=False)
	print("Done")
	 
	fourier = wave(A,B,X,0)
	#plt.plot(X, f)
	#plt.plot(X, fourier)
	fig, ax = plt.subplots()
	ax.set_ylim([-1,1])
	line, = ax.plot(X, fourier.reshape(len(X),))
	#ax.plot(X,Y)
	anim = animation.FuncAnimation(fig, animate, fargs=(A, B, X, line), frames=100000, interval=20, blit=True)

	plt.show()
	




if __name__ == '__main__':
	main()
