import numpy as np
import networkx as nx
from networkx.algorithms.flow import edmonds_karp
from networkx.algorithms.flow import boykov_kolmogorov
import datetime as dt
import pandas as pd
import statistics as stats

control_iteraciones = 0


genera_grafo = {"newman_watts_strogatz_graph": nx.newman_watts_strogatz_graph, 
                      "watts_strogatz_graph": nx.watts_strogatz_graph,
                      "connected_watts_strogatz_graph": nx.connected_watts_strogatz_graph}

algoritmos_flujomax = { "maximum_flow": nx.maximum_flow, 
                    "boykov_kolmogorov": boykov_kolmogorov,
                    "edmonds_karp": edmonds_karp}

estructura_CSV = { "grafo": [],
                   "generador": [],
                   "algoritmo_flujo": [],
                   "vertices": [],
                   "densidad": [],
                   "aristas": [],
                   "fuente": [],
                   "sumidero": [],
                   "media": [],
                   "mediana": [],
                   "varianza": [],
                   "desviacion": [] }

for generador_grafo in genera_grafo:
    for instancia_grafo_x_nodos in [round(pow(2.6, value + 1)) for value in range(4, 8)]: # eleva a la potencia partiendo de la base 2.6
      

        for grafo in range(1, 11):
            fuente = np.random.randint(1, high=(instancia_grafo_x_nodos - 1), dtype="int")
            sumidero = np.random.randint(1, high=(instancia_grafo_x_nodos - 1), dtype="int")
    
            while sumidero == fuente:
                fuente = np.random.randint(1, high=(instancia_grafo_x_nodos - 1), dtype="int")
                sumidero = np.random.randint(1, high=(instancia_grafo_x_nodos - 1), dtype="int")
    
            if fuente > sumidero:
                swapping = fuente
                fuente = sumidero
                sumidero = swapping
           
            grafo_temp = genera_grafo[generador_grafo](instancia_grafo_x_nodos,
                                                          round((instancia_grafo_x_nodos * 0.15) / 2),
                                                          0.15,
                                                          seed=None)

            aristas = grafo_temp.number_of_edges()
            pesos_normalmente_distribuidos = np.random.normal(15, 0.2, aristas)
           
            increment = 0 # incremento para que itere dentro del for que es el grafo, magia!!!
            for (u, v) in grafo_temp.edges():
                grafo_temp.edges[u, v]["capacity"] = pesos_normalmente_distribuidos[increment]
                increment += 1
           
            for instancia_grafo in range(1, 6):
                for algoritmo_flujo in algoritmos_flujomax:
                    tabla_tiempo_ejec = []
                    for medicion in range(1, 6):
                        hora_inicio = dt.datetime.now()
                        obj = algoritmos_flujomax[algoritmo_flujo](grafo_temp, fuente, sumidero, capacity="capacity")
                        hora_fin = dt.datetime.now()
                        tiempo_consumido_segundos = (hora_fin - hora_inicio).total_seconds()
                        tabla_tiempo_ejec.append(tiempo_consumido_segundos)
                    media = stats.mean(tabla_tiempo_ejec)
                    
                    
                    if media == 0:
                        raise ValueError("La media no puede ser 0 para esta tarea......")                      
                    print("iteración %s tiempo consumido promedio %s" % (control_iteraciones + 1, round(media, 4)))
                    control_iteraciones +=1
                    
                    estructura_CSV["grafo"].append("vertices" + str(instancia_grafo_x_nodos) + "aristas" + str(aristas))
                    estructura_CSV["algoritmo_flujo"].append(algoritmo_flujo)
                    estructura_CSV["generador"].append(generador_grafo)
                    estructura_CSV["vertices"].append(instancia_grafo_x_nodos)
                    estructura_CSV["aristas"].append(aristas)
                    estructura_CSV["fuente"].append(fuente)
                    estructura_CSV["sumidero"].append(sumidero)
                    estructura_CSV["densidad"].append(nx.density(grafo_temp))
                    estructura_CSV["media"].append(round(media, 5))
                    estructura_CSV["mediana"].append(round(stats.median(tabla_tiempo_ejec), 5))
                    estructura_CSV["varianza"].append(round(stats.pvariance(tabla_tiempo_ejec, mu=media), 5))
                    estructura_CSV["desviacion"].append(round(stats.pstdev(tabla_tiempo_ejec, mu=media), 5))
                    tabla_tiempo_ejec = []
                    
ds = pd.DataFrame(estructura_CSV)
ds.to_csv("datos.csv", encoding="utf-8", index=None)