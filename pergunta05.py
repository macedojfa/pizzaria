#mostre o numero do telefone dos clientes cujo pedido esta com o motoboy
#Alunos: Rodrigo Bento de Macedo e Gustavo Sobreira Pinto.

from pizzaria.Bebida import Bebida
from pizzaria.Cliente import Cliente
from pizzaria.MotoBoy import MotoBoy
from pizzaria.Pedido import Pedido
from pizzaria.Pizza import Pizza
from pizzaria.Sobremesa import Sobremesa

pizza1 = Pizza("margarita", 57.00)
pizza2 = Pizza("pepperoni", 67.00)
bebida1 = Bebida("coca-cola", 5.00)
bebida2 = Bebida("guarana", 4.00)
sobremesa1 = Sobremesa("brownie", 10.00)
cliente = Cliente("Samuel", "123456789","rua das flores, nº 0")
cliente2 = Cliente("João", "987654321","rua do contorno, nº 0")
motoboy = MotoBoy("Carlão", "987654321","00010221")
pedido02 = Pedido("002", cliente2)
pedido01 = Pedido("001", cliente)
pedido02.adicionar_produto(pizza1)
pedido02.adicionar_produto(pizza1)
pedido02.adicionar_produto(bebida1)
pedido01.adicionar_produto(pizza1)
pedido01.adicionar_produto(bebida1)
pedido01.adicionar_produto(bebida2)
pedido01.adicionar_produto(sobremesa1)

#motoboy.addPedido(pedido01)
motoboy.addPedido(pedido02)

motoboy.listarTelefone()