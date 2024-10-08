# graph = {
#     "Arad": {"Zerind", "Sibui", "Timisora"},
#     "Zerind": {"Arad", "Orades"},
#     "Orades": {"Zerind", "Sibiu"},
#     "Sibui": {"Fagaras", "Rimnicui" , "Arad"},
#     "Timisora": {"Arad", "Lugoj"},
#     "Lugoj": {"Timisora" , "Mehadia"},
#     "Mehadia": {"Lugoj" , "Dobreta"},
#     "Dobreta" : {"Mehadia","Craiova"},
#     "Craiova": {"Rimnicui" , "Pitesti"},
#     "Rimnicui" : {"Craiova" , "Pitesti"},
#     "Fagaras" : {"Sibui" , "Bucharest"},
#     "Pitesti" : {"Rimnicui" , "Bucharest"},
#     "Bucharest" : {"Giurgiue" },
#     "Giurgiue" : {"Bucharest"}
# }


# graph = {
#     "A": {"C", "B"},
#     "B": {"E", "A"},
#     "C": {"G", "D", "A"},
#     "E": {"B", "D"},
#     "D": {"F", "E", "C"},
#     "F": {"D"},
#     "G": {"C"}
# }


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

to_visit = []
visted = []
to_visit.append(('/' , 'Craiova' , 0))
while to_visit:
    minWeightCity = to_visit[0]
    for tup in to_visit:
        if tup[2] < minWeightCity[2] :
            minWeightCity = tup
    currNode = minWeightCity
    to_visit.remove(minWeightCity)
    visted.append(currNode)
    if currNode[1] == 'Fagaras':
        print(f'Goal is Found {currNode}')
        break
    else:
        childNodes = graph[currNode[1]]
        for child,weight in childNodes.items():
            cond = True
            for tuple in visted:
                if child ==  tuple[1]:
                    cond = False
                    break
            if cond :
                to_visit.append((currNode[1] , child ,currNode[2] + weight))
print("Nodes in closed list are : " , visted)
path = 'Fagaras'
parent = ''
while visted:
    currNode = visted.pop()  
    if(currNode[1] == 'Fagaras'):
        path = 'Fagaras'
        parent = currNode[0]
        break
while visted : 
    currNode = visted.pop()
    if(parent == currNode[1]):
        path = parent+ " (:==>" +path
        parent = currNode[0]

print("Path of Goal : " + path)