graph = {
    "src":[("A",10),("B",11)],
    "A":[("C",12),("D",15)],
    "B" :[("E",5),("F",34)],
    "C":[],
    "D":[],
    "E":[],
    "F" :[("dest",2)],
    "dest":[]
    }

heuristicValue = {
    "src":100,
    "A":90,
    "B":80,
    "C":70,
    "D":60,
    "E":50,
    "F":40,
    "dest":0
    }

needToVisit = [("src",0)]

while needToVisit :
    bestNode = needToVisit[0]
    for currentNode in needToVisit :
        if currentNode[1] + heuristicValue[currentNode[0]] < bestNode[1] + heuristicValue[bestNode[0]] :
            bestNode = currentNode
    needToVisit.remove(bestNode)

    node = bestNode[0]
    cost = bestNode[1]

    print(node ,cost , end=" ")

    if(node == "dest") :
        print("Goal Node found")
        break
        

    for child , edgeCost in graph[node]:
        needToVisit.append((child,cost + edgeCost))
