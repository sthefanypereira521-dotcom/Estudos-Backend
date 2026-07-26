class Carro:
    garagem = 'garagem central'

    def __init__(self, modelo, placa, cor):
        self.modelo = modelo
        self.placa = placa
        self.cor = cor

    def __str__(self):

        return f'modelo do carro {self.modelo}\nplaca {self.placa}\ncor {self.cor}\n{self.garagem}\n'


carros = [
    Carro('gol', 'abc-222', 'preto'),
    Carro('uno', 'bbjj-22', 'branco',),
    Carro('fusca', 'vvo-44', 'azul'),
    Carro('palio', 'hhi-099', 'prata')
]


for c in carros:
    print(c)

print('=' * 30)

carros[0].placa = 'xhy-456'


for car in carros:
    print(car)
