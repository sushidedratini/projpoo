from abc import ABC, abstractmethod
import sys

class Handler(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    @abstractmethod
    def handle(self, text):
        pass

class EspacoHandler(Handler):
    def handle(self, text):
        spaces = text.count(' ')
        print(f"Número de Espaços: {spaces}")
        if self.successor:
            self.successor.handle(text)

class LetraAHandler(Handler):
    def handle(self, text):
        letter_a_count = text.lower().count('a')
        print(f"Número de letras 'a': {letter_a_count}")
        if self.successor:
            self.successor.handle(text)

class PontoHandler(Handler):
    def handle(self, text):
        points = text.count('.')
        print(f"Número de Pontos: {points}")
        if self.successor:
            self.successor.handle(text)

class AnalisadorTexto:
    def __init__(self):
        self.handler_chain = EspacoHandler(LetraAHandler(PontoHandler()))

    def analyze_text(self, text):
        self.handler_chain.handle(text)

def main():
    text = sys.argv[1] # Pega o conteúdo da linha de comando
    analyzer = AnalisadorTexto()
    analyzer.analyze_text(text)

if __name__ == "__main__":
    main()