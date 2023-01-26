#5. Escribir un programa python que dado una palabra diga si es un palíndromo. 
# Un palíndromo es una palabra, número o frase que se lee igual hacia adelante que hacia atrás. Ejemplo: reconocer

palabra = input("Dime una palabra: ")

palabraInvertida = ""

for letra in palabra:
    palabraInvertida = letra + palabraInvertida

if palabra == palabraInvertida:
    print("Esta palabra es palíndroma")
else:
    print("Esta palabra no es palíndroma")