nombre=[]
actor=[]
años=[]
genero=[]

def abrirArchivo(ruta):
    archivo = open(ruta, 'r')
    contenido = archivo.read()
    archivo.close()
    return(contenido)

def leerPalabras():
    pass

print(abrirArchivo("LFP_P_202100692\entrada.lfp"))