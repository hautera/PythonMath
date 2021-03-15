import numpy as np
import matplotlib.pyplot as plt
import argparse as arg

PI = 3.141
#integrates a series of y values assuming evenly spaced y's
def integrate(a, b, y):
	n = len(y)
	s = np.sum(y) - (y[0]/2 + y[-1]/2) # simpons rule
	return ( b - a ) * s / n


def calc(x,y,num=5):
	a0 = integrate(-1,1,y)
	A = [a0]
	B = []
	n = 1
	PI = 3.14159
	while len(A) < num:
		an = integrate(-1,1, np.multiply(np.cos(n*PI*x),y))
		bn = integrate(-1,1, np.multiply(np.sin(n*PI*x),y))
		#plt.plot(np.cos(n*PI*x))
		A.append(an)
		B.append(bn)
		n += 1

	return A, B


if __name__ == '__main__':
	parser = arg.ArgumentParser(description="Calculates the Fourier series of a function")
	n = 10

	y = np.linspace(-1, 1, num=1000) 
	x = np.linspace(-1, 1, num=1000)
	A, B = calc(x,y,num=n) 
	
	fourier = np.zeros(len(x))
	for i in range(n):
		
		if i > 0:
			fourier = np.add(fourier, B[i-1] * np.sin(PI*i*x))
			fourier = np.add(fourier, A[i] * np.cos(PI*i*x))
		else:
			fourier = np.add(fourier, np.ones(len(x))*A[0]/2)
				
	try:
		plt.plot(x,y,x,fourier)
		plt.show()

	except KeyboardInterrupt as e:
		print("Quitting the program now")
		quit()

