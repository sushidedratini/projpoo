from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator
from typing import Any, List
from dataclasses import dataclass


class Figura(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


@dataclass
class Circulo(Figura):
    raio: float = 0.0

    def area(self) -> float:
        return 3.14 * self.raio * self.raio


@dataclass
class Quadrado(Figura):
    lado: float = 0.0

    def area(self) -> float:
        return self.lado * self.lado


@dataclass
class Retangulo(Figura):
    lado_1: float = 0.0
    lado_2: float = 0.0

    def area(self) -> float:
        return self.lado_1 * self.lado_2


class ListaDeFigurasCollection(Iterable):

    def __init__(self, collection: list[Any] | None = None) -> None:
        self._collection = collection or []

    def __getitem__(self, index: int) -> Any:
        return self._collection[index]

    def __iter__(self) -> Iterator:
        return ListaDeFigurasIterator(self)

    def add_item(self, item: Figura) -> None:
        self._collection.append(item)


class ListaDeFigurasIterator(Iterator):

    _position: int = None

    def __init__(self, collection: ListaDeFigurasCollection) -> None:
        self._collection = collection
        self._position = 0

    def __next__(self) -> Any:
        try:
            value = self._collection[self._position]
            self._position += 1
            return value
        except IndexError as idx_exc:
            print(idx_exc)

    def __has_next__(self) -> Any:
        try:
            value = self._collection[self._position + 1]
            if value:
                return True
        except Exception as idx_exc:
            print(idx_exc)
        return False


def main() -> None:
    circulo = Circulo(raio=10)
    print(circulo.area())

    quadrado = Quadrado(lado=5)
    print(quadrado.area())

    retangulo = Retangulo(lado_1=10, lado_2=5)
    print(retangulo.area())

    collection = ListaDeFigurasCollection()
    collection.add_item(circulo)
    collection.add_item(quadrado)
    collection.add_item(retangulo)

    iterador = ListaDeFigurasIterator(collection)
    print(iterador.__has_next__())
    print(iterador.__next__())
    print(iterador.__next__())
    print(iterador.__next__())
    print(iterador.__next__())



if __name__ == '__main__':
    main()
