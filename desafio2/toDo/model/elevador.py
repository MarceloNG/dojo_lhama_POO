class AndarInvalido(ValueError):
    def __init__(self, andar):
        self.message = f"{andar}º é um andar inválido!"


class Elevador:
    def __init__(self, id: int, primeiro_andar: int, ultimo_andar: int) -> None:
        self.id = id
        self.andar_atual = primeiro_andar
        self.primeiro_andar = primeiro_andar
        self.ultimo_andar = ultimo_andar

    def mover_para_o_andar(self, andar: int):
        if self.__andar_eh_valido(andar) and self.andar_atual:
            self.__alterar_andar(andar)
        else:
            raise AndarInvalido(andar)

    def __andar_eh_valido(self, andar):
        return self.primeiro_andar <= andar <= self.ultimo_andar

    def __alterar_andar(self, andar: int):
        self.andar_atual = andar
