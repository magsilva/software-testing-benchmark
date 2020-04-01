import unittest

class Calcular():
    def __init__(self):
        self.lista = []

    def addNum(self, num):
        for item in num:
            self.lista.append(item)

    def calculoSoma(self):
        resultado = 0 #caso esteja vazio
        for n in self.lista:
            resultado += n
            return resultado

    def zera(self):
        self.lista = []

class Testing(unittext.TestCase):
    def setUp(self):
        self.esperado = 0
        self.num = []
        self.calcula = Calcular()

    def test_somar_positivos(self):
        self.num = [2,8,9,11]
        self.calcula.addNum(self.num)
        self.esperado = 30
        self.assertEqual(self.calculadora.calculoSoma(), self.esperado)
        self.calcula.zera()

    def test_soma_negativos(self):
        self.num = [-2, -6, -7, -13]
        self.calcula.addNum(self.num)
        self.esperado = -28
        self.assertEqual(self.calculadora.calculoSoma(), self.esperado)
        self.calcula.zera()

    def test_soma_negativo_e_positivo(self):
        self.num = [-2,-8,9,11]
        self.calcula.addNum(self.num)
        self.esperado = 10
        self.assertEqual(self.calculadora.calculoSoma(), self.esperado)
        self.calcula.zera()

    def test_soma_vazia(self): #sem valores adicionados
        self.esperado = 0
        self.assertEqual(self.calcula.calculoSoma(), self.esperado)
        self.calcula.zera()
