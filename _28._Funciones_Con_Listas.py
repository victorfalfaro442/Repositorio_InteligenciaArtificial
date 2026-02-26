#Solicitar el año como argumento
def es_bisiesto(año):
    # Si no es divisible por 4, no es bisiesto
    if año % 4 != 0:
        return False
    # Si es divisible por 4 pero no por 100, es bisiesto
    elif año % 100 != 0:
        return True
    # Si es divisible por 100, debe serlo por 400 para ser bisiesto
    elif año % 400 == 0:
        return True
    else:
        return False

# Pruebas de escritorio
test_data = [1900, 2000, 2016, 1987, 2024]
test_results = [False, True, True, False, True]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", es_bisiesto(yr))
    
