import matplotlib.pyplot as plt
import networkx as nx

G=nx.Graph()

G.add_edge (1,2)

nx.draw (G)

plt.savefig("imagenes/Fig01.eps")


