# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 23:03:42 2019

@author: Dayli
"""
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# image from http://matplotlib.sourceforge.net/users/image_tutorial.html
path = "C:/Users/lapi7/Desktop/Para tarea 2/razas/"
img1=mpimg.imread("1.jpg")
img2=mpimg.imread("2.jpg")
img3=mpimg.imread("3.jpg")
img4=mpimg.imread("4.jpg")

G=nx.Graph()

G.add_nodes_from([1,2,3,4])

G.add_edges_from([(1,1), (1,2), (1,3), (1,4)])# Cada nodo es reflexivo 
G.add_edges_from([(2,2), (2,1), (2,3), (2,4)])#
G.add_edges_from([(3,3), (3,1), (3,2), (3,4)])#
G.add_edges_from([(4,4), (4,1), (4,3), (4,2)])#

G.node[1]["image"]=img1
G.node[2]["image"]=img2
G.node[3]["image"]=img3
G.node[4]["image"]=img4

pos=nx.circular_layout(G, scale=0.5)

fig=plt.figure(figsize=(13,13))
ax=plt.subplot(1,1,1)
ax.set_aspect("equal")
nx.draw_networkx_edges(G,pos,ax=ax,width=2)

plt.xlim(-0.5,1.5)
plt.ylim(-0.5,1.5)

plt.axis("off")

trans=ax.transData.transform
trans2=fig.transFigure.inverted().transform

piesize=0.2 # this is the image size
p2=piesize/2.0
for n in G:
   xx,yy=trans(pos[n]) # figure coordinates
   xa,ya=trans2((xx,yy)) # axes coordinates
   a = plt.axes([xa-p2,ya-p2, piesize, piesize])
   a.set_aspect("equal")
   a.imshow(G.node[n]["image"])
   a.axis("off")

plt.savefig("imagenes1/Fig03.eps", bbox_inches='tight')
#nx.draw(G)
plt.show()