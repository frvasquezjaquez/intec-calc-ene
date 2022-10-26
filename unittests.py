
import unittest
from unittest import result
from calc import Calc

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()
    
    def test_sumar_2_2(self):
        mycalc = Calc()
        resultado_deseado = 4
        resultado_calculo_suma = mycalc.sumar(2, 2)
        self.assertEquals(resultado_deseado, resultado_calculo_suma)
    
    def test_sumar_5_30(self):
        mycalc = Calc()
        resultado_deseado = 35
        resultado_calculo_suma = mycalc.sumar(5, 30)
        self.assertEquals(resultado_deseado, resultado_calculo_suma)
  
    def test_restar_2_2(self):
        mycalc = Calc()
        resultado_esperado = 0
        resultado_calculo_resta = mycalc.restar(2, 2)
        self.assertEquals(resultado_esperado, resultado_calculo_resta)
    
    def test_restar_100_50(self):
        mycalc = Calc()
        resultado_esperado = 50
        resultado_calculo_resta = mycalc.restar(100, 50)
        self.assertEquals(resultado_esperado, resultado_calculo_resta)

if __name__ == '__main__':
    unittest.main()