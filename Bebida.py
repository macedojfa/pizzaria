#Alunos: Rodrigo Bento de Macedo e Gustavo Sobreira Pinto.
from pizzaria.Produto import Produto


class Bebida(Produto):
    def __init__(self, nome, preco):
        Produto.__init__(self, nome, preco)
