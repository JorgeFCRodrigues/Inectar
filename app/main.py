import funcoes

def main():
    print("Executando o programa...")

    lista = funcoes.carregar_lista()
    lista = funcoes.menu(lista)

    print("\nLista final:", lista)

if __name__ == "__main__":
    main()
