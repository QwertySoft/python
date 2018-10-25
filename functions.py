def sum(x, y=10): # Definimos la funcion
    print(x + y) # Imprimimos la suma de los parametros

sum(2) # Invocamos la funcion con un valor para el parametro 'x' 
sum(2, 18) # Invocamos la funcion con un valor para el parametro 'x' e 'y' 

def print_values(*args): # Definimos otra funcion con una cantidad variable de parametros
    for i in args: # Iteramos sobre los parametros
        print(i) # Imprimimos cada parametro

print_values(1, 2) # Invocamos la funcion con dos parametros
print_values(1, 2, 3, 4, 5) # Invocamos la funcion con cinco parametros