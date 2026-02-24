# Leer el año de interés
año = int(input("Introduce un año: "))

#Establecer las condiciones de los años
if año < 1582:
    print("No va acorde al calendario Georgiano")
else:
    if año % 4 != 0:
        print("Es un año común")
    elif año % 100 != 0:
        print("Es un año bisiesto")
    elif año % 400 != 0:
        print("Es un año común")
    else:
        print("Año bisiesto")
