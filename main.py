from arboIterativa import Arbol

estadoInicial = [["1","2","5"],["4"," ","8"],["3","6","7"]]
estadoObjetivo = [[" ","1","2"],["3","4","5"],["6","7","8"]]
#estadoObjetivo = [["1","2","5"],["4","8","7"],["3","6"," "]]

eightPuzzle = Arbol(estadoInicial,estadoObjetivo)

eightPuzzle.iniciaBusqueda()