#3. Dada una lista de cadenas, pide una cadenena por teclado e indica si está en la lista, 
#indica cuantas veces aparece en la lista, lee otra cadena y sustituye la primera por la segunda en la lista, y por último borra la cadena de la lista

misCadenas = ["hola", "que", "tal", "estas tu", "hola"]

cadena = input("Que deseas buscar? ")

if cadena in misCadenas:
    print("Encontrado en la posicion", misCadenas.index(cadena))
else:
    print("No hemos encontrado coincidencias")

print(misCadenas.count(cadena))

cadena2 = input("Dime otra cadena: ")

veces = misCadenas.count(cadena)
pos = 0

for i in range(0, veces):
    pos = misCadenas.index(cadena, pos)
    misCadenas[pos] = cadena2

print(misCadenas)

del misCadenas[misCadenas.index(cadena2)]

print(misCadenas)

hola = "hola"