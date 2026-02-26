# Constantes de conversión
METROS_EN_MILLA = 1609.344
LITROS_EN_GALON = 3.785411784

def liters_100km_to_miles_gallon(litros):
    #Convertir 100 km a millas
    millas_en_100km = 100000 / METROS_EN_MILLA
    #Convertir los litros de entrada a galones
    galones = litros / LITROS_EN_GALON
    #MPG = Millas / Galones
    return millas_en_100km / galones

def miles_gallon_to_liters_100km(millas):
    #Convertir 1 galón a litros
    litros = LITROS_EN_GALON
    #Convertir las millas de entrada a kilómetros
    kilometros = (millas * METROS_EN_MILLA) / 1000
    #L/100km = (Litros / Kilómetros) * 100
    return (litros / kilometros) * 100

# --- Pruebas de verificación ---
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
