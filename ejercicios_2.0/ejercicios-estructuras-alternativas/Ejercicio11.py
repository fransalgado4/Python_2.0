#5. Escribir un programa que lea un año indicar si es bisiesto. 
#Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.

year = int(input("Dime el año: "))

if (year % 4) != 0:
    print("Año normal")
elif (year % 4) == 0 and (year % 100) != 0:
    print("Año bisiesto")
elif (year % 4) == 0 and (year % 100) == 0 and (year % 400) != 0:
    print("Año normal")
elif (year % 4) == 0 and (year % 100) == 0 and (year % 400) == 0:
    print("Año bisiesto")
