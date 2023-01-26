import json

datos_json = '{"nombre":"Carlos","edad":23}'

datos = json.loads(datos_json)

# print(datos["nombre"])
# print(datos["edad"])

with open("/Python/ejemplos/ficheros/ficheros-json/fichero1.json") as fichero:
    datos = json.load(fichero)

# print(datos)
# print(datos["librerÃ\xada"]["libro"][0]["precio"])

datosJSON = {"título": {"_lang": "es","__text": "XML de aprendizaje"},"autor": "Erik T. Ray","año": "2003","precio": "39,95","_category": "RED"}

fichero2 = open("/Python/ejemplos/ficheros/ficheros-json/fichero2.json", "w")

json.dump(datosJSON, fichero2)

fichero2.close()