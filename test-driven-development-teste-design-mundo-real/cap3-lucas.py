import unittest

class Romanos:
    def __init__(self):
        self.numero = ""
        self.caracter = ''

    def Tabela(self, caracter):
        self.caracter = caracter
        tabela = {}
        tabela['I'] = 1
        tabela['V'] = 5
        tabela['X'] = 10
        tabela['L'] = 50
        tabela['C'] = 100
        tabela['D'] = 500
        tabela['M'] = 1000
        return tabela[self.caracter]
    
    def Converte(self, numero):
        self.numero = numero
        ultimo = 0
        soma = 0
        romano = Romanos()
        for i in range (len(numero)-1, -1, -1):
            atual = romano.Tabela(numero[i])
            multiplicador = 1
            if (atual < ultimo):
                multiplicador = -1
            soma += atual * multiplicador
            ultimo = atual
        return soma
            
class Testing(unittest.TestCase):
    def setUp(self):
        self.esperado = 0
        self.numero = ""
        self.romano = Romanos()

    # Erro
    def test_one(self):
        self.numero = "XL"
        self.esperado = 60
        self.assertEqual(self.romano.Converte(self.numero) , self.esperado)

    # Correto
    def test_two(self):
        self.numero = "MDCCCLXX"
        self.esperado = 1870
        self.assertEqual(self.romano.Converte(self.numero) , self.esperado)

    # Erro
    def test_three(self):
        self.numero = "XIX"
        self.esperado = 18
        self.assertEqual(self.romano.Converte(self.numero) , self.esperado)

    # Correto
    def test_four(self):
        self.numero = "III"
        self.esperado = 3
        self.assertEqual(self.romano.Converte(self.numero) , self.esperado)
