from components import Edificio, AndarInvalido


class Elevador:
    def __init__(self, edificio: Edificio) -> None:
        self.__andar: int = edificio.andares[0]
        self.edificio = edificio

    def locomover(self, andar: int) -> str:
        try:
            if self.edificio.verifica_se_o_andar_eh_valido_para_o_edificio(andar):
                return self.__alterar_andar_do_elevador_e_retornar_informação(andar)
        except AndarInvalido as exception:
            return self.__retornar_menssagem_de_error(exception)

    def __alterar_andar_do_elevador_e_retornar_informação(self, andar):
        self.__andar = andar
        return self.__retorna_andar_do_elevador()

    def __retornar_menssagem_de_error(self, exception):
        return (
            f"{exception.andar} é um andar inválido! "
            + self.__retorna_andar_do_elevador()
        )

    def __retorna_andar_do_elevador(self) -> str:
        if self.__andar == 1:
            return "Elevador no terreo."
        return f"Elevador no {self.__andar}º andar."
