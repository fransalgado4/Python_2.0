#3. Calcular el perímetro y área de un círculo dado su radio.

import math

radioCirculo = float(input("Dime el radio del circulo:"))
numeroPi = math.pi

perimetroCirculo = (radioCirculo * 2) * numeroPi
areaCirculo = numeroPi * (radioCirculo ** 2)

print("El perimetro del circulo es: ", round(perimetroCirculo, 2), " y el area es: ", round(areaCirculo, 2))