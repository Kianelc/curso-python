lista = [1, 2, 3]

for i in range(len(lista)):
    print(lista[i])


for i in range(10):
    print(i)


# 1: Começa com o valor 1
# 10: O range vai de 0 a 9
# 2: Incrementa 2
for i in range(1, 10, 2):
    print(i)


class Pessoa:
    
    def __init__(self, nome, idade):

        self.nome = nome
        self.idade = idade

    def obterNome(self):
        return self.nome
    
    def obterIdade(self):
        return self.idade

    def setIdade(self, idade):
        self.idade = idade


p = Pessoa("kiane", 25)

print('Nome %s' % p.obterNome())
print('Idade %s' % p.obterIdade())

p1 = Pessoa("Kiane Lucia", 21)
p2 = Pessoa("Kamille Joana", 22)
p3 = Pessoa("Nazarete Marlene", 25)
p4 = Pessoa("Jurandir Antonio", 25)

pessoas = []

pessoas.append(p1)
pessoas.append(p2)
pessoas.append(p3)
pessoas.append(p4)


for pessoa in pessoas:
    print(pessoa.obterNome())


p5 = Pessoa('Kiki', 28)
print(p5.obterIdade())
p5.setIdade(30)
print(p5.obterIdade())

pares = [num for num in range(10) if (num % 2 == 0)]
print(pares)