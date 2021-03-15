import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import matplotlib as mpl


class MarkovChain():
	"""
	Creates a new markov chain representation
	TODO make that there graph support 
	"""
	def __init__(self, transition_matrix):
		
		self.M = transition_matrix
		self.size = transition_matrix.shape[0]

	"""
	Calculates the state at specified time step and initial state
	"""
	def __call__(self, steps, initial_state):
		assert sum(initial_state) == 1 and len(initial_state) == self.n, "Not a valid state for the chain"
		state = np.zeros(self.n)
		state[initial_state] = 1
		prob_matrix = matrix_power(self.M, steps)
		return np.dot(prob_matrix, state)

	"""
	Calculates the expected return time to state N
	"""
	def return_time(self, N, error=1e-9):
		assert N >= 0 and N < self.size, "Not a valid state\n {} was passed".format(N)
		state_vector = np.zeros(self.size)
		state_vector[N] = 1 
		prob_returned, prob_not_returned = 0, 1 
		step = 1 
		return_time = 0
		delta_rt = 1
		while delta_rt > error:
			#assert sum(state_vector) == 1, "Uh oh theres a bug :(\n State vector: {}".format(state_vector)
			state_vector = np.dot(self.M, state_vector)
			prob_returned = state_vector[N]
	
			# we don't update not returned bc it keeps track not returned for the prev step
			delta_rt = step * prob_returned * prob_not_returned
			return_time += delta_rt
			prob_not_returned = (1 - prob_returned) * prob_not_returned
			
			# now, we rescale the state vector such that the probability we return = 0 
			scalor = 1 / (1 - state_vector[N])
			state_vector[N] = 0
			state_vector = scalor * state_vector

			step += 1 
			if step % 100 == 0:
				print("Calculation on step {}.\nError = {}".format(step, delta_rt))

		return return_time


	"""
	Returns the stationary distribution of the markov chain
	"""
	def stationary_dist(self):
		# We can calculate using two methods 
		# M * x = x => (M - I) * x = 0 | sum(X) = 1
		# or x_i = 1/return_time(x_i)
		#A = self.M - np.identity(self.size)
		X = np.zeros(self.size)
		for n in range(self.size):
			X[n] = 1 / self.return_time(n)

		#assert np.all(np.dot(self.M, X) == X), "Uh oh math doesn't work.\n X = {}\nX = {}\nHence, X != X QED".format(X, np.dot(self.M, X))
		return X


	def time_reversal(self):
		pi = self.stationary_dist()
		time_reversal = np.zeros(self.M.shape)
		for i in range(self.size):
			for j in range(self.size):
				time_reversal[i][j] = (pi[j] * self.M[j][i]) / pi[i]

		return time_reversal

	def time_reversible(self):
		return np.all(self.M == self.time_reversal())



def main():
	trans_matrix = np.array([[0.5, 0.3], [0.5, 0.7]])
	mc = MarkovChain(trans_matrix)
	X = mc.stationary_dist()
	print(X)
	print(mc(1, X))

if __name__ == '__main__':
	main()