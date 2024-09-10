from abc import ABC, abstractmethod

class Reader(ABC):
    @abstractmethod
    def read(self):
        pass

class SimpleReader(Reader):
    def __init__(self, data):
        self._data = data

    def read(self) -> Reader:
        return self._data

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class NullCommand(Command):
    def execute(self) -> str:
        return "Comando Inválido!"

class NewCommand(Command):
    def __init__(self, command_args):
        self.id = command_args[0]
        self.name = command_args[1]

    def execute(self) -> str:
        return f"NewCommand executado com id={self.id} e nome={self.name}"

class DeleteCommand(Command):
    def __init__(self, command_args):
        self.id = command_args[0]

    def execute(self) -> str:
        return f"DeleteCommand executado com id={self.id}"

class GetCommand(Command):
    def __init__(self, command_args):
        self.id = command_args[0]

    def execute(self):
        return f"GetCommand executado com id={self.id}"

class GetAllCommand(Command):
    def execute(self):
        return "GetAllCommand executado"

class ComandoReader(Reader):
    def __init__(self, reader) -> None:
        self._reader = reader

    def read(self) -> Reader:
        return self._reader.read()

    def read_comando(self) -> Command:
        data = self.read().strip()
        parts = data.split()

        if not parts:
            return NullCommand()

        command = parts[0].lower()
        args = parts[1:]

        if command == "new" and len(args) == 2:
            return NewCommand(args)
        elif command == "delete" and len(args) == 1:
            return DeleteCommand(args)
        elif command == "get" and len(args) == 1:
            return GetCommand(args)
        elif command == "all" and len(args) == 0:
            return GetAllCommand()
        else:
            return NullCommand()


def main() -> None:
    reader = SimpleReader("new 123 Eduardo")
    comando_reader = ComandoReader(reader)
    command = comando_reader.read_comando()
    print(command.execute())

    reader = SimpleReader("delete 123")
    comando_reader = ComandoReader(reader)
    command = comando_reader.read_comando()
    print(command.execute())

    reader = SimpleReader("get 123")
    comando_reader = ComandoReader(reader)
    command = comando_reader.read_comando()
    print(command.execute())

    reader = SimpleReader("all")
    comando_reader = ComandoReader(reader)
    command = comando_reader.read_comando()
    print(command.execute())

    reader = SimpleReader("blablabla 123")
    comando_reader = ComandoReader(reader)
    command = comando_reader.read_comando()
    print(command.execute())


if __name__ == '__main__':
    main()
