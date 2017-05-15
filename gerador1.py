from random import randint
import vertex
import graph

class Gerador:
    def __init__(self,n):
        self.map=graph.Graph()
        self.numCity=n

    def gera(self):
        for i in range(self.numCity):
            self.map.addVertex(i)

        for i in range(self.numCity):
            for j in range(self.numCity):
                if j != i:
                    self.map.addEdge(i,j,randint(1,10),None,1)
    def printMap(self):
        for i in range(self.numCity):
            print(str(self.map.vertList[i]))

gerador=Gerador(5)
gerador.gera()
gerador.printMap()
