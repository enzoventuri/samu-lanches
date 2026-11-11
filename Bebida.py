# Samuel

"""Módulo contendo a classe Bebida para o sistema de Lanchonete (Delivery).

Este módulo representa itens do tipo bebida, aplicando herança da classe Produto,
encapsulamento de atributos e polimorfismo.
"""

import Produto


class Bebida(Produto):
    """Classe que representa um produto do tipo Bebida no sistema de Delivery.

    Herda da classe base Produto.
    """

    def __init__(
        self,
        nome: str,
        preco: float,
        tamanho_ml: int,
        gelada: bool = True,
    ):
        """Inicializa um objeto do tipo Bebida.

        :param nome: Nome da bebida (ex: 'Refrigerante de Cola').
        :param preco: Preço base em Reais.
        :param tamanho_ml: Volume da bebida em mililitros (ex: 350, 500, 2000).
        :param gelada: Indica se a bebida deve ser servida gelada (padrão: True).
        """
        # Chama o construtor da classe base (Produto)
        super().__init__(nome, preco)

        # Atributos específicos da classe Bebida (encapsulados)
        self._tamanho_ml = tamanho_ml
        self._gelada = gelada

    # --------------------------------------------------------------------------
    # GETTERS E SETTERS (ENCAPSULAMENTO COM VALIDAÇÃO)
    # --------------------------------------------------------------------------

    @property
    def tamanho_ml(self) -> int:
        """Getter do volume da bebida em ml."""
        return self._tamanho_ml

    @tamanho_ml.setter
    def tamanho_ml(self, valor: int) -> None:
        """Setter com validação para impedir volumes inválidos."""
        if valor <= 0:
            raise ValueError(
                "O volume da bebida em mL deve ser maior que zero!"
            )
        self._tamanho_ml = valor

    @property
    def gelada(self) -> bool:
        """Getter do estado térmico da bebida."""
        return self._gelada

    @gelada.setter
    def gelada(self, status: bool) -> None:
        """Setter para alterar se a bebida está gelada ou não."""
        self._gelada = status

    # --------------------------------------------------------------------------
    # MÉTODOS EXCLUSIVOS DA CLASSE BEBIDA
    # --------------------------------------------------------------------------

    def servir_com_gelo(self) -> str:
        """Método próprio da classe Bebida (não existe na classe Produto).

        :return: Mensagem de confirmação da adição de gelo.
        """
        if self._gelada:
            return (
                f"Adicionado gelo e limão à bebida {self.nome} ({self._tamanho_ml}ml)."
            )
        return f"A bebida {self.nome} é servida em temperatura ambiente (sem gelo)."

    # --------------------------------------------------------------------------
    # POLIMORFISMO (SOBRESECRITA DE MÉTODOS DA CLASSE BASE)
    # --------------------------------------------------------------------------

    def preparar(self) -> str:
        """Sobrescreve o método polimórfico preparar() da classe base Produto.

        :return: String com o modo de preparo específico da bebida.
        """
        estado = (
            "retirada do refrigerador trincando de gelada"
            if self._gelada
            else "embalada em temperatura ambiente"
        )
        return f"🥤 Servindo {self.nome} ({self._tamanho_ml}ml): {estado} e lacrada para entrega!"

    def __str__(self) -> str:
        """Retorna uma representação em texto legível da Bebida."""
        status_gelo = "Gelada" if self._gelada else "Sem gelo"
        return f"[BEBIDA] {self.nome} | Vol: {self._tamanho_ml}ml | Temp: {status_gelo} | Preço: R$ {self.preco:.2f}"