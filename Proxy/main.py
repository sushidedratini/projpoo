from abc import ABC, abstractmethod

class RemoteInterface(ABC):
    @abstractmethod
    def toUpper(self, string: str) -> str:
        pass

class ObjetoRemoto(RemoteInterface):
    def toUpper(self, string: str) -> str:
        return string.capitalize()

# Proxy
class Stub(RemoteInterface):
    def __init__(self, remoto: RemoteInterface) -> None:
        self.remoto = remoto

    def toUpper(self, string: str) -> str:
        return self.remoto.toUpper(string)

# Cliente    
class Cliente():
    def __init__(self, proxy: RemoteInterface) -> None:
        self.proxy = proxy

    def operacao(self, string: str):
        print(self.proxy.toUpper(string))

def main() -> None:

    stub = Stub(remoto=ObjetoRemoto())
    
    cliente = Cliente(proxy=stub)
    cliente.operacao("a")

if __name__ == "__main__":
    main()