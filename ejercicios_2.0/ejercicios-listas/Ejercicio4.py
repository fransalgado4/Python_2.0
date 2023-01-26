#4. Dado una lista, hacer un programa que indique si está ordenada o no.

lista = [1, 2, 11, 4, 5, 6, 7]

listaOrdenada = lista[:]
listaOrdenada.sort()

if lista == listaOrdenada:
    print("Esta ordenada")
else:
    print("No esta ordenada")

print("Mensaje nuevo")