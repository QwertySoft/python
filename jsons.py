import json # Importamos el modulo 'json'

print(json.dumps({'name': 'Leonel'})) # Serializamos un objeto e imprimimos el resultado

person = json.loads('{"name": "Leonel"}') # Deserializamos un string en un json (diccionario)
person['name'] = 'Leonel Messi' # Cambiamos el nombre del JSON
print(person) # Imprimimos el objeto
