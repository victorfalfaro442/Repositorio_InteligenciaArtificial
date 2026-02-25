#solicitar el número del usuario
numero_adivina = int(input("Introduzca el número que cree que ha elegido el mago: "))

#Establecer el numero secreto del mago
numero_secreto = 10

#Si el número no es igual a numero_secreto imprimir mensaje y solicitar otro numero

while numero_adivina != numero_secreto:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")

    numero_adivina = int(input("Introduzca el número que cree que ha elegido el mago: "))

print("¡Bien hecho, muggle! Ahora eres libre.")
