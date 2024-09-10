from abc import ABC, abstractmethod

# Componente
class Participante(ABC):
    @abstractmethod
    def getDados(self):
        pass

# Folha
class Individuo(Participante):
    def __init__(self, nome: str, assento: str) -> None:
        self.__nome = nome
        self.__assento = assento

    def getDados(self):
        print(f"Indivíduo - Nome: {self.__nome} | Assento: {self.__assento}")

    def getAssento(self) -> str:
        return self.__assento

# Folha
class Instituicao(Participante):
    def __init__(self, nome: str, num_membros: int):
        self.__nome = nome
        self.__num_membros = num_membros

    def getDados(self):
        print(f"Instituição - Nome: {self.__nome} | Número de Membros: {self.__num_membros}")

    def getMembros(self) -> int:
        return self.__num_membros

# Composite
class Congresso(Participante):
    def __init__(self, inscritos=[]) -> None:
        self.__inscritos = inscritos

    def getDados(self):
        for inscrito in self.__inscritos:
            inscrito.getDados()

    def add(self, inscrito) -> None:
        self.__inscritos.append(inscrito)

    def totalParticipantes(self) -> int:
        return len(self.__inscritos)

    def totalAssentos(self) -> int:
        total = 0
        for inscrito in self.__inscritos:
            if isinstance(inscrito, Individuo): total += 1
            else: total += inscrito.getMembros()
        return total

def main() -> None:
    '''
        Eduardo Augusto Saito
        RA: 140524
    '''

    congresso = Congresso()

    instituicao_1 = Instituicao("UNIFESP", 50)
    instituicao_2 = Instituicao("USP", 25)

    individuo_1 = Individuo("Eduardo", "A1")
    individuo_2 = Individuo("Rogerio", "B6")
    individuo_3 = Individuo("Laura", "D11")

    congresso.add(instituicao_1)
    congresso.add(instituicao_2)
    congresso.add(individuo_1)
    congresso.add(individuo_2)
    congresso.add(individuo_3)

    congresso.getDados()

    print(f"Total de Assentos: {congresso.totalAssentos()}")
    print(f"Total de Participantes: {congresso.totalParticipantes()}") # Individuos + Instituições

    return

if __name__ == "__main__":
    main()