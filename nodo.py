class Nodo:

    def __init__(self):

        self.nodoPadre = []
        self.data = []
        self.profundidad = 0
        self.hijos = []
        #Coordenadas del espacio en blanco
        self.x = 0
        self.y = 0

    def setPadre(self, e):

        self.nodoPadre = e

    def setData(self, e):

        self.data = e

    def sonIguales(self, dataPadre):

        if dataPadre == self.data:

            return True
        return False

    def printHijos(self):

        counter = 1
        for i in self.hijos:

            print("Hijo numero: ",counter)
            print(i.printData(),'\n')
            counter+=1

    def printData(self):

        for i in self.data:

            print(i,'\n')