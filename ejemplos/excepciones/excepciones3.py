x = input("Dame un numero: ")
y = input("Dame otro numero: ")

try:
    result = int(x) / int(y)
except ZeroDivisionError:
    print("División por cero!")
else:
    print("El resultado es", result)
finally:
    print("Terminamos el programa")