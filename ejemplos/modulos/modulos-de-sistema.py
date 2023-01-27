# funcionalidad del sistema operativo
import os
# ruta donde estamos
os.getcwd()
os.chdir("..")
os.getcwd()

# instrucciones
os.system("ls")
os.system("ls -al")

import subprocess
# para guardar las salidas de un comando en una variable
subprocess.call("ls")
salida = subprocess.check_output("ls")
print(salida)
# pintar la variable decodificada
print(salida.decode())
# comandos de excel
salida = subprocess.check_output(["df", ".h"])


import shutil, os

ruta = os.getcwd() + os.sep
origen = ruta + 'origen.txt'
destino = ruta + 'destino.txt'

try:
    shutil.copyfile(origen, destino)
    print("Archivo copiado")
except:
    print("Se ha producido un error")


import sys

sys.version
sys.platfrom
sys.argv