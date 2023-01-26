#1. Lee por teclado números y guardalo en una lista, el proceso finaliza cuando metamos un número negativo. 
#Muestra el máximo de los números guardado en la lista, muestra los números pares.

misNumeros = []
numero = 0

while numero != -1:

    numero = int(input("Introduce un numero: "))
    misNumeros.append(numero)

print(max(misNumeros))
print([i for i in misNumeros if i%2==0])