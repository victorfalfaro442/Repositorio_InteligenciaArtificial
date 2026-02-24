#Declaración de variables
kilometers = 12.25
miles = 7.38

# 1 milla = 1.61 km
#Factor de conversión
converter = 1.61

#operaciones de conversión
miles_to_kilometers = miles*converter
kilometers_to_miles = kilometers/converter

#Imprimir resultados debidamente señalados
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
print()

#Repetir proceso

pesos = 12.25
euros = 7.38

#1 peso = 0.049 euros
converter_2 = 0.049
 
pesos_to_euros = pesos * converter_2
euros_to_pesos = euros / converter_2

print(pesos, "pesos son", round(pesos_to_euros, 2), "euros")
print(euros, "euros son", round(euros_to_pesos, 2), "pesos")
print()
