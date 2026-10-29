from abc import ABC, abstractmethod


class BebidaQuente(ABC):

    def preparar(self):
        print("--- iniciando o preparo ---")

        self.ferver()
        self.misturar()
        self.servir()

        print("--- bebiba pronta ---\n")

    def ferver(self):
        print("1° fervendo algo...")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):

    def misturar(self):
        print("2° passando agua no coador contendo o Pó de café")

    def servir(self):
        print("3° servir em uma xícara...")


class Cha(BebidaQuente):

    def misturar(self):
        print("2° mergulho o sache na agua")

    def servir(self):
        print("3° servir em uma xícara...")


class ChocolateQuente(BebidaQuente):

    def misturar(self):
        print("2° misturo leite com tody com uma colher ")

    def servir(self):
        print("3° servir em uma caneca...")
