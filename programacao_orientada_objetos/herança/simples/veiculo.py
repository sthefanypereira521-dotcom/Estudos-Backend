class veiculo:
    def __init__(self, cor, placa, num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas

    def ligar_motor(self):
        print('ligando motor ')

    def trocar_marcha(self):
        print('trocando de macha...')

    def __str__(self):
        return f'veiculo: cor = {self.cor}, placa = {self.placa}, num_rodas = {self.num_rodas} '


class motocicleta(veiculo):
    pass


class carro(veiculo):
    pass


motocicleta = motocicleta('preta e vermelha', 'aaa-111', 2)
print()
motocicleta.ligar_motor()
motocicleta.trocar_marcha()
print(motocicleta)


carro = carro('prata', 'ajl-136', 4)
print()
carro.ligar_motor()
carro.trocar_marcha()
print(carro)
