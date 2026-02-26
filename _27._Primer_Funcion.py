#Definicion de la función
def mensaje():
    print("Introduzca el valor deseado: ")
datos = []

#Utilización de la función
for i in range(3):
    mensaje()
    valor = int(input()) # Leer dato
    datos.append(valor) #Introducir a la lista

#Mostrar resultados
print("Los valores introducidos son: ", datos)
