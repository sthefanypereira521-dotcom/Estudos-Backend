class Veiculo:
    def mover(self):
        print('o veiculo se move:')


class Carro(Veiculo):
    def mover(self):
        print('carro acelera na estrada.')


class Moto(Veiculo):
    def mover(self):
        print('moto acelera na pista.')


class Barco(Veiculo):
    def mover(self):
        print('barco se move pela agua.')


class Bike(Veiculo):
    def mover(self):
        print('a bike pedala.')


veiculo = [Carro(), Moto(), Barco(), Bike()]
for v in veiculo:
    v.mover()
