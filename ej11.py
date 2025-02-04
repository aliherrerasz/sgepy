# Python
# Manipular listas dentro de funciones.
def agregar_producto(productos, producto):
    # Agrega un producto a la lista de productos
    productos.append(producto)
    # Imprime un mensaje indicando que el producto ha sido agregado
    print(f"Producto {producto} agregado a la lista.")

# Lista inicial de productos
productos = ["manzana", "banana"]

# Agrega "naranja" a la lista de productos
agregar_producto(productos, "naranja")

# Imprime la lista actualizada de productos
print(productos)