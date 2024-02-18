nombres = []
actors = []
años = []
generos = []

def abrirArchivo(ruta):
    with open(ruta, 'r') as archivo:
        contenido = archivo.readlines()
    return contenido

def leerPalabras(ruta):
    global nombres,actors,años,generos
    
    contenido = abrirArchivo(ruta)
    
    for linea in contenido:
        partes = linea.strip().split(';')
        nombres.append(partes[0])
        actors.append(partes[1])
        años.append(partes[2])
        generos.append(partes[3])
        
    return nombres, actors, años, generos

def ordenarPorActor(nombres, actores):
    # Creamos un diccionario para almacenar las películas de cada actor
    peliculas_por_actor = {}
    
    # Recorremos los nombres y actores y los agregamos al diccionario
    for nombre, actor in zip(nombres, actores):
        # Eliminamos espacios en blanco y dividimos los actores por coma
        lista_actores = [a.strip() for a in actor.split(',')]
        # Recorremos los actores
        for a in lista_actores:
            # Si el actor ya está en el diccionario, agregamos la película
            if a in peliculas_por_actor:
                peliculas_por_actor[a].append(nombre)
            # Si no está en el diccionario, creamos una nueva entrada
            else:
                peliculas_por_actor[a] = [nombre]
    
    return peliculas_por_actor

def mostrarPeliculasPorNombre(datos_ordenados):
    nombre_buscar = input("Ingrese el nombre del actor: ").strip()
    peliculas = []
    for actor, lista_peliculas in datos_ordenados.items():
        if nombre_buscar in actor:
            peliculas.extend(lista_peliculas)
    if peliculas:
        print(f"Películas en las que participó {nombre_buscar}:")
        for pelicula in peliculas:
            print(f"- {pelicula.strip()}")
    else:
        print(f"No se encontraron películas para el nombre {nombre_buscar}.")
        

def obtenerActoresSinRepetir(actores):
    actores_sin_repetir = set()
    for lista_actores in actores:
        # Dividimos la cadena de actores por coma y eliminamos espacios en blanco
        actores_individuales = [actor.strip() for actor in lista_actores.split(',')]
        # Agregamos cada actor a un conjunto para evitar repeticiones
        actores_sin_repetir.update(actores_individuales)
    return list(actores_sin_repetir)

def obtenerActoresPeliculas(nombres, actores):
    actores_peliculas = []
    for nombre, lista_actores in zip(nombres, actores):
        actores_individuales = [actor.strip() for actor in lista_actores.split(',')]
        for actor in actores_individuales:
            actores_peliculas.append((actor, nombre))
    return actores_peliculas

def peliculasPorAño(año_buscado, años, nombres):
    peliculas_en_año = []
    for año, nombre in zip(años, nombres):
        if año_buscado == año:
            peliculas_en_año.append(nombre)
    return peliculas_en_año

def peliculasPorGenero(genero_buscado, generos, nombres):
    peliculas_del_genero = []
    for genero, nombre in zip(generos, nombres):
        if genero_buscado.lower() == genero.lower():
            peliculas_del_genero.append(nombre)
    return peliculas_del_genero

#nombres, actors, años, generos = leerPalabras("LFP_P_202100692\entrada.lfp")
#print("Nombres:", nombres)
#print("Actores:", actores)
#print("Años:", años)
#print("Géneros:", generos)
