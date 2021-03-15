#Finds "Derivative" of natural numbers
import matplotlib.pyplot as plt
import numpy as np

def multiply(l1, l2):
	new_list = []
	for i in l1:
		for j in l2:
			new_list.append(i*j)
	return list(set(new_list))

def is_prime(n):
	#dumb prime check
	if n == 2:
		return True
	for i in range(2,int(n/2)):
		if divides(i,n):
			return False
	return True

def divides(i,n):
	return n % i == 0

def deriv(n):
	if n == 1:
		return 0

	if is_prime(n):
		return 1

	for i in range(2,n):
		if divides(i,n): 
			return  int(n/i)*deriv(i)+i*deriv(int(n/i))


if __name__ == '__main__':

	odds = multiply([3,5,7,11,13,17,19,23,29,31,37,41,43],[3,5,7,11,13,17,19,23,29,31,37,41,43])
	odds.sort()
	print(odds)
	new_list = []
	for odd in odds:
		new_list.append(deriv(odd))
	print(new_list)

	plt.plot(odds,new_list)
	plt.plot(odds, np.sqrt(odds))
	plt.show()