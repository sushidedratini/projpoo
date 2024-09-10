from abc import ABC, abstractmethod


class Pessoa():
    __nome: str = None
    __identidade: str = None

    def __init__(self, nome: str, identidade: str) -> None:
        self.__nome = nome
        self.__identidade = identidade

    def __repr__(self) -> str:
        return f"Nome: {self.__nome} | Identidade: {self.__identidade}"


class Empresa():
    __nome: str = None
    __responsavel: Pessoa = None
    __identidade: str = None

    def __init__(self, nome: str, identidade: str) -> None:
        self.__nome = nome
        self.__identidade = identidade

    def set_responsavel(self, responsavel: Pessoa) -> None:
        self.__responsavel = responsavel

    def __repr__(self) -> str:
        return f"Empresa: {self.__nome} | Responsável: '{self.__responsavel}'"


class Construtor(ABC):
    @abstractmethod
    def construir_parte(self, nome: str, identidade: str) -> Pessoa | Empresa:
        pass


class ConstrutorPessoa(Construtor):
    def construir_parte(self, nome: str, identidade: str) -> Pessoa:
        return Pessoa(nome, identidade)


class ConstrutorEmpresa(Construtor):
    def construir_parte(self, nome: str, identidade: str) -> Empresa:
        return Empresa(nome, identidade)


class Diretor():
    __builder_pessoa: Construtor = None
    __builder_empresa: Construtor = None

    def __init__(self, builder_pessoa: Construtor, builder_empresa: Construtor) -> None:
        self.__builder_pessoa = builder_pessoa
        self.__builder_empresa = builder_empresa

    def construir(self, tipo, nome: str, identidade: str) -> None:
        if tipo == "Pessoa":
            pessoa = self.__builder_pessoa.construir_parte(nome, identidade)
            print(pessoa)
        else:
            pessoa = self.__builder_pessoa.construir_parte(nome, identidade)
            empresa = self.__builder_empresa.construir_parte(nome, identidade)
            empresa.set_responsavel(pessoa)

            print(pessoa)
            print(empresa)


def main() -> None:

    construtor_pessoa = ConstrutorPessoa()
    construtor_empresa = ConstrutorEmpresa()

    diretor = Diretor(construtor_pessoa, construtor_empresa)
    diretor.construir("Pessoa", "Wallace", "1234567890")

    diretor = Diretor(construtor_pessoa, construtor_empresa)
    diretor.construir("Empresa", "Wallace", "1234567890")


if __name__ == '__main__':
    main()
