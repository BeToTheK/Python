# import matplotlib.pyplot as plt
# import networkx as nx


# g = nx.DiGraph()
# g.add_nodes_from([40, 20, 10, 5, 16, 8, 4, 2, 1])
# g.add_edge(40,20)
# g.add_edge(20,10)
# g.add_edge(10,5)
# g.add_edge(5,16)
# g.add_edge(16,8)
# g.add_edge(8,4)
# g.add_edge(4,2)
# g.add_edge(2,1)

# #nx.nx_pydot.write_dot(g,'DiGraph.dot')
# nx.draw(g,with_labels=True)
# plt.draw()
# plt.show()

# import networkx as nx
# import matplotlib.pyplot as plt

# g = nx.DiGraph()
# g.add_nodes_from([1,2,3,4,5])
# g.add_edge(1,3)
# g.add_edge(2,3)
# g.add_edge(3,5)
# g.add_edge(3,4)

# nx.draw(g,with_labels=True)
# #plt.draw()
# plt.show()



# G = nx.Graph()  # or DiGraph, MultiGraph, MultiDiGraph, etc
# G = nx.Graph(name="my graph")
# e = [(1, 2), (2, 3), (3, 4)]  # list of edges
# G = nx.Graph(e)
# plt.draw()
# plt.show()