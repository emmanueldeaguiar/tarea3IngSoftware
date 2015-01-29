'''
Created on Jan 28, 2015

@author: Emmanuel
'''
import unittest
from estacionamiento import *


class TestReservar(unittest.TestCase):


    def testReservarExiste(self):
        reserva = Reserva(6,7)
        est = Estacionamiento(10)
        est.reservar(reserva)
        
    def testReservarPuesto(self):
        reserva = Reserva(6,7)
        est = Estacionamiento(10)
        self.assertEqual(est.reservar(reserva), True)
        
    def testReservarFueraHorario(self):
        reserva = Reserva(3,7)
        est = Estacionamiento(10)
        self.assertFalse(est.reservar(reserva))
        
    def testReservarHorasIntercambiadas(self):
        reserva = Reserva(8,7)
        est = Estacionamiento(10)
        self.assertFalse(est.reservar(reserva))
        
    def testAlmacenarReserva(self):
        reserva = Reserva(7,12)
        est = Estacionamiento(10)
        est.reservar(reserva)
        self.assertEqual(est.reservas[0].getInicio(),7)
        self.assertEqual(est.reservas[0].getFin(),12)
        
    def testComprobarDisponibilidadIntervalo(self):
        reserva = Reserva(7,12)
        est = Estacionamiento(10)
        est.comprobarDisponibilidad(est.reservas)
        