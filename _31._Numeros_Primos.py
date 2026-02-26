def detect_primo(num):
    if num < 2: return False
    if num == 2: return True  # El 2 es el único par primo
    if num % 2 == 0: return False # Descartamos pares
    
    # Probamos solo impares hasta la raíz cuadrada de num
    limite = int(num**0.5) + 1
    for i in range(3, limite, 2):
        if num % i == 0:
            return False
    return True

#Lista de números a probar
numeros = [3, 5, 15, 5659, 21, 24, 2, 49]

#Recorrer toda la lista
for n in numeros:
    valor = detect_primo(n)

#Si el valor retornado por la función es True, es primo
    if valor == True:
        print("El número es primo: ", valor)
    else:
        print("El número no es primo: ", valor)
