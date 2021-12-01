# acrescente ingredientes a um determinedo sabor, e mostre uma lista com os ingredientes desse sabor
#Alunos: Rodrigo Bento de Macedo e Gustavo Sobreira Pinto.

from pizzaria.Ingrediente import Ingrediente
from pizzaria.Sabor import Sabor

ingrediente1 = Ingrediente("Queijo")
ingrediente2 = Ingrediente("Peperone")
ingrediente3 = Ingrediente("Molho de Tomate")
ingrediente4 = Ingrediente("Calabresa")
ingrediente5 = Ingrediente("Cebola")
ingrediente6 = Ingrediente("Azeitona")
ingrediente7 = Ingrediente("Orégano")
ingrediente8 = Ingrediente("Pimentão")
ingrediente9 = Ingrediente("Molho picante")
sabor2 = Sabor("caliente" )
sabor1 = Sabor("peperone")
sabor1.acrescentaIngrediente(ingrediente1)
sabor1.acrescentaIngrediente(ingrediente2)
sabor1.acrescentaIngrediente(ingrediente3)
sabor1.acrescentaIngrediente(ingrediente7)
sabor2.acrescentaIngrediente(ingrediente4)
sabor2.acrescentaIngrediente(ingrediente5)
sabor2.acrescentaIngrediente(ingrediente3)
sabor2.acrescentaIngrediente(ingrediente1)
sabor2.acrescentaIngrediente(ingrediente7)
sabor2.acrescentaIngrediente(ingrediente9)
Sabor.listarIngredientes(sabor1)
