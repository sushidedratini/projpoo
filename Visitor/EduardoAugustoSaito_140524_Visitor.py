from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_adicao(self, adicao):
        pass

    @abstractmethod
    def visit_multiplicacao(self, multiplicacao):
        pass


class Operacao(ABC):
    @abstractmethod
    def calcular(self) -> int:
        pass

    @abstractmethod
    def imprimir(self) -> str:
        pass

    @abstractmethod
    def aceitar(self, visitor: Visitor):
        pass


class Adicao(Operacao):
    def __init__(self, operando_um: int, operando_dois: int):
        self.operando_um = operando_um
        self.operando_dois = operando_dois

    def calcular(self) -> int:
        return self.operando_um + self.operando_dois

    def imprimir(self) -> str:
        return f"{self.operando_um} + {self.operando_dois}"

    def aceitar(self, visitor: Visitor):
        visitor.visit_adicao(self)


class Multiplicacao(Operacao):
    def __init__(self, operando_um: int, operando_dois: int):
        self.operando_um = operando_um
        self.operando_dois = operando_dois

    def calcular(self) -> int:
        return self.operando_um * self.operando_dois

    def imprimir(self) -> str:
        return f"{self.operando_um} * {self.operando_dois}"

    def aceitar(self, visitor: Visitor):
        visitor.visit_multiplicacao(self)


class ImpressaoVisitor(Visitor):
    def visit_adicao(self, adicao: Adicao) -> None:
        print(f"Imprimindo Adicao: {adicao.imprimir()} = {adicao.calcular()}")

    def visit_multiplicacao(self, multiplicacao: Multiplicacao) -> None:
        print(f"Imprimindo Multiplicacao: {
              multiplicacao.imprimir()} = {multiplicacao.calcular()}")


def main() -> None:
    adicao = Adicao(3, 4)
    multiplicacao = Multiplicacao(5, 6)

    visitor = ImpressaoVisitor()

    adicao.aceitar(visitor)
    multiplicacao.aceitar(visitor)


if __name__ == '__main__':
    main()
