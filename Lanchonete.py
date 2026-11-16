"""Módulo que define a classe gerenciadora Lanchonete."""

from Produto import Produto


class Lanchonete:
    """Gerencia a lista de produtos cadastrados na lanchonete."""

    def __init__(self):
        """Inicializa a lista privada de produtos."""
        self.__produtos: list[Produto] = []

    @property
    def produtos(self) -> list[Produto]:
        """Retorna uma cópia da lista de produtos cadastrados."""
        return self.__produtos.copy()

    def cadastrar_produto(self, produto: Produto) -> None:
        """Adiciona um produto à lista.

        Raises:
            TypeError: se o objeto informado não for um Produto.
        """
        if not isinstance(produto, Produto):
            raise TypeError("Só é possível cadastrar objetos do tipo Produto.")
        self.__produtos.append(produto)

    def buscar_produto(self, nome: str) -> list[Produto]:
        """Busca produtos cujo nome contenha o texto informado.

        Returns:
            list[Produto]: produtos encontrados (lista vazia se não houver).
        """
        termo = nome.lower()
        return [p for p in self.__produtos if termo in p.nome.lower()]