from typing import List

class AndarInvalido(ValueError):
    def __init__(self, message, andar):
        self.message = message
        self.andar = andar

class Edificio:
    def __init__(self, andares: List[int]):
        self.andares = andares
    
    def verifica_se_o_andar_eh_valido_para_o_edificio(self, andar):
        if andar not in self.andares:
            raise AndarInvalido("Andar incorreto!", andar)
        else: return True