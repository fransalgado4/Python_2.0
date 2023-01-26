#3. Crea una aplicación que permita adivinar un número. En primer lugar la aplicación solicita un número entero por teclado. 
#A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido. El programa termina cuando se acierta el número.
from random import randrange, choice

numero = 0
numero2 = randrange(10000)

while numero != 4441:
    numero = int(input("Introduce un numero: "))
    if numero > 4441:
        print("El numero que buscas es mas pequeño") 
    elif numero < 4441:
        print("El numero que buscas es mas mayor")
    elif numero == 4441:
        print("Numero encontrado!")