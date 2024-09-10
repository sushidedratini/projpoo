from abc import ABC, abstractmethod


class Texto(ABC):
    @abstractmethod
    def get_texto(self) -> str:
        pass


class TextoSimples(Texto):
    def __init__(self, texto):
        self._texto = texto

    def get_texto(self) -> str:
        return self._texto


class TextoDecorator(Texto):
    def __init__(self, texto):
        self._texto = texto

    @abstractmethod
    def get_texto(self) -> str:
        pass


class CaixaAltaDecorator(TextoDecorator):
    def get_texto(self) -> str:
        return self._texto.get_texto().upper()


class InverterDecorator(TextoDecorator):
    def get_texto(self) -> str:
        return self._texto.get_texto()[::-1]


class TagBDecorator(TextoDecorator):
    def get_texto(self) -> str:
        return f"<b>{self._texto.get_texto()}</b>"


def main() -> None:
    # Testando os decoradores individualmente
    texto_simples = TextoSimples("Eduardo Augusto Saito")

    texto_maiusculo = CaixaAltaDecorator(texto_simples)
    texto_invertido = InverterDecorator(texto_simples)
    texto_com_tags = TagBDecorator(texto_simples)

    print(texto_maiusculo.get_texto())
    print(texto_invertido.get_texto())
    print(texto_com_tags.get_texto())

    # Testando os decoradores em cascata
    texto_maiusculo_invertido = CaixaAltaDecorator(
        InverterDecorator(texto_simples))
    texto_maiusculo_com_tags = CaixaAltaDecorator(TagBDecorator(texto_simples))
    texto_invertido_com_tags = InverterDecorator(TagBDecorator(texto_simples))
    texto_completo = CaixaAltaDecorator(
        InverterDecorator(TagBDecorator(texto_simples)))

    print(texto_maiusculo_invertido.get_texto())
    print(texto_maiusculo_com_tags.get_texto())
    print(texto_invertido_com_tags.get_texto())
    print(texto_completo.get_texto())


if __name__ == '__main__':
    main()
