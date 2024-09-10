from abc import ABC, abstractmethod
from typing import List, Dict

# Componente
class Publicacao(ABC):
    @abstractmethod
    def toString(self):
        pass

# Folha
class Artigo(Publicacao):
    def __init__(self, nome: str, autores: List[str]) -> None:
        self.__nome = nome
        self.__autores = autores

    def toString(self) -> None:
        authors = ", ".join(self.__autores)
        print(f"ARTIGO: {self.__nome} | Autor(es): {authors}")
        return

# Composite
class Colecao(Publicacao):
    def __init__(self, nome: str, publicacoes: List[Publicacao]) -> None:
        self.__nome = nome
        self.__publicacoes = publicacoes

    def getPublicacoes(self) -> List[Publicacao]:
        return self.__publicacoes

    def addPublicacao(self, publicacao: Publicacao) -> None:
        self.__publicacoes.append(publicacao)

    def countPublicacoes(self) -> Dict:
        dict_publicacoes = {"artigos": 0, "publicacoes": 0}
        for publicacao in self.__publicacoes:
            if isinstance(publicacao, Artigo):
                dict_publicacoes["artigos"] += 1
            elif isinstance(publicacao, Colecao):
                dict_publicacoes["publicacoes"] += 1
                dict_recursion = publicacao.countPublicacoes() # Recursão para calcular o número de publ/art dos filhos
                dict_publicacoes = {key: dict_publicacoes[key] + dict_recursion[key] for key in dict_publicacoes}
        return dict_publicacoes
    
    def toString(self) -> None:
        print(f"Nome: {self.__nome}")
        for publicacao in self.__publicacoes:
            publicacao.toString()

def main() -> None:

    # Cliente
    artigo_1 = Artigo(nome="Artigo Unifesp 1", autores=["Fabio", "Taciana", "Zelanis"])
    artigo_2 = Artigo(nome="Artigo Unifesp 2", autores=["Fabio", "Iraci", "Cappabianco"])
    artigo_3 = Artigo(nome="Artigo Unifesp 3", autores=["Vanessa", "Raquel", "Zelanis"])

    revista = Colecao(nome="National Geographic", publicacoes=[artigo_3])
    caderno = Colecao(nome="Tilibra", publicacoes=[artigo_2, revista])
    jornal = Colecao(nome="OVALE", publicacoes=[artigo_1, caderno])
    jornal.toString()
    
    colecao = Colecao(nome="As Melhores de SJC", publicacoes=[])
    colecao.addPublicacao(jornal)
    colecao.toString()
    dict_colecao = colecao.countPublicacoes()
    num_publicacoes = dict_colecao["publicacoes"]
    num_artigos = dict_colecao["artigos"]
    print(f"Número de Publicações: {num_publicacoes} | Número de Artigos: {num_artigos}")

if __name__ == "__main__":
    main()