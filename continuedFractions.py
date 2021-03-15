import matplotlib.pyplot as plt
import math

iterations = 10
# calculates a continued fraction of specified depth
# a(0) + f(1)/[a(1) + f(2)/...]
# a and f must be generators 
def continuedFaction(f, a, depth=10):

	if depth == 0:
		return next(f)/next(a)
	else:
		return next(a) + next(f)/(continuedFaction(f, a, depth=depth-1))


def one():
	while True:
		yield 1

def two():
	while True:
		yield 2

def odds_squared(one=1):
	num = 1
	while True:
		yield num ** 2
		num += 2

def two_ones_then_nats():
	num = 1
	yield num
	while True:
		yield num 
		num += 1

def one_then_twos():
	yield 1
	while True:
		yield 2

def two_then_nats():
	yield 2
	n = 1 
	while True:
		yield n 
		n = n + 1

def three_then_six():
	yield 3 
	while True:
		yield 6

if __name__ == '__main__':
	X = [i for i in range(iterations)]
	phi = [continuedFaction(one(), one(), depth=i) for i in X]
	root_two = [continuedFaction(one(), one_then_twos(), depth=i) for i in X]
	pi = [continuedFaction(odds_squared(), three_then_six(), depth=i) for i in X]
	e = [continuedFaction(two_ones_then_nats(), two_then_nats(), depth=i) for i in X]

	print(" X | e | phi | pi | root_two \n--------------------------------")
	for i in range(iterations):
		print(" {} | {} | {} | {} | {} ".format(i, e[i],phi[i],pi[i],root_two[i]))

	plt.plot(X, phi, 'g', X, pi, 'b', X, e, 'm', X, root_two, 'r' )
	plt.gca().legend(('phi', 'pi', 'e', 'root two'))
	plt.show()
