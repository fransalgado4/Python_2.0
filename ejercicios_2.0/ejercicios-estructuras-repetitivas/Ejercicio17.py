#5. Escribe un programa que diga si un número introducido por teclado es o no primo. Un número primo es aquel que sólo es divisible entre él mismo y la unidad.

numero = int(input("Introduce un numero: "))
primo = True

for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break

if primo:
    print("Es primo")
else:
    print("No es primo")