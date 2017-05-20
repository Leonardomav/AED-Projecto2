import gerador
import time
import os.path

def bruteForce(map):
    origem = map.getOrigem()

    listaCidades = list(range(map.numVertices))
    listaCidades.remove(origem.getId())
    caminhos = permutations(listaCidades)
    result={}

    for rideIndex in range(len(caminhos)):
        dist=0
        ride = caminhos[rideIndex]

        for i in range(len(ride)):
            if i==0:
                dist+=origem.getWeight(map.getVertex(ride[i]))
            else:
                dist+=map.getVertex(ride[i-1]).getWeight(map.getVertex(ride[i]))

        dist += origem.getWeight(map.getVertex(ride[i]))
        result.setdefault(dist,[])
        result[dist].append(ride)

    return result

def shortestPath(map,tarefa):
    start = time.time()

    short=[None, None]
    temp=None
    checked=set()

    origem = map.getOrigem()
    origemID = origem.getId()
    listaCidades = list(range(map.numVertices))
    listaCidades.remove(origemID)
    caminhos = permutations(listaCidades)

    for rideIndex in range(len(caminhos)):
        breaker=0
        ride = caminhos[rideIndex]
        temp=None
        if(tarefa==2 or (str(ride[::-1]) not in checked)):
            for j in range(len(ride)):
                if j == 0:
                    if temp == None: #so para teste
                        temp = origem.getWeight(map.getVertex(ride[j]))

                else:
                    if temp != None: #so para teste
                        temp = temp + map.getVertex(ride[j-1]).getWeight(map.getVertex(ride[j]))

                if rideIndex != 0:
                    if short[0] != None and temp != None:
                        if temp > short[0]:
                            breaker = 1
                            break

            if breaker == 0:
                if temp != None: #so para teste
                    temp = temp + map.getVertex(ride[len(ride)-1]).getWeight(origem)

                if rideIndex == 0:
                    if short[0] == None: #so para teste
                        short[0] = temp
                        short[1] = ride
                else:
                    if short[0] != None: #so para teste
                        if temp < short[0]:
                            short[0] = temp
                            short[1] = ride



            checked.add(str(ride))

    short[1].insert(0,origemID)
    short[1].append(origemID)

    return short


def permutations(lista):
    if lista:
        final = []
        for x in lista:
            temp = lista[:];
            temp.remove(x)
            for p in permutations(temp):
                final.append([x]+p)
        return final
    else:
        return [[]]


def shortestPathRecursivoOld(map,atual,visitados,caminhos,distancia):
    menor=0

    if(caminhos!={}):
        menor = min(caminhos.keys())

    visited = 0
    coneccoes = atual.getConnectedTo()

    for vizinho in atual.getConnections():

        if vizinho.getId() not in visitados:
            peso=atual.getWeight(vizinho)
            visited = 1

            if(menor==0 or distancia+peso<menor):
                visitadosN = visitados.copy()
                visitadosN.append(atual.getId())
                caminhos=shortestPathRecursivo(map,vizinho, visitadosN, caminhos, distancia + peso)

    if visited != 1:
        visitados.extend([atual.getId(),visitados[0]])
        distancia = distancia + atual.getWeight(map.getVertex(visitados[0]))

        caminhos.setdefault(distancia, [])
        caminhos[distancia].append(visitados)

    return caminhos


def shortestPathRecursivo(map,atual,visitados,caminhos,distancia):
    menor=0

    if(caminhos!={}):
        menor = min(caminhos.keys())

    visited = 0
    coneccoes = dict(atual.getConnectedTo())

    while coneccoes != {}:
        minimo = [None,None]
        for v in coneccoes.keys():
            if (minimo == [None,None]) or (minimo[1]>coneccoes[v]):
                minimo[0] = v
                minimo[1] = coneccoes[v]

        del coneccoes[minimo[0]]
        vizinho = minimo[0]

        if vizinho.getId() not in visitados:
            peso=minimo[1]
            visited = 1

            if(menor==0 or distancia+peso<menor):
                visitadosN = visitados.copy()
                visitadosN.append(atual.getId())
                caminhos=shortestPathRecursivo(map,vizinho, visitadosN, caminhos, distancia + peso)

    if visited != 1:
        visitados.extend([atual.getId(),visitados[0]])
        distancia = distancia + atual.getWeight(map.getVertex(visitados[0]))

        caminhos.setdefault(distancia, [])
        caminhos[distancia].append(visitados)

    return caminhos


