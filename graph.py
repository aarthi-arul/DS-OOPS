from collections import defaultdict
graph = defaultdict(list)

def addEdge(graph,u,v):
	graph[u].append(v)

# definition of function
def generate_edges(graph):
	edges = []

	# for each node in graph
	for node in graph:
		
		# for each neighbour node of a single node
		for neighbour in graph[node]:
			
			# if edge exists then append
			edges.append((node, neighbour))
	return edges

# declaration of graph as dictionary
addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'c','d')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'d','c')

print(generate_edges(graph))
