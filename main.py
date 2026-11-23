"""Módulo principal do sistema de Lanchonete Delivery."""

from Bebida import Bebida
from Lanche import Lanche
from Lanchonete import Lanchonete
from Sobremesa import Sobremesa

LARGURA = 45


# ----------------------------------------------------------------------
# Utilitários de tela
# ----------------------------------------------------------------------
def limpar_tela():
    """Simula o comando CLS utilizando linhas vazias."""
    print("\n" * 30)


def pausar():
    """Aguarda o usuário pressionar ENTER."""
    input("\nPressione ENTER para continuar...")


def exibir_titulo(texto):
    """Exibe um título centralizado entre linhas decorativas."""
    print("=" * LARGURA)
    print(texto.center(LARGURA))
    print("=" * LARGURA)


def mostrar_erro(mensagem):
    """Limpa a tela e exibe uma mensagem de erro."""
    limpar_tela()
    exibir_titulo("ERRO")
    print(f"\n{mensagem}")


def exibir_menu():
    """Exibe o menu principal."""
    exibir_titulo("SAMULANCHES")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Preparar produtos (Polimorfismo)")
    print("0 - Sair")
    print("=" * LARGURA)


# ----------------------------------------------------------------------
# Leitura de dados
# ----------------------------------------------------------------------
def ler_texto(mensagem, obrigatorio=True):
    """Lê um texto do usuário.

    Raises:
        ValueError: se o texto for obrigatório e estiver vazio.
    """
    valor = input(mensagem).strip()
    if obrigatorio and not valor:
        raise ValueError("Este campo não pode ficar vazio.")
    return valor


def ler_numero(mensagem, tipo=int):
    """Lê um número (int ou float) do usuário, aceitando vírgula decimal.

    Raises:
        ValueError: se o valor digitado não for um número válido.
    """
    try:
        return tipo(input(mensagem).strip().replace(",", "."))
    except ValueError:
        raise ValueError("Digite um número válido.") from None


# ----------------------------------------------------------------------
# Criação de cada tipo de produto
# ----------------------------------------------------------------------
def criar_lanche(nome, preco):
    """Solicita os dados específicos e cria um Lanche."""
    exibir_titulo("CADASTRO DE LANCHE")
    pao = ler_texto("Tipo de pão: ")
    ingredientes = input("Ingredientes separados por vírgula: ")
    lista = [item.strip() for item in ingredientes.split(",") if item.strip()]
    return Lanche(nome, preco, pao, lista)


def criar_bebida(nome, preco):
    """Solicita os dados específicos e cria uma Bebida."""
    exibir_titulo("CADASTRO DE BEBIDA")
    volume = ler_numero("Volume em ml: ")
    gelada = ler_texto("Servida gelada? (s/n): ").lower()

    if gelada not in ("s", "n"):
        raise ValueError("Digite somente s ou n.")

    return Bebida(nome, preco, volume, gelada == "s")


def criar_sobremesa(nome, preco):
    """Solicita os dados específicos e cria uma Sobremesa."""
    exibir_titulo("CADASTRO DE SOBREMESA")
    temperatura = ler_texto("Temperatura (Quente ou Gelada): ")
    calorias = ler_numero("Calorias (kcal): ")
    cobertura = ler_texto("Cobertura extra (ENTER para nenhuma): ", obrigatorio=False)

    sobremesa = Sobremesa(nome, preco, temperatura, calorias)

    if cobertura:
        sobremesa.adicionar_cobertura(cobertura)

    return sobremesa


# ----------------------------------------------------------------------
# Ações do menu
# ----------------------------------------------------------------------
def cadastrar_produto(lanchonete):
    """Pergunta o tipo, lê os dados e cadastra o produto na lanchonete."""
    exibir_titulo("CADASTRAR PRODUTO")
    print("1 - Lanche")
    print("2 - Bebida")
    print("3 - Sobremesa")
    print("0 - Voltar")

    match input("\nEscolha o tipo de produto: ").strip():
        case "0":
            return
        case "1":
            criar = criar_lanche
        case "2":
            criar = criar_bebida
        case "3":
            criar = criar_sobremesa
        case _:
            raise ValueError("Opção inválida! Escolha 0, 1, 2 ou 3.")

    exibir_titulo("DADOS DO PRODUTO")
    nome = ler_texto("Nome do produto: ")
    preco = ler_numero("Preço (R$): ", float)
    estoque = ler_numero("Quantidade em estoque: ")

    produto = criar(nome, preco)
    produto.quantidade_estoque = estoque
    lanchonete.cadastrar_produto(produto)

    print("\nProduto cadastrado com sucesso!")


def listar_produtos(lanchonete):
    """Exibe todos os produtos cadastrados."""
    produtos = lanchonete.produtos

    if not produtos:
        print("\nNenhum produto cadastrado.")
        return

    exibir_titulo("PRODUTOS CADASTRADOS")

    for indice, produto in enumerate(produtos, start=1):
        print(f"\n{indice}. {produto}")


def buscar_produto(lanchonete):
    """Lê um nome e exibe os produtos encontrados."""
    exibir_titulo("BUSCAR PRODUTO")
    nome = ler_texto("\nDigite o nome do produto: ")
    encontrados = lanchonete.buscar_produto(nome)

    if not encontrados:
        print("\nNenhum produto encontrado.")
        return

    print("\n--- RESULTADO DA BUSCA ---")

    for produto in encontrados:
        print(f"\n{produto}")


def preparar_produtos(lanchonete):
    """Percorre a lista e chama preparar() em todos (polimorfismo)."""
    produtos = lanchonete.produtos

    if not produtos:
        print("\nNenhum produto cadastrado para preparar.")
        return

    exibir_titulo("PREPARAÇÃO DOS PRODUTOS")

    for produto in produtos:
        print(f"\n{produto.nome}")
        print(produto.preparar())


def executar(acao, lanchonete):
    """Executa uma ação do menu tratando erros e pausando ao final."""
    try:
        acao(lanchonete)
    except (ValueError, TypeError) as erro:
        mostrar_erro(erro)

    pausar()


# ----------------------------------------------------------------------
# Programa principal
# ----------------------------------------------------------------------
def main():
    """Executa o laço principal do menu."""
    lanchonete = Lanchonete()

    while True:
        limpar_tela()
        exibir_menu()

        match input("\nEscolha uma opção: ").strip():
            case "1":
                executar(cadastrar_produto, lanchonete)
            case "2":
                executar(listar_produtos, lanchonete)
            case "3":
                executar(buscar_produto, lanchonete)
            case "4":
                executar(preparar_produtos, lanchonete)
            case "0":
                limpar_tela()
                print("Obrigado por utilizar nosso sistema!")
                print("Encerrando o programa...")
                break
            case _:
                mostrar_erro("Opção inválida! Escolha uma opção entre 0 e 4.")
                pausar()


if __name__ == "__main__":
    main()