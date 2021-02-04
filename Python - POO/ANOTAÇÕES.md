ENCAPSULAMENTO

O encapsulamento é a ferramenta que protege as variáveis e os métodos de serem alterados
    fora da classe (no instanciamento). De acordo com a convenção do python, para alterar o status
    de uma variável ou método:
    --  Adicionar _ para ssinalizar que ela é privada (mas o python ainda deixa alterar);
    -- Adicionar __ para afirmar que ela é privada (aqui o python não permite alterar).

RELAÇÕES ENTRE CLASSES:

Associação = um objeto usa o outro objeto
Agregação = um objeto tem o outro objeto
Composição = um objeto é dono do outro objeto
Herança = um objeto é o outro objeto

ASSOCIAÇÃO

Associação é o relacionamento entre classes na qual uma classe não depende da outra.
Na prática, um atributo é inserido no montador da primeira classe, sem ser passado como parâmetro
dentro do parêntese e aceitando qualquer tipo de dado. EX: 

class x:
    def __init__ (self):
        self.atributo = None

Após, outra classe, que vai ser relacionada com a classe x deve ser criada e deve ter ao menos um método,
pois são os métodos dela que serão utilizados. Ex:

class y:
    def Metodo():
        print("Mendagem")

Agora, ao instanciar a classe x, atribuiremos ao atributo "atributo" a classe Y. Ex:

Instancia = x
Instancia.atributo = y
Instancia.atributo.Metodo()

O retorno será a execução do método "Metodo" da classe y.

AGREGAÇÃO

É o tipo de associação na qual uma classe existe sem a outra, mas não fazem nada, como o carro sem as rodas e
as rodas sem o carro. 
Para montar uma agregação, a primeira classe deve ter um atributo vazio passado, como uma lista ou um dicionário
e deve ter um método que receberá esse atributo. Ex:

class x:
    def __init__(self):
        self.atributoY = []

    def MetodoX(self, item):
        self.atributoY.append(item)
        return self.atributoY

Além disso, temos que ter outra classe que será igual ao atributo Y, cujos atributos será possível acessar após
a agregação com a sintaxe Y.atributoDeY. Ex:

class y:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

Ao instanciar a classe x, torna-se possível, então, passar a classe y como argumento para o método MetodoX, da
seguinte maneira. Ex:

instanciaY = y("nome de Y", valorY)
x.MetodoX(instanciaY)

Se for necessário acessar um atributo específico da classe y, indica-se com o nome do argumento passado no método .nome do atributo
recebido. Ex:

class x:
    def __init__(self):
        self.atributoY = []

    def MetodoX(self, item):
        self.atributoY.append(item.nome)
        return self.atributoY

COMPOSIÇÃO

Composição é o tipo de ralcionamento entre classes em que a exclusão de uma das classes faz com que a outra também seja excluída.
Para utilizar a composição no código, é possível instanciar uma classe dentro de um método de outra classe. Dessa maneira, caso a classe
que instancia a outra seja apagada, a instanciada também será. Ex:

class x:
    def __init__(self):
        self.atributoX = []

    def adicionaAtributo (self, item):
        self.aributoX.append(y(atributoY))
        return self.atributoX

class y:
    def __init__(self, atributoY):
        self.atributoY = atributoY

Nesse caso, a classe y é instanciada automaticamente ao chamar o método "adicionaAtributo(item)" e o argumento "item" é preenchido. Dessa 
maneira, caso o objeto que instancia a classe x (ex: x1) seja apagado, o instanciamento "y(atributoY)" é automaticamente apagado. Por isso,
diz-se que essa é uma relação de composição.

HERANÇA

Herança é a relação entre classes a qual uma classe é a outra e pode ter especificidades. Ou seja, a sub-classe é completamente a super-classe
e mais um pouco, por exemplo, clientes e alunos são pessoas e mais um pouco (suas especificidades). No código:

class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    
    def fala(self, assunto):
        print(f'A pessoa {self.nome} está falando...)


class Cliente(Pessoa):
    def compra(self, produto):
        print(f'O cliente {self.nome} comprou {produto}.')

class Aluno(Pessoa):
    def estuda(self, materia):
        print(f'O aluno {self.aluno} estudou {materia}.')

Ou seja, os Alunos e os Clientes herdaram todos os atributos das Pessoas, assim como herdaram todos os métodos da classe pessoa. Entretanto, a 
classe Pessoa não herda nada das sub-classes Aluno e Cliente. Por isso, é possível:

Pessoa1 = Pessoa("João", 25, "M")
Pessoa1.fala("Carros")

Cliente1 = Cliente("Maria", 30, "F")
Cliente1.fala("preços")
Cliente1.compra("Casa")

Aluno1 = Aluno("Magali", 27, "F")
Aluno1 = fala("vestibular")
Aluno1.Estuda("Matemática")

- Poliformismo
O poliformismo acontece quando uma sub-classe herda uma super-classe e, ao alterar alguma método herdado, acaba sobrescrevendo o método.
Ex:

class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    
    def fala(self):
        print(f'A pessoa {self.nome} está falando...)


class Cliente(Pessoa):
    def __init__(self, nome, idade, sexo, IDCliente):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.IDCliente = IDCliente

Nesse exemplo, apesar do método falar continuar sendo herdado pela classe Cliente, o método __init__, ao ser alterado, foi sobrescrito e,
agora, para o python, ele é um método novo e seus atributos, apesar de serem na maioria iguais ao do método Pessoa (self.nome, self.idade
e self.sexo), não são mais herdados. Esse fenômeno acontece com todos os métodos herdados. 

- Super()
Super é a função do python em que um método de uma super-classe é chamado até a sub-classe, para que seja feita uma edição sem poliformismo.
dessa maneira, a sub-classe herda a super-classe e consegue alterar alguma parte do método herdado sem sobrescrever ele (poliformismo). Ex:

class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    
    def fala(self):
        print(f'A pessoa {self.nome} está falando...)


class Cliente(Pessoa):
    def __init__(self, nome, idade, sexo, IDCliente):
        super().__init__(nome, idade, sexo):
            self.IDCliente = IDCliente

Assim, com o super() eu consegui acrescentar mais atributos ao meu método __init__ sem sobrescrever o mesmo método herdado da classe Pessoa.
essa funcionalidade serve para qualquer método.

MÉTODOS E CLASSES ABSTRATAS
Existem classes e métodos que, por natureza, são muito abstratos e, por esse motivo, não precisam ser instanciados. Por exemplo, temos a classe Figura:
ela é muito abstrata, uma vez que de figura, podem ser derivadas diversas classes mais concretas e específicas, que porem herdar a classe Figura, como
Quadrado, Circulo, Triangulo... Por isso, para evitar que os desenvolvedores instanciem classes muito abstratas, o python oferece a lib abc, com os objetos
ABC e @abstractmethod. Exemplos de como utilizá-los:

from abc import ABC

class Figura(abc):
    def __init__(self, cor):
        self.cor = cor
    @abstractmethod
    def calculaArea(self)
        pass
    
class Quadrado(Figura):
    def __init__(self, cor, lado):
        super().__init__(cor)
        self.lado = lado
    
Ao tentar instanciar a classe Figura, o python retornará um erro, pois essa classe é abstrata. Por isso, são inválidos os comandos:

F1 = Figura("laranja")
Figura.cor(F1)


