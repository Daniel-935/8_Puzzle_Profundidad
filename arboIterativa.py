import copy
import sys
import os
from time import time

from nodo import Nodo

class Arbol:

    def __init__(self,nInicial,nObjetivo):

        self.raiz = 0
        self.objetivo = nObjetivo
        self.estadoInicial = nInicial
        self.costoFinal = 0
        self.encontroSolucion = False
        self.profundidadMax = 0

    def isSolution(self, nodo):

        if nodo.data == self.objetivo:
            print("**************************************")
            print("Se llego a la solucion\n")
            nodo.printData()
            print("\nNivel de profundidad: ",nodo.profundidad)
            print("Costo del camino: ",self.costoFinal)
            self.encontroSolucion == True
            #os.system("pause")
            sys.exit()

    def funcionSucesor(self,nodoPadre):

        #Comprueba si el nodo es solucion
        if self.isSolution(nodoPadre) == True:
            return
        #Comprueba el nivel de profundidad para determinar si encuentra solucion o no
        elif nodoPadre.profundidad < self.profundidadMax:
             
            #Moverlo derecha
            if nodoPadre.x+1 < 3:

                nuevoNodo = Nodo()
                #Toma la matriz del padre
                dataAux = copy.deepcopy(nodoPadre.data)

                #Hace el intercambio del numero y el espacio vacio
                aux = dataAux[nodoPadre.y][nodoPadre.x+1]
                dataAux[nodoPadre.y][nodoPadre.x+1] = " "
                dataAux[nodoPadre.y][nodoPadre.x] = aux
                
                #Se coloca al nuevo nodo su nodo padre
                nuevoNodo.nodoPadre = nodoPadre.data
                nuevoNodo.data = copy.deepcopy(dataAux)

                #Si no es igual a su padre, se agrega como hijo y este mismo desarrolla sus hijos
                if nuevoNodo.sonIguales(nodoPadre.nodoPadre) == False:

                    #Coloca las coordenadas del espacio vacio
                    nuevoNodo.x = nodoPadre.x+1
                    nuevoNodo.y = nodoPadre.y
                    #Agrega el nivel de profundidad
                    nuevoNodo.profundidad = nodoPadre.profundidad+1
                    self.costoFinal+=1
                    nuevoNodo.printData()
                    print("\n")
                    nodoPadre.hijos.append(nuevoNodo)
                    #Desarrolla el nuevo nodo sus propios hijos por la misma rama
                    self.funcionSucesor(nuevoNodo)

            #Moverse a la izquierda
            if nodoPadre.x-1>=0:

                nuevoNodo = Nodo()
                #Toma la matriz del padre
                dataAux = copy.deepcopy(nodoPadre.data)

                #Hace el intercambio del numero y el espacio vacio
                aux = dataAux[nodoPadre.y][nodoPadre.x-1]
                dataAux[nodoPadre.y][nodoPadre.x-1] = " "
                dataAux[nodoPadre.y][nodoPadre.x] = aux
                
                #Se coloca al nuevo nodo su nodo padre
                nuevoNodo.nodoPadre = nodoPadre.data
                nuevoNodo.data = copy.deepcopy(dataAux)

                #Si no es igual a su padre, se agrega como hijo
                if nuevoNodo.sonIguales(nodoPadre.nodoPadre) == False:

                    #Coloca las coordenadas del espacio vacio
                    nuevoNodo.x = nodoPadre.x-1
                    nuevoNodo.y = nodoPadre.y
                    nuevoNodo.profundidad = nodoPadre.profundidad+1
                    self.costoFinal+=1
                    nuevoNodo.printData()
                    print("\n")
                    nodoPadre.hijos.append(nuevoNodo)
                    #Desarrolla el nuevo nodo sus propios hijos por la misma rama
                    self.funcionSucesor(nuevoNodo)

            #Moverse arriba
            if nodoPadre.y-1>=0:

                nuevoNodo = Nodo()
                #Toma la matriz del padre
                dataAux = copy.deepcopy(nodoPadre.data)

                #Hace el intercambio del numero y el espacio vacio
                aux = dataAux[nodoPadre.y-1][nodoPadre.x]
                dataAux[nodoPadre.y-1][nodoPadre.x] = " "
                dataAux[nodoPadre.y][nodoPadre.x] = aux
                
                #Se coloca al nuevo nodo su nodo padre
                nuevoNodo.nodoPadre = nodoPadre.data
                nuevoNodo.data = copy.deepcopy(dataAux)

                #Si no es igual a su padre, se agrega como hijo
                if nuevoNodo.sonIguales(nodoPadre.nodoPadre) == False:

                    #Coloca las coordenadas del espacio vacio
                    nuevoNodo.x = nodoPadre.x
                    nuevoNodo.y = nodoPadre.y-1
                    nuevoNodo.profundidad = nodoPadre.profundidad+1
                    self.costoFinal+=1
                    nuevoNodo.printData()
                    print("\n")
                    nodoPadre.hijos.append(nuevoNodo)
                    #Desarrolla el nuevo nodo sus propios hijos por la misma rama
                    self.funcionSucesor(nuevoNodo)

            #Moverse abajo
            if nodoPadre.y+1<3:

                nuevoNodo = Nodo()
                #Toma la matriz del padre
                dataAux = copy.deepcopy(nodoPadre.data)

                #Hace el intercambio del numero y el espacio vacio
                aux = dataAux[nodoPadre.y+1][nodoPadre.x]
                dataAux[nodoPadre.y+1][nodoPadre.x] = " "
                dataAux[nodoPadre.y][nodoPadre.x] = aux
                
                #Se coloca al nuevo nodo su nodo padre
                nuevoNodo.nodoPadre = nodoPadre.data
                nuevoNodo.data = copy.deepcopy(dataAux)

                #Si no es igual a su padre, se agrega como hijo
                if nuevoNodo.sonIguales(nodoPadre.nodoPadre) == False:

                    #Coloca las coordenadas del espacio vacio
                    nuevoNodo.x = nodoPadre.x
                    nuevoNodo.y = nodoPadre.y+1
                    nuevoNodo.profundidad = nodoPadre.profundidad+1
                    self.costoFinal+=1
                    nuevoNodo.printData()
                    print("\n")
                    nodoPadre.hijos.append(nuevoNodo)
                    #Desarrolla el nuevo nodo sus propios hijos por la misma rama
                    self.funcionSucesor(nuevoNodo)

    
    def iniciaBusqueda(self):
    
        nodoRaiz = Nodo()
        nodoRaiz.setData(copy.deepcopy(self.estadoInicial))
        nodoRaiz.setPadre(copy.deepcopy(self.estadoInicial))
        nodoRaiz.x = 1
        nodoRaiz.y = 1
        
        self.raiz = nodoRaiz
        self.raiz.printData()
        print("\n")

        #Comienza a realizar la busqueda en profundidad
        #El Metodo es recursivo y tiene limite que se incrementa cada vez ya que es iterativo
        self.funcionSucesor(self.raiz)
        #Comprueba si al final se encontro solucion o no
        if self.encontroSolucion == False:

            self.profundidadMax+=1
            self.costoFinal = 0
            self.iniciaBusqueda()
        
    
    