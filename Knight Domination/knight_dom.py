import subprocess
import time

def create_string(N):
	# indexing squares as a standard matrix
	#checks if the coordinates k can be found on the board
	def on_board(k):
		return k[0] < N and k[0] >= 0 and k[1] < N and k[1] >= 0 


	#Predefined moves for every piece
	knight_moves = [(1,2), (1,-2), (2,1), (2,-1), (-1,-2), (-1,2), (-2,-1), (-2,1)] 
	queen_moves = [(1,0), (0,1), (-1,0), (0,-1)]
	#bishop is a subset of queen, so we only write out rook moves for queen
	bishop_moves = [(1,1), (1,-1), (-1,1), (-1,-1)]

	#this is the final string for our LP
	file_str = "min: "

	sum_q1 = ""
	sum_q2 = ""
	sum_b = ""

	for i in range(N):
		for j in range(N):
			file_str += "+k_{}_{}".format(i,j)
			sum_b += "+b_{}_{}".format(i,j)
			sum_q1 += "+q_{}_{}".format(i,j)

	# find midpoint on board 
	m = int(N / 2 if N % 2 == 0 else (N + 1) / 2)
	# restrict queen to top quarter of the board 
	for i in range(m + 1):
		for j in range(m + 1):
			sum_q2 += "+q_{}_{}".format(i,j)

	# this finalizes the minimization line 
	file_str += ";\n"

	# add the required queen and bishop 
	file_str += sum_q1 + "<= 1;\n"
	file_str += sum_b + "<= 1;\n"
	file_str += sum_q2 + ">= 1;\n"
	file_str += sum_b + ">= 1;\n"

	for i in range(N):
		for j in range(N):
			#only one piece can be on the square 
			file_str += "+k_{}_{} +q_{}_{} +b_{}_{} <= 1;\n".format(i,j, i,j, i,j)
			
			#every square must be attacked
			attack_str = ""
			for move in knight_moves:
				#lists all the squares that a knight can move from to this square
				# potential move, we've moved in a direction, but don't know if its on the board 
				pot_move = (i + move[0], j + move[1])
				if on_board(pot_move): 
					attack_str += "+k_{}_{} ".format(pot_move[0], pot_move[1])

			for move in queen_moves:
				#lists all the squares that a rook can move from to this square  
				# we compute the diagonal for the queen moves with the bishop 
				r = 1
				pot_move = (i + move[0], j + move[1])
				#queen can move more than one square at a time 
				while on_board(pot_move):
					attack_str += "+q_{}_{} ".format(pot_move[0], pot_move[1])
					r += 1 
					pot_move = (i + r * move[0], j + r * move[1])

			for move in bishop_moves:
				#lists all the squares that a bishop (and queen) can move from to this square  
				r = 1 
				pot_move = (i + move[0], j + move[1])
				while on_board(pot_move):
					attack_str += "+q_{}_{} +b_{}_{} ".format(pot_move[0], pot_move[1], pot_move[0], pot_move[1])
					r += 1
					pot_move = (i + r * move[0], j + r * move[1])

			file_str += attack_str + ">= 1;\n"
	
	# set all the pieces to be binary variables 
	all_piece_sq = "bin "
	for i in range(N):
		for j in range(N):
			all_piece_sq += "k_{}_{}, q_{}_{}, b_{}_{}".format(i,j, i,j, i,j)
			if i == N - 1 and j == N - 1:
				all_piece_sq += ";\n"
			else:
				all_piece_sq += ", "

	file_str += all_piece_sq
	return file_str

def main():
	t = 0
	N = 4
	while t < 10 * 60:
		input_file_location = "LP/KNIGHTDOM{}LP.txt".format(N)
		output_file_location = "A/KNIGHTDOM{}A.txt".format(N)
		s = create_string(N)

		with open(input_file_location, "w") as f:
			f.write(s)

		t0 = time.time()
		bits = subprocess.check_output(['lp_solve', input_file_location])
		t1 = time.time()
		t = t1 - t0 

		with open(output_file_location, "wb") as f:
			f.write(bits)

		print("Solved knight domination for board size {}\nTime elasped: {}s".format(N, t))
		N += 1
		
if __name__ == '__main__':
	main()



