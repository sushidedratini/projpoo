from abc import ABC, abstractmethod


class ClassGeneratorInterface(ABC):
    @abstractmethod
    def get_class_name(self):
        pass

    @abstractmethod
    def get_base_class(self):
        pass

    @abstractmethod
    def get_methods(self):
        pass


class ClassGenerator(ClassGeneratorInterface):
    def get_class_name(self):
        return "MinhaClasse"

    def get_base_class(self):
        return "ClassePai"

    def get_methods(self):
        return [
            {
                "name": "metodo_um",
                "body": ["print('Implementação Método 1')"]
            },
            {
                "name": "metodo_dois",
                "body": ["print('Implementação Método 2')"]
            }
        ]

    def generate_class(self):
        class_name = self.get_class_name()
        base_class = self.get_base_class()
        methods = self.get_methods()

        class_definition = f"class {class_name}({base_class}):\n"
        for method in methods:
            class_definition += f"    def {method['name']}(self):\n"
            for line in method['body']:
                class_definition += f"        {line}\n"
            class_definition += "\n"

        return class_definition


def main() -> None:
    generator = ClassGenerator()
    class_code = generator.generate_class()
    print(class_code)


if __name__ == "__main__":
    main()
