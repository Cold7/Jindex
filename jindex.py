import networkx as nx

if __name__ == "__main__":
  reference_name = "ref_chip.gml"
  inferred_name = "full_best_fimo_2000.gml"
  
  G = nx.read_gml(reference_name)
	H = nx.read_gml(inferred_name)

	edges = []
	common = 0

	for edge in G.edges:
		if edge not in edges:
			edges.append(edge)

	for edge in H.edges:
		if edge not in edges:
			edges.append(edge)
		if G.has_edge(edge[0], edge[1]):
			common += 1


	print("Jindex:", common/len(edges), "common:", common)
