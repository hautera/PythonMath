#Pandemic simulation 

import random 
import math
import matplotlib.pyplot as plt
import pandas as pd 


# distance of P1, P2
def d(P1, P2):
	s = 0
	for x, y in P1, P2:
		s += (x - y) ** 2
	d = math.sqrt(s)
	return d


#Two points are in a neighborhood if 
# d(P1, P2) < espilon
def neighborhood(P1, P2, eps):
	return d(P1, P2) < eps

def random_walk_reflection(P0, M=1, n=0, STEP=0.01):
	assert 2*STEP < M - n, "uh oh boundries too close"
	P1 = list()
	for x0 in P0:
		x1 = x0 + STEP * (random.random() - 0.5)
		if x1 > M:
			x1 = 2*M - x1 
		elif x1 < n:
			x1 = 2*n - x1
		P1.append(x1)
	return P1 

#We will have a population of individuals
class Individual():
	
	def __init__(self, P):
		"""
		The individual will have three possible states 
		S, I, and R, and can only be in one state 
		"""
		self.S = True 
		self.I = False
		self.R = False  

		"""
		The individual will also occupy a point in [0,1] x [0,1]
		"""
		self.x = random.random()
		self.y = random.random()

		"""
		And they will keep track of encounters with other individuals 
		"""
		self.encounters = 0
		self.recovery_counter = 0

		"""
		The individual will have a chance of infection per encounter
		"""
		self.chance_infected_per_encounter = P

	"""
	This will simulate the passage of time of the individual 
	"""
	def tick(self, delta=0.1):
		# the individual will wander around 
		self.x, self.y = random_walk_reflection((self.x, self.y), STEP=delta)

		# the individual will have a chance of being infected 
		p = random.random() 
		chance_infected = 1 - (1-self.chance_infected_per_encounter)**self.encounters
		if self.S and p < chance_infected:
			self.S = False 
			self.I = True 
		# the individual will recover from illness if given enough time 
		elif self.I and p > 0.33:
			self.recovery_counter += 1 
			if self.recovery_counter > 2:
				self.I = False
				self.R = True
	  
		# reset the number of encounters for next time
		self.encounters = 0
		

	def infected(self):
		return self.I

	def susceptible(self):
		return self.S

	def recovered(self):
		return self.R

	def position(self):
		return self.x, self.y 

	def add_encounter(self):
		self.encounters += 1 

	def __eq__(self, other):
		return self.S == other.S and self.I == other.I and self.x == other.x and self.y == other.y

	def __str__(self):
		return "X: {} Y: {} Susceptible: {} Infected: {}".format(self.x, self.y, self.S, self.I)

	def neighborhood(self, other, epsilon=0.1):
		return neighborhood((self.x, self.y), (other.x, other.y), epsilon)

	def num_encounters(self):
		return self.encounters

def random_pop(N, P):
	population = [Individual(P) for _ in range(N)]
	population[0].I = True
	population[0].S = False
	return population



if __name__ == '__main__':
	for v in range(1,10):
		for __ in range(1,10):
			for ___ in range(1,10):
				DELTA = 0.01 * v
				EPSILON = 0.01 * __ 
				P = 0.1 * ___
				PATH = "Simulations/Pandemic{}{}{}.csv".format(v, __, ___)



				data = pd.DataFrame(columns=["Step","Susceptible","Infected", "Recovered", "Encounters"])

				for j in range(1000):
					print("++++++++++++NEW PANDEMIC++++++++++++\nTRIAL : {}\nEPSILON : {} \nDELTA : {}\nP : {}\n++++++++++++++++++++++++++++++++++++".format(j, EPSILON, DELTA, P))
					N = 1000
					step = 0

					population = random_pop(N, P)
					STEPS = list() 
					S = list()
					I = list()
					R = list() 
					E = list()

					num_infected = 1

					# the simulation ends when no one is infected or everyone is infected 
					while num_infected < N and num_infected > 0: 
						num_infected = 0
						num_sus = 0
						num_recovered = 0
						encounters = 0
						for i, p in enumerate(population):
							#print("{} : {}".format(i, p))
							if p.susceptible():
								num_sus += 1
								other_population = population[:i] + population[i:]
								for other in other_population:
									if other.infected() and p.neighborhood(other, epsilon=EPSILON):
										p.add_encounter()
										encounters += 1 
							elif p.infected():
								num_infected += 1 
							elif p.recovered():
								num_recovered += 1 

						for p in population:
							p.tick()
							
						assert num_infected + num_sus + num_recovered == N, "There seems to be an error"
						step += 1
						#print("{}; {}; {}; {}".format(step, num_sus, num_infected, num_recovered, encounters))
						STEPS.append(step) 
						S.append(num_sus)
						I.append(num_infected)
						R.append(num_recovered) 
						E.append(encounters)
					#print(STEPS)
					data = data.append(pd.DataFrame(data={"Step" : STEPS, "Susceptible" : S,"Infected" : I , "Recovered" : R , "Encounters" : E}))

			
			
				data.to_csv(PATH)	
	#plt.scatter(x=data['Step'], y=data['Encounters'])
	#plt.scatter(x=data['Step'], y=data['Infected'], label="Infected")
	#plt.scatter(x=data['Step'], y=data['Susceptible'], label="Susceptible")
	#plt.scatter(x=data['Step'], y=data['Recovered'], label="Recovered")
	#plt.show()
	








	






