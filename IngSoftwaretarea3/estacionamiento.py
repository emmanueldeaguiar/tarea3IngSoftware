'''
Created on 27/1/2015

@author: Daniel Pelayo
         Emanuel De Aguiar
'''
from test.test_buffer import cap
class Reserva(object):
    

    def __init__(self, inicio, fin):
        self.__inicio = int(inicio)
        self.__fin = int(fin)
    def getInicio(self):
        return self.__inicio    
    def getFin(self):
        return self.__fin
    
class Estacionamiento(object):
    
    def __init__(self,cap):
        self.capacidad = cap
        self.reservas = []
        
    def comprobarDisponibilidad(self,lista):
        pass

    def reservar(self,intervalo):
        if (intervalo.getInicio()<6) or (intervalo.getFin() > 18):
            print('El estacionamiento solo funciona de 6 a 18')
            return False
        elif(intervalo.getFin()<intervalo.getInicio()):
            print('La hora de entrada debe ser menor que la hora de salida.')
            return False
            
        self.reservas.append(intervalo)
        return True
        