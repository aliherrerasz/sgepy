# Python
# Crear clases y objetos 
class Persona:
    # Constructor de la clase Persona
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Inicializa el atributo nombre
        self.edad = edad  # Inicializa el atributo edad

    # Método para saludar
    def saludar(self):
        # Imprime un saludo con el nombre y la edad
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear un objeto de la clase Persona
persona1 = Persona("Luis", 30)
# Llamar al método saludar del objeto persona1
persona1.saludar()
