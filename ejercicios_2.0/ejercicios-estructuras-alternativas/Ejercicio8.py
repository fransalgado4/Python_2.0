#2. Escribe un programa que lea un número e indique si es par o impar.

numero = int(input("Introduce un numero: "))

if (numero % 2) == 0:
    print("El numero es par")
else:
    print("El numero es impar")