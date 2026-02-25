#Solicitar numero
c0 = int(input("Introduce  número entero no negativo y no nulo: "))
i = 1
#Mientras c0 sea diferente de 1
while c0 != 1:
    #Si es par
    if c0 % 2 == 0:
        c0 = c0/2
        print("Numero actual: ", c0)
    #Si no es par
    else:
        c0 = (3 * c0)+1
        print("Numero actual: ", c0)
    i += 1

print("Pasos utilizados: ", i)
