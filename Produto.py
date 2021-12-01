#Alunos: Rodrigo Bento de Macedo e Gustavo Sobreira Pinto.
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def getNome(self):
        return self.nome
    def getPreco(self):
        return self.preco
    def setNome(self, nome):
        self.nome = nome
    def setPreco(self, preco):
        self.preco = preco

    
