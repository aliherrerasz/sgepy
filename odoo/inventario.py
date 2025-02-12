''' 
Diccionario que representa el inventario del restaurante.
 Cada clave es el nombre de un producto, y su valor es otro diccionario con:
 - "cantidad": Número de unidades disponibles en stock.
 - "precio": Costo por unidad del producto.
 Este diccionario se usa para gestionar el stock y calcular costos en facturación.
'''

inventario = {
    "Pan de hamburguesa": {"cantidad": 50, "precio": 0.50},
    "Carne de res": {"cantidad": 30, "precio": 2.00},
    "Queso": {"cantidad": 20, "precio": 1.00},
    "Tomate": {"cantidad": 30, "precio": 0.60},
    "Salsa": {"cantidad": 40, "precio": 0.80},
    "Lechuga": {"cantidad": 15, "precio": 0.30}
}

# Función para mostrar el inventario actual
def mostrar_inventario():
    """Muestra el inventario actual."""
    print("Inventario del restaurante:")
    # Bucle for sobre los elementos del inventario
    for producto, datos in inventario.items():
        # Para cada uno, imprime el nombre del producto, la cantidad de unidades y el precio por unidad
        print(f"{producto}: {datos['cantidad']} unidades - €{datos['precio']:.2f} cada uno")

mostrar_inventario()