clientes = {}

# Función para registrar un nuevo cliente
def registrar_cliente(id_cliente, nombre, telefono, email):
    """
    Registra un nuevo cliente en el diccionario.
    :param id_cliente: Identificador único del cliente
    :param nombre: Nombre del cliente
    :param telefono: Número de teléfono
    :param email: Correo electrónico
    """
    # Verificamos si el cliente ya está registrado por su ID
    # Si ya existe, mostramos un mensaje de error
    if id_cliente in clientes:
        print(f"Error: El cliente con ID {id_cliente} ya está registrado.")
        # Salimos de la función sin hacer nada más
        return
    # Si no existe, añadimos el cliente al diccionario
    clientes[id_cliente] = {
        "Nombre": nombre,
        "Teléfono": telefono,
        "Email": email
    }
    print(f"Cliente {nombre} registrado correctamente.")

# Ejemplo de uso
if __name__ == "__main__":
    registrar_cliente(1, "Juan Pérez", "123456789", "juan@gmail.com")
    registrar_cliente(2, "María López", "987654321", "maria@gmail.com")
    print(clientes)
