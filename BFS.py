graph = {
    "A" : ["B" , "C"] ,
    "B" : ["D" , "E" ] ,
    "C" : ["F"] ,
    "D" : [] ,
    "E" : [] ,
    "F" : []
    }

visited = []
needToVisit = ["A"]

while needToVisit :
    currentElement = needToVisit.pop(0)
    if currentElement not in visited :
        visited.append(currentElement)
        needToVisit.extend(graph[currentElement])

print(visited) 
