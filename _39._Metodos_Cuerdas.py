def arsenal_metodos_cadenas():
    print("--- SECCIÓN 2.3: MÉTODOS DE CUERDAS ---")
    
    txt = "  aprender Python es genial  "

    # 1. Familia de Limpieza (Strip)
    print(f"Original: '{txt}'")
    print(f"Limpio:   '{txt.strip()}'") # Quita espacios a ambos lados

    # 2. Familia de Búsqueda y Reemplazo
    print(f"¿Dónde está 'Python'?: {txt.find('Python')}") 
    print(f"Reemplazo: {txt.replace('genial', 'increíble').strip()}")

    # 3. Familia de Validación (Devuelven True/False)
    digitos = "2024"
    print(f"¿'{digitos}' es numérico?: {digitos.isdigit()}")
    print(f"¿'{txt.strip()}' es todo minúsculas?: {txt.strip().islower()}")

    # 4. Familia de Transformación y Unión
    lista_palabras = ["Python", "es", "top"]
    unido = "-".join(lista_palabras)
    print(f"Join: {unido}")
    print(f"Split de '{unido}': {unido.split('-')}")

if __name__ == "__main__":
    arsenal_metodos_cadenas()
