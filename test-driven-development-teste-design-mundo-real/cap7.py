import unittest

class Funcionario():
    def __init__(self):
        self.nome = ""
        self.salario = 0.0
        self.cargo = ""
    
    def add(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

class CalculadoraDeSalario():
    def __init__(self):
        self.func = func
        
    def calculaSal(self, func):
        if func.cargo == "desenvolvedor":
            return dezOuVintePerCentoDesconto(func)
        else :
            return quinzeOuVinteCincoPerCentoDesconto(func)

    def quinzeOuVinteCincoPerCentoDesconto(self, func):
        if self.func.salario<2500:
            return self.func.salario*0.85
        return self.func.salario*0.75

    def dezOuVintePerCentoDesconto(self, func):
        if self.func.salario>3000:
            return self.func.salario*0.8
        return self.func.salario*0.9

class Testing(unittest.TestCase):
    def setUp(self):
        self.func = Funcionario()
        self.calc = CalculadoraDeSalario()
        self.esperado = 0

    def test_dev(self):
        self.func.add("Arthur", 3050, "desenvolvedor")
        self.esperado = 3050*0.9
        self.assertEqual(self.calc.calculaSal(self.func), self.esperado)

    def test_dois(self):
        self.func.add("Marcelo", 2000, "dba")
        self.esperado = 2000*0.85
        self.assertEqual(self.calc.calculaSal(self.func), self.esperado)

    def test_tres(self):
        self.func.add("Andre", 5000, "dba")
        self.esperado = 5000*0.75
        self.assertEqual(self.calc.calculaSal(self.func), self.esperado)

    def test_quatro(self):
        self.func.add("Guarato", 3000, "desenvolvedor")
        self.esperado = 3000*0.8
        self.assertEqual(self.calc.calculaSal(self.func), self.esperado)
    
