from abc import ABC, abstractmethod
import math


class Figura(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Circulo(Figura):
    def __init__(self, raio) -> None:
        self.raio = raio

    def area(self) -> float:
        return math.pi * (self.raio * self.raio)


class Quadrado(Figura):
    def __init__(self, lado) -> None:
        self.lado = lado

    def area(self) -> float:
        return self.lado * self.lado


class TrEquilatero(Figura):
    def __init__(self, lado) -> None:
        self.lado = lado

    def area(self) -> float:
        return (math.sqrt(3) / 4) * self.lado * self.lado


class CirculoConstructor:
    @staticmethod
    def create(raio) -> Circulo:
        return Circulo(raio)


class QuadradoConstructor:
    @staticmethod
    def create(lado) -> Quadrado:
        return Quadrado(lado)


class TrEquilateroConstructor:
    @staticmethod
    def create(lado) -> TrEquilatero:
        return TrEquilatero(lado)

# Fachada com o HashMap de Construtores


class FiguraFactory:
    _constructors = {
        "circulo": CirculoConstructor,
        "quadrado": QuadradoConstructor,
        "trequilatero": TrEquilateroConstructor
    }

    @staticmethod
    def create_figure(tipo, medida) -> CirculoConstructor | QuadradoConstructor | TrEquilateroConstructor:
        constructor = FiguraFactory._constructors.get(tipo.lower())
        if constructor:
            return constructor.create(medida)
        raise ValueError(f"Tipo de figura '{tipo}' não reconhecido")


def main() -> None:
    figuras = [
        ("circulo", 5),
        ("quadrado", 4),
        ("trequilatero", 3),
        ("paralelepipedo", 4)
    ]

    try:
        for tipo, medida in figuras:
            figura = FiguraFactory.create_figure(tipo, medida)
            print(f"A área do {tipo} com medida {medida} é: {figura.area()}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
