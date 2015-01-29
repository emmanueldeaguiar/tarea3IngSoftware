'''
Created on Jan 28, 2015

@author: Daniel Pelayo         10-10539
@author: Emanuel De Aguiar     10-10179
'''
import unittest
from estacionamiento import *


class TestReservar(unittest.TestCase):


    def testReservarExiste(self): #TDD
        reserva = Reserva(6,7)
        est = Estacionamiento(10)
        est.reservar(reserva)
        
    def testReservarPuesto(self):#TDD
        reserva = Reserva(6,7)
        est = Estacionamiento(10)
        self.assertEqual(est.reservar(reserva), True)
        
    def testReservarFueraHorario(self):#TDD
        reserva = Reserva(3,7)
        est = Estacionamiento(10)
        self.assertFalse(est.reservar(reserva))
        
    def testReservarHorasIntercambiadas(self):#TDD
        reserva = Reserva(8,7)
        est = Estacionamiento(10)
        self.assertFalse(est.reservar(reserva))
        
    def testAlmacenarReserva(self):#TDD
        reserva = Reserva(7,12)
        est = Estacionamiento(10)
        est.reservar(reserva)
        self.assertEqual(est.reservas[0].getInicio(),7)
        self.assertEqual(est.reservas[0].getFin(),12)
        
    def testBuscarSuperposicionesExiste(self):#TDD
        est = Estacionamiento(10)
        est.buscarSuperposiciones(est.reservas)
        
    def testBuscarrSuperposiciones(self):#TDD
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
        
    def testReservarHorasLimite(self):  #Caso de Prueba Frontera
        est = Estacionamiento(10)
        r1 = Reserva(6,18)
        self.assertTrue(est.reservar(r1))
        
    def testReservarPuestoJusto(self): #Case por malicia
        est = Estacionamiento(1)
        r1 = Reserva(6,9)
        r2 = Reserva(11,15)
        r3 = Reserva(9,11)
        est.reservas = [r1,r2]
        self.assertTrue(est.reservar(r3))
        
    def testReservarPuestoYaReservado(self): #Caso de Prueba Frontera
        est = Estacionamiento(1)
        r1 = Reserva(6,9)
        r2 = Reserva(11,15)
        r3 = Reserva(8,12)
        est.reservas = [r1,r2]
        self.assertFalse(est.reservar(r3))
        
    def testComprobarListaDeHorasReservadas(self):
        est = Estacionamiento(1)
        r1 = Reserva(15,16)
        r2 = Reserva(16,17)
        r3 = Reserva(17,18)
        est.reservas = [r1,r2]
        est.reservar(r3)
        self.assertEqual(est.reservas,[r1,r2,r3])
        
        
        
        
    
        
        
        
        