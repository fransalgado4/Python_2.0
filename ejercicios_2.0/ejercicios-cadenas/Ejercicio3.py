# 3. Crea un programa python que lea una cadena de caracteres y muestre la siguiente información:

# La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe devolver USB.
# Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe república argentina debe devolver República Argentina.
# Las palabras que comiencen con la letra A. Por ejemplo, si recibe Antes de ayer debe devolver Antes ayer.

cadena = input("Cadena: ")

palabras = cadena.split()

primerasLetras = ""
mayusculas = ""
comienzaPorA = ""
encontrado = False

for i in palabras:
    primerasLetras += i[0]

print(primerasLetras)

for palabras in cadena.split():
    mayusculas += palabras.capitalize() + " "

print(mayusculas)

for palabras in cadena.split():
    if palabras[0].upper() == "A":
    #OR if palabra.startswith("a") or palabra.startswith("A"):
        comienzaPorA += palabras.capitalize() + " "
        encontrado = True

if encontrado != True:
    comienzaPorA = "No tenemos palabras que empiecen por A"

print(comienzaPorA)