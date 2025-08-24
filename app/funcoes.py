import json
import os

ARQUIVO = "lista_de_itens.json"

def limpar_tela():
    """Limpa o terminal (Windows, Linux ou macOS)."""
    os.system("cls" if os.name == "nt" else "clear")

def carregar_lista():
    # Carrega a lista do Json, se tiver uma
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return [] # se não tiver uma lista, começa vazia

def salvar_lista(lista):
    # Salva a lista em um Json
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)
 
# --- Ações do menu ---

def adicionar(lista):
    titulo = input("Digite o título do item: ")
    categoria = input("Digite a categoria (ou outro campo extra): ")
    item = {"titulo": titulo, "categoria": categoria}

    lista.append(item)
    salvar_lista(lista)
    print(f"Item '{titulo}' adicionado com sucesso!")

def editar(lista):
    if not lista:
        print("A lista está vazia!")
        return

    listar(lista)
    entrada = input("Digite o número do item que deseja editar: ")

    if entrada.isdigit():
        indice = int(entrada)
        if 1 <= indice <= len(lista): # Uso de comparação encadeada (o E lógico)
            item = lista[indice - 1]
            print(f"Editando: {item}")
            
            novo_titulo = input("Novo título (ou deixe em branco para manter): ")
            nova_categoria = input("Nova categoria (ou deixe em branco para manter): ")

            if novo_titulo:
                item["titulo"] = novo_titulo
            if nova_categoria:
                item["categoria"] = nova_categoria

            salvar_lista(lista)
            print("Item atualizado com sucesso!")
        else:
            print("Número inválido!")
    else:
        print("Digite apenas o número do item.")

def remover(lista):
    if not lista:
        print("A lista está vazia!")
        return

    listar(lista)
    entrada = input("Digite o número ou o nome do item a remover: ")

    # Se for número, tenta converter e remover pelo índice
    if entrada.isdigit():
        indice = int(entrada)
        if 1 <= indice <= len(lista): # Uso de comparação encadeada (o E lógico)
            item = lista.pop(indice - 1)
            salvar_lista(lista)
            print(f"Item '{item['titulo']}' removido da lista!")
        else:
            print("Número inválido!")
    else:
        # Caso contrário, tenta remover pelo nome
        for item in lista:
            if item["titulo"].lower() == entrada.lower():
                lista.remove(item)
                salvar_lista(lista)
                print(f"Item '{entrada}' removido da lista!")
                return
        print("Item não encontrado!")

def listar(lista):
    if not lista:
        print("Nenhum item na lista.")
        return
    
    print("Itens na lista:")
    for i, item in enumerate(lista, start=1):
        print(f"{i}. {item['titulo']} ({item['categoria']})")

def sair(lista):
    print("Saindo do menu...")
    return False # Uso do falso para sair do loop

# --- Menu Principal ---

def menu(lista):
    opcoes = {
        "a": adicionar,
        "e": editar,
        "r": remover,
        "l": listar,
        "s": sair
    }

    while True:
        limpar_tela()
        print("\nItens Favoritos.\n" \
        "[A]dicionar\n" \
        "[E]ditar\n" \
        "[R]emover\n" \
        "[L]istar\n" \
        "[S]air")

        opcao = input("Digite uma das opções: ").lower()

        acao = opcoes.get(opcao) # pega a função do dicionário
        if acao:
            if acao == sair:
                acao(lista) # executa a função SAIR
                break
            else:
                limpar_tela()
                acao(lista) # executa as funções ADICIONAR, EDITAR, REMOVER ou LISTAR
            input("\nPressione ENTER para continuar...")  # pausa antes de voltar ao menu
        else:
            print("Opção inválida, tente novamente.")
            input("Pressione ENTER para continuar...")

    return lista