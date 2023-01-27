# importar funciones de otro paquete
import potencias

# print(potencias.cuadrado(3))
print(dir(potencias))

# importar funciones con apodo para su uso
# import potencias as p

# print(p.cuadrado(3))
# print(p.cubo(3))

# importar funcion especifica desde otro paquete para importar varias una, otra. para importarlas todas '*'
# from potencias import *

# print(cuadrado(3))
# print(cubo(3))

# importar funcion especifica desde otro paquete con alias por si hay otra funcion como en el ejemplo

# from potencias import cuadrado as pc
# from dibujos import cuadrado as dc

# print(pc(3))
# print(dc(3))

# Para importar funciones desde otro modulo, se escribe el modulo.paquete
# import modulos.potencias
# print(modulos.potencias.cuadrado(3))