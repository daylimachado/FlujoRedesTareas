import random as rnd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as nup
import datetime as dt
import pandas as pd

 
def Generar(nombre, num_archivos, cant_nodos_min, probabilidad):
    G = nx.Graph() 
    for r in range(num_archivos):  
        print("Archivo", r)
        for i in range(cant_nodos_min):
           G.add_node(i)
           for j in range(i + 1, cant_nodos_min):
               crear_vertice = rnd.randint(0, 100) < probabilidad
               print(i, j, crear_vertice)
               if crear_vertice:                
                   G.add_edge(i,j, distancia=rnd.randint(10,15)) 
           df = nx.to_pandas_adjacency(G, dtype=int, weight='distancia')
           df.to_csv(nombre+str(r)+".csv", index = None,header=None )
    return 0   
 
#Generar("grafo", 5, 200, 25) 
    
def Clicgenerar(nombre, num_archivos, cant_nodos_min, probabilidad):
    G = nx.Graph() 
    for r in range(num_archivos):  
        print("Archivo", r)
        for i in range(cant_nodos_min):
           G.add_node(i)
           for j in range(i + 1, cant_nodos_min):
               crear_vertice = rnd.randint(0, 100) < probabilidad
               print(i, j, crear_vertice)
               if crear_vertice:                
                   G.add_edge(i,j, distancia=rnd.randint(10,15)) 
           df = nx.to_pandas_adjacency(G, dtype=int, weight='distancia')
           df.to_csv(nombre+str(r)+".csv", index = None,header=None )
    return 0   
 
#Clicgenerar("clicgrafo", 5, 40, 10)   
        
def Digenerar(nombre, num_archivos, cant_nodos_min, probabilidad):
    G = nx.DiGraph() 
    for r in range(num_archivos):  
        print("Archivo", r)
        for i in range(cant_nodos_min):
           G.add_node(i)
           for j in range(i + 1, cant_nodos_min):
               crear_vertice = rnd.randint(0, 100) < probabilidad
               print(i, j, crear_vertice)
               if crear_vertice:                
                   G.add_edge(i,j, distancia=rnd.randint(10,15)) 
           df = nx.to_pandas_adjacency(G, dtype=int, weight='distancia')
           df.to_csv(nombre+str(r)+".csv", index = None,header=None )
    return 0
     
#Digenerar("digrafo", 5, 400, 25)

def betweenness_centrality(name):
    dr = pd.read_csv(name,header=None)
    F = nx.from_pandas_adjacency(dr, create_using= nx.Graph())
    tiempo=[]
    for i in range(30):
        tiempo_inicial = dt.datetime.now()   
        d= nx.betweenness_centrality(F) #  aca estoy guardando el resultado del algoritmo y como no lo uso paranada me da           
        tiempo_final = dt.datetime.now()   
        tiempo_ejecucion = (tiempo_final - tiempo_inicial).total_seconds()
        tiempo.append(tiempo_ejecucion)
    
    media=nup.mean(tiempo)
    desv=nup.std(tiempo)
    mediana=nup.median(tiempo) 
    salvar=[]
    salvar.append(media)
    salvar.append(desv)
    salvar.append(mediana)
    df = pd.DataFrame(salvar)
    df.to_csv("bet_"+name, index = None,header=None )
    print("terminado betweeness")

def max_clique(name):
    dr = pd.read_csv(name,header=None)
    F = nx.from_pandas_adjacency(dr, create_using= nx.Graph())
    tiempo=[]
    for i in range(30):
        tiempo_inicial = dt.datetime.now()   
        d= nx.make_max_clique_graph(F,create_using=None) #  aca estoy guardando el resultado del algoritmo y como no lo uso paranada me da           
        tiempo_final = dt.datetime.now()   
        tiempo_ejecucion = (tiempo_final - tiempo_inicial).total_seconds()
        tiempo.append(tiempo_ejecucion)
    
    media=nup.mean(tiempo)
    desv=nup.std(tiempo)
    mediana=nup.median(tiempo) 
    salvar=[]
    salvar.append(media)
    salvar.append(desv)
    salvar.append(mediana)
    df = pd.DataFrame(salvar)
    df.to_csv("clique_"+name, index = None,header=None ) 
    print("terminado maxclique")

    
