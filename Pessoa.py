#Alunos: Rodrigo Bento de Macedo e Gustavo Sobreira Pinto.
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        self.nome = nome