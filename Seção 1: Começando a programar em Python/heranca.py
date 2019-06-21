'''
    O que é herança em Orientação a Objetos:
    É quando uma classe herda características de outra classe
'''

class Transporte:

    def __init__(self, nome, peso, preco):
        self.nome = nome
        self.peso = peso
        self.preco = preco


    def getNome(self):
        return self.nome
    

    def getPeso(self):
        return self.peso


    def getPreco(self):
        return self.preco


class Carro(Transporte):

    def __init__(self, nome, peso, preco, preco_seguro):
        Transporte.__init__(self, nome, peso, preco)
        self.preco_seguro = preco_seguro


    def getPrecoSeguro(self):
        return self.preco_seguro


print('--------- SEM HERANÇA ---------')
transporte = Transporte('Fusca',500, 3278.56)
print(transporte.getNome())
print(transporte.getPreco())
print('--------- COM HERANÇA ---------')
carro = Carro('Fusca',300.78, 3278.56, 800)
print('Nome do carro: ', carro.getNome())
print('Peso do carro: ', carro.getPeso())
print('Preço do carro: R$', carro.getPreco())
print('Preço do seguro do carro: R$', carro.getPrecoSeguro())
