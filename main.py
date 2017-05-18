import gerador
import time
import sys

def shortestPath(map,tarefa):
    start = time.time()
    print(map.getGraph())

    short=[None, None]
    temp=None
    checked=set()

    origem = map.getOrigem()
    print("\nOrigin - " + str(origem.getId()))
    listaCidades = list(range(map.numVertices))
    listaCidades.remove(origem.getId())
    caminhos = permutations(listaCidades)

    for rideIndex in range(len(caminhos)):
        breaker=0
        ride = caminhos[rideIndex]
        temp=None
        if (tarefa == 2) or ((str(ride[::-1]) not in checked) and tarefa==1):
            for j in range(len(ride)):
                if j == 0:
                    if temp == None: #so para teste
                #        print("entrei no j = 0")
                        temp = origem.getWeight(map.getVertex(ride[j]))

                else:
                    if temp != None: #so para teste
                #        print("entrei no j != 0")
                        temp = temp + map.getVertex(ride[j-1]).getWeight(map.getVertex(ride[j]))

                if rideIndex != 0:
                #    print("entrei no rideIndex != 0")
                    if short[0] != None and temp != None:
                        if temp > short[0]:
                            breaker = 1
                            break

            if breaker == 0:
                #print("entrei no breaker == 0")
                if temp != None: #so para teste
                    #print("depois entrei no temp != none")
                    temp = temp + map.getVertex(ride[len(ride)-1]).getWeight(origem)

                if rideIndex == 0:
                    #print("depois entrei no rideIndex == 0")
                    if short[0] == None: #so para teste
                        short[0] = temp
                        short[1] = ride
                else:
                    #print("depois entrei no else")
                    if short[0] != None: #so para teste
                        if temp < short[0]:
                            short[0] = temp
                            short[1] = ride


            #print(temp)
            checked.add(str(ride))
    timeElapsed = time.time()-start
    short.append(timeElapsed)
    short[1].insert(0, int(origem.getId()))
    short[1].append(int(origem.getId()))
    print("Time Elapsed -> " + str(short[2])+"s")
    print("The shortest path is " + str(short[1]) + " with a size of " + str(short[0]))

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

def writeInFile(map,result):
    file = open('grafosTestados.txt', 'a')
    origem = map.getOrigem()
    file.write("Starts in " + str(origem.getId())+'\n')
    for vertice in map.getGraph():
        for i in range(1,len(vertice)):
            file.write(str(vertice[0]) + '------' +str(vertice[i][1]) + '----->' +str(vertice[i][0]) + '\t')
        file.write('\n')


    file.write("The shortest path is " + str(result[1]) + " with a size of " + str(result[0]) + ' and takes '+ str(result[2])+' seconds. \n\n')
    file.close()

def inputInt(str):
    num = input(str)
    try:
        num = int(num)
        return num
    except ValueError:
        return None


def main():
    g=gerador.Gerador()

    num = inputInt("\nQuantos vertices quer?\n  >")
    tarefa = inputInt("\nQue tarefa quer?\n  >")

    g.gera(num,tarefa)
    map=g.getMap()
    result=shortestPath(map,tarefa)
    writeInFile(map,result)

main()
