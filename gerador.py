from random import randint
import vertex
import graph

class Gerador:
    def __init__(self):
        self.map=graph.Graph()
        self.numCity=0

    def gera(self,n,flag):
        self.numCity=n
        for i in range(self.numCity):
            self.map.addVertex(i)
        min=0;
        max=self.numCity;
        for i in range(self.numCity):
            min=min+1;
            for j in range(min, max):
                if(j != i):
                    self.map.addEdge(i,j,randint(10,100),randint(10,100),flag)

        self.map.setOrigem(randint(0,self.numCity-1))

    def getNumCity(self):
        return numCity;

    def getMap(self):
        return self.map
