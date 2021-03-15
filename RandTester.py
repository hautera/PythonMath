#Tests random events 

import random


# Returns true iff k divides x
# in other words returns true iff there 
# exists a n suck that n*k = x
def divides(k, X):
	return X % k == 0

count = 0
TESTS = 1000000000
for i in range(TESTS):
	X = int(random.random()*1000) + 1

	if divides(2, X) or divides(3, X) or divides(5, X):
		count += 1

print(count/TESTS)