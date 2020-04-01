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

    def get_salario(self):
        if (self.cargo == "desenvolvedor"):
            if (self.salario > 3000):
                return self.salario * 0.8
            return self.salario * 0.9
        if (self.salario > 2500):
            return self.salario * 0.75
        return self.salario * 0.85


class Testing_Arthur(unittest.TestCase):
    def setUp(self):
        self.func = Funcionario()
        self.esperado = 0

    def test_dev(self):
        self.func.add("Arthur", 3000, "desenvolvedor")
        self.esperado = 3000*0.9
        self.assertEqual(self.func.get_salario(), self.esperado)

    def test_dois(self):
        self.func.add("Breyt", 3700, "desenvolvedor")
        self.esperado = 3700*0.9 #error devia ser *0.8
        self.assertEqual(self.func.get_salario(), self.esperado)

    def test_tres(self):
        self.func.add("Ramos", 3570, "desenvolvedor")
        self.esperado = 3570*0.8
        self.assertEqual(self.func.get_salario(), self.esperado)

    def test_dba(self):
        self.func.add("Abreu",2500,"dba")
        self.esperado = 2500 * 0.85
        self.assertEqual(self.func.get_salario(), self.esperado)

    def test_dba1(self):
        self.func.add("A Lice", 3000, "dba")
        self.esperado = 3000*0.75
        self.assertEqual(self.func.get_salario(), self.esperado)
        

class Testing_Lucas(unittest.TestCase):
    def setUp(self):
        self.func = Funcionario()
        self.esperado = 0

    def test_desenvolvedor(self):
        # Menor ou igual a 3000 = 10% desconto
        self.func.add("Lucas",3000,"desenvolvedor")
        self.esperado = 3000 * 0.9
        self.assertEqual(self.func.get_salario(), self.esperado)

        # Maior que 3000 = 20% desconto
        self.func.add("Camila",3500,"desenvolvedor")
        self.esperado = 3500 * 0.9 # [ERRO] Deveria ser 0.8
        self.assertEqual(self.func.get_salario(), self.esperado)

        # Maior que 3000 = 20% desconto
        self.func.add("Camila",3000.01,"desenvolvedor")
        self.esperado = 3000.01 * 0.8
        self.assertEqual(self.func.get_salario(), self.esperado)

    def test_DBA(self):
        # Menor ou igual a 2500 = 15% desconto:
        self.func.add("Flavio",2500,"dba")
        self.esperado = 2500 * 0.85
        self.assertEqual(self.func.get_salario(), self.esperado)
        
        # Maior do que 2500 = 25% desconto:
        self.func.add("Alice",2500.10,"dba")
        self.esperado = 2500.10 * 0.85 # [ERRO] Deveria ser 0.75
        self.assertEqual(self.func.get_salario(), self.esperado)

        # Valor aleatorio acima 2500
        self.func.add("Alice",9999.99,"dba")
        self.esperado = 9999.99 * 0.75
        self.assertEqual(self.func.get_salario(), self.esperado)

        # Valor aleatorio abaixo 2500
        self.func.add("Thais",0,"dba")
        self.esperado = 0 * 0.85
        self.assertEqual(self.func.get_salario(), self.esperado)
        
    def test_testador(self):
        # Menor ou igual a 2500 = 15% desconto:
        self.func.add("Amaral",1800,"testador")
        self.esperado = 1800 * 0.85
        self.assertEqual(self.func.get_salario(), self.esperado)

        # Maior que 2500 = 25% desconto:
        self.func.add("Amaral",3000,"testador")
        self.esperado = 3000 * 0.75
        self.assertEqual(self.func.get_salario(), self.esperado)

