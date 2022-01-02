from components import Edificio, Elevador

edificio = Edificio(range(1, 15, 1))

elevador = Elevador(edificio)

while True:
    andar = int(input("Defina um andar: "))
    response = elevador.locomover(andar)
    print(response)
    print()
