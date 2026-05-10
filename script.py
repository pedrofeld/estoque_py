# Produtos mockados para nao precisar criar BD e sistema de cadastro
produtos = [
    {"idProduto": 1, "nomeProduto": "Barra de chocolate", "qtdProdutoEstoque": 100},
    {"idProduto": 2, "nomeProduto": "Farinha", "qtdProdutoEstoque": 50},
    {"idProduto": 3, "nomeProduto": "Agua mineral", "qtdProdutoEstoque": 250}
]

# Historico de movimentacoes, para fins de auditoria
movimentacoes = []

# Buscar um produto por id ou nome
def buscarProduto(nomeOuIdProduto):

    for produto in produtos:

        if isinstance(nomeOuIdProduto, int):
            if produto["idProduto"] == nomeOuIdProduto:
                return produto

        elif isinstance(nomeOuIdProduto, str):
            if produto["nomeProduto"] == nomeOuIdProduto:
                return produto

    return None


# Adicionar produtos ao estoque
# Adicionar produtos ao estoque
def entradaDeProduto(nomeOuIdProduto, quantidade, data):

    produto = buscarProduto(nomeOuIdProduto)

    if produto:

        estoqueAntes = produto["qtdProdutoEstoque"]
        estoqueDepois = estoqueAntes + quantidade

        print(f"\nVoce esta tentando adicionar {quantidade} de {produto['nomeProduto']}")
        print(f"Estoque antes: {estoqueAntes}")
        print(f"Estoque depois: {estoqueDepois}")

        produto["qtdProdutoEstoque"] = estoqueDepois

        movimentacoes.append({
            "tipo": "Entrada",
            "produto": produto["nomeProduto"],
            "quantidadeMovimentada": quantidade,
            "estoqueAntes": estoqueAntes,
            "estoqueDepois": estoqueDepois,
            "data": data
        })

        print("Entrada realizada.")

    else:
        print("Produto não encontrado.")


# Retirar produtos do estoque
def saidaDeProduto(nomeOuIdProduto, quantidade, data, responsavel):

    produto = buscarProduto(nomeOuIdProduto)

    if produto:

        print(f"\nVoce esta tentando retirar {quantidade} de {produto['nomeProduto']}")

        if produto["qtdProdutoEstoque"] >= quantidade:

            estoqueAntes = produto["qtdProdutoEstoque"]
            estoqueDepois = estoqueAntes - quantidade

            print(f"Estoque antes: {estoqueAntes}")
            print(f"Estoque depois: {estoqueDepois}")

            produto["qtdProdutoEstoque"] = estoqueDepois

            movimentacoes.append({
                "tipo": "Saída",
                "produto": produto["nomeProduto"],
                "quantidadeMovimentada": quantidade,
                "estoqueAntes": estoqueAntes,
                "estoqueDepois": estoqueDepois,
                "data": data,
                "responsavel": responsavel
            })

            print("Saída realizada.")

        else:
            print("Quantidade insuficiente em estoque.")

    else:
        print("Produto não encontrado.")


# Consultar o estoque atual
def consultarEstoque():

    print("\nESTOQUE ATUAL:")

    for produto in produtos:
        print(f'ID: {produto["idProduto"]}, Produto: {produto["nomeProduto"]}, Quantidade: {produto["qtdProdutoEstoque"]}')


# Consultar o histórico de movimentações
def consultarMovimentacoes():

    print("\nHISTÓRICO DE MOVIMENTAÇÕES:")

    for movimentacao in movimentacoes:

        print(f'''Tipo: {movimentacao["tipo"]}
            Produto: {movimentacao["produto"]}
            Quantidade antes: {movimentacao["estoqueAntes"]}
            Quantidade depois: {movimentacao["estoqueDepois"]}
            Data: {movimentacao["data"]}
            Responsável: {movimentacao.get("responsavel", "N/A")}
            ''')


# MENU PRINCIPAL
while True:

    print("""
======== MENU ========

1 - Consultar estoque
2 - Registrar entrada
3 - Registrar saida
4 - Consultar movimentacoes
0 - Sair

======================
""")

    opcao = input("Escolha uma opcao: ")

    # CONSULTAR ESTOQUE
    if opcao == "1":
        consultarEstoque()

    # ENTRADA
    elif opcao == "2":

        produto = input("Digite o ID ou o nome do produto: ")

        if produto.isdigit():
            produto = int(produto)

        quantidade = int(input("Digite a quantidade: "))
        data = input("Digite a data: ")

        entradaDeProduto(produto, quantidade, data)

    # SAIDA
    elif opcao == "3":

        produto = input("Digite o ID ou o nome do produto: ")

        if produto.isdigit():
            produto = int(produto)

        quantidade = int(input("Digite a quantidade: "))
        data = input("Digite a data: ")
        responsavel = input("Digite o responsavel: ")

        saidaDeProduto(produto, quantidade, data, responsavel)

    # MOVIMENTACOES
    elif opcao == "4":
        consultarMovimentacoes()

    # SAIR
    elif opcao == "0":
        print("Encerrando sistema...")
        break

    # ERRO
    else:
        print("Opcao invalida.")