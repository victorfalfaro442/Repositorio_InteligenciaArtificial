def calcular_digito_vida():
    # 1. Pedir la fecha al usuario
    fecha = input("Introduce tu fecha de nacimiento (solo números, ej. 20170101): ")

    # 2. Validación básica: que solo sean números
    if not fecha.isdigit():
        print("Error: La entrada debe contener solo dígitos.")
        return

    # 3. Lógica de suma y reducción
    # Primero sumamos todos los dígitos de la entrada inicial
    suma = 0
    for digito in fecha:
        suma += int(digito)

    # 4. Bucle de reducción: mientras la suma tenga más de un dígito
    # Un número tiene más de un dígito si es >= 10
    while suma >= 10:
        aux_suma = 0
        for digito in str(suma):
            aux_suma += int(digito)
        suma = aux_suma

    print(f"Tu Dígito de la Vida es: {suma}")

if __name__ == "__main__":
    calcular_digito_vida()
