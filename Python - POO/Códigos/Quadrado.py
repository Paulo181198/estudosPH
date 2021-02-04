from Figura import Figura

class Quadrado(Figura):
    def __init__(self, lado, cor):
        super().__init__(cor)
        self.lado = lado
    
    def calculoArea(self):
        area = self.lado ** 2
        return area



#Teste instanciamento de classe abstrata
f1 = Figura ("laranja")
print(f1.cor)