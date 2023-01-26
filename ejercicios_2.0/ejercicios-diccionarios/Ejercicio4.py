# 4. Suponga un diccionario que contiene como clave el nombre de una persona y como valor una lista con todas sus “gustos”. Desarrolle un programa que agregue “gustos” a la persona:

# Si la persona no existe la agregue al diccionario con una lista que contiene un solo elemento.
# Si la persona existe y el gusto existe en su lista, no tiene ningún efecto.
# Si la persona existe y el gusto no existe en su lista, agrega el gusto a la lista.
# Se deja de pedir personas cuando introducimos el carácter “*”.

diccionario = {'Francisco' : ['Futbol', 'Padel', 'Cine'],
               'Paula' : ['Cine', 'Salir'],
               'Antonio' : ['Baloncesto', 'Tenis']}

print(diccionario)

nombre = input("Nombre (Salir = *): ")
encontrado = False

while nombre != "*":

    miGusto = input("Introduce tu gusto: ")

    if nombre.capitalize() in diccionario:
        for gustos in diccionario[nombre.capitalize()]:
            if miGusto.capitalize() == gustos:
                encontrado = True

        if encontrado == False:
            diccionario[nombre.capitalize()].append(miGusto.capitalize())

    else:
        diccionario.setdefault(nombre.capitalize(), [miGusto.capitalize()])
    
    nombre = input("Nombre (Salir = *): ")

print(diccionario)

