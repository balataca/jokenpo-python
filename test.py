import unittest
from game import compareChoices

class TestCases(unittest.TestCase):
    def test_rock_rock(self):
        result = compareChoices("pedra", "pedra")
        self.assertEqual(result, "empate")

    def test_rock_paper(self):
        result = compareChoices("pedra", "papel")
        self.assertEqual(result, "Jogador 2 ganhou!")
    
    def test_rock_scissor(self):
        result = compareChoices("pedra", "tesoura")
        self.assertEqual(result, "Jogador 1 ganhou!")

    def test_paper_rock(self):
        result = compareChoices("papel", "pedra")
        self.assertEqual(result, "Jogador 1 ganhou!")
    
    def test_paper_paper(self):
        result = compareChoices("papel", "papel")
        self.assertEqual(result, "empate")

    def test_paper_scissor(self):
        result = compareChoices("papel", "tesoura")
        self.assertEqual(result, "Jogador 2 ganhou!")

    def test_scissor_rock(self):
        result = compareChoices("tesoura", "pedra")
        self.assertEqual(result, "Jogador 2 ganhou!")
    
    def test_scissor_paper(self):
        result = compareChoices("tesoura", "papel")
        self.assertEqual(result, "Jogador 1 ganhou!")

    def test_scissor_scissor(self):
        result = compareChoices("tesoura", "tesoura")
        self.assertEqual(result, "empate")

unittest.main()