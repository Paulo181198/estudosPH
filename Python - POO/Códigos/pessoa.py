from random import randint
from Endereco import Endereco

class Pessoa:
    fala = False
    
    #O __init__ declara as variáveis usadas em toda a classe, em qualquer método que chamar o self. 
    def __init__ (self, nome, idade, sexo, fala=False, come=False, anda=True):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.come = come
        self.fala = fala
        self.anda = anda 
        self.assunto = None #associação
        self.hobby = [] #agregação
        self.endereco = [] #composição

    #Método para agregação
    def AdicionaHobby (self, Modalidade):
        self.hobby.append(Modalidade.tema)
        return self.hobby


    #Método para composição
    def AdicionaEndereco (self, cidade, estado):
        endCompleto = Endereco(cidade, estado)
        novoEndereco = {'cidade': endCompleto.cidade, 'estado': endCompleto.estado}
        return self.endereco.append(novoEndereco)
    
    #Criação dos métodos da classe
    def Falar(self):
        if self.come:
            print(f'{self.nome} não pode falar com a boca cheia.')
            return
        self.fala = True
        print(f'O/A {self.nome} está falando sobre {self.assunto}.')


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


    #Esse @ acessa as variávels da classe, declaradas fora do __init__. Por convenção, troca-se o self por cls
    @classmethod
    def Falar2(cls):
        if cls.fala == False:
            print('Pegou o False do cls.')
        else:
            print('Pegou o True do Self')
    
    
    #Esse @ gera uma função fora da classe. Por isso, não acessa nenhuma variável dela e nem do __init__
    @staticmethod
    def GeraID(nome):
        id = randint(0, 10000)
        print(f'O ID do {nome} é {id}.')


    #Esse @ gera uma função para edição estruturada de um atributo do __init__ em duas etapas: getter e setter
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor):
        self._idade = valor + 1
