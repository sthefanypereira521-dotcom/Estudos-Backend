class Passaro:
    def voar(self):
        print('voando...')


class Pardal(Passaro):
    def voar(self):
        print('voando')


class Avestruz(Passaro):
    def voar(self):
        print('avestruz nao pode voar ')


passaro = [Pardal(), Avestruz()]
for p in passaro:
    p.voar()
