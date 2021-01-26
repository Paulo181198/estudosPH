class Pessoa:
    
    def __init__ (self, nome, idade, sexo, fala=True, come=True, anda=True):

        self.nome = nome
        self.idade = idade
        self.sexo = sexo


    def falar(self, assunto):
        print(f'O/A {self.nome} está falando sobre {assunto}.')
    
    def comer(self, alimento):
        print(f'O/A {self.nome} está comendo {alimento}.')