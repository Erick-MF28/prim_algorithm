# Algoritmo de Prim / Python

Este repositorio contiene una implementación del algoritmo de Prim en lenguaje Python.

## Descripción:

Como es bien conocido el algoritmo de Prim es un procedimiento para encontrar el árbol extendido de costo mínimo de un grafo. Y al igual que el algoritmo de Kruskal es un algoritmo voraz con la particularidad de que no requiere una subrutina que compruebe que no se están generando ciclos, ya que implícitamente lo hace.

El procedimiento simplificado es el siguiente:

Sea un grafo no dirigido ponderado G = {V, E} 
donde V es el conjunto de vértices y E el conjunto de arcos.

entonces:

1.- Elegimos un vértice de V al azar (inicio)
2.- Lo agregamos al conjunto TV (vértices del árbol) y lo borramos de V

mientras V no sea vacío:
{
Evaluamos todos los nodos que inciden en los vértices de TV y que no se encuentre en T.

Elegimos el del menor peso, lo agregamos a T y el vértice nuevo a TV
}

Fin

## Características:
Este algoritmo tiene datos de entrada en archivos CSV de la siguiente manera: 

nodo, nodo, peso
nodo, nodo, peso
.....

Utilizo la biblioteca [Networkx](http://https://networkx.org/documentation/stable/index.html "Networkx") para una visualización final del árbol.
Es importante hacer notar que editando el código es posible crear visualizaciones dinámicas. 

## Ejemplo:

Grafo

1, 2, 2
1, 3, 3
1, 4, 3
2, 3, 4
2, 5, 3
3, 4, 5
3, 5, 1
3, 6, 6
4, 6, 7
5, 6, 8
6, 7, 9

Resultado

![](https://media.giphy.com/media/b3FtsxwlUBEtGWHHj9/giphy.gif)
