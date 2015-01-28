'''
Created on Jan 28, 2015

@author: Emmanuel
'''
import unittest
from estacionamiento import *


class TestReservar(unittest.TestCase):


    def testReservarExiste(self):
        reserva = Reserva(6,7)
        reservar(reserva)
        
    def testReservarPuesto(self):
        reserva = Reserva(6,7)
        self.assertEqual(reservar(reserva), True)
        
    def testReservarFueraHorario(self):
        reserva = Reserva(3,7)
        self.assertFalse(reservar(reserva))
        
    def testReservarHorasIntercambiadas(self):
        reserva = Reserva(8,7)
        self.assertFalse(reservar(reserva))