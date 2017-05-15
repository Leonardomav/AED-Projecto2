import vertex

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = vertex.Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

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


    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
