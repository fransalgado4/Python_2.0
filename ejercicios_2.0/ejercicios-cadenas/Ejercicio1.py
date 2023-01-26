# 1. Crear un programa que lea por teclado una cadena y un carácter, e inserte el carácter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r

cadena = input("Inserta una cadena: ")
caracter = input("Introduce un caracter: ")

superCadena = ""

for i in range(0, len(cadena)):
    superCadena += cadena[i] + caracter

print(superCadena)
print(superCadena)