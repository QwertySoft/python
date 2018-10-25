class Person():
    def __init__(self, name, age):
        self.name = name # Un atributo cualquiera
        self.age = age # Otro atributo cualquiera

    def show_age(self): # Es necesario que, al menos, tenga un parámetro, generalmente: "self"
        print(self.age) # mostrando un atributo

    def change_age(self, age): # Modificando edad
        if age < 0 or age > 150: # Se comprueba que la edad no sea menor de 0 (algo imposible), ni mayor de 150 (algo realmente difícil)
            return False
        else: # Si está en el rango 0-150, entonces se modifica la variable
            self.age = age # Se modifica la edad

p = Person("Alicia", 20) # Instanciar la clase, como se puede ver, no se especifica el valor de "self"
print(p.name) # La variable "name" del objeto sí es accesible desde fuera
p.name = "Andrea" # Y por tanto, se puede cambiar su contenido
print(p.name)
p.show_age() # Se llama a un método de la clase
p.change_age(21) # Es posible cambiar la edad usando el método específico que hemos hecho para hacerlo de forma controlada
p.show_age()