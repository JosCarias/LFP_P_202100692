from leerCSV import *
from grafica import *

def pantalaDeInicio():
    mensaje='''“Lenguajes Formales y de Programación”,
    Sección: B+, 
    Número de carnet: 202100692,
    Nombre: Josue Ricardo Carias Ordoñez'''
    
    print(mensaje)
    
    input("Presione cualquier tecla para continuar:")
    print("-----------------------------------------")
    menu()
    
    
def menu():
    global nombres,actors,años,generos
    opciones='''Ingrese el Numero de la accion que desea realizar:
    1) Cargar Archivo.
    2) Gestionar Peliculas.
    3) Filtrado.
    4) Grafica.
    5) Salir.'''
    print(opciones)
    selecion=input("Ingrese un numero para continuar:")
    print("-----------------------------------------")
    if(selecion=="1"):
        ruta=input("Ingrese la ruta relativa del archivo:")     
        nombres,actors,años,generos=leerPalabras(ruta)
        print("Ese ha cargado el archivo")
        input("Presione cualquier tecla para continuar:")
        print("-----------------------------------------")
        menu()
    if(selecion=="2"):
        opciones='''Ingrese el Numero de la accion que desea realizar:
            1) Mostrar Peliculas.
            2) Mostrar Actores.
            3) Salir.'''
        print(opciones)
        selecion=input("Ingrese un numero para continuar:")
        print("-----------------------------------------")   
        if(selecion=="1"):
            for i in range(len(nombres)):
                print(str(i)+"). La pelicula de "+nombres[i]+" protagonizadao por los actores "+actors[i]+" lanzada el año "+años[i]+" de genero de cine "+generos[i]+".")
            input("Presione cualquier tecla para continuar:")
            print("-----------------------------------------")
            menu()
        if(selecion=="2"):
            datos_ordenados = ordenarPorActor(nombres, actors)
            for actor, peliculas in datos_ordenados.items():
                print(f"Actor: {actor}")
                print("* Películas:")
                for pelicula in peliculas:
                    print(f"  - {pelicula.strip()}")
            input("Presione cualquier tecla para continuar:")
            print("-----------------------------------------")
            menu()
        if(selecion=="3"):
            menu()
    if(selecion=="3"):
        opciones='''Ingrese el Numero de la accion que desea realizar:
            1) Filtrado por actor.
            2) Filtrado por año.
            3) Filtrado por género
            4) Salir.'''
        print(opciones)
        selecion=input("Ingrese un numero para continuar:")
        print("-----------------------------------------")   
        if(selecion=="1"):
            datos_ordenados = ordenarPorActor(nombres, actors)
            mostrarPeliculasPorNombre(datos_ordenados)
            selecion=input("Ingrese un numero para continuar:")
            print("-----------------------------------------")
            menu()
        if(selecion=="2"):
            año_usuario = input("Ingrese un año para ver las películas lanzadas en ese año: ").strip()
            peliculas_del_año = peliculasPorAño(año_usuario, años, nombres)
            if peliculas_del_año:
                print(f"Películas lanzadas en {año_usuario}:")
                for pelicula in peliculas_del_año:
                    print(f"- {pelicula.strip()}")
            else:
                print(f"No se encontraron películas para el año {año_usuario}.")
            print("-----------------------------------------")
            menu()
        if(selecion=="3"):
            genero_usuario = input("Ingrese un género para ver las películas de ese género: ").strip()
            peliculas_del_genero = peliculasPorGenero(genero_usuario, generos, nombres)
            if peliculas_del_genero:
                print(f"Películas del género {genero_usuario}:")
                for pelicula in peliculas_del_genero:
                    print(f"- {pelicula.strip()}")
            else:
                print(f"No se encontraron películas para el género {genero_usuario}.")
            print("-----------------------------------------")
            menu()
        if(selecion=="4"):
            menu()
    if(selecion=="4"):
        hacerGrafico()
        print("-----------------------------------------")
        menu()
    if(selecion=="5"):
        quit()
        
pantalaDeInicio()
    
