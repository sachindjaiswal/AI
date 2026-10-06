
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


graph = {
    "src" : [1,2,3] ,
    1:[4,5],
    2:[6,7] ,
    3:[8] ,
    4:[],
    5:[],
    6:[],
    7:["dest"],
    8:[],
    "dest":[]
    
    }

heuristicValue = {
    "src" : 50 ,
    1:34,
    2:65,
    3:78,
    4:67,
    5:69,
    6:23,
    7:5,
    8:49,
    "dest":0

    }

needToVisit = ["src"]

while needToVisit :
    bestNode = needToVisit[0]

    for currentNode in needToVisit:
        if heuristicValue[currentNode] < heuristicValue[bestNode] :
            bestNode = currentNode

    needToVisit.remove(bestNode)
    print(bestNode , end=" ")

    if(bestNode == "dest") :
        print("Goal Node found")
        break

    needToVisit.extend(graph[bestNode])


graph = {
    "src" : [1,2,3],
    1:[4,5],
    2:[6,7],
    3:[8],
    4:[],
    5:[],
    6:[],
    7:["dest"],
    8:[]
    }

heuristicValue = {
    "src" :100 ,
    1:90,
    2:80,
    3:70,
    4:60,
    5:50,
    6:40,
    7:5 ,
    8:30,
    "dest" :0 
    }

needToVisit = ["src"]

while needToVisit :
    bestNode = needToVisit[0]

    for currentNode in needToVisit :
        if heuristicValue[currentNode] < heuristicValue[bestNode] :
            bestNode = currentNode

    needToVisit.remove(bestNode)

    print(bestNode , end=" ")

    if(bestNode == "dest") :
        print("Goal Node Found " )
        break

    needToVisit.extend(graph[bestNode])




print("practice")
graph = {
    "src" : ["A","B"],
    "A" : ["C","D"],
    "B" : ["E" ,"F"],
    "C" : [],
    "D" :[] ,
    "E" : [] ,
    "F" : []
    }

heuristicValue =  {
    "src" :100 ,
    "A":90,
    "B":80,
    "C":70,
    "D":60,
    "E":50,
    "F":40
    }

needToVisit = ["src"]

while needToVisit :
    bestNode = needToVisit[0]

    for currentNode in needToVisit :
        if ( heuristicValue[currentNode] < heuristicValue[bestNode]):
            bestNode = currentNode

    needToVisit.remove(bestNode)

    print(bestNode , end=" " )

    if bestNode == "dest" :
        print("goal node found")
        break

    needToVisit.extend(graph[bestNode])
    
