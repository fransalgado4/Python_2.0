cad = input("Dame un numero: ")

try:
    print (10/int(cad))
except ValueError:
    print("No se puede converir a entero")
except ZeroDivisionError:
    print("No se puede divir por cero")
except:
    print("Otro error")