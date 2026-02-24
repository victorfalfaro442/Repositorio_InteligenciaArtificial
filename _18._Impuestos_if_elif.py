#Solicitar el ingreso de táleros
ingreso = float(input("Ingresa el número de táleros anuales: "))

#Comparar con los umbrales
if ingreso < 85528:
    imp = (ingreso * 0.18) - 556.02
elif ingreso > 85528:
    imp = 14839.02+(0.32*82528)

#Redondear e imprimir
imp = round(imp, 0)
print("Los impuestos a pagar son:", imp, "táleros")
