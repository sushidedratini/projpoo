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

class PCDConcreteObservable(PCDObservable):
    def __init__(self, observers: List[Observer] = []) -> None:
        self._observers = observers
        self._data = {}

    def add(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)
        else: print("Este observer não foi encontrado!")
    
    def notify(self) -> None:
        if len(self._observers) > 0:
            for obs in self._observers:
                obs.update(self)
        else: print("Nenhum Observer para a ser notificado!")

    def setData(self, data) -> None:
        if self._data != data:
            self._data = data
            self.notify()
        else: print("Não houve alteração nos dados!")

    def getData(self):
        return self._data

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

    pcd = PCDConcreteObservable()
    pcd.add(unifesp)
    pcd.add(ufrj)
    pcd.setData({'pressao': 1.0, 'temperatura': 26.0, 'ph': 7.0})

    print(f"Data UNIFESP: {unifesp.data}")
    print(f"Data UFMG: {ufmg.data}")
    print(f"Data UFRJ: {ufrj.data}")

    return

if __name__ == '__main__':
    main()