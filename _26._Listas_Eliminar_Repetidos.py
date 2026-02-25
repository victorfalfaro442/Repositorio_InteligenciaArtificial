#Crear una lsta con elementos repetidos
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9, 10, 111, 111, 10]
#Lista limpia para almacenar los datos
lista_limpia = []

for numero in my_list:
    if numero not in lista_limpia:
        lista_limpia.append(numero)

print("La lista sin valores repetidos es:", lista_limpia)








