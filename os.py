import os

print(os.getcwd()) # Imprimimos cual es el directorio actual
os.mkdir('./nuevo_directorio') # Creamos un directorio 'nuevo_directorio' en el directorio actual
print(os.listdir('.')) # Listamos el directorio actual
os.rmdir('./nuevo_directorio') # Eliminamos el directorio 'nuevo_directorio' dentro del directorio actual
print(os.listdir('.')) # Listamos el directorio actual nuevamente

os.system('bash') # Ejecutamos el binario 'bash'