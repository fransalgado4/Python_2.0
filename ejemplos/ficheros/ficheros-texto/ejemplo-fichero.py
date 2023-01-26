fichero = open("/Python/ejemplos/ficheros/ficheros-texto/fichero.txt", "r")

# tipo de fichero
# print(type(fichero)) 

# cerrar fichero
# print(fichero.closed) 

# nombre del fichero
# print(fichero.name)

#modo en el que se ha abierto el fichero
# print(fichero.mode)

# leer el ficher
# print(fichero.read(4))

# posicion en la que se encuentra el puntero en la lectura del fichero
# print(fichero.tell())

# print(fichero.read())

# poner el puntero en la primera casilla 
# fichero.seek(0)

# leer el fichero desde una posicion en concreto
# print(fichero.read(4))

# print(fichero.read())
# print(fichero.read())

# leer una linea del fichero
# print(fichero.readline())

# devuelve un array con las lineas escritas del fichero
# print(fichero.readlines())

fichero.close()

fichero2 = open("/Python/ejemplos/ficheros/ficheros-texto/fichero2.txt", "r+")
fichero2.write("Primera escritura")
# print(fichero2.read())
fichero2.writelines(["Primera linea\n", "Segunda linea\n"])
fichero2.close()

with open("/Python/ejemplos/ficheros/ficheros-texto/fichero.txt", "r") as archivo:
    contenido = archivo.read()
    
with open("/Python/ejemplos/ficheros/ficheros-texto/fichero2.txt", "r") as archivo2:
    contenido2 = archivo2.read()

# with open("/Python/ejemplos/ficheros/ficheros-texto/fichero2.txt", "r") as archivo3:
    # for linea in archivo3:
        # print(linea)

# print(contenido)
# print(contenido2)

