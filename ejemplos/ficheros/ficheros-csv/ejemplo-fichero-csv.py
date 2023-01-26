import csv

fichero = open("/Python/ejemplos/ficheros/ficheros-csv/fichero.csv", "r")

contenido = csv.reader(fichero)

miContenido = list(contenido)

print(list(contenido))
print(miContenido)

fichero.seek(0)

print(miContenido[0])

for row in contenido:
    print("Fila " + str(contenido.line_num) + " " + str(row))
    # for campo in row:
    #     print(campo)

fichero.close()

fichero2 = open("/Python/ejemplos/ficheros/ficheros-csv/fichero2.csv", "r")
contenido2 = csv.reader(fichero2, quotechar = '"')

for row in contenido2:
    print(row)

fichero2.close()

fichero3 = open("/Python/ejemplos/ficheros/ficheros-csv/fichero3.csv", "w")

contenido = csv.writer(fichero3)

contenido.writerow(['1996', 'Jeep', 'Grand Cherokee', 'MUST SELL!\nair,moon roof, loaded', '4799.00'])

fichero3.close()