#import argparser as arg
DEFAULT_PATH = "bernoulli_numbers.txt"
PATH = DEFAULT_PATH
ERROR = 10E-5

"""
Calculates the kth bernoulli number 
speed up computation by passing ls of previously
calculated values 
"""
def bernoulli(k, ls=[]):
	
	if k < len(ls) and k >= 0:
		return ls[k]

	if k == 0:
		return 1
	else:
		if k > 1 and k % 2 == 1:
			return 0
		
		s = 0
		for i in range( k ):
			s -= (choose(k + 1, i) * bernoulli(i, ls=ls))
		answer = s / (k + 1)
		return 0 if abs(answer) < ERROR else answer 

def choose(n, k):
	return factorial(n) / (factorial(k) * factorial(n - k))		
		

def factorial(n): 
	product =1 
	for i in range(1, n + 1):
		product *= i

	return product


def read(PATH):
	with open(PATH, "r") as f:
		precalc_nums = f.read()

	precalc_nums = precalc_nums.split(",")
	return [float(x) for x in precalc_nums[:-1]]


def write(ls):
	with open(PATH, "w") as f: 			
		for x in ls:
			f.write("%f," % x)

	print("Output saved!")

def calc(k):
	b = read(PATH)
	while len(b) < k:
		b.append( bernoulli(len(b), ls=b) )

	return b


def main():
	print(calc(100))

if __name__ == '__main__':
	main()


