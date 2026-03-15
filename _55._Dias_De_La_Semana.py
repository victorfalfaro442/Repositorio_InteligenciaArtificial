class WeekDayError(Exception):
    pass
	

class Weeker:
    # Propiedad de clase privada con los días permitidos
    __dias = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']

    def __init__(self, dia):
        # Verificamos si el día existe en nuestra lista
        if dia not in self.__dias:
            raise WeekDayError
        # Guardamos el índice del día (privado)
        self.__actual = self.__dias.index(dia)

    def __str__(self):
        # Devolvemos el nombre correspondiente al índice actual
        return self.__dias[self.__actual]

    def add_days(self, n):
        # Sumamos n y usamos módulo 7 para mantenernos en el rango 0-6
        self.__actual = (self.__actual + n) % 7

    def subtract_days(self, n):
        # Restamos n y usamos módulo 7 (Python maneja módulos negativos correctamente)
        self.__actual = (self.__actual - n) % 7


try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday_error = Weeker('Jueves') # Esto debería fallar
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")
