def naturaleza_de_las_cadenas():
    # 2.2.2 Cuerdas multilínea
    multilinea = """Esta es una cadena
    que abarca varias líneas."""
    
    # 2.2.4 Cadenas como secuencias (Indexación)
    palabra = "Python"
    print(f"--- SECCIÓN 2.2: CADENAS ---")
    print(f"Primera letra: {palabra[0]}") # P
    
    # 2.2.5 Cortes (Slicing) - [inicio:fin:paso]
    print(f"Corte [1:4]: {palabra[1:4]}") # yth
    
    # 2.2.6 Operadores in y not in
    print(f"¿Está 'th' en Python?: {'th' in palabra}")
    
    # 2.2.7 Inmutabilidad (¡IMPORTANTE!)
    print("\n[DATO CLAVE] Las cadenas son INMUTABLES.")
    try:
        palabra[0] = "p" # Esto lanzará un error
    except TypeError:
        print("Error: No puedes cambiar una letra de la cadena original.")

    # 2.2.8 Operaciones: min(), max(), index()
    print(f"Carácter mínimo en 'Python': {min(palabra)}") # P (basado en ASCII)
    print(f"Posición de la 'y': {palabra.index('y')}")

if __name__ == "__main__":
    naturaleza_de_las_cadenas()
