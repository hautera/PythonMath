
from graph import Graph, graph_from_file
from LP_Solver import run_lp

"""returns linear program representing graph color problem""" 
def coloring(g: Graph, max_colors=2):
	assert max_colors >= 2, "Cannot color a graph with 1 color"
	colors = [i for i in range(max_colors)]
	vertices = g.get_vertices()
 	
	every_color_count = "min:"
	every_color_bin = ""
	for color in colors:
		every_color_bin += " c_{},".format(color)
		every_color_count += " +c_{}".format(color)
	every_color_count +=";\n"


	every_vertex_color = ""
	color_used = ""
	every_vertex_colored = ""

	neighbor_conditions = ""


	for index, vertex in enumerate(vertices):
		neighbors = [edge.get_connected_vertex(vertex) for edge in g.get_edges(vertex)]
		print(str(vertex) + "->" + str(neighbors))
		for color in colors:

			every_vertex_color += " v_{}_{},".format(vertex, color)
			every_vertex_colored += "+v_{}_{}".format(vertex, color)
			color_used += "+c_{}-v_{}_{} >= 0;\n".format(color, vertex, color)

			for neighbor in neighbors:
				n_index = vertices.index(neighbor)
				temp = "+v_{}_{} +v_{}_{} <= 1;\n".format(vertex, color, neighbor, color)
				neighbor_conditions += temp
		every_vertex_colored += "= 1;\n"

	result = every_color_count + color_used + every_vertex_colored + neighbor_conditions
	binary_var = "bin " + every_color_bin + every_vertex_color[:-1] + ";\n"
	result += binary_var
	return result


if __name__ == '__main__':
	g = graph_from_file("Diplomacy.g")
	run_lp(coloring(g, max_colors=4), "diplo_color_input.txt", "diplo_color_output.txt")
		
