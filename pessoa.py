class Pessoa:
    
    def __init__ (self, nome, idade, sexo, fala=False, come=False, anda=True):

        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.come = come
        self.fala = fala


    def Falar(self, assunto):
        if self.come:
            print(f'{self.nome} não pode falar com a boca cheia.')
            return
        self.fala = True
        print(f'O/A {self.nome} está falando sobre {assunto}.')


    def PararFalar(self):
        print(f'{self.nome} parou de falar.')
        self.fala = False
    

    def PararComer(self):
        print(f'{self.nome} parou de comer.')
        self.come = False


    def Comer(self, alimento):
            if self.fala:
                print(f'{self.nome} não pode comer falando.')
                return
            self.come = True    
            print(f'O/A {self.nome} está comendo {alimento}.')


    def Finalizar(self):
        self.fala = False
        self.come = False