#Pyhton


'''
Ejercicio 1 - Crear un diccionario

'''

# Define un diccionario con pares clave-valor
mi_diccionario = {
# Clave: Valor
 "nombre": "Juan",
 "edad": 25,
 "ciudad": "Madrid"
}
# Acceder a un valor usando la clave
print(mi_diccionario["nombre"]) # Salida: Juan
print(mi_diccionario["edad"]) # Salida: 25


'''
Ejercicio 2 - Modificar un diccionario

'''

# Agregar un nuevo par clave-valor
mi_diccionario["profesion"] = "Ingeniero"
# Mostramos el diccionario
print(mi_diccionario)
# Modificar el valor de una clave existente
mi_diccionario["edad"] = 26
# Imprimimos el valor modificado
print(mi_diccionario) # Edad será ahora 26


'''
Ejercicio 3 - Eliminar un elemento de un diccionario

'''

# Eliminar un elemento usando su clave
del mi_diccionario["ciudad"]
print(mi_diccionario) # "ciudad" se elimina del diccionario
# Usar el método pop() para eliminar y obtener el valor
edad = mi_diccionario.pop("edad")
print(edad) # Salida: 26
print(mi_diccionario) # El diccionario ahora no tiene la clave "edad"


'''
Ejercicio 4 - Verificar si una clave existe en un diccionario

'''

# Verificar si la clave 'nombre' existe en el diccionario

if "nombre" in mi_diccionario:
    print("La clave 'nombre' existe.")
else:
    print("La clave 'nombre' no existe.")


'''
Ejercicio 5 - Recorrer un diccionario

'''

# No hace falta volver a definir el diccionario, 
# ya que lo hemos hecho en el ejercicio 1
'''
mi_diccionario = {
 "nombre": "Juan",
 "edad": 25,
 "ciudad": "Madrid"
}
'''
# Recorrer las claves y los valores
# Con un bucle for podemos recorrer las claves del diccionario
# y acceder a los valores correspondientes

for clave, valor in mi_diccionario.items():
 print(f"{clave}: {valor}")


'''
Ejercicio 6 - Obtener las claves y los valores de un diccionario

'''


# Obtener las claves
claves = mi_diccionario.keys()
print(claves) # Salida: dict_keys(['nombre', 'edad', 'ciudad'])
# Obtener los valores
valores = mi_diccionario.values()
print(valores) # Salida: dict_values(['Juan', 25, 'Madrid'])


'''
Ejercicio 7 - Crear un diccionario con dict()

'''

# Usando dict() para crear un diccionario
mi_diccionario = dict(nombre="Juan", edad=25, ciudad="Madrid") # No se usan las comillas para las claves
# Mostrar el diccionario
print(mi_diccionario) # Salida: {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid'}


'''
Ejemplo Complejo

'''

# Diccionario anidado (diccionario dentro de un diccionario)
# Definimos un diccionario con un diccionario anidado
estudiante = {
 "nombre": "Ana",
 "edad": 22,
 # Diccionario anidado
 "materias": {
 "matematica": 85,
 "fisica": 90,
 "quimica": 88
 }
}
# Acceder a una clave dentro de un diccionario anidado
print(estudiante["materias"]["fisica"]) # Salida: 90

