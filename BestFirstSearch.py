
graph = {
    'src' : [1,2,3] ,
    1 : [4,5],
    2: [6,7],
    3: [8],
    4 : [],
    5 : [],
    6 : [],
    7 : ["dest"],
    8 : [],
    "dest" : []
    }

heuristicValue = {
    "src" : 20 ,
    1: 30 ,
    2 :34,
    3: 54,
    4: 98 ,
    5:24,
    6:47,
    7:5,
    8:69,
    "dest" : 0 
    }

needToVisit = ["src"]

while needToVisit :
    bestNode = needToVisit[0]

    for currentNode in needToVisit :
        if heuristicValue[currentNode] < heuristicValue[bestNode]:
            bestNode = currentNode

    needToVisit.remove(bestNode)

    print(bestNode , end=" ")

    if(bestNode == "dest"):
        print("Goal Node reched")
        break

    needToVisit.extend(graph[bestNode])

