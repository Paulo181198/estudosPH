
from pessoa import Pessoa


class Personalidade():

    def __init__(self, Roupa, Calcado, Cabelo, nome, idade, sexo):
        self.Roupa = Roupa
        self.Calcado = Calcado
        self.Cabelo = Cabelo
        super().__init__(nome, idade, sexo)

    def Expressa(self, como):
        self.como =  como
        print(f'O {self.nome} expressa sua personalidade {self.como}. Além disso, ele complementa sua personalidade com suas características: {self.Roupa}, {self.Calcado}, {self.Cabelo}...')

    