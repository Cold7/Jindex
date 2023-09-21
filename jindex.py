import sys
import networkx as nx

if __name__ == "__main__":
	reference_name = sys.argv[1]
	inferred_name = sys.argv[2]
	G = nx.read_gml(reference_name)
	H = nx.read_gml(inferred_name)
	jindex = None
	try:
		jindex = str(len(nx.intersection(G,H).edges)/len(nx.compose(G,H).edges))
	except:
		jindex = "0"
	
	with open(reference_name.replace(".gml","")+"_"+inferred_name.replace(".gml",".jindex"),"w")>
		f.write("Reference: "+reference_name+"\n")
		f.write("Inferred: "+inferred_name+"\n")
		f.write("Jindex: "+jindex+"\n")
