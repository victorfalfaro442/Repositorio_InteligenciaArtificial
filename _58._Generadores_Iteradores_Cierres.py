# 4.1.2 La declaración yield (Generadores)
def contador_generador(n):
    """Un generador no devuelve todo a la vez, entrega uno por uno."""
    for i in range(1, n + 1):
        yield i  # Pausa la función y devuelve el valor

# 4.1.5 La función lambda
# Es una función anónima de una sola línea: lambda parámetros: expresión
duplicar = lambda x: x * 2

# 4.1.7 y 4.1.8 Map y Filter
numeros = [1, 2, 3, 4, 5]

# Filter: Filtra elementos basados en una condición (solo pares)
pares = list(filter(lambda x: x % 2 == 0, numeros))

# Map: Aplica una función a cada elemento (elevar al cuadrado)
cuadrados = list(map(lambda x: x**2, numeros))

# 4.1.9 Cierres (Closures)
def fabricar_multiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar

duplicador_cierre = fabricar_multiplicador(2)

# Ejecución de ejemplos
print(f"Pares con filter: {pares}")
print(f"Cuadrados con map: {cuadrados}")
print(f"Resultado del cierre: {duplicador_cierre(10)}")

print("Generador en acción:")
for num in contador_generador(3):
    print(num)
