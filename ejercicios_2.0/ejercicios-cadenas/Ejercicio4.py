# 4. Escribir funciones que dadas dos cadenas de caracteres:

# Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, cadena es una subcadena de subcadena.
# Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe kde y gnome debe devolver gnome.

cadena1 = input("Cadena1: ")
cadena2 = input("Cadena2: ")

if cadena1.find(cadena2) > -1:
    print("Cadena2 es una sub cadena de cadena1")
else:
    print("Cadena2 no es una sub cadena de cadena1")

print(cadena1 if cadena1 > cadena2 else cadena2)