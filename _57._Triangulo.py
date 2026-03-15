import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_point(self, point):
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        # Almacenamos los puntos en una lista privada
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        # Calculamos la distancia entre cada par de puntos
        # Lado 1: del Punto 0 al Punto 1
        lado1 = self.__vertices[0].distance_from_point(self.__vertices[1])
        # Lado 2: del Punto 1 al Punto 2
        lado2 = self.__vertices[1].distance_from_point(self.__vertices[2])
        # Lado 3: del Punto 2 al Punto 0 (cerramos el triángulo)
        lado3 = self.__vertices[2].distance_from_point(self.__vertices[0])
        
        return lado1 + lado2 + lado3

# Código de prueba
triangulo = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangulo.perimeter())
