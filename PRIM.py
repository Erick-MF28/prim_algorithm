# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 00:46:35 2020

@author: Erick Martínez
"""
import random
import csv 
import networkx as nx
import matplotlib.pyplot as plt
from timeit import default_timer

itime= default_timer()
reader = csv.reader(open('C:\\Users\\Erick Martinez\\Documents\\test.csv')) 

G = {} #grafo importante que la numeracion de los nodos empiece en 1
 
for row in reader: 
    key = row[0] 
    if key in G:
        G[key].append(tuple((row[1], int(row[2]))))
             
        pass
    else:
        G[key] = [tuple((row[1], int(row[2])))]
                           
TV = [] #Vertices en el arbol 
T=[] #Arcos en el arbol
E = [] #Conjunto de Arcos en G 

#Inicio de Algoritmo de PRIM

#Iniciamos con un vertice aleatorio

inicial =list( G.keys())

inicio = random.choice(inicial)

#Añadimos el primer vertice en los vertices del arbol

TV.append(inicio)

#Generamos el conjunto E
for key in G.keys():
    for destino, peso in G[key]:
        E.append((key, destino, peso))

#Generamos conjunto V (Conjunto de vertices en G)
V=list(G.keys())
for key in G.keys():
    for destino, peso in G[key]:
        if destino not in V:
            V.append(destino)
#Dibujar Grafo
grafo=nx.DiGraph()
grafo.add_weighted_edges_from(E)
grafo=grafo.to_undirected()
labels = {}
colorin=[]
for u,v,data in grafo.edges(data=True):
    labels[(u,v)] = data['weight']
           
for i in range(len(grafo.edges())):
    colorin.append("#A0CBE2")
            
#Mientras sigan habiendo vertices en V se ejecuta el codigo
nodos=(len(V))
z=1           
while len(V)>1:
    
    print("Se han agregado", z, "de", nodos, "nodos totales")
    V.remove(inicio) #Se quita el vertice inicial del conjunto V
        
    listaA=[]
    for i in TV:
        if i in G:
            for destino, peso in G[i]:
                listaA.append((i, destino, peso))
        for i in TV:
           for o in E: #Se agregan los arcos que faltan
                if o[1]==i:
                    listaA.append(o)
        pos=0
        act=0
        listaB=[]
        for i in range(len(listaA)):
            listaB=listaA[i]
            act=listaA[i][2]
            pos=i
            while pos> 0 and listaA[pos-1][2] > act:
                listaA[pos] = listaA[pos-1]
                pos=pos-1
                listaA[pos]=listaB
    
    
    for i in listaA: 
        if i[0] in TV:
            if i[1] in V:
                inicio=i[1]
                TV.append(inicio)
                break
        else:
            inicio=i[0]
            TV.append(inicio)
            break
        
    T.append(i) 
    

    for u in G[listaA[0][0]]: #Se remueve el arco del diccionario
        if u[0]== listaA[0][1]:
            G[listaA[0][0]].remove(u)
            
    G = { k: v for k,v in G.items() if v }
    
    for i in E:              #Se remueve el arco del conjunto E
        if i[0]==listaA[0][0]:
            if i[1]==listaA[0][1]:
                if i[2]==listaA[0][2]:
                    E.remove(i)
    z=z+1

print("Se han agregado", z, "de", nodos, "nodos totales")
print('')

z=0
for edge in grafo.edges():
    for i in T:        
        if (edge[0]==i[0] and edge[1]==i[1]) or(edge[0]==i[1] and edge[1]==i[0]):
            colorin[z]='r'
    z=z+1
 
pos = nx.random_layout(grafo) #spring #spectral #circular #random
options = {"node_size": 50, "alpha": 0.7}
nx.draw_networkx_nodes(grafo, pos, node_color='g', **options)
nx.draw_networkx_edges(grafo, pos, width=2, alpha=.5, edge_color=colorin) 
nx.draw_networkx_labels(grafo, pos, font_size=5, font_family="sans-serif", font_color='w')
#nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
plt.show()
ftime=default_timer()
tiempo = (ftime - itime)
print("Tiempo de ejecucion", tiempo, "segundos")
print('')    
print("La secuencia de nodos es la liguiente:", TV)
print('')
print("La secuencia de arcos es la siguiente:", T)
 

            
        
 