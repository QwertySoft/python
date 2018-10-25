from functools import partial # Importamos funcion 'partial' del modulo 'functools'

def multiply(x,y): # Definimos una funcion que multiplica dos valores
        return x * y # Retorno de la funcion

dbl = partial(multiply,2) # Crear una nueva función que multiplica un valor por dos
print(dbl(4)) # Imprimimos el resultado de la ejecucion de la funcion parcial