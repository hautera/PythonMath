import numpy as np
import random 
import matplotlib.pyplot as plt


def number_of_non_draws(n,k,j):
	N = list(range(n))
	drawn = set()
	for i in range(j):
		draw = random.sample(N,k)
		for e in draw:
			drawn.add(e)
	return n - len(drawn)

def Enumber_of_non_draws(n,k,j):
	return (1-(k/n))**j * (n-k)

def Efriends(n,k,j):
	return (k**2) * j / n

def ave_friends(n,k,j):
	if j > 0:
		pop = [int(i) for i in range(N)]
		friends_count = dict()
		for _ in range(j):
			group = random.sample(pop, k)
			for e in group: 
				if e in friends_count.keys():
					fc = friends_count.pop(e) + k - 1 
				else:
					fc = k - 1 
				friends_count.update({e: fc})
		f = friends_count.values()
		ave = sum(f)/len(f)
		return ave
	else:

		return 0


def friends_matrix(n,k,j):
	assert j > 0 and k > 0 and n > k, "Constraints: j > 0 and k > 0 and n > k not met!"
	pop = [int(i) for i in range(n)]
	M = np.zeros((n,n))
	friends_count = dict()
	for _ in range(j):
		group = random.sample(pop, k)
		for i, e in enumerate(group): 
			subgroup = group[:i] + group[i+1:]
			if e in friends_count.keys():
				friend_set = friends_count.pop(e)
				friend_set.update(subgroup)
			else:
				friend_set = set(subgroup)
			friends_count.update({e:friend_set})


	for i in range(n):
		friends = friends_count.get(i)
		if friends is not None:
			weight = 1
			for j in friends:
				M[i][j] = weight

	return M


if __name__ == '__main__':
	M1 = friends_matrix(100, 2, 100) 
	M2 = friends_matrix(100, 3, 100)
	print(M1)
	v = np.zeros(100)
	v[0] = 1 
	v1, v2 = v, v

	X = list(range(100))
	infected1 = list()
	infected2 = list()
	for i in X:
		num_inf1, num_inf2 = 0,0
		for i1,i2 in zip(v1,v2):
			num_inf1 += 1 if i1 >= 1 else 0
			num_inf2 += 1 if i2 >= 1 else 0
		infected1.append(num_inf1)
		infected2.append(num_inf2)

		v1 = np.dot(v1, M1)
		v2 = np.dot(v2, M2)

	plt.plot(X, infected1, X, infected2)
	plt.show()



def show_expected_friends(N, K, TRIALS):
	X = list(range(TRIALS)) 
	Y1 = list()
	Y2 = list()
	for x in X:
		af = 0
		for _ in range(N):
			af += ave_friends(N,K,x)
		af /= N 
		
		Y1.append(af)
		Y2.append(Efriends(N,K,x))

	plt.plot(X,Y1, X,Y2)
	plt.show()

