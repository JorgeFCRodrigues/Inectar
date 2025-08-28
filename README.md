# Lista de Itens Favoritos (CLI)

Um pequeno projeto em **Python** que implementa um menu interativo no
terminal para gerenciar uma lista de itens favoritos.\
Os dados são salvos em um arquivo **JSON**, garantindo persistência
entre execuções do programa.

------------------------------------------------------------------------

## 📌 Funcionalidades

-   ➕ **Adicionar** item (com título e categoria)\
-   ✏️ **Editar** item existente\
-   ➖ **Remover** itens existentes (por número ou título)\
-   📋 **Listar** todos os itens salvos\
-   🚪 **Sair** do programa\
-   💾 **Persistência automática** em arquivo `lista_de_itens`

------------------------------------------------------------------------

## 🛠️ Tecnologias utilizadas

-   [Python 3.x](https://www.python.org/)\
-   Manipulação de arquivos JSON para persistência

------------------------------------------------------------------------

## 📂 Estrutura do Projeto

``` bash
.
├── funcoes.py     # Lógica principal (menu e ações)
├── main.py        # Ponto de entrada do programa
├── lista_de_itens     # Arquivo de dados (salva os itens favoritos)
```

------------------------------------------------------------------------

## ▶️ Como executar

1.  Clone o repositório:

    ``` bash
    git clone https://github.com/JorgeFCRodrigues/Inectar.git
    cd Inectar
    cd app
    ```

2.  Execute o programa:

    ``` bash
    python main.py
    ```

------------------------------------------------------------------------

## 💻 Exemplo de uso

``` bash
Executando o programa...

Itens Favoritos
[A]dicionar
[E]ditar
[R]emover
[L]istar
[S]air
Digite uma das opções: a
Digite o título do item: Café
Digite a categoria (ou outro campo extra): Bebida
Item 'Café' adicionado com sucesso!

Itens Favoritos
[A]dicionar
[E]ditar
[R]emover
[L]istar
[S]air
Digite uma das opções: l
Itens na lista:
1. Café (Bebida)

Itens Favoritos
[A]dicionar
[E]ditar
[R]emover
[L]istar
[S]air
Digite uma das opções: e
Digite o número do item que deseja editar: 1
Editando: {'titulo': 'Café', 'categoria': 'Bebida'}
Novo título (ou deixe em branco para manter): Café Expresso
Nova categoria (ou deixe em branco para manter): Bebida Quente
Item atualizado com sucesso!
```

------------------------------------------------------------------------

## 👨‍💻 Autor

Projeto desenvolvido por [Jorge Fernando Cardoso
Rodrigues](https://github.com/JorgeFCRodrigues)
