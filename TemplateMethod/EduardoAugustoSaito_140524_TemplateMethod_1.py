
def comparator(palavras):
    return sorted(palavras, key=lambda palavra: palavra[-1])

def main() -> None:
    # Ordem correta: [ama, fio, ler, luz]
    palavras = ["fio", "luz", "ama", "ler"]
    ordenadas = comparator(palavras)
    print(ordenadas)

if __name__ == "__main__":
    main()
    teste = 1
    teste = None
