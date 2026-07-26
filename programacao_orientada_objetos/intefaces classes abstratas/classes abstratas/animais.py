from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass


class Cachorro(Animal):
    def falar(self):
        return 'auuu auu'


class Gato(Animal):
    def falar(self):
        return 'miaau miaau'


dog = Cachorro()
cat = Gato()

print(dog.falar())
print(cat.falar())
