# Plots a pandas csv 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize 

def choose(n, k):
	return factorial(n) / (factorial(k) * factorial(n - k))		
		

def factorial(n): 
	product =1 
	for i in range(1, n + 1):
		product *= i

	return product

def logistic(x, A, B, x0):
	return A / (1 + np.exp(-B * (x - x0)))

if __name__ == '__main__':
	e = 1 
	for j in range(1,10):
		
		file_path = "Pandemic21{}.csv".format(j)
		data = pd.read_csv(file_path)
		#data.plot.scatter(x='Step', y='Infected')
		#plt.show() 
		ave_steps = 0
		num_rec = 0
		for r, i, step in zip(data['Recovered'], data['Infected'], data['Step']):
			if i == 0:
				ave_steps += step
				num_rec += r


		print("E-{} R-{} Steps-{} Ave_Rec-{}".format(0.01*e, 0.1*j, ave_steps/1000, num_rec/1000))


	"""
	plt.scatter(data["Step"], data['Recovered'])
	STEPS = list(range(max(data['Step'])))
	params, _ = optimize.curve_fit(logistic, data['Step'], data['Recovered'])
	plt.plot(STEPS, logistic(STEPS, params[0], params[1], params[2]))
	plt.show()
	"""
	