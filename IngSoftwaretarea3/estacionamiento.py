'''
Created on 27/1/2015

@author: Daniel Pelayo
         Emanuel De Aguiar
'''
class Reserva(object):
    

    def __init__(self, inicio, fin):
        self.__inicio = int(inicio)
        self.__fin = int(fin)
    def getInicio(self):
        return self.__inicio    
    def getFin(self):
        return self.__fin

def reservar(reserva):
    if (reserva.getInicio()<6) or (reserva.getFin() > 18):
        print('El estacionamiento solo funciona de 6 a 18')
        return False
    elif(reserva.getFin()<reserva.getInicio()):
        print('La hora de entrada debe ser menor que la hora de salida.')
        return False
    else: 
        return True