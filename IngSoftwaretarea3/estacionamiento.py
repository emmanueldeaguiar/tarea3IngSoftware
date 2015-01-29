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
    
class Tupla(object):
    
    def __init__(self,offset,tipo):
        self.__offset = int(offset)
        self.__tipo = int(tipo)
    
    def getOffset(self):
        return self.__offset
    
    def getTipo(self):
        return self.__tipo
    
class Estacionamiento(object):
    
    def __init__(self,cap):
        self.capacidad = cap
        self.reservas = []
    
    '''Metodo creado a partir del algoritmo de Marzullo'''
    def buscarSuperposiciones(self,reservas_en_estacionamiento):
        best = 0
        cnt = 0
        beststart = 0
        bestend = 0
        p = 0
        tuplas = []
        '''Se convierten las reservas en el formato Tupla: <offset,tipo>'''
        for r in reservas_en_estacionamiento:
            pi = Tupla(r.getInicio(),-1)
            pf = Tupla(r.getFin(),+1)
            tuplas.append(pi)
            tuplas.append(pf)
        
        '''Ordeno la lista de tuplas'''
        self.ordenarTuplas(tuplas) 
           
        while p < len(tuplas):
            cnt = cnt - tuplas[p].getTipo()
            if cnt > best:
                best = cnt
                beststart = tuplas[p].getOffset()
                if p < len(tuplas) -1:
                    bestend = tuplas[p+1].getOffset()                
            else:
                pass             
            p+=1
            
        superposicion = [best,beststart,bestend]
        return superposicion
    
    '''Ordena las tuplas segun el algoritmo de Marzullo'''
    def ordenarTuplas(self,listaDeTuplas):
        tam = len(listaDeTuplas)
        for i in range(1,tam):
            for j in range(0,tam-i):
                if(listaDeTuplas[j].getOffset() > listaDeTuplas[j+1].getOffset()):
                    k = listaDeTuplas[j+1]
                    listaDeTuplas[j+1] = listaDeTuplas[j]
                    listaDeTuplas[j] = k;     
        for j in range(1,tam):
            for i in range(0,tam-1):
                if(listaDeTuplas[i].getOffset() == listaDeTuplas[i+1].getOffset()):
                    if(listaDeTuplas[i].getTipo() == -1 and listaDeTuplas[i+1].getTipo() == 1 ):
                        k = listaDeTuplas[i+1]
                        listaDeTuplas[i+1] = listaDeTuplas[i]
                        listaDeTuplas[i] = k; 
                    elif(listaDeTuplas[i].getTipo() == 1 and listaDeTuplas[i+1].getTipo() == -1 ):
                        pass
    
    def reservar(self,intervalo):
        if (intervalo.getInicio()<6) or (intervalo.getFin() > 18):
            print('El estacionamiento solo funciona de 6 a 18')
            return False
        elif(intervalo.getFin()<intervalo.getInicio()):
            print('La hora de entrada debe ser menor que la hora de salida.')
            return False
            
        self.reservas.append(intervalo)
        superposicion = self.buscarSuperposiciones(self.reservas)
        return True
        