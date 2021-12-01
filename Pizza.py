#Alunos: Rodrigo Bento de Macedo e Gustavo Sobreira Pinto.
from pizzaria.Produto import Produto



class Pizza(Produto):
    def __init__(self, nome, preco):
        Produto.__init__(self, nome, preco)
        self.sabores = []

    def getSabor(self, sabor):
        return self.sabor

    def setSabor(self, sabor):
        self.sabor = sabor
    def addSabores(self, sabor):
        self.sabores.append(sabor)


    def removeSabores(self, sabor):
        self.sabores.remove(sabor)

    def listarSabores(self):
        for sabor in self.sabores:
            print(sabor.getNome())




