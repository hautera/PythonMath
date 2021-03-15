import matplotlib.pyplot as plt

global all_fib_nums
all_fib_nums = []

def f(n):
	if len(all_fib_nums) > n:
		return all_fib_nums[n]
	else:
		if n == 0 or n == 1:
			all_fib_nums.append(1)
			return 1
		fn = f(n-1) + f(n-2)
		all_fib_nums.append(fn)
		return fn

def g(n):
	return 0.75 * n + 0.45833 * n**2 - 0.25 * n**3 + 0.04167 * n**4

if __name__ == '__main__':
	X = [i for i in range(101)]
	Y1 = [f(i) for i in X]
	Y2 = [g(i) for i in X]
	#print("Limit approximation: {}".format(Y2[100]/Y1[100]))
	plt.plot(X, Y1, 'r', X, Y2, 'g')
	plt.show()