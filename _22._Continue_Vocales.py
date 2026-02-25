#Pedir al usuario que introduzca una palabra
user_word = input("Introduce una palabra: ")

#Convertir la palabra a mayúsculas
user_word = user_word.upper()

#Recorrer la palabra letra por letra
for letter in user_word:
    #Si la letra recorrida es vocal, pasar de largo
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        #Imprime las letras diferentes a vocal
        print(letter)
