#1. Pedir un número por teclado y mostrar la tabla de multiplicar
numero = int(input("Introduce un numero: "))

for contador in range(1,11):
    print(numero, " * ", contador, " = ", numero * contador)