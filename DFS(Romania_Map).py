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
visited = []
to_visit.append(('/' , 'Arad'))
while to_visit:
    currNode = to_visit.pop()
    visited.append(currNode)
    if(currNode[1] == 'Bucharest'):
        print("Goal is Found.")
        break
    else:
        childNodes = graph[currNode[1]]
        for child in childNodes:
            cond = True
            for tuple in visited:
                if(tuple[1] == child):
                    cond = False
                    break
            if cond:
                to_visit.append((currNode[1] , child))
print(visited)
print(to_visit)

while visited:
    currNode = visited.pop()  
    if(currNode[1] == 'Bucharest'):
        path = 'Bucharest'
        parent = currNode[0]
        break
while visited : 
    currNode = visited.pop()
    if(parent == currNode[1]):
        path = parent+ "->" + path
        parent = currNode[0]
print(path)