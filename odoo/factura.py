import datetime
from inventario import inventario

# Lista de facturas generadas (inicialmente vacía)
facturas = []

# Función para generar una factura
def generar_factura(cliente_id, productos):
    """
    Genera una factura con número único basado en la fecha y los productos comprados.
    :param cliente_id: ID del cliente que realiza la compra
    :param productos: Lista de productos comprados [(nombre, cantidad)]
    """
    fecha = datetime.datetime.now()
    num_factura = f"{fecha.year}{fecha.month:02d}{fecha.day:02d}{len(facturas) + 1}"
    # Calculamos el subtotal, IVA y total de la factura
    subtotal = sum(inventario[prod]["precio"] * cant for prod, cant in productos)
    iva = subtotal * 0.21  # IVA del 21%
    total = subtotal + iva
    
    # Usamos un diccioario para representar la factura
    # La estructura es similar a la de los clientes y el inventario
    # El número de factura se genera automáticamente según la fecha

    factura = {
        "Número": num_factura,
        "Fecha": fecha.strftime("%Y-%m-%d"),
        "Cliente ID": cliente_id,
        "Productos": productos,
        "Subtotal": subtotal,
        "IVA": iva,
        "Total": total
    }

    # Agregamos la factura a la lista de facturas
    facturas.append(factura)
    print(f"Factura generada con éxito: Nº {num_factura}")
    # Devolvemos la factura generada
    return factura

# Ejemplo de uso
if __name__ == "__main__":
    factura_ejemplo = generar_factura(1, [("Pan de hamburguesa", 2), ("Carne de res", 1), ("Queso", 1)])
    print(factura_ejemplo)
