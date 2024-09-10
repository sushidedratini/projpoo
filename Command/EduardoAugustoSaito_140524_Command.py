from abc import ABC, abstractmethod

# Classe Pessoa
class Pessoa:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __str__(self):
        return f"Pessoa[ID={self.id}, Nome={self.nome}]"

# Interface Command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Implementação do Banco de Pessoas usando um dicionário
class BancoPessoas:
    def __init__(self):
        self.pessoas = {}

    def add_pessoa(self, pessoa):
        self.pessoas[pessoa.id] = pessoa

    def delete_pessoa(self, id):
        return self.pessoas.pop(id, None)

    def get_pessoa(self, id):
        return self.pessoas.get(id, None)

    def get_all_pessoas(self):
        return list(self.pessoas.values())

# Comando para adicionar uma nova pessoa
class NewCommand(Command):
    def __init__(self, banco, id, nome):
        self.banco = banco
        self.pessoa = Pessoa(id, nome)

    def execute(self):
        self.banco.add_pessoa(self.pessoa)
        return f"Added: {self.pessoa}"

# Comando para deletar uma pessoa
class DeleteCommand(Command):
    def __init__(self, banco, id):
        self.banco = banco
        self.id = id

    def execute(self):
        pessoa = self.banco.delete_pessoa(self.id)
        if pessoa:
            return f"Deleted: {pessoa}"
        return f"No person with ID={self.id} found."

# Comando para obter uma pessoa pelo ID
class GetCommand(Command):
    def __init__(self, banco, id):
        self.banco = banco
        self.id = id

    def execute(self):
        pessoa = self.banco.get_pessoa(self.id)
        if pessoa:
            return str(pessoa)
        return f"No person with ID={self.id} found."

# Comando para listar todas as pessoas
class GetAllCommand(Command):
    def __init__(self, banco):
        self.banco = banco

    def execute(self):
        pessoas = self.banco.get_all_pessoas()
        if pessoas:
            return "\n".join(str(p) for p in pessoas)
        return "No people found."

class CommandManager:
    def __init__(self, banco):
        self.banco = banco
        self.commands = {
            "new": self.new_command,
            "delete": self.delete_command,
            "get": self.get_command,
            "all": self.all_command
        }

    def execute(self, command, *args):
        command_func = self.commands.get(command.lower())
        if command_func:
            return command_func(*args)
        return "Unknown command."

    def new_command(self, id, nome):
        command = NewCommand(self.banco, int(id), nome)
        return command.execute()

    def delete_command(self, id):
        command = DeleteCommand(self.banco, int(id))
        return command.execute()

    def get_command(self, id):
        command = GetCommand(self.banco, int(id))
        return command.execute()

    def all_command(self):
        command = GetAllCommand(self.banco)
        return command.execute()

def main() -> None:
    banco = BancoPessoas()
    command_manager = CommandManager(banco)

    while True:
        input_str = input("BancoPessoas> ").strip()
        if input_str.lower() in {"sair", "quit"}:
            print("Finalizando...")
            break

        parts = input_str.split()
        if not parts:
            continue

        command = parts[0]
        args = parts[1:]
        print(command_manager.execute(command, *args))

if __name__ == "__main__":
    main()