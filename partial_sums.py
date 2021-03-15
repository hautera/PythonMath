import math 

#calculates the nth partial sum of a series for austin

def sequence():
	n = 1
	while True: 
		yield 1/((n)*(math.log(n+1))) 
		n = n + 1 

s = 1
partial_sums = [0]
for i in sequence():
	partial_sums.append(partial_sums[-1]+i)
	s += 1 
	if s > 100000:
		break
print(partial_sums[-1])