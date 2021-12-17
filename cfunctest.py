import matplotlib.pyplot as plt
import networkx as nx

# **Draws a random graph connecting the nodes of the collatz chain**


starting_num_list=[]
tuple_list=[]
def collatz_tuple(n):
	while n>1:
		bk=n
		if n%2==0:
			n=int(n/2)
			starting_num_list.append(n)
		else:
			n=int(3*n+1)
			starting_num_list.append(n)
		tuple_list.append((bk,n))   #this add the previous collatz number 'bk' for an easy tuple
	return starting_num_list,tuple_list

collatz_tuple(808)   #Pick any number youd like here to see the chain
print("chain length=",len(starting_num_list))

g = nx.Graph()
g.add_nodes_from(starting_num_list)
g.add_edges_from(tuple_list)

nx.draw(g,with_labels=True)
plt.draw()
plt.show()


