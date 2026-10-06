graph = {
    "A" : ["B" , "C" ],
    "B" : ["D" , "E"],
    "C" : ["F"],
    "D": [],
    "E": [],
    "F": [],
    
    }

visited = []
needToVisit = ["A"]

while needToVisit :
    currentNode = needToVisit.pop(-1)
    if currentNode not in visited :
        visited.append(currentNode)
        needToVisit.extend(reversed(graph[currentNode]))

print(visited)
