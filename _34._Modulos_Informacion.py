def resumen_modulo_1():
    curso = "Cisco: Esenciales de Python 2"
    seccion = "Sección 1 - Introducción a los módulos en Python"
    
    temas = [
        "Definición de módulos y paquetes",
        "Importación selectiva vs. total (import vs. from)",
        "Manejo del Namespace (Espacio de nombres)",
        "Aliasing de módulos y funciones (palabra clave 'as')",
        "Uso del comodín '*'"
    ]

    print(f"--- {curso.upper()} ---")
    print(f"Módulo: {seccion}\n")
    print("Conceptos clave aprendidos:")
    
    for i, tema in enumerate(temas, 1):
        print(f"{i}. {tema}")

    print("\nResumen técnico:")
    print("> Un módulo es un archivo con código (.py) diseñado para ser reutilizado.")
    print("> El 'Aliasing' permite evitar conflictos de nombres y escribir menos código.")
    
if __name__ == "__main__":
    resumen_modulo_1()
