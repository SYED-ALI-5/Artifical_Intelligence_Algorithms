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
    "Arad": {"Zerind", "Sibiu", "Timisoara"},
    "Zerind": {"Arad", "Oradea"},
    "Oradea": {"Zerind", "Sibiu"},
    "Sibiu": {"Fagaras", "Rimnicu", "Arad", "Oradea"},
    "Timisoara": {"Arad", "Lugoj"},
    "Lugoj": {"Timisoara", "Mehadia"},
    "Mehadia": {"Lugoj", "Dobreta"},
    "Dobreta": {"Mehadia", "Craiova"},
    "Craiova": {"Rimnicu", "Pitesti"},
    "Rimnicu": {"Craiova", "Pitesti"},
    "Fagaras": {"Sibiu", "Bucharest"},
    "Pitesti": {"Rimnicu", "Bucharest"},
    "Bucharest": {"Giurgiu"},
    "Giurgiu": {"Bucharest"}
}

to_visit = []
visted = []
to_visit.append(('/' , 'Arad'))
while to_visit:
    currNode = to_visit.pop(0)
    visted.append(currNode)
    if currNode[1] == 'Bucharest':
        print(f'Goal is Found {currNode}')
        break
    else:
        childNodes = graph[currNode[1]]
        # print(childNodes)
        for child in childNodes:
            cond = True
            for tuple in visted:
                if child ==  tuple[1]:
                    cond = False
                    break
            if cond :
                to_visit.append((currNode[1] , child))
print("Nodes in closed list are : " , visted)
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