from datetime import datetime

# 1. Crear el objeto datetime para la fecha específica
# Año, Mes, Día, Hora, Minuto, Segundo
dt = datetime(2020, 11, 4, 14, 53, 0)

# 2. Imprimir los diferentes formatos usando strftime
print(dt.strftime("%Y/%m/%d %H:%M:%S"))
print(dt.strftime("%y/%B/%d %H:%M:%S %p"))
print(dt.strftime("%a, %Y %b %d"))
print(dt.strftime("%A, %Y %B %d"))
print(dt.strftime("Weekday: %u")) # %u es el día de la semana (1-7)
print(dt.strftime("Day of the year: %j")) # %j es el día del año (001-366)
print(dt.strftime("Week number of the year: %W")) # %W es el número de semana
