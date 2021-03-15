
from graph import Graph, graph_from_file
from LP_Solver import run_lp


def stalemate_lines(g: Graph, starting_set):
	V = g.get_vertices()
	for s in starting_set:
		assert s in V, "Starting set is not valid {}".format(s)
	
	M = len(starting_set)
	N = len(V)

	list_of_binary_variables = "bin "
	one_defender_condition = ""
	attacker_indicator = ""
	stalemate_contains_starting_set = ""
	stalemate_condition = ""
	objective_function = "min:"

	for index, vertex in enumerate(V):
		neighbors = [edge.get_connected_vertex(vertex) for edge in g.get_edges(vertex)]
		objective_function += "+s_{}".format(vertex) 
		list_of_binary_variables += " s_{},".format(vertex)
		attacker_indicator += "a_{} + s_{} = 1;\n".format(vertex, vertex)
		if vertex in starting_set:
			stalemate_contains_starting_set += "+s_{}".format(vertex)

 		# avoids making attacking regions also defend  
		stalemate_condition += "+{}*a_{}".format(N, vertex)
		
		for n in neighbors:
			one_defender_condition += "+d_{}_{}".format(vertex, n)
			list_of_binary_variables += " d_{}_{},".format(vertex, n)
			stalemate_condition += "+d_{}_{} - a_{}".format(n, vertex, n)
			
		one_defender_condition += "+d_{}_{}-s_{}=0;\n".format(vertex, vertex, vertex)
		stalemate_condition += ">= 0;\n"
	objective_function += ";\n"
	stalemate_contains_starting_set += "= {};\n".format(M)

	return objective_function + attacker_indicator + one_defender_condition + stalemate_contains_starting_set + stalemate_condition + list_of_binary_variables[:-1]+";"

if __name__ == '__main__':
	g = graph_from_file("Diplomacy.g")
	s = stalemate_lines(g, {"Moscow", "Sevastopol"})
	with open("test_output.txt", "w") as f:
		f.write(s)


	
