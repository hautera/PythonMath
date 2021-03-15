import itertools

class Polynomial():

	# Creates a polynomial object with the provided list of numbers
	# The index of each number will be used as the degree of each coeffiecient
	def __init__( self, ls ):
		self.coefs = []
		for coef in ls:
			self.coefs.append( coef )

	# Adds the two polynomials within the definition of
	# normal mathematical addition
	# Returns a new polymial
	def __add__( self, other ):
		ls = []
		for i, j in zip_longest( self.coefs, other.coefs, fillvalue=0):
            ls.append( i + j )

		return Polynomial( ls )

	# Returns the polynomial's value at x
	def __call__( self, x ):
		answer = 0
		for degree, coef in enumerate( self.coefs ):
			answer += coef * ( x ** degree )

		return answer

def main():
    print("Hello  world")

if __name__ == '__main__':
    main()
