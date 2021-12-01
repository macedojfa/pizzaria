#Alunos: Rodrigo Bento de Macedo e Gustavo Sobreira Pinto.
from pizzaria.Pessoa import Pessoa


class MotoBoy(Pessoa):
    def __init__(self, nome, telefone, cnh):
      Pessoa.__init__(self, nome)
      self.telefone = telefone
      self.cnh = cnh
      self.pedidos = []

    def getTelefone(self):
        return self.telefone
    def setTelefone(self, telefone):
        self.telefone = telefone

    def getCnh(self):
        return self.cnh
    def setCnh(self, cnh):
        self.cnh = cnh

    def getPedidos(self):
        return self.pedidos
    def setPedidos(self, pedidos):
        self.pedidos = pedidos

    def addPedido(self, pedido):
        self.pedidos.append(pedido)

    def listarCliente(self):
        for pedido in self.pedidos:
            print(pedido.cliente.get_nome())

    def listarEndereco(self):
        for pedido in self.pedidos:
            print(f"O endereço do clinte {pedido.cliente.get_nome()} é: {pedido.cliente.getEndereco()}.")

    def listarTelefone(self):
        for pedido in self.pedidos:
            print(f" O telefone do cliente {pedido.cliente.get_nome()}, é: {pedido.cliente.getTelefone()}.")



