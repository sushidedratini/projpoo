from abc import ABC, abstractmethod

'''
    4.1 - No caso do ex 4.1, deve-se criar um bridge em FIFOQueue, que recebe uma das implementações,
    sendo elas ArrayListQueue ou VectorQueue. Assim, caso 
'''


class List(ABC):
    @abstractmethod
    def add(self, lista, obj, index) -> None:
        pass

    @abstractmethod
    def remove(self, lista, index: int) -> None:
        pass


class ArrayListQueue(List):
    def add(self, lista: list, obj, index: int) -> None:
        if index == -1:
            lista.append(obj)
        else:
            lista.insert(index, obj)

    def remove(self, lista, index: int) -> None:
        lista.pop(index)


class VectorListQueue(List):
    # Default -1 para que seja adicionado no fim da lista
    def add(self, lista: list, obj, index: int = -1) -> None:
        if index == -1:
            lista.append(obj)
        else:
            lista.insert(index, obj)

    def remove(self, lista, index: int) -> None:
        lista.pop(index)


class Queue(ABC):
    @abstractmethod
    def dequeue(self) -> None:
        pass

    @abstractmethod
    def enqueue(self, obj) -> None:
        pass

    @abstractmethod
    def isEmpty(self) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass


class FIFOQueue(Queue):
    def __init__(self, lista: List, fila: list) -> None:
        self.__list = lista
        self.__fila = fila

    def dequeue(self) -> None:
        if len(self.__fila) == 0:
            print("Fila está vazia!")
        else:
            self.__list.remove(self.__fila, 0)

    def enqueue(self, obj) -> None:
        self.__fila.insert(0, obj)

    def isEmpty(self) -> bool:
        return len(self.__fila) == 0

    def size(self) -> int:
        return len(self.__fila)

    def printQueue(self):
        print(self.__fila)


def main() -> None:
    '''
        Eduardo Augusto Saito
        RA: 140524
    '''

    vectorlistqueue = VectorListQueue()

    fifoqueue = FIFOQueue(lista=vectorlistqueue, fila=[])
    fifoqueue.enqueue(1)    # Insere no topo
    fifoqueue.enqueue(2)    # Insere no topo
    fifoqueue.dequeue()     # Remove do topo
    fifoqueue.enqueue(3)    # Insere no topo
    fifoqueue.printQueue()
    print(f"Está vazio: {fifoqueue.isEmpty()}")
    print(f"Tamanho da fila: {fifoqueue.size()}")

    fifoqueue.dequeue()     # Remove do topo
    fifoqueue.dequeue()     # Remove do topo
    fifoqueue.dequeue()     # Remove do topo (fila já está vazia, imprime erro)
    fifoqueue.printQueue()  # Remove do topo
    print(f"Está vazio: {fifoqueue.isEmpty()}")
    print(f"Tamanho da fila: {fifoqueue.size()}")

    arraylistqueue = ArrayListQueue()

    arraylistqueue = FIFOQueue(lista=arraylistqueue, fila=[])
    arraylistqueue.enqueue(1)    # Insere no topo
    arraylistqueue.enqueue(2)    # Insere no topo
    arraylistqueue.dequeue()     # Remove do topo
    arraylistqueue.enqueue(3)    # Insere no topo
    arraylistqueue.printQueue()
    print(f"Está vazio: {arraylistqueue.isEmpty()}")
    print(f"Tamanho da fila: {arraylistqueue.size()}")

    arraylistqueue.dequeue()     # Remove do topo
    arraylistqueue.dequeue()     # Remove do topo
    arraylistqueue.dequeue()     # Remove do topo (fila já está vazia, imprime erro)
    arraylistqueue.printQueue()  # Remove do topo
    print(f"Está vazio: {arraylistqueue.isEmpty()}")
    print(f"Tamanho da fila: {arraylistqueue.size()}")

    return


if __name__ == "__main__":
    main()
