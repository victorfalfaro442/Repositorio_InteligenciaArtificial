def demo_excepciones():
    print("--- SECCIÓN 2.7: EXCEPCIONES EN PYTHON ---")
    
    # 1. El bloque Try-Except básico
    try:
        numero = int(input("Introduce un divisor (intenta con 0 o con letras): "))
        resultado = 100 / numero
        print(f"Resultado: {resultado}")
        
    # 2. Capturando excepciones específicas (Orden de importancia)
    except ZeroDivisionError:
        print("Error: No puedes dividir entre cero. (ZeroDivisionError)")
        
    except ValueError:
        print("Error: Debes introducir un número entero, no texto. (ValueError)")
        
    # 3. La excepción genérica (La red de seguridad)
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        
    # 4. El bloque final (Opcional pero importante)
    else:
        print("¡Perfecto! El código se ejecutó sin errores.")
    finally:
        print("Fin del proceso de división.")

if __name__ == "__main__":
    demo_excepciones()
