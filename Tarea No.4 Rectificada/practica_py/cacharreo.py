# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 19:34:11 2019

@author: lapi7
"""

import numpy as np
import networkx as nx
from networkx.algorithms.flow import edmonds_karp
from networkx.algorithms.flow import boykov_kolmogorov
import datetime as dt
import pandas as pd
import statistics as stats
import winsound as snd

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
control_iteraciones = 0

generadores_grafos = {"newman_watts_strogatz_graph": nx.newman_watts_strogatz_graph, 
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

for generador_grafo in generadores_grafos:
    
    for instancia_grafo_x_nodos in [round(pow(2.6, value + 1))
                                    for value in
                                    range(4, 8)]:
      

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
            grafo_temp = generadores_grafos[generador_grafo](instancia_grafo_x_nodos,
                                                          round((instancia_grafo_x_nodos * 0.22) / 2),
                                                          0.22,
                                                          seed=None)

            aristas = grafo_temp.number_of_edges()
            pesos_normalmente_distribuidos = np.random.normal(15, 0.2, aristas)
            loop = 0
            for (u, v) in grafo_temp.edges():
                grafo_temp.edges[u, v]["capacity"] = pesos_normalmente_distribuidos[loop]
                loop += 1
            for instancia_grafo in range(1, 6):
                for algoritmo_flujo in algoritmos_flujomax:
                    matriz_tiempos_ejecucion = []
                    for medicion in range(1, 6):
                        hora_inicio = dt.datetime.now()
                        obj = algoritmos_flujomax[algoritmo_flujo](grafo_temp, fuente, sumidero, capacity="capacity")
                        hora_fin = dt.datetime.now()
                        tiempo_consumido_segundos = (hora_fin - hora_inicio).total_seconds()
                        matriz_tiempos_ejecucion.append(tiempo_consumido_segundos)
                    media = stats.mean(matriz_tiempos_ejecucion)
                    if media == 0:
                        snd.Beep(frequency, duration)
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
                    estructura_CSV["mediana"].append(round(stats.median(matriz_tiempos_ejecucion), 5))
                    estructura_CSV["varianza"].append(round(stats.pvariance(matriz_tiempos_ejecucion,
                                                                            mu=media), 5))
                    estructura_CSV["desviacion"].append(round(stats.pstdev(matriz_tiempos_ejecucion,
                                                                           mu=media), 5))
                    matriz_tiempos_ejecucion = []
ds = pd.DataFrame(estructura_CSV)
ds.to_csv("datos.csv", encoding="utf-8", index=None)