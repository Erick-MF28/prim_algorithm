# Algoritmo de Prim / Python

Este repositorio contiene una implementación del algoritmo de Prim en lenguaje Python.

## Descripción:

Como es bien conocido el algoritmo de Prim es un procedimiento para encontrar el árbol extendido de costo mínimo de un grafo. Y al igual que el algoritmo de Kruskal es un algoritmo voraz con la particularidad de que no requiere una subrutina que compruebe que no se están generando ciclos, ya que implícitamente lo hace.

El procedimiento simplificado es el siguiente:<br/>

Sea un grafo no dirigido ponderado G = {V, E}<br/> 
donde V es el conjunto de vértices y E el conjunto de arcos.<br/>

entonces:

1.- Elegimos un vértice de V al azar (inicio)<br/>
2.- Lo agregamos al conjunto TV (vértices del árbol) y lo borramos de V<br/>

mientras V no sea vacío:<br/>
{
Evaluamos todos los nodos que inciden en los vértices de TV y que no se encuentre en T.<br/>

Elegimos el del menor peso, lo agregamos a T y el vértice nuevo a TV<br/>
}

Fin

## Características:
Este algoritmo tiene datos de entrada en archivos CSV de la siguiente manera: 

nodo, nodo, peso<br/>
nodo, nodo, peso<br/>
.....<br/>

Utilizo la biblioteca [Networkx](http://https://networkx.org/documentation/stable/index.html "Networkx") para una visualización final del árbol.
Es importante hacer notar que editando el código es posible crear visualizaciones dinámicas. 

## Ejemplo:

Grafo

1, 2, 2<br/>
1, 3, 3<br/>
1, 4, 3<br/>
2, 3, 4<br/>
2, 5, 3<br/>
3, 4, 5<br/>
3, 5, 1<br/>
3, 6, 6<br/>
4, 6, 7<br/>
5, 6, 8<br/>
6, 7, 9<br/>

Resultado

![](https://media.giphy.com/media/b3FtsxwlUBEtGWHHj9/giphy.gif)

## Ejercicio:

En el archivo prueba.csv esta contenido un grafo con 26 vertices y mas de 200 arcos con el cual puedes probar el algoritmo

![](https://media.giphy.com/media/8tIJmjgnyEvOZ1e0fa/giphy.gif)




