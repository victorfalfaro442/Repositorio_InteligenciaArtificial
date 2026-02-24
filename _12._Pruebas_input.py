#anything = input("Tell me anything...")
#print("Hmm...", anything, "...Really?\n")

#Prueba con valores enteros
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

#Prueba con valores enteros negativos
anything = float(input("Enter a number: "))
something = (-anything) ** 2.0
print(anything, "to the power of 2 is", something)
print()

#Cálculo de la hipotenusa
#El programa no reacciona al error de introducir negativos
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)
print()

#utilizar + como concatenador
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

#Prueba de utilización * con strings
print(" " * 4 + "*")
print(" " * 3 + "*" * 3)
print(" " * 2 + "*" * 5)
print(" " * 1 + "*" * 7)
print("*" * 9)

