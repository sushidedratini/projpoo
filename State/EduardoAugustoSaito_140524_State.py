# Implementar um Semáforo
from abc import ABC, abstractmethod
from dataclasses import dataclass
from time import sleep

class InterfaceSemaforo(ABC):
    @abstractmethod
    def acao(self) -> str:
        pass

class SemaforoFechado(InterfaceSemaforo):
    def acao(self) -> str:
        print("Não pode passar!")

class SemaforoAtencao(InterfaceSemaforo):
    def acao(self) -> str:
        print("Atenção!")

class SemaforoAberto(InterfaceSemaforo):
    def acao(self) -> str:
        print("Pode passar!")

@dataclass
class Motorista():
    state: InterfaceSemaforo = None

    def __init__(self, state: InterfaceSemaforo) -> None:
        self.state = state

    def acao(self) -> None:
        self.state.acao()

def timer(seconds: int) -> None:
    for i in range(seconds, 0, -1):
        print(f"{i}", end="\r", flush=True)
        sleep(1)

def main() -> None:
    aberto = SemaforoFechado()
    atencao = SemaforoAtencao()
    fechado = SemaforoAberto()

    motorista = Motorista(aberto)
    motorista.acao()

    timer(10)
    motorista.state = atencao
    motorista.acao()

    timer(5)
    motorista.state = fechado
    motorista.acao()

if __name__ == "__main__":
    main()
