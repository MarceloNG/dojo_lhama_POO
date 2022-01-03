from typing import Set, List
from model import Elevador, AndarInvalido

class IdElevadorInvalido(ValueError):
    def __init__(self, id_elevador):
        self.id_elevador = id_elevador
        self.message = f"{id_elevador} é um id inválido de elevador!"

class GerenciadorDeElevadores():
    def __init__(self):
        self.elevadores: Set[Elevador] = set()

    def adicionar_elevadores(self, elevadores: List[Elevador]):
        for elevador in elevadores: self.adicionar_elevador(elevador)

    def adicionar_elevador(self, elevador: Elevador):
        self.elevadores.add(elevador)

    def mover_elevador(self, id_elevador, andar_de_destino) -> str:
        try:
            elevador = self.get_elevador_por_id(id_elevador)
            andar_atual = elevador.andar_atual
            elevador.mover_para_o_andar(andar_de_destino)
            return self.__messagem_de_alteracao_do_elevador(andar_atual, andar_de_destino, id_elevador)
        except (IdElevadorInvalido, AndarInvalido) as e:
            return e.message
        

    def get_elevador_por_id(self, id: int) -> Elevador:
        try:
            return next(elevador for elevador in self.elevadores if elevador.id == id)
        except StopIteration:
            raise IdElevadorInvalido(id)

    def __menssagem_de_erro(self):
        return "erro"

    def __get_str_andar(self, andar):
        if andar == 1: return "terreo"
        return f"{andar}º andar"

    def __messagem_de_alteracao_do_elevador(self, andar_atual, andar_de_destino, id_elevador):
        return f"Movendo elevador {id_elevador} do {self.__get_str_andar(andar_atual)} para o {self.__get_str_andar(andar_de_destino)}."       
    
