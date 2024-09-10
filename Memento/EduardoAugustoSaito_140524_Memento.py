from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    @abstractmethod
    def update(self, observer) -> None:
        pass


class PCDObservable(ABC):
    @abstractmethod
    def add(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def remove(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Memento:
    def __init__(self, estado: float) -> None:
        self._estado: float = estado

    def __repr__(self) -> str:
        return f"Temperatura: {self._estado} ºC"

    def getEstado(self) -> float:
        return self._estado

    def setEstado(self, estado: float) -> None:
        self._estado = estado


class PCDConcreteObservable(PCDObservable):
    def __init__(self, observers: List[Observer], estados: List[Memento]) -> None:
        self._observers: List[Observer] = observers
        self._estados: List[Memento] = estados
        self._data = {}

    def add(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)
        else:
            print("Este observer não foi encontrado!")

    def notify(self) -> None:
        if len(self._observers) > 0:
            for obs in self._observers:
                obs.update(self)
        else:
            print("Nenhum Observer para a ser notificado!")

    def setData(self, data) -> None:
        if self._data != data:
            self._data = data
            self.notify()
        else:
            print("Não houve alteração nos dados!")

    def getData(self):
        return self._data

    def criarMemento(self, temp: float) -> None:
        if len(self._estados) < 3:
            self._estados.append(Memento(temp))
        else:
            self._estados.pop(0)
            print(self._estados)
            self._estados.append(Memento(temp))

    def setMemento(self, memento: Memento) -> None:
        if len(self._estados) > 0:
            self._estados[-1] = memento
        else:
            print("Nenhum dado para alterar!")

    def getEstados(self) -> List[Memento]:
        return self._estados


class UniversidadeObserver(Observer):
    data = {}

    def __init__(self, nome: str) -> None:
        self._nome = nome

    def update(self, observer: Observer) -> None:
        self.data = observer.getData()


def main() -> None:
    '''
        Eduardo Augusto Saito
        RA: 140524
    '''

    unifesp = UniversidadeObserver(nome="unifesp")
    ufmg = UniversidadeObserver(nome="ufmg")
    ufrj = UniversidadeObserver(nome="ufrj")

    print(f"Data UNIFESP: {unifesp.data}")
    print(f"Data UFMG: {ufmg.data}")
    print(f"Data UFRJ: {ufrj.data}")

    pcd = PCDConcreteObservable(estados=[], observers=[])
    # Apenas Unifesp e UFRJ serão notificadas
    pcd.add(unifesp)
    pcd.add(ufrj)

    weather_data = {'pressao': 1.0, 'temperatura': 26.0, 'ph': 7.0}
    pcd.setData(weather_data)
    pcd.criarMemento(weather_data['temperatura'])
    print("\nMemento: ", pcd.getEstados())

    weather_data['temperatura'] = 18.0
    pcd.setData(weather_data)
    pcd.criarMemento(weather_data['temperatura'])
    print("\nMemento: ", pcd.getEstados())

    weather_data['temperatura'] = 24.0
    pcd.setData(weather_data)
    pcd.criarMemento(weather_data['temperatura'])
    print("\nMemento: ", pcd.getEstados())

    # Como máximo é 3, ele move os itens para a esquerda e atualiza o último
    weather_data['temperatura'] = 10.0
    pcd.setData(weather_data)
    pcd.criarMemento(weather_data['temperatura'])
    print("\nMemento: ", pcd.getEstados())

    print(f"Data UNIFESP: {unifesp.data}")
    # Printa vazio pois ela não foi add a lista de observers
    print(f"Data UFMG: {ufmg.data}")
    print(f"Data UFRJ: {ufrj.data}")

    return


if __name__ == '__main__':
    main()
