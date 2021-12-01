#Alunos: Rodrigo Bento de Macedo e Gustavo Sobreira Pinto.
class Sabor:
    def __init__(self, nome):

        self.nome = nome

        self.ingredientes = []
    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome


    def acrescentaIngrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def listarIngredientes(self):
        for i in self.ingredientes:
            print (i.getNome())
