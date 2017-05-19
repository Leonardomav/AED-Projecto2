import random
import vertex
import graph

class Gerador:
    def __init__(self):
        self.map=graph.Graph()
        self.numCity=0

    def gera(self,n,flag):
        dobro = n * 2
        if flag == 1:
            aleatorio = iter(random.sample(range(10,((dobro*dobro+dobro)//2)+10), ((n*n)+n)//2))
        else:
            aleatorio = iter(random.sample(range(10,((dobro*dobro+dobro))+10), ((n*n)+n)))

        self.numCity=n
        for i in range(self.numCity):
            self.map.addVertex(i)
        min=0;
        max=self.numCity;
        for i in range(self.numCity):
            min=min+1;
            for j in range(min, max):
                if(j != i):
                    if flag == 1:
                        cost = next(aleatorio)
                        self.map.addEdge(i,j,cost,cost,flag)
                    else:
                        cost = next(aleatorio)
                        costN = next(aleatorio)
                        self.map.addEdge(i,j,cost,costN,flag)

        self.map.setOrigem(random.randint(0,self.numCity-1))

    def getNumCity(self):
        return numCity;

    def getMap(self):
        return self.map
