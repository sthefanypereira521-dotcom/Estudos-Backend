class Animal:
    def falar(self):
        print("O animal faz um som")


class Cachorro(Animal):
    def falar(self):
        print("Au au!")


class Gato(Animal):
    def falar(self):
        print("Miau!")


animais = [Cachorro(), Gato(), Animal()]

for animal in animais:
    animal.falar()
