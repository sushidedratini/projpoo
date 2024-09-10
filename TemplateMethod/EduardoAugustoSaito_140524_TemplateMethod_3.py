from abc import ABC, abstractmethod
import os


class ClassGeneratorInterface(ABC):
    @abstractmethod
    def get_class_name(self):
        pass

    @abstractmethod
    def get_methods(self):
        pass


class ClassGenerator(ClassGeneratorInterface):

    def __init__(self, name: str, msg: str) -> None:
        self._name = name
        self._msg = msg

    def get_class_name(self):
        return self._name

    def get_methods(self):
        return {
            "name": "printar_mensagem",
            "body": f"print('{self._msg}')"
        }

    def generate_class(self):
        class_name = self.get_class_name()
        method = self.get_methods()

        class_definition = f"class {class_name}():\n"
        class_definition += f"    def {method['name']}(self):\n"
        class_definition += f"        {method['body']}\n"
        class_definition += "\n"

        class_definition += "if __name__ == '__main__':\n"
        class_definition += f"    classe = {self._name}('{self._msg}')\n"
        class_definition += f"    classe.{method['name']}()"

        return class_definition


def main() -> None:
    generator = ClassGenerator("ClasseDoProfFabio", "Teste 123!")
    class_code = generator.generate_class()
    print(class_code)

    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "arquivo.py")

    with open(file_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(class_code)
        txt_file.close()


if __name__ == "__main__":
    main()
