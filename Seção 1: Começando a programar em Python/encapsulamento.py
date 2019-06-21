class Pessoa:

    def __init__(self):
        self.__nome = None


    #def getNome(self):
    #    return self.nome


    @property
    def nome(self):
        return self.__nome


    @nome.setter
    def nome(self, nome):
        self.__nome = nome


#pessoa = Pessoa('Kiane')
#print(pessoa.getNome())

pessoa = Pessoa()
pessoa.nome = 'Kiane'
print(pessoa.nome)