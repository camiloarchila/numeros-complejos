"""
Created on Thu Aug 13 11:39:28 2020

@author: Camilo
"""
import unittest
import libreriac_cuantica
import math


class unit_calculadora(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(libreriac_cuantica.suma([-6, 10], [15, -5]), [9, 5])

    def test_mult(self):
        self.assertEqual(libreriac_cuantica.producto([-6, 10], [15, -5]), [-40, 180])

    def test_resta(self):
        self.assertEqual(libreriac_cuantica.resta([-6, 10], [15, -5]), [-21, 15])

    def test_division(self):
        self.assertEqual(libreriac_cuantica.division([-6, 10], [15, -5]), [-0.56, 0.48])

    def test_modulo(self):
        self.assertEqual(libreriac_cuantica.modulo([-3, 4]), 5)
        self.assertEqual(libreriac_cuantica.modulo([-3, -4]), 5)
        self.assertEqual(libreriac_cuantica.modulo([3, 4]), 5)
        self.assertEqual(libreriac_cuantica.modulo([3, -4]), 5)

    def test_conjugado(self):
        self.assertEqual(libreriac_cuantica.conjugado([-45, -10]), [-45, 10])

    def test_polarcart(self):
        self.assertEqual(libreriac_cuantica.polar_c((math.sqrt(2), (math.pi*3)/4)), (-1.0, 1.0))

    def test_cartepoalr(self):
        self.assertEqual(libreriac_cuantica.carte_p((-1.0, 1.0)), (math.sqrt(2), 135.0))
        self.assertEqual(libreriac_cuantica.carte_p((2.0, 1.0)), (math.sqrt(5), 26.56505117707799))
        self.assertEqual(libreriac_cuantica.carte_p((-3.0, -4.0)), (5, 233.13010235415598))

    def test_fase(self):
        self.assertEqual(libreriac_cuantica.fase_c((-6, 15)), 111.80140948635182)
        self.assertEqual(libreriac_cuantica.fase_c((6, -15)), 291.8014094863518)
        self.assertEqual(libreriac_cuantica.fase_c((6, 15)), 68.19859051364818)
        self.assertEqual(libreriac_cuantica.fase_c((-6, -15)), 248.19859051364818)


unittest.main()