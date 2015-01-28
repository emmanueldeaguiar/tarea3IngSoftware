'''
Created on Jan 28, 2015

@author: Emmanuel
'''
import unittest
from estacionamiento import *


class TestReservar(unittest.TestCase):


    def testReservarExiste(self):
        reservar(6,7)
        
    def testReservarPuesto(self):
        self.assertEqual(reservar(6, 7), True)
        
    def testReservarFueraHorario(self):
        self.assertFalse(reservar(3,7))