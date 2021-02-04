from pessoa import Pessoa

class Cliente(Pessoa):
    def compra (self, produto):
        print(f'O cliente {self.nome} compra {produto}.')