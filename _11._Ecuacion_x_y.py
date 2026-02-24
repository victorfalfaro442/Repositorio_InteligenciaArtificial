#primer valor para la primera evaluación
x_0 =  0
x_0 = float(x_0)

#evaluar en la ecuación 
x_0 = (3*(x_0**3))-(2*(x_0**2))+(3*x_0)-1

#asígnar valor a y
y_0 = x_0
y_0 = float(y_0)

#Repetir proceso

x_1 =  1
x_1 = float(x_1)

x_1 = (3*(x_1**3))-(2*(x_1**2))+(3*x_1)-1

y_1 = x_1
y_1 = float(y_1)

x_2 =  -1
x_2 = float(x_2)

x_2 = (3*(x_2**3))-(2*(x_2**2))+(3*x_2)-1

y_2 = x_2
y_2 = float(y_2)

#Imprimir valores obtenidos debidamente señalados
print("El resultado de la ecuación evaluada en x=0 es: ", y_0)
print("\nEl resultado de la ecuación evaluada en x=1 es: ", y_1)
print("\nEl resultado de la ecuación evaluada en x=-1 es: ", y_2)
print()
