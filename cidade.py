class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def connections(self):
        vertexConnected=[x.id for x in self.connectedTo]
        vertexWeight=[self.connectedTo[x] for x in self.connectedTo]
        connections=[self.id]
        for i in range(len(vertexConnected)):
            connections.append([vertexConnected[i],vertexWeight[i]])

        return connections

    def getConnections(self):
        return self.connectedTo.keys()

    def getConnectedTo(self):
        return self.connectedTo

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
