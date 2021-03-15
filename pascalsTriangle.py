
def adder(ls, modulo=0):
	ans = []
	ans.append(1)
	for i in range(1, len(ls)):
		if modulo != 0:
			ans.append((ls[i-1] + ls[i]) % modulo)
		else:
			ans.append(ls[i-1] + ls[i])
	ans.append(1)

	return ans 

def radder(superls, depth=1, mod=0):
	if depth == 0:
		return superls

	superls.append(adder(superls[-1], modulo=mod))
	return radder(superls, depth=depth-1,mod=mod)


if __name__ == '__main__':
	from pprint import pprint
	ls = [[1]]
	ls = radder(ls,depth=16,mod=3)
	pprint(ls)
