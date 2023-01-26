#6. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.

minutos = int(input("Dime los minutos: "))

horas = minutos // 60
minutos = minutos % 60

print("Son ", horas, " horas y ", minutos, " minutos.")