#Alunos: Rodrigo Bento de Macedo e Gustavo Sobreira Pinto.
from pizzaria.Pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, telefone, endereco):
        Pessoa.__init__(self, nome)
        self.telefone = telefone
        self.endereco = endereco

    def getTelefone(self):
        return self.telefone
    def setTelefone(self, telefone):
        self.telefone = telefone

    def getEndereco(self):
        return self.endereco
    def setEntedeco(self, endereco):
        self.endereco = endereco