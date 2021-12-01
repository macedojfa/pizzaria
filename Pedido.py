
#Alunos: Rodrigo Bento de Macedo e Gustavo Sobreira Pinto.

class Pedido:
    def __init__(self, numero, cliente):
        self.cliente = cliente
        self.produtos = []
        self.numero = numero




    def getProdutos(self):
        return self.produtos
    def setProdutos(self, produtos):
        self.produtos = produtos

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)


    def get_cliente(self):
        return self.cliente
    def set_cliente(self, cliente):
        self.cliente = cliente


    def listarProdutos(self,):
     for i in self.produtos:
        print (i.getNome())



    def listarCliente(self):
        print (self.cliente.get_nome())


    def somarLista(self):
        soma = 0
        for produtos in self.produtos:
            soma += produtos.getPreco()
        print (f"O total dos produtos deste pedido é: {soma}.")


