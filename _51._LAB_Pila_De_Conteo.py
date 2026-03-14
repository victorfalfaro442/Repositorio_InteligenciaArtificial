class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        # 1. Invocamos al constructor de la clase padre (Stack)
        Stack.__init__(self)
        # 2. Inicializamos el contador oculto a cero
        self.__counter = 0

    def get_counter(self):
        # 3. Devolvemos el valor del contador
        return self.__counter

    def pop(self):
        # 4. Incrementamos el contador cada vez que se hace un pop
        self.__counter += 1
        # 5. Ejecutamos el método pop original de la clase padre
        return Stack.pop(self)
	

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter()) # Debería imprimir 100
