import matplotlib.pyplot as plt
import networkx as nx

H=nx.Graph()

H.add_path([0,1,2,3,4,])
nx.draw (H) 
 
plt.savefig("imagenes/Fig01.eps")




