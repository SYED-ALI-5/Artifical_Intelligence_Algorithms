graph = {
    "Arad": {"Zerind": 75, "Sibiu": 140, "Timisoara": 118},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Sibiu": {"Fagaras": 99, "Rimnicu": 80, "Arad": 140, "Oradea": 151},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia": 70},
    "Mehadia": {"Lugoj": 70, "Dobreta": 75},
    "Dobreta": {"Mehadia": 75, "Craiova": 120},
    "Craiova": {"Dobreta": 120, "Rimnicu": 146, "Pitesti": 138},
    "Rimnicu": {"Craiova": 146, "Sibiu": 80, "Pitesti": 97},
    "Fagaras": {"Sibiu": 99, "Bucharest": 211},
    "Pitesti": {"Rimnicu": 97, "Craiova": 138, "Bucharest": 101},
    "Bucharest": {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90},
    "Giurgiu": {"Bucharest": 90}
}
straight_line_distance = {
    "Arad" : 366,
    "Bucharest" : 0,
    "Craiova" : 160,
    "Dobreta": 242,
    "Fagaras": 178,
    "Giurgiu":77,
    "Hirsova": 151,
    "lasi" : 226,
    "Lugoj" : 244,
    "Mehedia": 241,
    "Neamt": 234,
    "Oradea":380,
    "Pitesti" : 98,
    "Rimnicu" : 193,
    "Sibiu" : 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vasiui":191 , 
    "Zerind" : 374
}
to_visit = []
visted = []
to_visit.append(('/' , 'Arad' , 366))
while to_visit:
    minWeightCity = to_visit[0]
    for tup in to_visit:
        if tup[2] < minWeightCity[2] :
            minWeightCity = tup
    currNode = minWeightCity
    to_visit.remove(minWeightCity)
    visted.append(currNode)
    if currNode[1] == 'Bucharest':
        print(f'Goal is Found {currNode}')
        break
    else:
        print("=>"+currNode[0] + " " + currNode[1] + " " + str(currNode[2]))
        childNodes = graph[currNode[1]]
        for child,weight in childNodes.items():
            cond = True
            for tuple in visted:
                if child ==  tuple[1]:
                    cond = False
                    break
            if cond:
                prevweight = 0
                nextweight = 0
                for key,value in straight_line_distance.items():
                    if(key == currNode[1]):
                        prevweight = value
                    if(key == child):
                        nextweight = value
                print(currNode[0] + " Parent of " + currNode[1] + " has the value : " + str(prevweight) +" and prev weight is " + str(currNode[2]))
                print("weight  of " + child + " : " + str(weight) + " and " + str(nextweight))
                to_visit.append((currNode[1] , child ,currNode[2] - prevweight + weight + nextweight))
                print("Nodes in open list are : " , to_visit)
print("Nodes in closed list are : " , visted)
print("Nodes in opened list are : " , to_visit)
path = 'Bucharest'
parent = ''
while visted:
    currNode = visted.pop()  
    if(currNode[1] == 'Bucharest'):
        path = 'Bucharest'
        parent = currNode[0]
        break
while visted : 
    currNode = visted.pop()
    if(parent == currNode[1]):
        path = parent+ " (:==>" +path
        parent = currNode[0]

print("Path of Goal : " + path)