def writeInFile(map,result,mapStr,tarefa,numCity,algorithm):
    fileName = "Tarefa_"+str(tarefa)+"_"+str(numCity)+"_"+str(algorithm)

    if os.path.exists(fileName):
        file = open(fileName, 'a')
    else:
        file = open(fileName, 'w')

    origem = map.getOrigem()
    file.write("Tarefa " + str(tarefa) + " and starts in " + str(origem.getId())+' and used the ' + str(result[3])+"\n")

    file.write(mapStr)

    file.write("The shortest path is " + str(result[1]) + " with a size of " + str(result[0]) + ' and takes '+ str(result[2])+' seconds. \n\n')
    file.close()

def geraMapa(num, cenarios):

    if cenarios[0]:
        tarefa=1
    elif cenarios[1]:
        tarefa=2

    g=gerador.Gerador()
    g.gera(int(num),tarefa)
    map=g.getMap()
    print(map.getGraph())
    print("Origem - " +  str(map.getOrigem().getId()))

    return map

def main(map, cenarios, algoritmo):

    if cenarios[0]:
        tarefa=1
    elif cenarios[1]:
        tarefa=2

    numCity = len(list(range(map.numVertices)))

    mapStr = ""
    for vertice in map.getGraph():
        for i in range(1,len(vertice)):
            mapStr = mapStr + (str(vertice[0]) + '-' +str(vertice[i][1]) + '->' +str(vertice[i][0]) + '  ')

        mapStr = mapStr + ('\n')

    if(algoritmo == 3):
        start = time.process_time()
        result = shortestPathRecursivo(map,map.getOrigem(),[],{},0)
        timeElapsed=time.process_time()-start
        print("\nFound shortest path at " + str(result[min(result.keys())]) + ", with a size of " + str(min(result.keys())) + ", in " + str(timeElapsed) + " seconds.")

        forMap1 = [min(result.keys()),result[min(result.keys())],timeElapsed,"Recursivo com Greedy"]
        writeInFile(map,forMap1,mapStr,tarefa,numCity,algoritmo)

        infoForGui = []
        infoForGui.extend([mapStr, map.getOrigem().getId(),min(result.keys()),result[min(result.keys())],str(timeElapsed)])

    #--------------------------------------------------------------
    if(algoritmo == 2):

        start = time.process_time()
        result = shortestPathRecursivoOld(map,map.getOrigem(),[],{},0)
        timeElapsed=time.process_time()-start
        print("\nFound shortest path at " + str(result[min(result.keys())]) + ", with a size of " + str(min(result.keys())) + ", in " + str(timeElapsed) + " seconds.")

        forMap1 = [min(result.keys()),result[min(result.keys())],timeElapsed,"Recursivo"]
        writeInFile(map,forMap1,mapStr,tarefa,numCity,algoritmo)

        infoForGui = []
        infoForGui.extend([mapStr, map.getOrigem().getId(),min(result.keys()),result[min(result.keys())],str(timeElapsed)])

    #--------------------------------------------------------------

    if(algoritmo == 1):
        start = time.process_time()
        result=shortestPath(map,tarefa)
        timeElapsed=time.process_time()-start
        print("\nFound shortest path at " + str(result[1]) + ", with a size of " + str(result[0]) + ", in " + str(timeElapsed) + " seconds.")

        result.extend([timeElapsed,"Brute Force Optimizado"])
        forMap2=result
        writeInFile(map,forMap2,mapStr,tarefa,numCity,algoritmo)

        infoForGui = []
        infoForGui.extend([mapStr, map.getOrigem().getId(),result[0],result[1],str(timeElapsed)])

    #--------------------------------------------------------------

    if(algoritmo == 0):
        start = time.process_time()
        result = bruteForce(map)
        timeElapsed=time.process_time()-start
        print("\nFound shortest path at " + str(result[min(result.keys())]) + ", with a size of " + str(min(result.keys())) + ", in " + str(timeElapsed) + " seconds.")

        forMap3 = [min(result.keys()),result[min(result.keys())],timeElapsed,"Brute Force"]
        writeInFile(map,forMap3,mapStr,tarefa,numCity,algoritmo)

        infoForGui = []
        infoForGui.extend([mapStr, map.getOrigem().getId(),min(result.keys()),result[min(result.keys())],str(timeElapsed)])

    return infoForGui
