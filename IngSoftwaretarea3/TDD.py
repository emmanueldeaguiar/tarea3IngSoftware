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
        
    def testBuscarSuperposicionesExiste(self):
        est = Estacionamiento(10)
        est.buscarSuperposiciones(est.reservas)
        
    def testBuscarrSuperposiciones(self):
        est = Estacionamiento(10)
        r1 = Reserva(7,12)
        r2 = Reserva(7,12)
        r3 = Reserva(7,12)
        r4 = Reserva(7,12)
        r5 = Reserva(7,12)
        r6 = Reserva(7,12)
        r7 = Reserva(7,12)
        r8 = Reserva(7,12)
        r9 = Reserva(7,12)
        r10 = Reserva(7,12)
        est.reservas = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10]
        self.assertEqual(est.buscarSuperposiciones(est.reservas),[10,7,12])
    
    def testReservar_EstacionamientoLleno(self): #Caso de Prueba Frontera
        est = Estacionamiento(10)
        r1 = Reserva(7,12)
        r2 = Reserva(7,12)
        r3 = Reserva(7,12)
        r4 = Reserva(7,12)
        r5 = Reserva(7,12)
        r6 = Reserva(7,12)
        r7 = Reserva(7,12)
        r8 = Reserva(7,12)
        r9 = Reserva(7,12)
        r10 = Reserva(7,12)
        r11 = Reserva(7,12)
        est.reservas = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10]
        self.assertFalse(est.reservar(r11))
        
    def testReservar_EstacionamientoCasiLleno(self): #Caso de Prueba Frontera
        est = Estacionamiento(10)
        r1 = Reserva(7,12)
        r2 = Reserva(7,12)
        r3 = Reserva(7,12)
        r4 = Reserva(7,12)
        r5 = Reserva(7,12)
        r6 = Reserva(7,12)
        r7 = Reserva(7,12)
        r8 = Reserva(7,12)
        r9 = Reserva(7,12)
        r10 = Reserva(7,12)
        est.reservas = [r1,r2,r3,r4,r5,r6,r7,r8,r9]
        self.assertTrue(est.reservar(r10))
        
    def testReservar_EstacionamientoVacio(self): #Caso de Prueba Frontera
        est = Estacionamiento(10)        
        r1 = Reserva(7,12)
        self.assertTrue(est.reservar(r1))
        
    def testReservarHoraImposible(self): #Caso de Prueba Frontera
        est = Estacionamiento(10)        
        r1 = Reserva(7,7)
        self.assertFalse(est.reservar(r1))
        
    
        
        
        
        