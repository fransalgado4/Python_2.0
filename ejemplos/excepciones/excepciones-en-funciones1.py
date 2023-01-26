def dividir(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        raise 

def dividir2(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return "No se puede dividir"

print(dividir2(2,0))
try:
    print(dividir(2,0))
except ZeroDivisionError:
    print("No se puede dividir por cero")