
def isPrime(N):
	something = 2
	while something <= N/2:
		if N % something == 0: 
			return False  
		something = something + 1 

	return True 

N = 2
while True:
	if isPrime(N):
		print(N)
	N = N + 1 

