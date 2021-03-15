#dice_game.py

import random as r
import numpy as np
import fractions
import matplotlib.pyplot as plt
import math 

def simulation(score_limit, num_sides):
	score = list()
	die = [i for i in range(1, num_sides + 1)]
	score.append(r.choice(die))
	while score[-1] < score_limit:
		result = r.choice(die)
		next_score = int(score[-1] / result) if score[-1] % result == 0 else score[-1] + result 
		score.append(next_score)
	
	return score

def trasition_matrix(score_limit, num_sides):
	M = np.zeros((score_limit + 1, score_limit + 1))
	for score in range(score_limit):
		for result in range(1, num_sides + 1):
			if score == 0:
				next_score = result 
			else:
				next_score = int(score / result) if score % result == 0 else score + result 
			
			if next_score >= score_limit:
				M[score][-1] += 1
			else:
				M[score][next_score] = 1
	M[-1][-1] = num_sides
	return M 

def calculate_hitting_time(A, P, initial_state, num_sides=6):
	assert type(A) == list, "A is not a list of states"
	if initial_state in A:
		return 0

	N = len(P[0])
	assert initial_state < N, "Initial state not valid"
	inital_ind = None

	Q_ind = list()
	for i in range(N):
		if not i in A:
			if i == initial_state:
				inital_ind = len(Q_ind)
			Q_ind.append(i)
	assert inital_ind != None, "Theres a bug in the code"
	
	assert len(Q_ind) == N - len(A), "Theres a bug in the code"
	Q_size = len(Q_ind)
	Q = np.zeros((Q_size,Q_size))
	I = num_sides * np.identity(Q_size)

	for i, k in enumerate(Q_ind):
		for j, l in enumerate(Q_ind):
			Q[i][j] = M[k][l]
	
	hitting_matrix = np.linalg.inv(I - Q)
	hitting_times = np.sum(hitting_matrix, axis=1)

	return [fractions.Fraction.from_float(num_sides * x).limit_denominator(10) for x in hitting_times]


if __name__ == '__main__':
	X = list()
	Y1 = list()
	Y2 = list()
	num_sides = 6
	for score_limit in range(10, 100, 10):
		
		M = trasition_matrix(score_limit, num_sides)
		hitting_fract = calculate_hitting_time([score_limit], M, 0)[0]
		h = float(hitting_fract)
		
		ave_rolls = 0
		count = 0
		for _ in range(50000):
			rolls = len(simulation(score_limit, num_sides))
			ave_rolls += rolls
			if rolls > 10: 
				count += 1

		X.append(score_limit)
		ave_rolls /= 50000
		Y1.append(ave_rolls)
		Y2.append(h)
		print("M = {}; Average rolls over 50,000 simulations = {}; Expected = {}; P(rolls > 10) = {}; Error = {}".format(score_limit, ave_rolls, hitting_fract, ave_rolls - h))

	plt.plot(X,Y1, label="Average number of rolls")
	plt.plot(X,Y2, label="Expected number of rolls")
	plt.xlabel("Maximum score")
	plt.ylabel("Average rolls")
	plt.show()



