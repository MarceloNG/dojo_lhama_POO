from model import Elevador
from controller import GerenciadorDeElevadores

primeiro_andar = 1
ultimo_andar = 15


gerenciador_de_elevadores = GerenciadorDeElevadores()

gerenciador_de_elevadores.adicionar_elevadores([
    Elevador(1, primeiro_andar, ultimo_andar),
    Elevador(2, primeiro_andar, ultimo_andar)
])

while (True):
    elevadorId = int(input('Defina o elevador: '))
    andar = int(input('Defina um andar: '))
    mensagem = gerenciador_de_elevadores.mover_elevador(elevadorId, andar)
    print(mensagem)
    print()