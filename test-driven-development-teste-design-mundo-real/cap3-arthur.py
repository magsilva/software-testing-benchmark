import unittest
import collections #OrderedDict 

class Conversor(object):
	def __init__(self):
		self.dic = collections.OrderedDict() #pra ficar bonitinho
	        self.dic["I"] = 1 #assim nao precisa abrir uma funcao 
	        self.dic["V"] = 5 #apenas pro dicionario ser armazenado
	        self.dic["X"] = 10
	        self.dic["L"] = 50
	        self.dic["C"] = 100
	        self.dic["D"] = 500
	        self.dic["M"] = 1000 

	def converte(self, rom): #wololo
		self.num = 0
		self.rom = rom
	        atual = 0 #valor do caracter atual
	        vizinho = 0 #valor do caracter a direita da posicao atual
	        for i in range(len(self.rom)-1, -1, -1):
	            m = 1
	            atual = self.dic[self.rom[i]]
	            if atual<vizinho: #se o numero atual for menor que o caracter da direita (ex: IX)
		        m = -1 #ele recebe o valor * -1 (IX recebe -1 e nao 1)
		    self.num+= c*m
		    m = 1
		    c_d = c
		return self.num

class Testing(unittest.TestCase):
    def setUp(self):
        self.conv = Conversor()
        self.previsao = None #tupla exige muito codigo desnecessario pra testar

    def test_one(self):
        self.previsao = 2
        self.assertEqual(self.conv.converte("II"), self.previsao) #numero simples

    def test_two(self):
        self.previsao = 19
        self.assertEqual(self.conv.converte("XIX"), self.previsao) #numero parcialmente complexo

    def test_three(self):
        self.previsao = 651
        self.assertEqual(self.conv.converte("DCL"), self.previsao) #feito para falhar

    def test_four(self):
        self.previsao = 1499
        self.assertEqual(self.conv.converte("MCDXCIX"), self.previsao) #numero complexo
