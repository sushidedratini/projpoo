'''
18.1 Escreva um programa que descubra o dia da
semana e, repasse o controle para uma estratégia
específica
• A estratégia deve imprimir uma mensagem
• Para descobrir o dia da semana crie um new
GregorianCalendar() para obter a data corrente e use
get(Calendar.DAY_OF_WEEK) para obter o dia da
semana (de 0 a 6).
• 18.2 Qual a diferença entre Strategy e State?
Como tratar o caso dos estados ou estratégias nulas?
Qual padrão resolve isso?
'''

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date

class DiaSemana(ABC):
    @abstractmethod
    def acao(self) -> None:
        pass

class Inicio(DiaSemana):
    def acao(self) -> None:
        print("Começo da Semana, bora trabalhar!")

class Meio(DiaSemana):
    def acao(self) -> None:
        print("Que isso a semana não acaba nunca!")

class Fim(DiaSemana):
    def acao(self) -> None:
        print("Zzzzzz Zzzzzz Zzzzzz")

# Null Object Design Pattern
class Null(DiaSemana):
    def acao(self) -> None:
        print("Algo deu errado!")

@dataclass
class Calendario():
    dia_da_semana: DiaSemana = None

    def executar(self) -> None:
        hoje = date.today().isoweekday()

        if hoje in (1, 3):
            self.dia_da_semana = Inicio()
            self.dia_da_semana.acao()
        elif hoje in (4, 5):
            self.dia_da_semana = Meio()
            self.dia_da_semana.acao()
        elif hoje in (6, 7):
            self.dia_da_semana = Fim()
            self.dia_da_semana.acao()
        else:
            self.dia_da_semana = Null()
            self.dia_da_semana.acao()

def main() -> None:
    calendario = Calendario()
    calendario.executar()

if __name__ == "__main__":
    main()
