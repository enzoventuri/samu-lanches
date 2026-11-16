
"""Módulo principal do sistema de Lanchonete Delivery."""

from Produto import Produto
from Lanche import Lanche
from Bebida import Bebida
from Sobremesa import Sobremesa


class Lanchonete:
    """Gerencia os produtos cadastrados na lanchonete."""

    def __init__(self):
        """Inicializa a lista de produtos."""
        self.__produtos = []

    def cadastrar_produto(self, produto: Produto):
        """Adiciona um produto à lista."""
        self.__produtos.append(produto)
        print("\nProduto cadastrado com sucesso!")

    def listar_produtos(self):
        """Lista todos os produtos cadastrados."""
        if not self.__produtos:
            print("\nNenhum produto cadastrado.")
            return

        print("\n========== PRODUTOS CADASTRADOS ==========")

        for indice, produto in enumerate(self.__produtos, start=1):
            print(f"\n{indice}. {produto}")

    def buscar_produto(self, nome):
        """Busca produtos pelo nome."""
        encontrados = [
            produto for produto in self.__produtos
            if nome.lower() in produto.nome.lower()
        ]

        if encontrados:
            print("\n========== RESULTADO DA BUSCA ==========")

            for produto in encontrados:
                print(produto)
        else:
            print("\nNenhum produto encontrado.")

    def preparar_produtos(self):
        """Executa a preparação dos produtos utilizando polimorfismo."""
        if not self.__produtos:
            print("\nNenhum produto cadastrado para preparar.")
            return

        print("\n========== PREPARANDO PRODUTOS ==========")

        for produto in self.__produtos:
            print(f"\n{produto.nome}")
            print(produto.preparar())


def limpar_tela():
    """Simula o comando CLS utilizando linhas vazias."""
    for _ in range(30):
        print("")


def pausar():
    """Aguarda o usuário pressionar ENTER."""
    input("\nPressione ENTER para continuar...")


def mostrar_erro(mensagem):
    """Limpa a tela e exibe uma mensagem de erro."""
    limpar_tela()

    print("=" * 45)
    print("                 ERRO")
    print("=" * 45)
    print(f"\n{mensagem}")

    pausar()


def ler_preco():
    """Solicita um preço válido."""
    while True:
        try:
            preco = float(input("Preço (R$): ").replace(",", "."))

            if preco <= 0:
                raise ValueError("O preço precisa ser maior que zero!")

            return preco

        except ValueError as erro:
            mostrar_erro(str(erro))
            return None


def cadastrar_produto(lanchonete):
    """Realiza o cadastro de um produto."""

    print("\n========== CADASTRAR PRODUTO ==========")
    print("1 - Lanche")
    print("2 - Bebida")
    print("3 - Sobremesa")
    print("0 - Voltar")

    tipo = input("\nEscolha o tipo de produto: ").strip()

    # Verifica o tipo antes de solicitar os dados.

    if tipo == "0":
        return

    if tipo not in ("1", "2", "3"):
        mostrar_erro("Opção inválida! Escolha somente 1, 2 ou 3.")
        return

    try:
        print("\n========== DADOS DO PRODUTO ==========")

        nome = input("Nome do produto: ").strip()

        preco = ler_preco()

        if preco is None:
            return

        if tipo == "1":

            print("\n========== CADASTRO DE LANCHE ==========")

            pao = input("Tipo de pão: ").strip()

            ingredientes = input(
                "Ingredientes separados por vírgula: "
            )

            lista_ingredientes = [
                item.strip()
                for item in ingredientes.split(",")
                if item.strip()
            ]

            produto = Lanche(
                nome,
                preco,
                pao,
                lista_ingredientes
            )

        elif tipo == "2":

            print("\n========== CADASTRO DE BEBIDA ==========")

            tamanho = int(input("Volume em ml: "))

            gelada = input(
                "A bebida será servida gelada? (s/n): "
            ).strip().lower()

            if gelada not in ("s", "n"):
                raise ValueError("Digite somente s ou n.")

            produto = Bebida(
                nome,
                preco,
                tamanho,
                gelada == "s"
            )

        elif tipo == "3":

            print("\n========== CADASTRO DE SOBREMESA ==========")

            temperatura = input(
                "Temperatura (Quente ou Gelada): "
            ).strip()

            calorias = int(input("Quantidade de calorias: "))

            produto = Sobremesa(
                nome,
                preco,
                temperatura,
                calorias
            )

        lanchonete.cadastrar_produto(produto)

    except (ValueError, TypeError, AttributeError) as erro:
        mostrar_erro(str(erro))
        return


def exibir_menu():
    """Exibe o menu principal."""

    print("=" * 45)
    print("       SISTEMA LANCHONETE DELIVERY")
    print("=" * 45)
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Preparar produtos (Polimorfismo)")
    print("0 - Sair")
    print("=" * 45)


def main():
    """Executa o programa principal."""

    lanchonete = Lanchonete()

    while True:

        limpar_tela()
        exibir_menu()

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":

            cadastrar_produto(lanchonete)

            # Se o cadastro não gerou erro, mostra a pausa.
            # Em caso de erro, mostrar_erro já fez a pausa.

        elif opcao == "2":

            lanchonete.listar_produtos()
            pausar()

        elif opcao == "3":

            nome = input(
                "\nDigite o nome do produto: "
            ).strip()

            if nome:
                lanchonete.buscar_produto(nome)
            else:
                mostrar_erro("O nome não pode ser vazio.")

            if nome:
                pausar()

        elif opcao == "4":

            lanchonete.preparar_produtos()
            pausar()

        elif opcao == "0":

            limpar_tela()
            print("\nObrigado por utilizar nosso sistema!")
            print("Encerrando o programa...")
            break

        else:

            mostrar_erro(
                "Opção inválida! Escolha uma opção entre 0 e 4."
            )

        # Aguarda ENTER depois de um cadastro bem-sucedido.
        if opcao == "1":
            pausar()


if __name__ == "__main__":
    main()