def greedy_color(name):
    dr = pd.read_csv(name,header=None)
    F = nx.from_pandas_adjacency(dr, create_using= nx.Graph())
    tiempo=[]
    for i in range(300):
        tiempo_inicial = dt.datetime.now()   
        d= nx.greedy_color(F) 
        tiempo_final = dt.datetime.now()   
        tiempo_ejecucion = (tiempo_final - tiempo_inicial).total_seconds()
        tiempo.append(tiempo_ejecucion)
    
    media=nup.mean(tiempo)
    desv=nup.std(tiempo)
    mediana=nup.median(tiempo) 
    salvar=[]
    salvar.append(media)
    salvar.append(desv)
    salvar.append(mediana)
    df = pd.DataFrame(salvar)
    df.to_csv("greed_"+name, index = None,header=None ) 
print("Terminado greedy")
    
def maximum_flow (name):
    dr = pd.read_csv(name,header=None)
    F = nx.from_pandas_adjacency(dr, create_using= nx.DiGraph())
    tiempo=[]
    for i in range(30):
        tiempo_inicial = dt.datetime.now()   
        d= nx.maximum_flow (F, 4, 2) #  aca estoy guardando el resultado del algoritmo y como no lo uso paranada me da           
        tiempo_final = dt.datetime.now()   
        tiempo_ejecucion = (tiempo_final - tiempo_inicial).total_seconds()
        tiempo.append(tiempo_ejecucion)
    
    media=nup.mean(tiempo)
    desv=nup.std(tiempo)
    mediana=nup.median(tiempo) 
    salvar=[]
    salvar.append(media)
    salvar.append(desv)
    salvar.append(mediana)
    df = pd.DataFrame(salvar)
    df.to_csv("maxflow_"+name, index = None,header=None ) 
print ("terminado maximun flow")

def minimum_spanning_tree(name):
    dr = pd.read_csv(name,header=None)
    F = nx.from_pandas_adjacency(dr, create_using= nx.Graph())
    tiempo=[]
    for i in range(30):
        tiempo_inicial = dt.datetime.now()   
        d= nx.minimum_spanning_tree(F) #  aca estoy guardando el resultado del algoritmo y como no lo uso paranada me da           
        tiempo_final = dt.datetime.now()   
        tiempo_ejecucion = (tiempo_final - tiempo_inicial).total_seconds()
        tiempo.append(tiempo_ejecucion)
    
    media=nup.mean(tiempo)
    desv=nup.std(tiempo)
    mediana=nup.median(tiempo) 
    salvar=[]
    salvar.append(media)
    salvar.append(desv)
    salvar.append(mediana)
    df = pd.DataFrame(salvar)
    df.to_csv("spanning_tree_"+name, index = None,header=None ) 
print ("terminado spanning_tree ")

def GrafosElementos(cant):
    grafos={
             "clicgrafoN":[],
             "digrafoN":[],
             "grafoN":[],
             "clicgrafoE":[],
             "digrafoE":[],
             "grafoE":[],
           }
    for i in range(cant):
        dr = pd.read_csv("clicgrafo"+str(i)+".csv",header=None)  
        F = nx.from_pandas_adjacency(dr, create_using= nx.Graph())
        grafos[ "clicgrafoN"].append(F.number_of_nodes())
        
        dr = pd.read_csv("digrafo"+str(i)+".csv",header=None)  
        F = nx.from_pandas_adjacency(dr, create_using= nx.Graph())
        grafos[ "digrafoN"].append(F.number_of_nodes())
    
        dr = pd.read_csv("grafo"+str(i)+".csv",header=None)  
        F = nx.from_pandas_adjacency(dr, create_using= nx.Graph())
        grafos[ "grafoN"].append(F.number_of_nodes())    
   
        dr = pd.read_csv("clicgrafo"+str(i)+".csv",header=None)  
        F = nx.from_pandas_adjacency(dr, create_using= nx.Graph())
        grafos[ "clicgrafoE"].append(F.number_of_edges())
        
        dr = pd.read_csv("digrafo"+str(i)+".csv",header=None)  
        F = nx.from_pandas_adjacency(dr, create_using= nx.Graph())
        grafos[ "digrafoE"].append(F.number_of_edges())
    
        dr = pd.read_csv("grafo"+str(i)+".csv",header=None)  
        F = nx.from_pandas_adjacency(dr, create_using= nx.Graph())
        grafos[ "grafoE"].append(F.number_of_edges())
        
    df = pd.DataFrame(grafos)
    df.to_csv("cantNE.csv" ) 
         
