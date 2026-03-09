def demostracion_caracteres_y_codigos():
    print("--- RESUMEN TÉCNICO: SECCIÓN 2.1 ---")
    
    # 1. ASCII y Unicode: De letra a número (ord) y viceversa (chr)
    caracter = 'A'
    punto_codigo = ord(caracter)
    print(f"\n[ASCII/Unicode] El carácter '{caracter}' tiene el punto de código: {punto_codigo}")
    print(f"[Inverso] El código 65 corresponde a: {chr(65)}")

    # 2. I18N (Internationalization)
    # i + 18 letras + n = Internationalization
    print(f"\n[I18N] Concepto: Diseñar software para adaptarse a múltiples idiomas y regiones.")

    # 3. Unicode y UTF-8 (Codificación)
    emoji = '🐍'
    # UTF-8 es una forma de guardar Unicode usando bytes variables
    print(f"\n[UNICODE] Punto de código del emoji {emoji}: {ord(emoji)}")
    print(f"[UTF-8] Representación en bytes: {emoji.encode('utf-8')}")

if __name__ == "__main__":
    demostracion_caracteres_y_codigos()
