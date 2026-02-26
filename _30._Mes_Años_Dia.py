def es_bisiesto(año):
    """Paso 1: Determinar si el año es bisiesto."""
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def dias_en_mes(año, mes):
    """Paso 2: Obtener cuántos días tiene un mes específico."""
    if año < 1 or mes < 1 or mes > 12:
        return None
    
    meses_dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if mes == 2 and es_bisiesto(año):
        return 29
    
    return meses_dias[mes - 1]

def dia_del_año(año, mes, día):
    """Paso 3: Calcular el número de día del año (1-366)."""
    # 1. Validar que el año y mes sean correctos mediante la función anterior
    limite_dias = dias_en_mes(año, mes)
    
    # 2. Si dias_en_mes devolvió None o el día es inválido para ese mes
    if limite_dias is None or día < 1 or día > limite_dias:
        return None
    
    # 3. Sumar los días de los meses anteriores
    contador_dias = 0
    for m in range(1, mes):
        contador_dias += dias_en_mes(año, m)
    
    # 4. Sumar los días del mes actual
    contador_dias += día
    
    return contador_dias

# --- PRUEBAS DEL SISTEMA ---
print("Probando función dia_del_año:")
print("-" * 50)

# Casos: (Año, Mes, Día, Resultado Esperado)
test_cases = [
    (2024, 1, 1, 1),       # Primer día del año bisiesto
    (2024, 12, 31, 366),   # Último día del año bisiesto
    (2023, 12, 31, 365),   # Último día de año normal
    (2024, 2, 29, 60),     # Día bisiesto
    (2023, 2, 29, None),   # Error: 2023 no tiene 29 de feb
    (2024, 13, 1, None),   # Error: Mes inexistente
    (2024, 5, 32, None)    # Error: Día inexistente en Mayo
]

for a, m, d, esperado in test_cases:
    resultado = dia_del_año(a, m, d)
    status = "OK" if resultado == esperado else "FALLÓ"
    print(f"Fecha: {d:02}/{m:02}/{a} -> Calculado: {str(resultado):4} | Esperado: {str(esperado):4} | {status}")

print("-" * 50)
