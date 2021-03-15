import numpy as np
import matplotlib.pyplot as plt
import random as r

# Takes 2 * hsteps to complete 
def random_walk_bridge(hsteps=10000, plots=3):
	for z in range(plots):
		ls = [1 for i in range(hsteps)]
		ls.extend([-1 for i in range(hsteps)])
		r.shuffle(ls)
		index = [i for i in range(2*hsteps + 1)]
		s = [sum(ls[:k]) for k in range(2*hsteps + 1)]
		plt.plot(index, s)
	plt.show()

#Generates a random exponential variable with specified rate 
def exponential(rate):
	#Generate a random number 

	#map it to reals with exponential dist. 
	pass 

# does a ssrw at point k 
def simple_symmetric_random_walk(k, steps=100):
	for i in range(steps):
		n = r.random()
		if n <= 0.5:
			k += 1
		else:
			k -= 1

	return k

def plot_dist_ssrw(k, steps=100):
	ls = []
	X = []
	numX = []
	for i in range(steps):
		ls.append(simple_symmetric_random_walk(k))
	for e in ls:
		if not (e in X):
			X.append(e)
			numX.append(ls.count(e))
	plt.bar(X,numX)
	plt.show()

# Runs one simulation of the EHRFEST URN MODEL 
# Yields k after every step to specified number 
# N represents the total number of balls in both urns  
def ehr_urn(N,k,steps=10):
	for i in range(steps):
		yield k
		if r.random() < float(k/N):
			k -= 1
		else:
			k += 1  
	return k

def f():
	ls = ['c', 'c', 'c', 'c', 'c', 'c', 'l', 'l', 'l', 'l', 'l', 'l', 'l']
	sample = r.sample(ls, 5)
	return sample.count('c') > sample.count('l')



if __name__ == '__main__':
	s = 0
	for i in range(1000):
		if f():
			s+= 1

	print(s/1000)



