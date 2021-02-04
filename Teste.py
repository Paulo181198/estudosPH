from Hobby import Hobby
from Assunto import Assuntos
from Cliente import Cliente
from pessoa import Pessoa

#Criei uma instância da classe pessoa
p1 = Pessoa('João', 20, 'M')

#Chamei um método da instância
#p1.Falar("Comida")

#Chamei um método da classe
#p1.Falar2()

#Chamei um método estático
p1.GeraID("João")

#Teste alteração getter e setter. Idade + 1
print(p1.idade)

#Associação 
p1.assunto = Assuntos
p1.assunto.falado("Carro")

#Agregação
Hobby1 = Hobby("Andar", "10 anos")
Assunto1 = Assuntos("Corrida")
print(p1.AdicionaHobby(Assunto1))

#Composição
p1.AdicionaEndereco("São Paulo", "SP")
p1.AdicionaEndereco('Juquitiba', 'SP')
print(p1.endereco)

#Herança
C1 = Cliente("João", 25, "M")
C1.compra("Mala")