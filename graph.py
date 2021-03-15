
import numpy as np

class Edge:
	def __init__(self, v1, v2):
		self.v1, self.v2 = v1, v2

	#TODO write this as a dunder method 
	def contains(self, vertex):
		return vertex == self.v1 or vertex == self.v2 

	#Returns true iff vertices are in the same order 
	#EVEN IF graph is undirected :)
	def __eq__(self, other):
		# the vertices are in the same order 
		result = self.v1 == other.v1 and self.v2 == other.v2
		return result 

	"""Returns the vertex on the other end of the edge"""
	def get_connected_vertex(self, vertex):
		if self.v1 == vertex:
			return self.v2
		elif self.v2 == vertex:
			return self.v1
		else:
			return None

	def __hash__(self):
		return hash((self.v1, self.v2))

	def __str__(self):
		return "{} {}".format(self.v1, self.v2)

	def reversed(self):
		return Edge(self.v2, self.v1)

	def weighted(self):
		return False



class WeightedEdge(Edge):
	def __init__(self, v1, v2, w):
		self.weight = w
		super().__init__(v1, v2)

	def __str__(self):
		return super().__str__() + ": {}".format(self.weight)

	def __hash__(self):
		return hash((self.v1, self.v2))

	def weight(self):
		return self.weight

	def weighted(self):
		return True




class Graph:
	def __init__(self):
		self.vertices = set()
		self.edges = set()
		self.directed = False
		self.size = 0
		self.num_edges = 0

	"""Adds a vertex to the graph"""
	def add_vertex(self, vertex):
		self.vertices.add(vertex)
		self.size += 1
		#probably fails when we do lists

	"""returns a list of all vertices"""
	def get_vertices(self):
		return list(self.vertices)

	"""Returns true if graph contains a vertex"""
	def contains_vertex(self, vertex):
		return vertex in self.vertices

	"""Returns true if graph contains a edge"""
	def contains_edge(self, edge):
		if self.directed:
			return edge in self.edges
		else:
			return edge in self.edges or edge.reversed() in self.edges 



	"""Returns the edges connected to the specified vertex"""
	def get_edges(self, vertex):
		result = list()
		for edge in self.edges:
			if edge.contains(vertex):
				result.append(edge)
		return result 

	def __str__(self):
		s = "V = " + str(self.vertices) + "\n\n"
		for edge in self.edges:
			s = s + str(edge) + "\n"
		return s

	"""Adds an edge to the graph"""
	def add_edge(self, v1, v2, w=None):
		#Make sure the vertices are in the graph 
		if v1 in self.vertices and v2 in self.vertices:
			edge = Edge(v1, v2) if w == None else WeightedEdge(v1, v2, w)
			#Dont want duplicate edges 
			if not self.contains_edge(edge):
				self.edges.add(edge)
				self.num_edges += 1
				return True 
		return False

	def weighted(self):
		if self.num_edges > 0:
			weighted = True	
			for edge in self.edges:
				weighted = weighted and edge.weighted()
		
			return weighted 
		
		return False 

	def get_adj_matrix(self):
		N = self.size
		V = self.get_vertices()
		A = np.zeros((N,N))
		for i in range(N):
			for edge in self.get_edges(V[i]):
				j = V.index(edge.get_connected_vertex(V[i]))
				w = edge.weight
				A[i][j] = w 

		return A
						

#Creates a graph object from the specified file path
def graph_from_file(file_path):
	g = Graph()
	with open(file_path, 'r') as f:
		for line in f.readlines():
			temp = line.split(": ")
			vertex = temp[0]
			connections = temp[1].split(", ")
			g.add_vertex(vertex)
			for connection in connections:
				if connection.endswith('\n'):
					connection = connection[:-1]
				g.add_vertex(connection)
				g.add_edge(vertex, connection)
	
	return g


		
if __name__ == '__main__':
	g = Graph()
	g.add_vertex("v1")
	g.add_vertex("v2")
	g.add_vertex("v3")
	g.add_vertex("v4")
	g.add_edge("v1", "v2", w=42)
	print(g.get_adj_matrix())






