#1. Realiza un programa que pida dos números ‘a’ y ‘b’ e indique si su suma es positiva, negativa o cero.

a = int(input("Introduce un numero: "))
b = int(input("introduce un numero: "))

if (a+b) > 0:
    print("Positiva")
elif (a+b) < 0:
    print("Negativa")
else:
    print("Cero")