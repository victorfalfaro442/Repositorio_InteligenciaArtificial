# Leer los 3 numeros a comparar
number1 = int(input("Introduce el primer numero: "))
number2 = int(input("Introduce el segundo numero: "))
number3 = int(input("Introduce el tercer numero: "))

#Si el primer numero es mas grande que el segundo, comparar con el tercero e imprimir
if number1 > number2:
    if number1 > number3:
        print("El número mas grande es: ", number1)
    else:
        print("El número mas grande es: ", number3)
else:
    if number2 > number3:
        print("El número mas grande es: ", number2)
    else:
        print("El número mas grande es: ", number3)

numero_mayor = max(number1, number2, number3)
print("El número mas grande es: ", numero_mayor)
