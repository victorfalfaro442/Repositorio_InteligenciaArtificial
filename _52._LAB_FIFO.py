class QueueError(IndexError):  # Elegimos IndexError como clase base
    pass


class Queue:
    def __init__(self):
        # Inicializamos el almacenamiento como una lista vacía
        self.__queue = []

    def put(self, elem):
        # Añadimos elementos al INICIO de la lista (índice 0)
        self.__queue.insert(0, elem)

    def get(self):
        # Si la lista está vacía, levantamos nuestra excepción personalizada
        if len(self.__queue) == 0:
            raise QueueError
        
        # Tomamos el elemento del FINAL de la lista
        elem = self.__queue[-1]
        del self.__queue[-1]
        return elem


que = Queue()
que.put(1)
que.put("dog")
que.put(False)

try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")
