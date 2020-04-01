import unittest

class Produto(object):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __eq__(self, outro):
        if outro == None:
            return False
        if not isinstance(outro, Produto):
            return False
        if self.nome == outro.nome and self.preco == outro.preco:
            return True
        else:   
            return False

class Carrinho(object):
    def __init__(self):
        self.lista = []

    def add(self, produto):
        self.lista.append(produto)

    def imprime(self):
        for produto in self.lista:
            print(produto.nome, produto.preco)

    def getLista(self): #Java feels
            return self.lista

    def delete(self):
        del self.lista[:]

    def maior_e_menor(self):
        maior = None
        menor = None
        for produto in self.lista:
            if (menor == None or produto.preco < menor.preco):
                menor = produto
            elif (maior == None or produto.preco > maior.preco):
                maior = produto
        return maior, menor
        

class Testing_Arthur(unittest.TestCase):
    def setUp(self):
        self.carro = Carrinho()
        self.esperado = (None, None)

    def test_um(self):
        self.carro.add(Produto("Headset", 75))
        self.carro.add(Produto("Joystick", 300))
        self.carro.add(Produto("Cubo de guitarra", 175))
        self.assertEqual(self.carro.maior_e_menor()[0].preco, Produto("Joystick", 300).preco)
        self.assertEqual(self.carro.maior_e_menor()[1].preco, Produto("Joystick", 300).preco)  #falha proposital

    def test_dos(self):
        self.carro.add(Produto("Pedaleira", 1350))
        self.esperado = (1350, 1350)
        print(self.carro.maior_e_menor(maior, menor))
        self.assertEqual(self.carro.maior_e_menor()[0].preco, self.esperado[0]) 
        self.assertEqual(self.carro.maior_e_menor()[1].preco, self.esperado[1])
        
    def teste_free(self):
        self.carro.add(Produto("Cabo P10", 35))
        self.carro.add(Produto("Pacote com 50 palhetas", 77))
        self.carro.add(Produto("Pacote com 12 cordas de guitarra",75))
        self.esperado = (77,35)
        self.assertEqual(self.carro.maior_e_menor()[0].preco, self.esperado[0])
        self.assertEqual(self.carro.maior_e_menor()[1].preco, self.esperado[1])

    def teste_cuatro(self):
        self.carro.add(Produto("Black Monday", 2))
        self.carro.add(Produto("Black Tuesday", 0))
        self.carro.add(Produto("Black Wednesday", -87))
        self.carro.add(Produto("Black Thursday", -357))
        self.carro.add(Produto("Black Friday", 357))
        self.esperado = (357, -357)
        self.assertEqual(self.carro.maior_e_menor()[0].preco, self.esperado[0])
        self.assertEqual(self.carro.maior_e_menor()[1].preco, self.esperado[1])


class Testing_Lucas(unittest.TestCase):
    def setUp(self):
        self.car = Carrinho()

    def test_one(self):
        self.car.adiciona(Produto("Geladeira", 3000))
        self.car.adiciona(Produto("Teclado", 150))
        self.car.adiciona(Produto("TekPix", 3001))
        self.assertEqual(self.car.maiorMenor()[0], Produto("TekPix", 3001))
        self.assertEqual(self.car.maiorMenor()[1], Produto("Teclado", 150))

    def test_two(self):
        self.car.adiciona(Produto("Notebook", 2500))
        self.esperado = (2500, 2500)
        self.assertEqual(self.car.maiorMenor(), self.esperado)

    def test_three(self):
        self.car.adiciona(Produto("HeadPhone Sony", 150))
        self.car.adiciona(Produto("Arduino Uno", 150))
        self.car.adiciona(Produto("MP3", 149))
        self.esperado = (150, 149)
        self.assertEqual(self.car.maiorMenor(), self.esperado)

    def test_four(self):
        self.car.adiciona(Produto("Item 1",151))
        self.car.adiciona(Produto("Item 2",1))
        self.car.adiciona(Produto("Item 3",0))
        self.car.adiciona(Produto("Item 4",9999))
        self.car.adiciona(Produto("Item 5",8000))
        self.car.adiciona(Produto("Item 6",3))
        self.car.adiciona(Produto("Item 7",-9999))
        self.esperado = (9999, -9999)
        self.assertEqual(self.car.maiorMenor(), self.esperado)
