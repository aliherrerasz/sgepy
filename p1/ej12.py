# Python
# Algoritmo sencillo para verificar si un número es primo. 
def es_primo(numero):
    # Si el número es menor que 2, no es primo
    if numero < 2:
        return False
    # Verifica si el número es divisible por algún número entre 2 y el número - 1
    for i in range(2, numero):
        if numero % i == 0:
            return False
    # Si no es divisible por ningún número en el rango anterior, es primo
    return True

# Prueba la función con el número 11 (debería ser True)
print(es_primo(11)) # True
# Prueba la función con el número 4 (debería ser False)
print(es_primo(4)) # False
