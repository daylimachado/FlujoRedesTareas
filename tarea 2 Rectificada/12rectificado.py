import matplotlib.pyplot as plt
import networkx as nx

G=nx.MultiDiGraph()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)

G.add_edge(1,2, weight=3)
G.add_edge(1,2, weight=4)
G.add_edge(1,2, weight=5)
G.add_edge(2,3, weight=3)
G.add_edge(2,3, weight=4)
G.add_edge(2,3, weight=4)
G.add_edge(3,4, weight=3)
G.add_edge(3,4, weight=3)
G.add_edge(3,4, weight=3)
G.add_edge(4,5, weight=3)
G.add_edge(4,5, weight=3)
G.add_edge(4,5, weight=3)

y=[(1,2),(2,3),(3,4),(4,5)]
g=[(1,2),(2,3),(3,4),(4,5)]
r=[(1,2),(2,3),(3,4),(4,5)]

pos=nx.shell_layout( G , nlist = None , scale = 1 , center = None , dim = 2 ) 
list=[]
list=G.nodes()
listacolor=['black', 'y', 'b','r','g']

for i in list:
    nx.draw_networkx_nodes(G, pos, node=i, node_size=300, node_color=listacolor, node_shape='o')
nx.draw_networkx_edges(G, pos, edgelist=y, width=8, alpha=1,
edge_color='y', style='dashed')
nx.draw_networkx_edges(G, pos, edgelist=g, width=6, alpha=0.5,
edge_color='g')
nx.draw_networkx_edges(G, pos, edgelist=r, width=2, alpha=0.8,
edge_color='r')
plt.axis('off')
plt.savefig("imagenes1/Fig13.eps")
plt.show()
