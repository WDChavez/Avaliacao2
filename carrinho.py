'''2 - Desenvolva um programa em Python utilizando orientação a objetos para simular o funcionamento de um
carrinho de compras.
Crie uma classe chamada Produto, com atributos privados __nome, __preco __descrição e __quantidade, e
implemente métodos públicos para acessar e modificar esses dados de forma segura (getters e setters).
Em seguida, implemente a classe CarrinhoDeCompras, que armazena uma lista de objetos Produto e oferece
funcionalidades para adicionar produtos, remover produtos pelo nome, calcular o valor total da compra e
exibir os itens do carrinho com suas respectivas informações.
O programa principal deve apresentar um menu interativo no console, permitindo ao usuário realizar
operações como incluir e excluir produtos, visualizar o conteúdo do carrinho e consultar o total da compra.
Utilize boas práticas de encapsulamento e organização orientada a objetos para garantir a integridade dos
dados'''

class Produto:
    def __init__(self, nome, preco, descricao, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__descricao = descricao
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_descricao(self):
        return self.__descricao

    def get_quantidade(self):
        return self.__quantidade

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
            print("Novo preço adicionado!")
        else:
            print("Novo preço não adicionado!")

    def set_descricao(self, nova_descricao):
        self.__descricao = nova_descricao

    def set_quantidade(self, nova_quantidade):
        if nova_quantidade > 0:
            self.__quantidade = nova_quantidade
            print("Quantidade adicionada!")
        else:
            print("Quantidade não adicionada!")


class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = []

    def adicionar_produto(self, produto):
        self.__produtos.append(produto)
        print("Produto adicionado ao carrinho!")

    def remover_produto(self, nome):
        for produto in self.__produtos:
            if produto.get_nome().lower() == nome.lower():
                self.__produtos.remove(produto)
                print("Produto removido do carrinho!")
                return

        print("Produto não encontrado!")

    def calcular_total(self):
        total = 0

        for produto in self.__produtos:
            total += produto.get_preco() * produto.get_quantidade()

        return total

    def listar_produtos(self):
        if len(self.__produtos) == 0:
            print("O carrinho está vazio!")
            return

        print("\n--- PRODUTOS NO CARRINHO ---")

        for produto in self.__produtos:
            print(f"Produto: {produto.get_nome()}")
            print(f"Preço: R$ {produto.get_preco():.2f}")
            print(f"Descrição: {produto.get_descricao()}")
            print(f"Quantidade: {produto.get_quantidade()}")
            print("----------------------------")


carrinho = CarrinhoDeCompras()

while True:
    print("\n===== CARRINHO DE COMPRAS =====")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Listar produtos")
    print("4 - Ver total")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        descricao = input("Descrição do produto: ")

        try:
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade: "))

            produto = Produto(nome, preco, descricao, quantidade)

            carrinho.adicionar_produto(produto)

        except ValueError:
            print("Digite valores válidos para preço e quantidade.")

    elif opcao == "2":
        nome = input("Digite o nome do produto que deseja remover: ")
        carrinho.remover_produto(nome)

    elif opcao == "3":
        carrinho.listar_produtos()

    elif opcao == "4":
        total = carrinho.calcular_total()
        print(f"\nTotal da compra: R$ {total:.2f}")

    elif opcao == "5":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")