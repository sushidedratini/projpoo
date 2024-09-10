from abc import ABC, abstractmethod
from typing import List


class Mediador(ABC):
    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def notify(self, data):
        pass


class MediadorConcreto(Mediador):
    def __init__(self):
        self.__observers: List[Observer] = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def notify(self, data):
        for observer in self.__observers:
            for key, value in data.items():
                if key in observer.notify_params:
                    observer.update(key, value)


class Observer(ABC):
    @abstractmethod
    def update(self, key, value):
        pass


class Universidade(Observer):
    notify_params = []

    def __init__(self, name: str, notify_params: List[str]):
        self.__name = name
        self.notify_params = notify_params
        self.data = {}

    def getName(self) -> str:
        return self.__name

    def update(self, key: str, value: float):
        if key in self.data:
            if value != self.data[key]:
                self.data[key] = value
        else:
            self.data[key] = value


class Componente(ABC):
    @abstractmethod
    def send(self, data):
        pass

    @abstractmethod
    def receive(self, data):
        pass


class EstacaoClimatica(Componente):
    def __init__(self, data: dict, mediador: Mediador = None):
        self.__mediador = mediador
        self.__data = data

    def send(self, data):
        self.__mediador.notify(data)

    def receive(self, data):
        data_to_send = {}

        for key, value in data.items():
            if self.__data[key] != value:
                self.__data[key] = value
                data_to_send[key] = value
        self.send(data=data_to_send)


def main() -> None:
    '''
        Eduardo Augusto Saito
        RA: 140524
    '''

    unifesp = Universidade(name="UNIFESP", notify_params=[
                           'pressao', 'temperatura'])
    ufmg = Universidade(name="UFMG", notify_params=['temperatura'])
    ufrj = Universidade(name="UFRJ", notify_params=['pressao', 'ph'])

    mediador = MediadorConcreto()
    mediador.add_observer(unifesp)
    mediador.add_observer(ufmg)
    mediador.add_observer(ufrj)

    pcd = EstacaoClimatica(
        data={'ph': None, 'pressao': None, 'temperatura': None}, mediador=mediador)
    pcd.receive(data={'ph': 7.0, 'pressao': 1.0, 'temperatura': 20.0})
    pcd.receive(data={'ph': 7.0, 'pressao': 1.0,
                'temperatura': 20.0})  # Mesmo Valor
    pcd.receive(data={'ph': 8.0, 'pressao': 1.0, 'temperatura': 15.0})

    print(f"Data {unifesp.getName()}: {unifesp.data}")
    print(f"Data {ufmg.getName()}: {ufmg.data}")
    print(f"Data {ufrj.getName()}: {ufrj.data}")

    return


if __name__ == '__main__':
    main()
