"""Módulo que define a classe base Produto da lanchonete."""


class Produto:
    """Classe base que representa um produto vendido pela lanchonete.

    As classes filhas (Lanche, Bebida e Sobremesa) herdam desta classe
    e sobrescrevem o método calcular_preco_final().
    """

    def __init__(self, nome, preco, quantidade_estoque):
        """Inicializa um produto.

        Args:
            nome (str): nome do produto (não pode ser vazio).
            preco (float): preço unitário (deve ser maior que zero).
            quantidade_estoque (int): quantidade disponível (não pode ser negativa).
        """
        self.__nome = None
        self.__preco = None
        self.__quantidade_estoque = None
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    @property
    def nome(self):
        """Retorna o nome do produto."""
        return self.__nome

    @nome.setter
    def nome(self, valor):
        """Define o nome do produto.

        Raises:
            ValueError: se o nome for vazio.
        """
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome do produto não pode ser vazio.")
        self.__nome = valor.strip()

    @property
    def preco(self):
        """Retorna o preço unitário do produto."""
        return self.__preco

    @preco.setter
    def preco(self, valor):
        """Define o preço do produto.

        Raises:
            ValueError: se o preço for menor ou igual a zero.
        """
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        self.__preco = float(valor)

    @property
    def quantidade_estoque(self):
        """Retorna a quantidade disponível em estoque."""
        return self.__quantidade_estoque

    @quantidade_estoque.setter
    def quantidade_estoque(self, valor):
        """Define a quantidade em estoque.

        Raises:
            ValueError: se a quantidade for negativa.
        """
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("A quantidade em estoque não pode ser negativa.")
        self.__quantidade_estoque = valor

    def calcular_preco_final(self):
        """Calcula o preço final do produto.

        Na classe base retorna o preço simples. As classes filhas
        sobrescrevem este método com regras próprias (polimorfismo).

        Returns:
            float: preço final do produto.
        """
        return self.__preco

    def __str__(self):
        """Retorna os dados do produto de forma legível."""
        return (f"Produto: {self.__nome} | "
                f"Preço: R$ {self.__preco:.2f} | "
                f"Estoque: {self.__quantidade_estoque}")