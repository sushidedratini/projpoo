from typing import List

class Aluno:
    def __init__(self, matricula: str, nome: str) -> None:
        self.__matricula = matricula
        self.__nome = nome

    def getNome(self) -> str:
        return self.__nome
    
    def getMatricula(self) -> str:
        return self.__matricula

class Turma:
    def __init__(self, alunos: List[Aluno] = [], curso = None) -> None:
        self.__alunos = alunos
        self.__curso = curso

    def setCurso(self, curso) -> None:
        self.__curso = curso
    
    def addAluno(self, aluno) -> None:
        self.__alunos.append(aluno)

    def getAlunos(self):
        return self.__alunos

class Curso:
    def __init__(self, codigo: int, nome: str) -> None:
        self.__codigo = codigo
        self.__nome = nome

    def getCodigo(self) -> int:
        return self.__codigo

    def getNome(self) -> str:
        return self.__nome

class Escola:
    def __init__(self, cursos: List[Curso] = [], alunos: List[Aluno] = []) -> None:
        self.__cursos = cursos
        self.__alunos = alunos

    def getCurso(self, codCurso):
        for curso in self.__cursos:
            if curso.getCodigo() == codCurso:
                return curso
        else:
            print("Nenhum curso encontrado com o código informado!")
            return None
        
    def getAluno(self, codAluno):
        for aluno in self.__alunos:
            if aluno.getMatricula() == codAluno:
                return aluno
        else:
            print("Nenhum aluno encontrado com o código informado!")
            return None


class MatriculaGUI:
    _instance = None
    _turmas  = []

    '''
        SINGLETON
        Verifica se uma instância já existe, senão, cria uma nova
    '''
    @classmethod
    def instance(cls, turmas):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        cls._turmas = turmas
        return cls._instance
    
    def matricular(self, codAluno, codCurso: int, escola: Escola, turma=None) -> None:
        if turma is None:
            turma = Turma(curso=escola.getCurso(codCurso=codCurso))
            self._turmas.append(turma)
        rex = escola.getAluno(codAluno=codAluno)
        turma.addAluno(aluno=rex)
    
    def exibirStatus(self, turma: Turma):
        alunos = turma.getAlunos()
        print(f"Matriculados na turma: {turma}")
        for aluno in alunos: print(f"ALUNO - Nome: {aluno.getNome()} | Matricula: {aluno.getMatricula()}")

    def getTurmas(self):
        if len(self._turmas) == 0: return None
        else:
            return self._turmas
    
def main() -> None:
    matricula_gui_1 = MatriculaGUI.instance(turmas=[])
    matricula_gui_2 = MatriculaGUI.instance(turmas=[])

    # Verifica se as instância de GUI criadas são iguais
    if matricula_gui_1 == matricula_gui_2: print("Iguais")

    matematica = Curso(codigo=1, nome="Matemática")
    portugues = Curso(codigo=2, nome="Português")
    historia = Curso(codigo=3, nome="História")

    aluno1 = Aluno(matricula=1, nome="Eduardo")
    aluno2 = Aluno(matricula=2, nome="Ana")
    aluno3 = Aluno(matricula=3, nome="Rogerio")

    escola = Escola(cursos=[matematica, portugues, historia], alunos=[aluno1, aluno2, aluno3])
    
    matricula_gui_1.matricular(codAluno=1, codCurso=3, escola=escola)

    turmaTeste = matricula_gui_1.getTurmas()
    print(turmaTeste)

    matricula_gui_1.matricular(codAluno=2, codCurso=3, escola=escola, turma=turmaTeste[0])
    matricula_gui_1.matricular(codAluno=3, codCurso=3, escola=escola, turma=turmaTeste[0])
    matricula_gui_1.exibirStatus(turma=turmaTeste[0])

    '''
    Ex 5.3

    A classe 'java.lang.Math' parece ser um singleton visto que seu construtor é privado, ou seja, 
    não é possível criar um objeto Math diretamente. Podendo apenas utilizar sua função de 'seed'.
    Não está explícito se ele possui métodos de instance(), mas se possuir, é sim um singleton pois tem
    um construtor privado.

    Não existem informações suficientes de PrinterManager e PrinterSpooler para que possamos identificar
    se são singletons ou não. Mas como PrinterManager é um gerenciador de impressão, pode-se assumir que ele
    possa ser um singleton, visto que ele irá gerenciar outras classes/objetos que atuam em algum tipo de impressão.
    Se ele possuir um construtor privado será um singleton, se não possuir, podem haver outras instâncias dele, portanto
    deixaria de ser um singleton.

    O 'java.lang.System' é uma classe de java que não pode ser instanciada, não possui um construtor privado nem público, 
    portanto não é um singleton.
    '''

    return

if __name__ == "__main__":
    main()