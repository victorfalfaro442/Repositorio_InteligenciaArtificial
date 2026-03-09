import math
import random
import platform

def demostracion_seccion_2():
    print("--- RESUMEN TÉCNICO: SECCIÓN 2 ---")
    
    # 1. Módulo math: Funciones matemáticas precisas
    # Ejemplo: factorial y constantes
    print(f"\n[MATH] El factorial de 5 es: {math.factorial(5)}")
    print(f"[MATH] Valor de pi: {math.pi}")

    # 2. Módulo random: ¿Aleatoriedad real? (Pseudoaleatoriedad)
    # Ejemplo: elegir un número entre 1 y 100
    numero_azar = random.randint(1, 100)
    print(f"\n[RANDOM] Número aleatorio generado: {numero_azar}")
    
    # 3. Módulo platform: Información del sistema
    # Nos dice sobre qué "plataforma" corre el código
    print(f"\n[PLATFORM] Sistema Operativo: {platform.system()}")
    print(f"[PLATFORM] Procesador: {platform.processor()}")

    # 4. Función dir(): El inspector de módulos
    # Imprimimos los primeros 5 elementos que contiene el módulo math
    print(f"\n[DIR] Contenido de math (primeros 5): {dir(math)[:5]}")

if __name__ == "__main__":
    demostracion_seccion_2()
