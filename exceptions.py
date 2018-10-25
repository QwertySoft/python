try:
    1/0
except ZeroDivisionError as e:
    print('¡No se puede dividir por cero!')
    print(e)
finally:
    print('Fin del manejador de excepciones')