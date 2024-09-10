'''
    Eduardo Augusto Saito
    RA: 140524
'''

from typing import List, Optional

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
    def __init__(self, turmas: List[Turma] = []) -> None:
        self.__turmas = turmas

    def matricular(self, codAluno, codCurso: int, escola: Escola, turma=None) -> None:
        if turma is None:
            turma = Turma(curso=escola.getCurso(codCurso=codCurso))
            self.__turmas.append(turma)
        rex = escola.getAluno(codAluno=codAluno)
        turma.addAluno(aluno=rex)
    
    def exibirStatus(self, turma: Turma):
        alunos = turma.getAlunos()
        print(f"Matriculados na turma: {turma}")
        for aluno in alunos: print(f"ALUNO - Nome: {aluno.getNome()} | Matricula: {aluno.getMatricula()}")

    def getTurmas(self):
        if len(self.__turmas) == 0: return None
        else:
            return self.__turmas


def main() -> None:

    print("Eduardo Augusto Saito\nRA: 140524\n")

    #2.2
    # Inicializando
    matematica = Curso(codigo=1, nome="Matemática")
    portugues = Curso(codigo=2, nome="Português")
    historia = Curso(codigo=3, nome="História")

    aluno1 = Aluno(matricula=1, nome="Eduardo")
    aluno2 = Aluno(matricula=2, nome="Ana")
    aluno3 = Aluno(matricula=3, nome="Rogerio")

    escola = Escola(cursos=[matematica, portugues, historia], alunos=[aluno1, aluno2, aluno3])
    
    matricula = MatriculaGUI()
    matricula.matricular(codAluno=1, codCurso=3, escola=escola)

    turmaTeste = matricula.getTurmas()
    print(turmaTeste)

    matricula.matricular(codAluno=2, codCurso=3, escola=escola, turma=turmaTeste[0])
    matricula.matricular(codAluno=3, codCurso=3, escola=escola, turma=turmaTeste[0])

    matricula.exibirStatus(turma=turmaTeste[0])

    # 2.3
    '''
        A diferença de Facade e Adapter é que o Facade cria uma interface fácil de se entender e simples, esta que consegue
        consumir subsistemas ou serviços de forma mais simplificada. No exemplo de hoje, utilizamos a classe "MatriculaGUI" que 
        contém duas funções "simples" (matricular e exibirStatus) que conversam com classes mais específicas, como a Escola, 
        Curso, Turma, Aluno, etc.
        Já o adapter visa adaptar classes já existentes para uma outra interface que será utilizada, como no exemplo do envio
        de mensagem via SMS/Push, utilizando a classe INotificador do exercício anterior, adaptávamos a função de "enviarSMS" ou 
        "enviarPush" para que pudéssemos usar a função "enviar" da interface INotificador.
    '''


if __name__ == "__main__":
    main()