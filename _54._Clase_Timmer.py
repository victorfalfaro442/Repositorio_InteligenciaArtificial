def formatear(val):
    # Función auxiliar para añadir el cero inicial si el valor es < 10
    if val < 10:
        return "0" + str(val)
    return str(val)

class Timer:
    def __init__(self, hora=0, min=0, seg=0):
        # Propiedades privadas con doble guion bajo
        self.__hora = hora
        self.__min = min
        self.__seg = seg

    def __str__(self):
        # Retorna el formato hh:mm:ss usando la función auxiliar
        return formatear(self.__hora) + ":" + \
               formatear(self.__min) + ":" + \
               formatear(self.__seg)

    def next_second(self):
        self.__seg += 1
        if self.__seg > 59:
            self.__seg = 0
            self.__min += 1
            if self.__min > 59:
                self.__min = 0
                self.__hora += 1
                if self.__hora > 23:
                    self.__hora = 0

    def prev_second(self):
        self.__seg -= 1
        if self.__seg < 0:
            self.__seg = 59
            self.__min -= 1
            if self.__min < 0:
                self.__min = 59
                self.__hora -= 1
                if self.__hora < 0:
                    self.__hora = 23

# Código de prueba
timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
