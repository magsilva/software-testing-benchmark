import unittest

class Item:
    def __init__(self, desc, quant, val):
        self.descricao = desc
        self.quantidade = quant
        self.valorUnitario = val

    def getTotal(self):
        return self.valorUnitario * self.quantidade

class Carrinho:
    def __init__(self):
        self.lista = [];

    def adiciona(self, item):
        self.lista.append(item);

    def maiorValor(self):
        if len(self.lista) == 0:
            return 0
        maior = self.lista[0].getTotal()
        for item in self.lista:
            if (item.getTotal() > maior):
                maior = item.getTotal()
        return maior
		
class Testing(unittest.TestCase):
    def setUp(self):
        self.esperado = 0
        self.carrinho = Carrinho()

    # Carrinho VAZIO
    def test_one(self):
        self.esperado = 0
        self.assertEqual(self.carrinho.maiorValor(), self.esperado)

    # Carrinho 1 ITEM
    def test_two(self):
        self.carrinho.adiciona(Item("Batata",30,1.50))
        self.esperado = 30 * 1.50
        self.assertEqual(self.carrinho.maiorValor(), self.esperado)

    # Carrinho VARIOS ITEMS
    def test_tree(self):
        self.carrinho.adiciona(Item("Batata",30,1.50))
        self.carrinho.adiciona(Item("Abacaxi",12,3.00))
        self.carrinho.adiciona(Item("Melao",15,3.50))
        self.esperado = 15 * 3.50
        self.assertEqual(self.carrinho.maiorValor(), self.esperado)

    # Carrinho VARIOS ITEMS
    def test_four(self):
        self.carrinho.adiciona(Item("Chocolate",3,33.00))
        self.carrinho.adiciona(Item("Panetone",2,50.00))
        self.carrinho.adiciona(Item("Suplemento",1,99.99))
        self.esperado = 100.00
        self.assertEqual(self.carrinho.maiorValor(), self.esperado)
