class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.insert(0, elem)

    def get(self):
        if len(self.__queue) == 0:
            raise QueueError
        elem = self.__queue[-1]
        del self.__queue[-1]
        return elem

    def isempty(self):
        # Retorna True si la longitud es 0, de lo contrario False
        return len(self.__queue) == 0


class SuperQueue(Queue):
    
    pass


que = Queue()
que.put(1)
que.put("dog")
que.put(False)

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
