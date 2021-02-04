from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, idade, sexo, IDCliente):
        super().__init__(nome, idade, sexo)
        self.IDCliente = IDCliente

    def compra (self, produto):
        print(f'O cliente {self.nome}, ID: {self.IDCliente}, comprou {produto}.')