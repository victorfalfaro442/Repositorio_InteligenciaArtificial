def es_bisiesto(año):
    #Devuelve True si el año es bisiesto, False si no lo es.
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    return False

def dias_en_mes(año, mes):
    #Devuelve el número de días para un mes y año dados. Retorna None si los datos son inválidos.
    if año < 1 or mes < 1 or mes > 12:
        return None
    
    # Lista de días por mes (Enero es índice 0)
    #           Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic
    meses_dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Si es febrero y el año es bisiesto, cambiamos 28 por 29
    if mes == 2 and es_bisiesto(año):
        return 29
    
    return meses_dias[mes - 1]

# --- SECCIÓN DE PRUEBAS ---
test_años = [1900, 2000, 2016, 1987, 2024, 2022, 2024]
test_meses = [2, 2, 1, 11, 2, 13, -1]
test_resultados = [28, 29, 31, 30, 29, None, None]

print("Verificando resultados...")
print("-" * 40)

for i in range(len(test_años)):
    a = test_años[i]
    m = test_meses[i]
    resultado_real = dias_en_mes(a, m)
    
    print(f"Año: {a} | Mes: {m:2} | Resultado esperado: {str(test_resultados[i]):4} | Obtenido: {str(resultado_real):4}", end=" -> ")
    
    if resultado_real == test_resultados[i]:
        print("PASÓ")
    else:
        print("FALLÓ")

print("-" * 40)
print("Prueba finalizada.")
