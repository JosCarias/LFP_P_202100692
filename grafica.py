import graphviz
from leerCSV import *

def hacerGrafico():
    grafo = graphviz.Digraph()

    # Obtener actores sin repetir y actores con sus películas
    actores_sin_repetir = obtenerActoresSinRepetir(actors)
    actores_peliculas = obtenerActoresPeliculas(nombres, actors)

    # Agregar nodos de actores al grafo
    for actor in actores_sin_repetir:
        grafo.node(actor, shape='box',color='gray')

    # Agregar nodos de películas al grafo
    for nombre in nombres:
        grafo.node(nombre, shape='ellipse',color='skyblue')  # Supongamos que las películas tienen forma de elipse

    # Agregar aristas entre actores y películas correspondientes
    for actor, pelicula in actores_peliculas:
        grafo.edge(actor, pelicula)

    # Guardar el grafo en un archivo y visualizarlo
    grafo.render('grafo', format='png', cleanup=True)
    grafo.view()