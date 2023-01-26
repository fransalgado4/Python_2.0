# 3. Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.
numero = input("Dime un numero del 1 al 12: ")

if numero == "1" or numero == "3" or numero == "5" or numero == "7" or numero == "8" or numero == "10" or numero == "12":
    print("31")
elif numero == "3" or numero == "4" or numero == "6" or numero == "9" or numero == "11":
    print("30")
elif numero == "2":
    print("28")
else:
    print("No tenemos esos datos.")
    
