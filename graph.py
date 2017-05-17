import vertex

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.origem = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = vertex.Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        return self.vertList[n]

    def addEdge(self,f,t,cost1,cost2,generator):
        if f not in self.vertList:
            nv = self.addVertex(f)
            if t not in self.vertList:
                nv = self.addVertex(t)
        if generator == 1:
            self.vertList[f].addNeighbor(self.vertList[t], cost1)
            self.vertList[t].addNeighbor(self.vertList[f], cost1)
        elif generator == 2:
            self.vertList[t].addNeighbor(self.vertList[f], cost1)
            self.vertList[f].addNeighbor(self.vertList[t], cost2)

    def getVerticesList(self):
        return self.vertList.keys()

    def getOrigem(self):
        return self.vertList[self.origem]

    def setOrigem(self, n):
        self.origem = n

    def getGraph(self):
        connections=[]
        for i in range(self.numVertices):
            connections.append(self.vertList[i].connections())

        return connections

    def __contains__(self,n):
        return n in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())
