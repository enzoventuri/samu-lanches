
from produto import Produto


class Sobremesa(Produto):


    def __init__(self, nome: str, preco: float, temperatura: str, calorias: int):
        """Inicializa os atributos da Sobremesa.

        Args:
            nome (str): Nome da sobremesa.
            preco (float): Preço unitário.
            temperatura (str): Temperatura de serviço (ex: Gelada, Quente).
            calorias (int): Quantidade de calorias em kcal.
        """
        super().__init__(nome, preco)
        self.__temperatura = temperatura
        self.calorias = calorias  # Utiliza o setter com validação
        self.__cobertura_extra: str = "Nenhuma"

    @property
    def temperatura(self) -> str:
        """Retorna a temperatura ideal para consumo."""
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, nova_temperatura: str) -> None:

        if not nova_temperatura.strip():
            raise ValueError("A temperatura não pode ser vazia.")
        self.__temperatura = nova_temperatura

    @property
    def calorias(self) -> int:
        return self.__calorias

    @calorias.setter
    def calorias(self, valor: int) -> None:
        if valor <= 0:
            raise ValueError("A quantidade de calorias deve ser maior que zero.")
        self.__calorias = valor

    @property
    def cobertura_extra(self) -> str:
        return self.__cobertura_extra

    def adicionar_cobertura(self, cobertura: str) -> None:
        if cobertura.strip():
            self.__cobertura_extra = cobertura
            print(f"Cobertura '{cobertura}' adicionada à sobremesa {self.nome}!")

    def eh_diet(self) -> bool:
        return self.__calorias < 150

    def preparar(self) -> str:
        status_diet = "Diet/Baixa Caloria" if self.eh_diet() else "Padrão"
        return (
            f"[PREPARO SOBREMESA] Retirando '{self.nome}' da refrigeração/forno "
            f"({self.__temperatura}), adicionando cobertura '{self.__cobertura_extra}' "
            f"e embalando em recipiente térmico. ({self.__calorias} kcal - {status_diet})"
        )

    def __str__(self) -> str:
        """Retorna a representação textual legível do objeto."""
        base_str = super().__str__()
        return (
            f"{base_str} | Tipo: Sobremesa | Servir: {self.__temperatura} | "
            f"Calorias: {self.__calorias} kcal | Cobertura Extra: {self.__cobertura_extra}"
        )