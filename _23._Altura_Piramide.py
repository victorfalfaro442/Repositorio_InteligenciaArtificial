#Pedir el número de bloques que se tienen
bloq = int(input("Introduce el número de bloques que tienes: "))
#Numero de bloques necesario para el siguiente nivel
bloq_Siguiente_nivel = 1
#Altura inicial
altura = 0

#Mientras los bloques que tenemos sean mayores o iguales a los necesarios
while bloq >= bloq_Siguiente_nivel:
    #Restar los bloques necesarios a los tenidos
    bloq -= bloq_Siguiente_nivel
    #Subir un nivel
    altura += 1
    #Aumentar los necesarios en 1 
    bloq_Siguiente_nivel += 1

#Imprimir la altura final
print("La altura de la pirámide es:", altura)
    
