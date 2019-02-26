import matplotlib.pyplot as plt
import networkx as nx

G  =  nx . DiGraph ()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)

nod1={1}
nod2={2}
nod3={3}
nod4={4}
nod5={5}

G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,4)
G.add_edge(4,5)

positions = { 5:(0, 10), 4:(0, 20), 3:(0,30), 2:(0,40), 1:(0,50)}
#fixeds={1,2}
pos = nx.spring_layout(G, k=3, fixed=None, pos=positions, center=(0,0), iterations=50)

nx.draw_networkx_nodes(G, pos, nodelist=nod1, node_size=400, node_color='#580cf0', node_shape='o')
nx.draw_networkx_nodes(G, pos,nodelist=nod2, node_size=400, node_color='#6332c5', node_shape='o')
nx.draw_networkx_nodes(G, pos,nodelist=nod3, node_size=400, node_color='#6240a7', node_shape='o')
nx.draw_networkx_nodes(G, pos,nodelist=nod4, node_size=400, node_color='#574184', node_shape='o')
nx.draw_networkx_nodes(G, pos,nodelist=nod5, node_size=400, node_color='#433958', node_shape='o')


nx.draw_networkx_edges(G, pos, width=2, alpha=0.8, edge_color='black')
plt.axis('on')
#plt.axis('off')
plt.savefig("imagenes1/Fig04.eps")
plt.show()

#plt.show()