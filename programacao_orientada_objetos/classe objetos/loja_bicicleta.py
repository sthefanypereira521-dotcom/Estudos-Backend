class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def empinar(self):
        print('empinar a bicicleta')
        print('empinando a bicicleta...\n')

    def correr(self):
        print('correndo com a bike')

    def parar(self):
        print('freiando,parando a bike')
        print('bike parada')

    def __str__(self):
        return f'bicicleta: cor = {self.cor}, modelo = {self.modelo} , ano = {self.ano}, valor = {self.valor}'


bike = bicicleta('preto e vermelha', 'bmx', 2026, 1340)

bike.correr()
bike.empinar()
bike.correr()
bike.parar()
print()
print(bike)