#GrafosElementos(5) 

def lee_valores(cant):
    
    algorit={
            
            "Media_A1bc":[],
            "Media_A2mc":[],
            "Media_A3gc":[],
            "Media_A4mf":[],
            "Media_A5mst":[],
            "Desvi_A1bc":[],
            "Desvi_A2mc":[],
            "Desvi_A3gc":[],
            "Desvi_A4mf":[],
            "Desvi_A5mst":[]
              } 
   
    for i in range(cant):
        
        dr = pd.read_csv("bet_grafo"+str(i)+".csv",header=None,)  
#        print(dr[0][0])
        algorit[ "Media_A1bc"].append(dr[0][0])
        
        dr = pd.read_csv("clique_clicgrafo"+str(i)+".csv",header=None)  
        
        algorit["Media_A2mc"].append(dr[0][0])
        
        dr = pd.read_csv("greed_digrafo"+str(i)+".csv",header=None)  
        algorit["Media_A3gc"].append(dr[0][0])
        
        dr = pd.read_csv("maxflow_digrafo"+str(i)+".csv",header=None)  
        algorit["Media_A4mf"].append(dr[0][0])
        
        dr = pd.read_csv("spanning_tree_grafo"+str(i)+".csv",header=None)  
        algorit["Media_A5mst"].append(dr[0][0])
        
        dr = pd.read_csv("bet_grafo"+str(i)+".csv",header=None)  
#        print(dr[0][1])
        algorit[ "Desvi_A1bc"].append(dr[0][1])
        
        dr = pd.read_csv("clique_clicgrafo"+str(i)+".csv",header=None)  
        algorit["Desvi_A2mc"].append(dr[0][1])
        
        dr = pd.read_csv("greed_digrafo"+str(i)+".csv",header=None)  
        algorit["Desvi_A3gc"].append(dr[0][1])
        
        dr = pd.read_csv("maxflow_digrafo"+str(i)+".csv",header=None)  
        algorit["Desvi_A4mf"].append(dr[0][1])
        
        dr = pd.read_csv("spanning_tree_grafo"+str(i)+".csv",header=None)  
        algorit["Desvi_A5mst"].append(dr[0][1])

    df = pd.DataFrame(algorit)
    df.to_csv("algori_med.csv" ) 


lee_valores(5)    
    
#for r in range(5):
#     betweenness_centrality("grafo"+str(r)+".csv") # OK
#     max_clique("clicgrafo"+str(r)+".csv")# OK
##     all_shortest_paths("grafo"+str(r)+".csv") #No funciona  
##     topological("digrafo"+str(r)+".csv") # No funciona 
#     greedy_color("digrafo"+str(r)+".csv")#OK
#     maximum_flow("digrafo"+str(r)+".csv") #OK
##     min_weighted_vertex_cover("grafo"+str(r)+".csv")#no esta en networkx
#     minimum_spanning_tree ("grafo"+str(r)+".csv") # OK
##     strongly_connected_components ("digrafo"+str(r)+".csv")#No funciona
##     treewidth_min_degree ("grafo"+str(r)+".csv")# no esta mi networkx
##     min_maximal_matching ("grafo"+str(r)+".csv") no esta en mi networkx