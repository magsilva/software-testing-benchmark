import unittest

class Calculadora:
    def __init__(self):
        self.lista = []

    def adicionarNumeros(self, numeros):
        for item in numeros:
            self.lista.append(item)

    def calculoSoma(self):
        # Resultado vem por 0, pois caso nao haja nenhum item, este sera o retorno
        resultado = 0
        for num in self.lista:
            resultado += num
        return resultado

    def zeraLista(self):
        self.lista = []

class Testing(unittest.TestCase):
    # Funcionando como um before
    # E recomendado que crie a classe e a configure aqui, para que caso sua estrutura
    # seja alterada, seria necessario editar apenas esta parte
    def setUp(self):
        self.esperado = 0
        self.numeros = []
        self.calculadora = Calculadora()

    # Um teste para cada procedimento possivel da funcao [Somar]
    def test_soma_apenas_positivos(self):
        self.numeros = [3,7,5,10]
        self.calculadora.adicionarNumeros(self.numeros)
        self.esperado = 25
        self.assertEqual(self.calculadora.calculoSoma(), self.esperado)
        # Agindo como um after, para que o proximo teste obtenha a classe limpa
        self.calculadora.zeraLista()

    def test_soma_com_negativos_e_positivos(self):
        self.calculadora.adicionarNumeros([3,-7,-2,4])
        self.esperado = -2
        self.assertEqual(self.calculadora.calculoSoma(), self.esperado)
        self.calculadora.zeraLista()

    def test_soma_apenas_negativos(self):
        self.calculadora.adicionarNumeros([-2,-26,-2])
        self.esperado = -30
        self.assertEqual(self.calculadora.calculoSoma(), self.esperado)
        self.calculadora.zeraLista()

    def test_soma_sem_valores(self):
        #self.calculadora.adicionarNumeros()
        self.esperado = 0
        self.assertEqual(self.calculadora.calculoSoma(), self.esperado)
        self.calculadora.zeraLista()    
        
