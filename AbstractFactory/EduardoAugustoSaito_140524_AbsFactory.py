from abc import ABC, abstractmethod

class Ponto:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Ponto({self.x}, {self.y})"

class Circulo:
    def __init__(self, ponto: Ponto, raio: int):
        self.ponto = ponto
        self.raio = raio

    def __repr__(self) -> str:
        return f"Circulo(Ponto={self.ponto}, Raio={self.raio})"

class Retangulo:
    def __init__(self, ponto1: Ponto, ponto2: Ponto):
        self.ponto1 = ponto1
        self.ponto2 = ponto2

    def __repr__(self) -> str:
        return f"Retangulo(Ponto1={self.ponto1}, Ponto2={self.ponto2})"

class Triangulo:
    def __init__(self, ponto1: Ponto, ponto2: Ponto, ponto3: Ponto):
        self.ponto1 = ponto1
        self.ponto2 = ponto2
        self.ponto3 = ponto3

    def __repr__(self) -> str:
        return f"Triangulo(Ponto1={self.ponto1}, Ponto2={self.ponto2}, Ponto3={self.ponto3})"

class FormaFactory(ABC):
    @abstractmethod
    def criar_ponto(self, x: int, y: int) -> Ponto:
        pass

    @abstractmethod
    def criar_circulo(self, ponto: Ponto, raio: int) -> Circulo:
        pass

    @abstractmethod
    def criar_retangulo(self, ponto1: Ponto, ponto2: Ponto) -> Retangulo:
        pass

    @abstractmethod
    def criar_triangulo(self, ponto1: Ponto, ponto2: Ponto, ponto3: Ponto) -> Triangulo:
        pass

class FormaGeometricaFactory(FormaFactory):
    def criar_ponto(self, x: int, y: int) -> Ponto:
        return Ponto(x, y)

    def criar_circulo(self, ponto: Ponto, raio: int) -> Circulo:
        return Circulo(ponto, raio)

    def criar_retangulo(self, ponto1: Ponto, ponto2: Ponto) -> Retangulo:
        return Retangulo(ponto1, ponto2)

    def criar_triangulo(self, ponto1: Ponto, ponto2: Ponto, ponto3: Ponto) -> Triangulo:
        return Triangulo(ponto1, ponto2, ponto3)

def main() -> None:
    fabrica = FormaGeometricaFactory()

    # Criando objetos através do factory
    p1 = fabrica.criar_ponto(1, 2)
    p2 = fabrica.criar_ponto(3, 4)
    p3 = fabrica.criar_ponto(5, 6)

    circulo = fabrica.criar_circulo(p1, 10)
    retangulo = fabrica.criar_retangulo(p1, p2)
    triangulo = fabrica.criar_triangulo(p1, p2, p3)

    print(p1)
    print(circulo)
    print(retangulo)
    print(triangulo)

if __name__ == "__main__":
    main()
