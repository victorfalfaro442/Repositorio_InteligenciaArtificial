#Introducir los valores
hour = int(input("Introduzca la hora: "))
mins = int(input("Introduzca los minutos: "))
dura = int(input("¿Cuántos minutos duró el evento? "))

#Sumamos la duración total a los minutos iniciales
total_minutos = mins + dura

#Los minutos finales son el sobrante de dividir entre 60
final_minutos = total_minutos % 60

#Calcular cuántas horas extra se generaron desde los minutos
horas_extra = total_minutos // 60

#Sumar la hora inicial + horas de duración + horas extra de los minutos
#Usar % 24 para que si pasa de medianoche, vuelva a empezar en 0
final_hora = (hour + horas_extra) % 24

print("El evento termina a las:", final_hora, ":", final_minutos)

x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)





